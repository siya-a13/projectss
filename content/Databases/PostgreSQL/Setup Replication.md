---
longform:
  format: single
  title: Setup Replication
title: Setup Replication
---
![[postgres-replication.png]]
## Synchronous Replication:

### 1. **Set Up PostgreSQL Servers**

- Ensure you have at least two PostgreSQL servers: one as the primary and the other as the standby.

### 2. **Configure `postgresql.conf` on the Primary Server**

- Locate and edit the `postgresql.conf` file on the primary server.
    
- Set the following parameters:

```
wal_level = replica
synchronous_commit = on
synchronous_standby_names = 'standby1'  # Replace with your standby's name
max_wal_senders = 3                     # Adjust based on the number of standbys
max_replication_slots = 3               # Adjust based on the number of standbys
```

- The `synchronous_standby_names` parameter specifies which standby servers should be synchronous. You can list multiple standbys, separated by commas.

Refer - https://postgresqlco.nf/doc/en/param/synchronous_standby_names/

### 3. **Configure `pg_hba.conf` on the Primary Server**

- Edit the `pg_hba.conf` file on the primary server to allow the standby server to connect for replication.

```
host replication all standby_ip/32 md5
```

- Replace `standby_ip` with the actual IP address of the standby server.

### 4. **Create a Replication Slot (Optional)**

- On the primary server, create a replication slot for the standby:

```
SELECT * FROM pg_create_physical_replication_slot('standby1_slot');

```

- This step is optional but recommended to prevent WAL files from being recycled before the standby has applied them.
### 5. **Configure the Standby Server**

- Copy the data directory from the primary server to the standby server. You can use `pg_basebackup` for this:

```
pg_basebackup -h primary_ip -U replication_user -X stream -C -S slaveslot3 -P -v -R -D /var/lib/postgresql/14/main/
```

- Replace `primary_ip` with the primary server’s IP address and `replication_user` with the user allowed for replication.
    
- Edit the `recovery.conf` file on the standby server (create it if it doesn't exist):

### 6. **Edit / Start the Standby Server**

- Locate and open the `postgresql.conf` file on the standby server. This file is usually located in the PostgreSQL data directory (e.g., `/var/lib/postgresql/data/postgresql.conf`).
    
- Find the `cluster_name` parameter and set it to `standby1`. If the `cluster_name` parameter does not exist in the file, you can add it:

```
cluster_name = 'standby1'
```

- Start the PostgreSQL service on the standby server. The standby server will connect to the primary and begin replication.

### 7. **Verify the Configuration**

- On the primary server, check the synchronous replication status:

```
SELECT * FROM pg_stat_replication;
```

- Ensure that the standby server is listed as `sync` in the `sync_state` column.