using Microsoft.AspNetCore.Diagnostics.HealthChecks;
#if (HasApiVersioning)
using Asp.Versioning;
#endif
#if (HasAuthentication)
using Company.Service.Authentication;
#endif
#if (Controllers)
using Company.Service.Controllers;
#endif
#if (MinimalApi)
using Company.Service.Endpoints;
#endif
#if (HasEfCore)
using Company.Service.Persistence;
#endif
#if (HasHttpIntegration)
using Company.Service.Integrations;
#endif
#if (HasMessaging)
using Company.Service.Messaging;
#endif
#if (HasReliableMessaging)
using Company.Service.Reliability;
#endif
#if (HasJobs)
using Company.Service.Jobs;
#endif
#if (HasCache)
using Company.Service.Caching;
#endif
#if (OpenTelemetry)
using Company.Service.Observability;
#endif

var builder = WebApplication.CreateBuilder(args);
builder.Logging.AddJsonConsole();
#if (OpenTelemetry)
builder.Services.AddServiceObservability(builder.Configuration);
#endif

builder.Services.AddProblemDetails();
builder.Services.AddHealthChecks();
#if (HasHttpIntegration)
builder.Services.AddServiceHttpIntegrations(builder.Configuration);
#endif
#if (HasMessaging)
builder.Services.AddServiceMessaging(builder.Configuration);
#endif
#if (HasReliableMessaging)
builder.Services.AddReliableMessaging();
#endif
#if (HasJobs)
builder.Services.AddServiceJobs();
#endif
#if (HasCache)
builder.Services.AddServiceCaching(builder.Configuration);
#endif
#if (HasEfCore)
builder.Services.AddServicePersistence(builder.Configuration);
#endif
#if (HasApiVersioning)
builder.Services.AddApiVersioning(options =>
{
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
});
#endif
#if (Controllers)
builder.Services.AddControllers();
#endif
#if (OpenApi)
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
#endif
#if (HasAuthentication)
builder.Services.AddServiceAuthentication(builder.Configuration);
#endif

var app = builder.Build();

app.UseExceptionHandler();
app.UseStatusCodePages();
#if (OpenApi)
var exposeOpenApi = app.Configuration.GetValue<bool?>("OpenApi:Enabled") ?? app.Environment.IsDevelopment();
if (exposeOpenApi)
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
#endif
#if (HasAuthentication)
app.UseAuthentication();
#endif
#if (HasAuthorization)
app.UseAuthorization();
#endif

app.MapHealthChecks("/health/live", new HealthCheckOptions { Predicate = _ => false });
app.MapHealthChecks("/health/ready");
#if (Controllers)
app.MapControllers();
#endif
#if (MinimalApi)
app.MapServiceEndpoints();
#endif

app.Run();

public partial class Program;
