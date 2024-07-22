---
title: Amazon Keyspaces (for Apache Cassandra)
---
AWS Keyspaces is a fully managed, serverless, scalable Apache Cassandra-compatible database service provided by Amazon Web Services (AWS). It is designed to handle high availability and performance requirements of Cassandra workloads without the need for managing the underlying infrastructure.

## Key Features of AWS Keyspaces:

### Apache Cassandra Compatibility:

AWS Keyspaces is fully compatible with Apache Cassandra 3.11. This compatibility ensures that you can use existing Cassandra Query Language (CQL) and APIs, allowing seamless migration of Cassandra workloads to AWS Keyspaces without modifying your applications.

### Serverless and Managed:

AWS Keyspaces is a serverless service, which means AWS manages the infrastructure provisioning, setup, scaling, patching, and maintenance tasks automatically. This allows developers to focus more on building applications rather than managing databases.

### **Scalability:**

AWS Keyspaces scales automatically based on your workload demands. It supports multi-region replication, allowing you to deploy globally distributed applications with low-latency access to data.

### High Availability:

AWS Keyspaces replicates data across multiple Availability Zones (AZs) within an AWS Region to provide fault tolerance and high availability. It automatically handles hardware and software failures, ensuring that your database remains operational.

### **Security:**

AWS Keyspaces integrates with AWS Identity and Access Management (IAM) for authentication and authorization. It supports encryption at rest using AWS Key Management Service (KMS) and encryption in transit using TLS.

### Backup and Restore:

AWS Keyspaces provides continuous backups with point-in-time recovery. This feature allows you to restore your data to any second within your specified retention period (up to 35 days), helping protect against accidental data loss.



