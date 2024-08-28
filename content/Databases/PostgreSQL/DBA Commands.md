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
nohup sudo pg_basebackup -h 13.201.7.67 -U replica_user -X stream -C -S slaveslot3 -P -v -R -w -D /var/lib/postgresql/14/main/ > pg_basebackup.log 2>&1 &
```