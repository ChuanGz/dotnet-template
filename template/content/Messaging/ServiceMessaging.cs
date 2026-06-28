namespace Company.Service.Messaging;

public sealed record IntegrationMessage(Guid Id, string Type, string Payload, DateTimeOffset OccurredAt);

public interface IMessagePublisher
{
    Task PublishAsync(IntegrationMessage message, CancellationToken cancellationToken);
}

internal sealed class ConfiguredMessagePublisher(ILogger<ConfiguredMessagePublisher> logger, IConfiguration configuration) : IMessagePublisher
{
    public Task PublishAsync(IntegrationMessage message, CancellationToken cancellationToken)
    {
        cancellationToken.ThrowIfCancellationRequested();
        logger.LogInformation("Publishing {MessageId} through {Broker}", message.Id, configuration["Messaging:Broker"]);
        return Task.CompletedTask;
    }
}

public static class MessagingExtensions
{
    public static IServiceCollection AddServiceMessaging(this IServiceCollection services, IConfiguration configuration)
    {
        _ = configuration["Messaging:ConnectionString"] ?? throw new InvalidOperationException("Messaging:ConnectionString is required.");
        services.AddSingleton<IMessagePublisher, ConfiguredMessagePublisher>();
        return services;
    }
}
