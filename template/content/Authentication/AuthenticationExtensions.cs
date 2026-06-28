using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;

namespace Company.Service.Authentication;

public static class AuthenticationExtensions
{
    public static IServiceCollection AddServiceAuthentication(this IServiceCollection services, IConfiguration configuration)
    {
        var section = configuration.GetRequiredSection("Authentication");
        services.AddOptions<AuthenticationSettings>()
            .Bind(section)
            .Validate(settings => Uri.TryCreate(settings.Authority, UriKind.Absolute, out _), "Authentication:Authority must be an absolute URI.")
            .Validate(settings => !string.IsNullOrWhiteSpace(settings.Audience), "Authentication:Audience is required.")
            .ValidateOnStart();

        services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
            .AddJwtBearer(options =>
            {
                options.Authority = section["Authority"];
                options.Audience = section["Audience"];
                options.RequireHttpsMetadata = true;
                options.TokenValidationParameters = new TokenValidationParameters
                {
                    ValidateIssuer = true,
                    ValidateAudience = true,
                    ValidateLifetime = true,
                    ValidateIssuerSigningKey = true
                };
            });

        services.AddAuthorization(options =>
        {
            options.FallbackPolicy = new Microsoft.AspNetCore.Authorization.AuthorizationPolicyBuilder()
                .RequireAuthenticatedUser()
                .Build();
            if (string.Equals("AuthorizationModeToken", "policy", StringComparison.Ordinal))
                options.AddPolicy("service-access", policy => policy.RequireClaim("scope", "service.access"));
        });

        return services;
    }
}

public sealed class AuthenticationSettings
{
    public string Authority { get; init; } = string.Empty;
    public string Audience { get; init; } = string.Empty;
}
