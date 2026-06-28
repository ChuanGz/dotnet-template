namespace Company.Service.Reliability;

public sealed class OutboxMessage
{
    public Guid Id { get; init; }
    public string Type { get; init; } = string.Empty;
    public string Payload { get; init; } = string.Empty;
    public DateTimeOffset OccurredAt { get; init; }
    public DateTimeOffset? PublishedAt { get; set; }
}

public sealed class InboxMessage
{
    public Guid Id { get; init; }
    public DateTimeOffset ProcessedAt { get; init; }
}

public static class ReliableMessagingExtensions
{
    public static IServiceCollection AddReliableMessaging(this IServiceCollection services) => services;
}
