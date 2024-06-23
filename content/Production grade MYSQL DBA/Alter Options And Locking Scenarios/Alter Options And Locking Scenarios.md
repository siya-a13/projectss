---
title: Alter Options And Locking Scenarios
---
## Algorithm Option

This option is typically used in statements that alter the structure of tables, such as `ALTER TABLE`. It controls how MySQL will perform the operation.

- **ALGORITHM**: Specifies the algorithm to use for the operation.

	- `DEFAULT`: Uses the default algorithm chosen by MySQL based on the operation and table type.
	
	- `INPLACE`: Attempts to perform the operation in place, which means it tries to modify the table's structure without requiring a complete table copy. This option is often faster for large tables but may not be supported for all operations or table types.
	
	- `COPY`: Forces MySQL to use a copy algorithm, where it creates a new table with the altered structure and then replaces the old table with the new one. This approach ensures consistency but can be slower for large tables.

## Lock Option

This option specifies the locking strategy to use during the execution of certain statements, primarily `SELECT` and `UPDATE`.

- **LOCK**: Specifies the type of lock to use.

	- `DEFAULT`: Uses the default locking strategy determined by MySQL.
	
	- `NONE`: Specifies that no explicit locking should be used.
	
	- `SHARED`: Specifies a shared lock, allowing other sessions to read but not modify the locked rows.
	
	- `EXCLUSIVE`: Specifies an exclusive lock, preventing other sessions from reading or modifying the locked rows.
## [[Demo Setup]]