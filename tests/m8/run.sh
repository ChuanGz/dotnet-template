#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/../.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
hive="$work/hive"
dotnet new install "$root/template/content" --debug:custom-hive "$hive" >/dev/null
dotnet new dotnet-service --debug:custom-hive "$hive" -n SampleService -o "$work/SampleService" --dotnet-version net10.0 >/dev/null
dotnet restore "$work/SampleService/SampleService.csproj" >/dev/null
dotnet build "$work/SampleService/SampleService.csproj" -c Release --no-restore --nologo >/dev/null
test -f "$work/SampleService/Dockerfile"
test -f "$work/SampleService/.github/workflows/ci.yml"
python3 - "$root" <<'PY'
import pathlib, re, sys
root = pathlib.Path(sys.argv[1])
missing = []
for source in root.rglob("*.md"):
    if ".git" in source.parts:
        continue
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", source.read_text()):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if not (source.parent / target.split("#", 1)[0]).resolve().exists():
            missing.append(f"{source.relative_to(root)} -> {target}")
if missing:
    raise SystemExit("Broken local links:\n" + "\n".join(missing))
PY
echo "M8 adoption checks passed."
