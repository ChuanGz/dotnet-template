namespace Company.Service.Caching;

public static class CachingExtensions
{
    public static IServiceCollection AddServiceCaching(this IServiceCollection services, IConfiguration configuration)
    {
#if (RedisCache)
        var connection = configuration.GetConnectionString("Redis")
            ?? throw new InvalidOperationException("ConnectionStrings:Redis is required.");
        services.AddStackExchangeRedisCache(options => options.Configuration = connection);
#else
        services.AddMemoryCache();
#endif
        return services;
    }
}
