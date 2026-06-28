using System.ComponentModel.DataAnnotations;

namespace Company.Service.Contracts;

public sealed record ServiceStatusResponse(string Status, DateTimeOffset Timestamp);

public sealed record EchoRequest(
    [property: Required, MinLength(1), MaxLength(200)] string Message);

public sealed record EchoResponse(string Message);
