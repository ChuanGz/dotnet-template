namespace Company.Service.Persistence;

public sealed class ServiceRecord
{
    public Guid Id { get; private set; }
    public string Value { get; private set; } = string.Empty;
    public DateTimeOffset CreatedAt { get; private set; }

    private ServiceRecord() { }

    public ServiceRecord(Guid id, string value, DateTimeOffset createdAt)
    {
        Id = id;
        Value = string.IsNullOrWhiteSpace(value)
            ? throw new ArgumentException("Value is required.", nameof(value))
            : value;
        CreatedAt = createdAt;
    }
}
