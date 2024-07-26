---
title: Redshift System Tables and System Views
---
## Redshift System Tables and System Views

#### SVV metadata views

SVV views are system views in Amazon Redshift that contain information about database objects.

#### SYS monitoring views

_Monitoring views_ are system views in Amazon Redshift that are used to monitor query and workload resource usage of provisioned clusters and serverless workgroups. These views are located in the `pg_catalog` schema. To display the information provided by these views, run SQL SELECT statements.

#### STL views for logging

STL system views retain seven days of log history. Log retention is guaranteed for all cluster sizes and node types, and it isn't affected by changes in cluster workload. Log retention also isn't affected by cluster status, such as when the cluster is paused. You have less than seven days of log history only in the case where the cluster is new. You don't need to take any action to retain logs, but you have to periodically copy log data to other tables or unload it to Amazon S3 to keep log data that's more than 7 days old.

#### STV tables for snapshot data

STV tables are virtual system tables that contain snapshots of the current system data.

