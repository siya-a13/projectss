---
title: Demo Setup for performing all locking scenarios
---
## Setup MYSQL 

Setup MYSQ with docker [[MYSQL Container]]
## Create Database 

```
Create database sysbench_test
```

## Populate table rows with sysbench utility

```
sysbench oltp_read_write --db-driver=mysql --mysql-db=sysbench_test --mysql-host=127.0.0.1 --mysql-port=3306 --mysql-user=root --mysql-password=secret_pwd --tables=1 --table-size=4000000 prepare
```

Above command will populate the table named sbtest1 with 4000000 rows.

## Perform Ongoing Changes

```
sysbench oltp_read_write --threads=2 --db-driver=mysql --mysql-db=sysbench_test --mysql-host=127.0.0.1 --mysql-port=3306 --mysql-user=root --mysql-password=secret_pwd --tables=1 --table-size=4000000 --time=10000 --report-interval=1 --events=0 --delete-inserts=10 --index-updates=10 --non-index-updates=10 --db-ps-mode=disable run
```

Above command will perform Insert / Update / Delete operation on table.

## Alter table with ALGORITHM=COPY, LOCK=SHARED

```
ALTER TABLE sbtest1 ADD INDEX idx_k(k),ALGORITHM=COPY,LOCK=SHARED
```

Untill above command will finish executing only SELECT query will execute i.e only reads are allowed.

## Alter table with ALGORITHM=COPY, LOCK=EXCLUSIVE

```
ALTER TABLE sbtest1 ADD INDEX idx_k(k),ALGORITHM=COPY,LOCK=EXCLUSIVE
```

Untill above command will finish executing read / writes both are locked i.e SELECT / UPDATE / DELETE will not execute.

## Alter table with ALGORITHM=INPLACE, LOCK=NONE

```
ALTER TABLE sbtest1 ADD INDEX idx_k(k),ALGORITHM=INPLACE,LOCK=NONE;
```

Log file stores the data inserted , update , deleted in the table during DDL operation . Here you won't see any locking issue.

 Note - pay attention to `Innodb_online_alter_log_max_size` variable .