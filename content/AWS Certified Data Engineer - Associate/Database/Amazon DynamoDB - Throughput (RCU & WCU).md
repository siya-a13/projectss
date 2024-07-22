---
title: Amazon DynamoDB - Throughput (RCU & WCU)
---
### Provisioned Mode (default)

- You specify the number of reads/writes per second
- You need to plan capacity beforehand
- Pay for provisioned read & write capacity units
### On-Demand Mode

- Read/writes automatically scale up/down with your workloads
- No capacity planning needed
- Pay for what you use, more expensive
- You can switch between different modes once every 24 hours

### Write Capacity Units (WCU)

- One Write Capacity Unit (WCU) represents one write per second for an
item up to I KB in size
- If the items are larger than I KB, more WCUs are consumed

##### Example I: we write 10 items per second, with item size 2 KB

- We need 10 * (2 kb / 1 kb ) = 20 WCUs
##### Example 2: we write 6 items per second, with item size 4.5 KB

- We need 6 * ( 5 kb / 1 kb ) = 30 WCUs (4.5 gets rounded to the upper KB)
##### Example 3: we write 120 items per minute, with item size 2 KB

- We need (120 / 60 ) * ( 2 kb / 1 kb ) = 4 WCUs

## Strongly Consistent Read vs. Eventually Consistent Read

### Eventually Consistent Read (default)

- If we read just after a write, it's possible we'll get some stale data because of replication

### Strongly Consistent Read

- If we read just after a write, we will get the correct data
- Set "ConsistentRead" parameter to True in API calls (Getltem, BatchGetltem, Query, Scan)
- Consumes twice the RCU

## DynamoDB - Read Capacity Units (RCU)

- One Read Capacity Unit (RCU) represents one Strongly Consistent Read per second, or two Eventually Consistent Reads per second, for an item up to 4 KB in size
- If the items are larger than 4 KB, more RCUs are consumed

##### Example I: 10 Strongly Consistent Reads per second, with item size 4 KB

- We need 10 * (4 kb / 4 kb) = 10 RCUs

##### Example 2: |6 Eventually Consistent Reads per second, with item size 12 KB

- We need  (16 / 2) * ( 12 KB /  4 KB ) = 24 RCUs

##### Example 3: 10 Strongly Consistent Reads per second, with item size 6 KB

- We need 10 * (8 kb/ 4 kb) = 20 RCUs (we must round up 6 KB to 8 KB)

## DynamoDB-Throttling

- If we exceed provisioned CUs or WCUs, we get "ProvisionedThroughputExceededException"
- Reasons:
	- Hot Keys - one partition key is being read too many times (e.g. popular item)
	- Hot Partitions
	- Very large items, remember RCU and WCU depends on size of items
- Solutions:
	- Exponential backoff when exception is encountered (already in SDK)
	- Distribute partition keys as much as possible
	- If RCU issue, we can use DynamoDB Accelerator (DAX)













