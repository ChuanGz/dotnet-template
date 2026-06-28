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
for symbol in ("Framework", "ApiStyle", "OpenApi", "ApiVersioning", "Authentication", "Authorization"):
    option = host["symbolInfo"][symbol]["longName"]
    expected = next(item for item in contract["options"] if item["name"] == option)
    actual = template["symbols"][symbol]
    assert actual["defaultValue"] == expected["default"], option
    if "choices" in actual:
        assert [item["choice"] for item in actual["choices"]] == expected["values"], option
PY

frameworks=(net8.0)
if dotnet --list-sdks | grep -q '^10\.'; then
  frameworks+=(net10.0)
else
  echo "Skipping net10.0 build: .NET 10 SDK is not installed. CI validates both LTS targets."
fi

for framework in "${frameworks[@]}"; do
  for style in controllers minimal none; do
    output="$work/$framework-$style"
    dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.Service -o "$output" \
      --dotnet-version "$framework" --api-style "$style" --authentication none --authorization none --openapi false >/dev/null
    dotnet build "$output/Generated.Service.csproj" --configuration Release --nologo >/dev/null

    if [[ "$style" == "controllers" && ! -f "$output/Controllers/ServiceController.cs" ]]; then exit 1; fi
    if [[ "$style" == "minimal" && ! -f "$output/Endpoints/ServiceEndpoints.cs" ]]; then exit 1; fi
    if [[ "$style" == "none" && ( -d "$output/Controllers" || -d "$output/Endpoints" ) ]]; then exit 1; fi
    if grep -R -qE 'FrameworkTarget|ApiStyleToken|OpenApiToken|AuthModeToken|AuthorizationModeToken|ApiVersioningToken' "$output"; then
      echo "unresolved template token in $output" >&2
      exit 1
    fi
  done
done

secure="$work/secure"
dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.SecureService -o "$secure" \
  --dotnet-version net8.0 --api-style controllers --authentication jwt --authorization policy --openapi true >/dev/null

grep -q 'Authorize(Policy = "service-access")' "$secure/Controllers/ServiceController.cs"
grep -q 'Echo(\[FromBody\] EchoRequest request)' "$secure/Controllers/ServiceController.cs"
if grep -R -q 'EchoCommand' "$secure"; then
  echo "controller and minimal API contracts have drifted" >&2
  exit 1
fi

normalized="$work/normalized-security"
dotnet new dotnet-service --debug:custom-hive "$hive" -n NormalizedSecurity -o "$normalized" \
  --dotnet-version net8.0 --api-style minimal --authentication none --authorization policy --openapi false >/dev/null

if grep -R -q 'RequireAuthorization' "$normalized"; then
  echo "authorization must be disabled when authentication is none" >&2
  exit 1
fi

dotnet build "$normalized/NormalizedSecurity.csproj" --configuration Release --nologo >/dev/null
port=$(python3 -c 'import socket; s=socket.socket(); s.bind(("127.0.0.1", 0)); print(s.getsockname()[1]); s.close()')
dotnet run --project "$normalized/NormalizedSecurity.csproj" --configuration Release --no-build --urls "http://127.0.0.1:$port" >"$work/runtime.log" 2>&1 &
app_pid=$!
ready=false
for _ in {1..30}; do
  if curl -fsS "http://127.0.0.1:$port/health/live" >/dev/null 2>&1; then ready=true; break; fi
  sleep 0.2
done
if [[ "$ready" != true ]]; then cat "$work/runtime.log" >&2; exit 1; fi
curl -fsS "http://127.0.0.1:$port/api/v1/service/status" >/dev/null
kill "$app_pid" 2>/dev/null || true
wait "$app_pid" 2>/dev/null || true
app_pid=""
dotnet build "$secure/Generated.SecureService.csproj" --configuration Release --nologo >/dev/null
test -f "$secure/Authentication/AuthenticationExtensions.cs"

echo "M4 generation checks passed."
