---
longform:
  format: single
  title: Analyze Table
title: Analyze Table
---
## Commands to analyze table : -

	- EXPLAIN ANALYZE TABLE <table_name> \G;
	
This command is used to get detailed information about the performance and structure of a table, including statistics about its indexes and the number of rows. It's similar to `EXPLAIN`, but specifically for analyzing a table.

```
EXPLAIN ANALYZE TABLE orders \G;
```

**Output Explanation:** This will provide detailed information about the `orders` table, such as:

- The number of rows in the table.
- The number of index scans.
- The total data length.
- Whether the table's indexes are being used efficiently.
## Show indexes

	- SHOW INDEXES FROM <table_name> \G;
	
This command provides information about the indexes on a given table. It shows details such as the name of the index, the column(s) involved, and whether the index is unique or not.

```
SHOW INDEXES FROM employees \G;
```

**Output Explanation:** The output will show a list of indexes associated with the `employees` table, including:

- `Table`: The name of the table.
- `Non_unique`: Whether the index is unique (0 means unique).
- `Key_name`: The name of the index.
- `Seq_in_index`: The sequence number of the column in the index.
- `Column_name`: The name of the indexed column.
- `Cardinality`: An estimate of the number of unique values in the index.

This helps you understand how the database is optimizing queries and what indexes exist on the table.
## Explain

	- EXPLAIN SELECT * FROM cnext_user_branches_log WHERE id = 100000 \G;
	
The `EXPLAIN` command is used to analyze how a query will be executed by MySQL. It provides a breakdown of the query plan, showing how the database will retrieve the data (e.g., whether it will use indexes, perform a table scan, etc.).

```
EXPLAIN SELECT * FROM cnext_user_branches_log WHERE id = 100000 \G

```

```
+----+-------------+-----------------------------+-------+----------------+-------------+---------+------+------+-------------+
| id | select_type | table                       | type  | possible_keys  | key         | key_len | ref  | rows | Extra       |
+----+-------------+-----------------------------+-------+----------------+-------------+---------+------+------+-------------+
|  1 | SIMPLE      | cnext_user_branches_log      | ref   | idx_id         | idx_id      | 4       | const|    1 | Using where |
+----+-------------+-----------------------------+-------+----------------+-------------+---------+------+------+-------------+

```

In this example:

- The query is a `SIMPLE` query, which means it’s a basic select without any subqueries or joins.
- It uses the `idx_id` index on the `id` column (`key`).
- The query will examine 1 row (`rows`), which is an estimate.
- `Using where` means MySQL will apply the `WHERE` condition (`id = 100000`) after scanning the index.