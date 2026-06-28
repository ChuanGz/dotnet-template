using Microsoft.EntityFrameworkCore;

namespace Company.Service.Persistence;

public static class PersistenceExtensions
{
    public static IServiceCollection AddServicePersistence(
        this IServiceCollection services,
        IConfiguration configuration)
    {
        var configuredConnection = configuration.GetConnectionString("ServiceDatabase");

        services.AddDbContext<ServiceDbContext>(options =>
#if (PostgreSql)
            options.UseNpgsql(configuredConnection ?? "Host=localhost;Database=service;Username=postgres;Password=change-me"));
#elif (SqlServer)
            options.UseSqlServer(configuredConnection ?? "Server=localhost;Database=service;User Id=sa;Password=change-me-now;TrustServerCertificate=true"));
#elif (Sqlite)
            options.UseSqlite(configuredConnection ?? "Data Source=service.db"));
#endif

        services.AddHealthChecks()
            .AddDbContextCheck<ServiceDbContext>("database");

        return services;
    }
}
