#if (HasAuthentication)
using Microsoft.AspNetCore.Authorization;
#endif
using Microsoft.AspNetCore.Mvc;
using Company.Service.Contracts;
#if (ApiVersioning)
using Asp.Versioning;
#endif

namespace Company.Service.Controllers;

[ApiController]
#if (ApiVersioning)
[ApiVersion(1.0)]
[Route("api/v{version:apiVersion}/service")]
#else
[Route("api/service")]
#endif
#if (HasAuthorization)
#if (PolicyAuthorization)
[Authorize(Policy = "service-access")]
#elif (BasicAuthorization)
[Authorize]
#endif
#endif
public sealed class ServiceController : ControllerBase
{
    [HttpGet("status")]
    [ProducesResponseType<ServiceStatusResponse>(StatusCodes.Status200OK)]
    public ActionResult<ServiceStatusResponse> GetStatus() =>
        Ok(new ServiceStatusResponse("ok", DateTimeOffset.UtcNow));

    [HttpPost("echo")]
    [ProducesResponseType<EchoResponse>(StatusCodes.Status200OK)]
    [ProducesResponseType<ValidationProblemDetails>(StatusCodes.Status400BadRequest)]
    public ActionResult<EchoResponse> Echo([FromBody] EchoRequest request) =>
        Ok(new EchoResponse(request.Message));
}
