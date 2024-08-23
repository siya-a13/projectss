---
longform:
  format: single
  title: Setup Replication
---
## **Check Replication Status on the Master**

You can use the `pg_stat_replication` view on the master server to check the status of connected standby servers.

```
SELECT 
    client_addr, 
    state, 
    sync_state, 
    sent_lsn, 
    write_lsn, 
    flush_lsn, 
    replay_lsn,
    write_lag,
    flush_lag,
    replay_lag
FROM 
    pg_stat_replication;
```
### Key Columns:

- **state**: Indicates the current state of the replication process. The value should be `streaming` when the standby is actively replicating.
- **sync_state**: Shows whether the standby is `sync` (synchronous replication) or `async` (asynchronous replication).
- **sent_lsn, write_lsn, flush_lsn, replay_lsn**: These fields show the progress of WAL records sent, written, flushed, and replayed on the standby. Ideally, these values should be close to each other, indicating minimal lag.
- **write_lag, flush_lag, replay_lag**: These fields display the time lag between the master and the standby in writing, flushing, and replaying WAL records. If these values are close to zero, it indicates that the replication is in sync.
### Example Output:

```
 client_addr | state    | sync_state | sent_lsn | write_lsn | flush_lsn | replay_lsn | write_lag | flush_lag | replay_lag 
-------------+----------+------------+----------+-----------+-----------+------------+-----------+-----------+------------
 192.168.0.107 | streaming | async      | 0/3000200 | 0/3000200  | 0/3000200 | 0/3000200  |           |           | 

```

In the example above, the `state` is `streaming`, and the `write_lag`, `flush_lag`, and `replay_lag` are empty (or close to zero), indicating that the replication is in sync.

## **Check Replication Lag on the Standby**

You can check the replication lag directly on the standby server using the `pg_last_wal_receive_lsn()` and `pg_last_wal_replay_lsn()` functions.

```
SELECT 
    pg_last_wal_receive_lsn() AS last_received_lsn,
    pg_last_wal_replay_lsn() AS last_replayed_lsn,
    pg_is_in_recovery() AS in_recovery;
```

### Key Points:

- **pg_last_wal_receive_lsn()**: Returns the last WAL location received by the standby.
- **pg_last_wal_replay_lsn()**: Returns the last WAL location replayed by the standby.
- **pg_is_in_recovery()**: Should return `true`, indicating that the server is in recovery mode (i.e., it's a standby server).

### Example Output:

```
 last_received_lsn | last_replayed_lsn | in_recovery 
-------------------+-------------------+-------------
 0/3000200         | 0/3000200         | t
```

If `last_received_lsn` and `last_replayed_lsn` are equal or very close, it means the standby server is up-to-date with the master.