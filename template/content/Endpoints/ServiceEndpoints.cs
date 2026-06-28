using Company.Service.Contracts;
using Company.Service.Validation;
#if (ApiVersioning)
using Asp.Versioning;
#endif

namespace Company.Service.Endpoints;

public static class ServiceEndpoints
{
    public static IEndpointRouteBuilder MapServiceEndpoints(this IEndpointRouteBuilder endpoints)
    {
#if (ApiVersioning)
        var versions = endpoints.NewApiVersionSet()
            .HasApiVersion(new ApiVersion(1, 0))
            .ReportApiVersions()
            .Build();
        var group = endpoints.MapGroup("/api/v{version:apiVersion}/service")
            .WithApiVersionSet(versions)
            .MapToApiVersion(1.0);
#else
        var group = endpoints.MapGroup("/api/service");
#endif
#if (HasAuthorization)
#if (PolicyAuthorization)
        group.RequireAuthorization("service-access");
#elif (BasicAuthorization)
        group.RequireAuthorization();
#endif
#endif

        group.MapGet("/status", () =>
            Results.Ok(new ServiceStatusResponse("ok", DateTimeOffset.UtcNow)));

        group.MapPost("/echo", (EchoRequest request) =>
            Results.Ok(new EchoResponse(request.Message)))
            .AddEndpointFilter<ValidationFilter<EchoRequest>>();

        return endpoints;
    }
}
