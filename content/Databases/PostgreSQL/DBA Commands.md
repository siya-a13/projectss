---
longform:
  format: single
  title: DBA Commands
title: DBA Commands
---
## Databases 

- #### Size of all databases 

	To find the size of all databases in a PostgreSQL instance in gigabytes (GB), you can modify the query to convert the size to GB:

```
SELECT 
    pg_database.datname AS database_name,
    pg_database_size(pg_database.datname) / (1024 * 1024 * 1024) AS size_gb
FROM 
    pg_database
ORDER BY 
    pg_database_size(pg_database.datname) DESC;
```

## Table

- #### View Table Structure

	To view the structure of a table in PostgreSQL, you can use the `\d` command in the `psql` command-line interface. This command displays the schema of a table, including column names, data types, indexes, and constraints.

```
\d table_name
```

## Switchover To Master

Promote the standby server to become the new primary by running the following command.

```
SELECT pg_promote();
```

## PG_BASE_BACKUP

Take postgresql backup in background .

```
nohup pg_basebackup -h 172.31.33.236 -U replica_user -X stream -C -S slaveslot5 -P -w -v -R -D ./main/ > pg_basebackup.log 2>&1 &
```

- #### Use `pg_basebackup` with the `.pgpass` file

When running `pg_basebackup`, specify the host and user directly in the command. The password will be automatically picked from the `.pgpass` file.

```
localhost:5432:*:myuser:mypassword
```

**Set permissions** (important for security):

```
chmod 600 ~/.pgpass
```

## Active connection


```
SELECT
    usename,
    ssl,
    client_addr,
    application_name,
    state
FROM
    pg_stat_ssl
JOIN
    pg_stat_activity
ON
    pg_stat_ssl.pid = pg_stat_activity.pid;
```
