#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "$0")/../.." && pwd)
work=$(mktemp -d)
app_pid=""
cleanup() {
  if [[ -n "$app_pid" ]]; then kill "$app_pid" 2>/dev/null || true; fi
  rm -rf "$work"
}
trap cleanup EXIT
hive="$work/hive"

dotnet new install "$root/template/content" --debug:custom-hive "$hive" >/dev/null

python3 - "$root" <<'PY'
import json, pathlib, sys
root = pathlib.Path(sys.argv[1])
contract = json.loads((root / "config/template-options.json").read_text())
template = json.loads((root / "template/content/.template.config/template.json").read_text())
host = json.loads((root / "template/content/.template.config/dotnetcli.host.json").read_text())
for symbol in ("DataProvider", "DatabaseProvider"):
    option = host["symbolInfo"][symbol]["longName"]
    expected = next(item for item in contract["options"] if item["name"] == option)
    actual = template["symbols"][symbol]
    assert actual["defaultValue"] == expected["default"], option
    assert [item["choice"] for item in actual["choices"]] == expected["values"], option
PY

for provider in postgresql sqlserver sqlite; do
  output="$work/$provider"
  dotnet new dotnet-service --debug:custom-hive "$hive" -n "Generated.${provider}" -o "$output" \
    --dotnet-version net8.0 --api-style none --authentication none --authorization none --openapi false \
    --data-provider efcore --database-provider "$provider" >/dev/null
  dotnet build "$output/Generated.${provider}.csproj" --configuration Release --nologo >/dev/null
  test -f "$output/Persistence/ServiceDbContext.cs"
done

none="$work/none"
dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.None -o "$none" \
  --dotnet-version net8.0 --api-style none --authentication none --authorization none --openapi false \
  --data-provider none --database-provider none >/dev/null
dotnet build "$none/Generated.None.csproj" --configuration Release --nologo >/dev/null
test ! -d "$none/Persistence"
if dotnet list "$none/Generated.None.csproj" package | grep -q 'EntityFrameworkCore'; then
  echo "data-free output restored EF Core packages" >&2
  exit 1
fi

sqlite="$work/sqlite-runtime"
dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.SqliteRuntime -o "$sqlite" \
  --dotnet-version net8.0 --api-style minimal --authentication none --authorization none --openapi false \
  --data-provider efcore --database-provider sqlite >/dev/null
dotnet build "$sqlite/Generated.SqliteRuntime.csproj" --configuration Release --nologo >/dev/null
port=$(python3 -c 'import socket; s=socket.socket(); s.bind(("127.0.0.1", 0)); print(s.getsockname()[1]); s.close()')
database="$work/service.db"
touch "$database"
ConnectionStrings__ServiceDatabase="Data Source=$database" \
  dotnet run --project "$sqlite/Generated.SqliteRuntime.csproj" --configuration Release --no-build --urls "http://127.0.0.1:$port" >"$work/runtime.log" 2>&1 &
app_pid=$!
ready=false
for _ in {1..40}; do
  if curl -fsS "http://127.0.0.1:$port/health/ready" >/dev/null 2>&1; then ready=true; break; fi
  sleep 0.25
done
if [[ "$ready" != true ]]; then cat "$work/runtime.log" >&2; exit 1; fi

echo "M5 data generation checks passed."
