namespace Company.Service.Jobs;

internal sealed class ServiceWorker(ILogger<ServiceWorker> logger) : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        using var timer = new PeriodicTimer(TimeSpan.FromMinutes(1));
        while (await timer.WaitForNextTickAsync(stoppingToken))
            logger.LogDebug("Background job heartbeat");
    }
}

public static class JobExtensions
{
    public static IServiceCollection AddServiceJobs(this IServiceCollection services) => services.AddHostedService<ServiceWorker>();
}
