---
longform:
  format: single
  title: Benchmark PostgreSQL
---
These commands are for benchmarking a PostgreSQL database using `sysbench`, specifically focusing on OLTP (Online Transaction Processing) read-write workloads.

## Pgbench

```
pgbench -i -s 50 -h 127.0.0.1 -p 5432 -U dba test
```

## Command 1: Preparation Phase

```
sysbench oltp_read_write --db-driver=pgsql --pgsql-db=sysbench_test --pgsql-host=52.66.63.7 --pgsql-port=5432 --pgsql-user=deepak --pgsql-password=password123 --tables=1 --table-size=4000000 prepare
```

**Explanation:**

- **`sysbench oltp_read_write`**: Indicates that you are running a test based on an OLTP read-write workload.
- **`--db-driver=pgsql`**: Specifies that the database driver is PostgreSQL.
- **`--pgsql-db=sysbench_test`**: Defines the target PostgreSQL database as `sysbench_test`.
- **`--pgsql-host=52.66.63.7`**: Specifies the PostgreSQL server’s IP address.
- **`--pgsql-port=5432`**: Defines the port on which PostgreSQL is listening (default is 5432).
- **`--pgsql-user=deepak`**: Uses `deepak` as the PostgreSQL user for the connection.
- **`--pgsql-password=password123`**: Specifies the password for the `deepak` user.
- **`--tables=1`**: Defines the number of tables to create for the test, which is 1.
- **`--table-size=4000000`**: Sets the size of the table to 4 million rows.
- **`prepare`**: This prepares the test by creating and populating the tables with the specified number of rows.

## Command 2: Running the Benchmark

```
sysbench oltp_read_write --threads=2 --db-driver=pgsql --pgsql-db=sysbench_test --pgsql-host=52.66.63.7 --pgsql-port=5432 --pgsql-user=deepak --pgsql-password=password123 --tables=1 --table-size=4000000 --time=10000 --report-interval=1 --events=0 --delete-inserts=10 --index-updates=10 --non-index-updates=10 --db-ps-mode=disable run
```

**Explanation:**

- **`sysbench oltp_read_write`**: Again, indicates that you are running an OLTP read-write test.
- **`--threads=2`**: Specifies that the benchmark will run with 2 parallel threads.
- **`--db-driver=pgsql`**: PostgreSQL is the database driver in use.
- **`--pgsql-db=sysbench_test`**: Target database is `sysbench_test`.
- **`--pgsql-host=52.66.63.7`**: Specifies the PostgreSQL server’s IP address.
- **`--pgsql-port=5432`**: PostgreSQL is listening on port 5432.
- **`--pgsql-user=deepak`**: Uses `deepak` as the PostgreSQL user.
- **`--pgsql-password=password123`**: Password for the `deepak` user.
- **`--tables=1`**: Number of tables involved in the test is 1.
- **`--table-size=4000000`**: Each table contains 4 million rows.
- **`--time=10000`**: The benchmark will run for 10,000 seconds (approximately 2 hours and 46 minutes).
- **`--report-interval=1`**: The progress report will be printed every second.
- **`--events=0`**: The benchmark will run indefinitely or until the time limit is reached.
- **`--delete-inserts=10`**: Specifies that 10% of the operations will be DELETEs followed by INSERTs (to simulate updates).
- **`--index-updates=10`**: Indicates that 10% of the operations will be updates to indexed columns.
- **`--non-index-updates=10`**: Indicates that 10% of the operations will be updates to non-indexed columns.
- **`--db-ps-mode=disable`**: Disables the use of server-side prepared statements, meaning each query will be parsed and planned separately.
- **`run`**: This command starts the actual benchmarking process.

**Summary**: The first command prepares the PostgreSQL database by creating a table and populating it with 4 million rows. The second command runs a read-write performance test on this table using 2 parallel threads for 10,000 seconds, with specific operational percentages for deletes, inserts, and updates.