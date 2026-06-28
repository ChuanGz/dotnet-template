using Microsoft.EntityFrameworkCore;

namespace Company.Service.Persistence;

public sealed class ServiceDbContext(DbContextOptions<ServiceDbContext> options) : DbContext(options)
{
    public DbSet<ServiceRecord> ServiceRecords => Set<ServiceRecord>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        var record = modelBuilder.Entity<ServiceRecord>();
        record.ToTable("service_records");
        record.HasKey(item => item.Id);
        record.Property(item => item.Value).HasMaxLength(200).IsRequired();
        record.Property(item => item.CreatedAt).IsRequired();
    }
}
