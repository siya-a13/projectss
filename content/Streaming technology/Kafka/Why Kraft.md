---
longform:
  format: single
  title: Why Kraft
title: Why Kraft
---
![[KRaft.jpg]]
## Zookeeper and Kafka are two different systems - Complexity

**Apache zookeeper Server Application for Coordinating Distributed Systems**

- **Example**: Metadata management
- **FileSystem API**: On top of a log data structure

**Apache Kafka for a Distributed Event-Streaming Platform**

- **Pub/Sub API**: Based on event-driven consensus on top of a log data structure

**Complexity for Kafka Admins**

- **Two Different Systems to Manage**
    - Configuration
    - Security
    - Monitoring
    - Networking
- **Performance Optimization Methods**: Different for each system
- **Kafka Viewed as Heavyweight Infrastructure**
    - Not a single-process deployment due to additional Kafka deployments
    - Considered primarily for scale
    - Startups may prefer simpler systems like RabbitMQ

## External Metadata Management and Scalability in Kafka

- **What is Scalability in Kafka?**
    
    - Scalability refers to Kafka's ability to add more partitions to support additional topics and data.
    
- **Impact of External Metadata Management (via Zookeeper) on Scalability:**
    
    - Time for operations involving metadata movement between Zookeeper and the Kafka Controller increases with the number of partitions (O(#partitions)).
    
- **Key Operations Affected:**
    
    - **Controlled Shutdown (CS)**
    - **Uncontrolled Shutdown & Recovery (USR)**
    - **Controller Failover & Recovery (CFR)**
    
- **Effects of Increased Partitions:**
    
    - **Increased Metadata**: More metadata about partitions is generated.
    - **Increased Data Movement**: More data needs to be transferred between Zookeeper and the Controller.
    - **Increased Operation Time**: More time is required for the above operations.
    
- **Performance Impact:**
    
    - The performance of the Kafka cluster can be negatively affected by the increased time required for metadata operations.
    
- **Divergent Views:**
    
    - Metadata views may become inconsistent between Zookeeper, the Controller, and Brokers.