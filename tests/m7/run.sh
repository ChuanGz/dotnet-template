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
  test -f "$output/Directory.Packages.props"
  grep -q "dotnet/sdk:${framework#net}" "$output/Dockerfile"
  grep -q "dotnet/aspnet:${framework#net}" "$output/Dockerfile"
  if command -v docker >/dev/null; then
    image="generated-production-${framework//./-}:test"
    container="generated-production-${framework//./-}-$RANDOM"
    docker build -t "$image" "$output" >/dev/null
    docker run -d --rm --name "$container" -p 127.0.0.1::8080 \
      -e ASPNETCORE_ENVIRONMENT=Production -e OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4317 "$image" >/dev/null
    trap 'docker rm -f "$container" >/dev/null 2>&1 || true; rm -rf "$work"' EXIT
    port=$(docker port "$container" 8080/tcp | sed 's/.*://')
    healthy=0
    for _ in {1..30}; do
      if curl --fail --silent --show-error "http://127.0.0.1:$port/health/live" >/dev/null; then healthy=1; break; fi
      sleep 1
    done
    if [[ "$healthy" != "1" ]]; then
      docker logs "$container" >&2
      echo "Container liveness probe failed for $framework." >&2
      exit 1
    fi
    if curl --fail --silent "http://127.0.0.1:$port/swagger/index.html" >/dev/null; then
      echo "Swagger must not be exposed in Production by default." >&2; exit 1
    fi
    docker rm -f "$container" >/dev/null
  elif [[ "${REQUIRE_DOCKER:-0}" == "1" ]]; then
    echo "Docker is required for this validation run." >&2; exit 1
  fi
done
lean="$work/lean"
dotnet new dotnet-service --debug:custom-hive "$hive" -n Generated.Lean -o "$lean" --dotnet-version net8.0 --observability none --container false --ci-provider none >/dev/null
test ! -e "$lean/Dockerfile" && test ! -d "$lean/.github" && test ! -d "$lean/Observability"
echo "M7 production-readiness checks passed."
