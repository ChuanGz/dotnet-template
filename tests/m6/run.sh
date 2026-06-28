#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/../.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
export PATH="$HOME/.dotnet:$PATH"
hive="$work/hive"
dotnet new install "$root/template/content" --debug:custom-hive "$hive" >/dev/null
for args in \
  "--integration http --cache-provider memory" \
  "--integration messaging --message-broker rabbitmq --message-pattern outbox --data-provider efcore --database-provider sqlite" \
  "--job-processing hosted-service --cache-provider redis"; do
  output="$work/$(echo "$args" | tr ' -' '__')"
  dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.M6 -o "$output" --dotnet-version net8.0 $args >/dev/null
  dotnet build "$output/Generated.M6.csproj" --configuration Release --nologo >/dev/null
done
plain="$work/plain"
dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.Plain -o "$plain" --dotnet-version net8.0 --integration none --job-processing none --cache-provider none >/dev/null
test ! -d "$plain/Integrations" && test ! -d "$plain/Messaging" && test ! -d "$plain/Jobs" && test ! -d "$plain/Caching"
echo "M6 generation checks passed."
