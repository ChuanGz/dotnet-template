using Microsoft.EntityFrameworkCore;
#if (HasReliableMessaging)
using Company.Service.Reliability;
#endif

namespace Company.Service.Persistence;

public sealed class ServiceDbContext(DbContextOptions<ServiceDbContext> options) : DbContext(options)
{
    public DbSet<ServiceRecord> ServiceRecords => Set<ServiceRecord>();
#if (HasReliableMessaging)
    public DbSet<OutboxMessage> OutboxMessages => Set<OutboxMessage>();
    public DbSet<InboxMessage> InboxMessages => Set<InboxMessage>();
#endif

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        var record = modelBuilder.Entity<ServiceRecord>();
        record.ToTable("service_records");
        record.HasKey(item => item.Id);
        record.Property(item => item.Value).HasMaxLength(200).IsRequired();
        record.Property(item => item.CreatedAt).IsRequired();
#if (HasReliableMessaging)
        modelBuilder.Entity<OutboxMessage>().HasKey(item => item.Id);
        modelBuilder.Entity<InboxMessage>().HasKey(item => item.Id);
#endif
    }
}
