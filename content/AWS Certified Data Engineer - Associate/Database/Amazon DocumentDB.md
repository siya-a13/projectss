---
title: Amazon DocumentDB
---
DocumentDB is a fully managed document database service provided by AWS that is compatible with MongoDB. It is designed to offer high performance, scalability, and availability for applications that require a flexible, document-oriented data model.

## Key Features of DocumentDB:

### Compatibility with MongoDB:

DocumentDB is compatible with MongoDB 3.6 and 4.0 API, which means you can use existing MongoDB drivers, applications, and tools (like Compass or Studio 3T) with DocumentDB seamlessly. This makes it easier to migrate existing MongoDB workloads to DocumentDB without needing to rewrite code.

### Fully Managed Service:

AWS handles routine database tasks such as hardware provisioning, setup, configuration, patching, backups, and scaling. This allows developers to focus more on building applications rather than managing infrastructure.

### Scalability:

DocumentDB supports horizontal scaling (scaling out) by automatically distributing data across multiple instances using sharding. This helps in handling growing workloads and provides high throughput and low latency for read-intensive and write-intensive applications.

### High Availability:

DocumentDB replicates your data across multiple Availability Zones (AZs) within a AWS Region to provide fault tolerance and high availability. It automatically handles failovers and ensures that your database remains operational in the event of a hardware failure or other issues.

### Security:

DocumentDB integrates with AWS Identity and Access Management (IAM) for authentication and authorization. It supports encryption at rest using AWS Key Management Service (KMS) and encryption in transit using TLS.

### Backup and Restore:

DocumentDB provides automated backups that are enabled by default, allowing you to restore your database to any point within your specified retention period (up to 35 days). This helps in data protection and recovery.

### Performance Monitoring and Metrics:

AWS CloudWatch provides performance metrics and monitoring for DocumentDB clusters. You can set alarms and automate actions based on these metrics to maintain performance and availability.

### Global Clusters:

DocumentDB supports global clusters, which allows you to deploy clusters that span multiple AWS Regions. This feature enables low-latency global read and write capabilities for your applications, serving users in different geographic locations.