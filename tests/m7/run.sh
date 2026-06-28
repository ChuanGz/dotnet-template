#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/../.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
hive="$work/hive"
dotnet new install "$root/template/content" --debug:custom-hive "$hive" >/dev/null
for framework in net8.0 net10.0; do
  output="$work/$framework"
  dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.Production -o "$output" --dotnet-version "$framework" --observability opentelemetry --container true --ci-provider github-actions >/dev/null
  dotnet build "$output/Generated.Production.csproj" -c Release --nologo
  test -f "$output/Dockerfile" && test -f "$output/.github/workflows/ci.yml" && test -f "$output/Observability/ObservabilityExtensions.cs"
done
lean="$work/lean"
dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.Lean -o "$lean" --dotnet-version net8.0 --observability none --container false --ci-provider none >/dev/null
test ! -e "$lean/Dockerfile" && test ! -d "$lean/.github" && test ! -d "$lean/Observability"
echo "M7 production-readiness checks passed."
