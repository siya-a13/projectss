---
longform:
  format: single
  title: Container setup
title: Local setup
---
## Launch container

```
docker run -d --name postgres -e POSTGRES_USER=deepak -e POSTGRES_PASSWORD=password123 -e POSTGRES_DB=test -p 5432:5432 -v $(pwd)/data:/var/lib/postgresql/data postgres:latest
```

## Login to postgresql


```
docker exec -it postgres psql --dbname=test --username=deepak —host=127.0.0.1 --password
```

## Create User

```
CREATE USER dba WITH SUPERUSER PASSWORD 'password123';
```

**Edit the `pg_hba.conf` File:** Open the `pg_hba.conf` file in a text editor with root or appropriate permissions. Add a line to grant access to your user from a specific IP address or range. For example:

```
# TYPE  DATABASE        USER            ADDRESS                 METHOD
host    all             your_username    192.168.1.100/32         md5
```

**Reload PostgreSQL Configuration:** After editing the `pg_hba.conf` file, reload the PostgreSQL service to apply the changes:

```
sudo systemctl reload postgresql
```
## List User

```
\du
```

## List Replication Slot

```
SELECT * FROM pg_replication_slots;
```

## Drop Replication Slot

```
 SELECT pg_drop_replication_slot('slaveslot1');
```

## PG_BASE_BACKUP

Take postgresql backup in background .

```
nohup sudo pg_basebackup -h 13.201.7.67 -U replica_user -X stream -C -S slaveslot3 -P -v -R -w -D /var/lib/postgresql/14/main/ > pg_basebackup.log 2>&1 &
```




