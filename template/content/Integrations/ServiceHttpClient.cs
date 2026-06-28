namespace Company.Service.Integrations;

public sealed class ServiceHttpClient(HttpClient client)
{
    public async Task<string> GetAsync(string path, CancellationToken cancellationToken) =>
        await client.GetStringAsync(path, cancellationToken);
}

public static class HttpIntegrationExtensions
{
    public static IServiceCollection AddServiceHttpIntegrations(this IServiceCollection services, IConfiguration configuration)
    {
        var baseUrl = configuration["Integrations:Service:BaseUrl"]
            ?? throw new InvalidOperationException("Integrations:Service:BaseUrl is required.");
        services.AddHttpClient<ServiceHttpClient>(client => client.BaseAddress = new Uri(baseUrl))
            .AddStandardResilienceHandler();
        return services;
    }
}
