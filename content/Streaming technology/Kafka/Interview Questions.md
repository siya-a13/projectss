---
longform:
  format: single
  title: Interview Questions
title: Interview Questions
---
- ## What is Apache Kafka ?

Apache Kafka is a distributed event streaming platform designed for high-throughput, low-latency data streaming and processing. It was originally developed by LinkedIn and later open-sourced as an Apache project. Kafka is widely used in various industries for building real-time data pipelines and streaming applications.

## Must Know terminology


1. **Kafka Topic**: A topic in Kafka is a logical channel where messages are published. Each topic has multiple partitions that allow Kafka to scale horizontally. Producers write to topics, and consumers read from them. Partitions in topics help distribute data and improve performance.
    
2. **Message Size**: Kafka messages can vary in size, with a default limit of 1MB. You can increase it by adjusting the `message.max.bytes` configuration. Large messages can lead to higher latency and lower throughput, so optimal sizing is crucial.
    
3. **Replication Factor**: This determines how many copies of the data exist in Kafka across brokers. A higher replication factor improves fault tolerance but increases storage costs. The typical value is 3, meaning the data is stored in three brokers for redundancy.
    
4. **Kafka Configuration**: Kafka can be fine-tuned through various configurations like `num.partitions`, `log.retention.ms`, `compression.type`, `auto.create.topics.enable`, and `replication.factor`. These configurations manage behavior like retention policies, compression, and partitioning.
    
5. **Kafka Connector**: Kafka Connect is a tool for integrating Kafka with external systems such as databases or file systems. It provides connectors for common systems (JDBC, Elasticsearch, S3, etc.), facilitating seamless data import/export.
    
6. **Kafka Brokers and Kraft Mode**: Kafka brokers are individual servers in the Kafka cluster. They store topics and handle data streams. Kraft mode eliminates the need for Apache ZooKeeper for metadata management by integrating it directly into Kafka brokers.
    
7. **Load Testing**: Load testing involves using tools like Apache JMeter or open-source Kafka tools to simulate high message volumes. It's essential to identify performance bottlenecks, such as message throughput, latency, and consumer lag.
    
8. **Kafka Backup**: Kafka can be backed up using tools like Confluent Replicator or Kafka MirrorMaker. Backup strategies ensure data safety across clusters and regions. Snapshots and offloading to storage like S3 can also be used.
    
9. **Kafka Resource Allocation**: Allocate resources by tuning parameters like memory (`Xmx`), disk throughput, and partition allocation. Kafka clusters should be sized appropriately based on workload. Monitoring resource utilization helps optimize broker performance.
    
10. **Schema**: Kafka can enforce schemas using Schema Registry, which stores and enforces schema evolution (backward/forward compatibility). Avro, JSON, or Protobuf schemas are common, enabling strong data typing.
    
11. **Kafka Authentication and Authorization**: Kafka supports security through SASL (Simple Authentication and Security Layer) and SSL. For authorization, ACLs (Access Control Lists) are used to define which users or groups can access which topics or operations.
    
12. **Kafka Metrics**: Metrics provide insight into Kafka's performance. Tools like Prometheus and Grafana can track key metrics such as `message-in-rate`, `consumer lag`, `under-replicated-partitions`, `disk usage`, and `request latency`.
    
13. **Kafka Consumer Lag**: Consumer lag measures the difference between the last committed message and the latest message in the partition. High lag indicates that consumers are not keeping up, potentially leading to data delays.
    
14. **Kafka Consumer Groups**: A consumer group is a set of consumers that share the work of consuming from a topic's partitions. Kafka distributes partitions among consumers, providing parallelism and load distribution.
    
15. **Kafka Migration Strategies**: Migrating Kafka involves strategies like blue-green deployments, where both clusters run in parallel until the new setup is validated. Data migration can be done using tools like MirrorMaker.
    
16. **MirrorMaker and Its Uses**: MirrorMaker is used for replicating data between Kafka clusters, often for disaster recovery, data backup, or multi-datacenter setups. It enables easy synchronization of topic data across regions.
    
17. **Confluent Kafka (Managed Service)**: Confluent Kafka is a managed Kafka service that abstracts infrastructure management. It provides tools like Confluent Schema Registry, Kafka Connect, and KSQL, simplifying operations and offering enterprise features.
    
18. **Velero-Kafka Backup**: Velero is typically used for Kubernetes cluster backup and restore, but can also be configured with Kafka to back up Kafka cluster configurations or broker states, ensuring disaster recovery.
    
19. **CI/CD Pipeline**: In Kafka environments, a CI/CD pipeline involves automated deployments of Kafka configuration changes, topic management, and schema evolution. Tools like Jenkins, GitLab CI, and ArgoCD are commonly used.
    
20. **Kafka Version Upgradation**: Kafka upgrades should follow a step-by-step approach. First, update brokers, then the producers and consumers. Upgrades should be planned carefully with backward compatibility in mind, using rolling upgrades to avoid downtime.
    