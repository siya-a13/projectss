---
title: Shared and exclusive locks in RDS
---
## Shared Locks:

Shared locks (also known as read locks) are used when a transaction needs to read data without intending to modify it. Multiple transactions can hold shared locks on the same resource simultaneously, allowing concurrent reads but preventing any transaction from modifying the data while it is being read.

#### Example

Imagine a scenario where you have a table `Orders` in an RDS MySQL database. Several users are simultaneously querying this table to view orders without intending to update them.

- **Transaction 1:** User A runs a `SELECT * FROM Orders WHERE status = 'pending';`
	- This transaction acquires a shared lock on the rows it reads, ensuring that other transactions can also read the same rows concurrently but cannot modify them until this transaction releases its lock.
	
- **Transaction 2:** User B concurrently runs `SELECT COUNT(*) FROM Orders WHERE status = 'pending';`
	- This transaction also acquires shared locks on the rows it reads (if any), ensuring consistency and preventing interference with Transaction 1's read operation.

## Exclusive Locks:

Exclusive locks (also known as write locks) are used when a transaction intends to modify data. Only one transaction can hold an exclusive lock on a resource at any given time. This ensures that no other transaction can read or modify the data until the exclusive lock is released.

#### Example

Continuing with the `Orders` table example:

- **Transaction 3:** User C wants to update the status of an order from 'pending' to 'processed'. The SQL statement might be `UPDATE Orders SET status = 'processed' WHERE order_id = 123;`
	- This transaction acquires an exclusive lock on the row(s) it modifies (`order_id = 123` in this case). This prevents other transactions from reading or modifying this specific row until Transaction 3 completes and releases its lock.