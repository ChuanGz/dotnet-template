# Company.Service

Generated with `dotnet-service`.

## Selected options

- Target framework: `FrameworkTarget`
- API style: `ApiStyleToken`
- OpenAPI: `OpenApiToken`
- Authentication: `AuthModeToken`
- Authorization: `AuthorizationModeToken`
- Data access: `DataProviderToken`
- Database: `DatabaseProviderToken`

## Verify

```bash
dotnet restore
dotnet build --no-restore
dotnet run
```

Health endpoints are `/health/live` and `/health/ready`. When generated, Swagger UI is exposed at `/swagger` only in Development by default. Set `OpenApi__Enabled=true` to expose it explicitly in another environment.

Authentication-enabled projects require a real HTTPS authority and audience. Replace the non-routable example authority through configuration; do not commit secrets.

Database-enabled projects require a `ConnectionStrings:ServiceDatabase` value. Apply reviewed migrations during deployment; the service does not mutate schema at startup.
