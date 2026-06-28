#if (Net8)
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
#else
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
#endif
WORKDIR /src
COPY . .
RUN dotnet publish Company.Service.csproj -c Release -o /app --no-self-contained

#if (Net8)
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine
#else
FROM mcr.microsoft.com/dotnet/aspnet:10.0-alpine
#endif
WORKDIR /app
COPY --from=build /app .
USER $APP_UID
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080
ENTRYPOINT ["dotnet", "Company.Service.dll"]
