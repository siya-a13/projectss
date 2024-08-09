---
longform:
  format: single
  title: Kinesis Data Streams
title: Kinesis Data Streams
---
![[kinesis-data-stream.png]]

The architecture of Amazon Kinesis Data Streams is designed to facilitate real-time data processing at scale. It allows for the collection, processing, and analysis of streaming data, providing the flexibility to handle high-throughput, low-latency use cases. Here's an overview of the key components and how they fit together:

### **Producers**

- **Role**: Producers are data sources that continuously generate data and send it to the Kinesis Data Stream.
- **Examples**: Web applications, mobile devices, IoT sensors, servers, and event logging systems.
- **Mechanism**: Producers send data records to a specific Kinesis Data Stream using the AWS SDK, Kinesis Producer Library (KPL), or directly through the AWS CLI/API. Each data record includes a partition key that determines which shard the data will be routed to.

### **Kinesis Data Stream**

- **Role**: The core component that handles the ingestion of streaming data. A stream is divided into one or more shards, which are the units of capacity.
- **Shards**:
    - **Function**: Shards are units of parallelism in the stream. Each shard has a fixed capacity in terms of read and write operations.
    - **Capacity**: A single shard can handle up to 1 MB of data per second for writes and 2 MB per second for reads. It can support up to 1,000 write transactions per second.
- **Scaling**: The number of shards can be adjusted based on the required throughput, either manually or through automatic scaling.
- **Retention**: Data in a stream is retained for a default of 24 hours but can be extended up to 7 days.

### **Consumers**

- **Role**: Consumers read data from Kinesis Data Streams and process it. They can either process data in real-time or batch process it.
- **Types of Consumers**:
    - **Kinesis Client Library (KCL)**: Manages the complexity of reading from the stream, handling shard splits/merges, and checkpointing.
    - **AWS Lambda**: A serverless function that can be triggered by data records arriving in a stream, ideal for lightweight real-time processing.
    - **Kinesis Data Analytics**: Provides real-time processing capabilities, including running SQL queries on the streaming data to generate insights.
    - **Custom Applications**: Applications developed using the AWS SDK to consume and process data according to specific business logic.
- **Data Retrieval**: Consumers can retrieve data using shard iterators that specify the position within the shard from where to start reading.

### **Data Storage and Processing**

- **Integration**: Kinesis Data Streams integrates with various AWS services to store and process the data:
    - **Amazon S3**: For durable storage of processed or raw streaming data.
    - **Amazon Redshift**: For data warehousing and complex queries.
    - **Amazon DynamoDB**: For real-time data indexing and lookup.
    - **Amazon Elasticsearch Service**: For search and analytics.
    - **Amazon CloudWatch**: For monitoring and logging.
- **Data Pipeline**: Data can flow from producers to Kinesis, be processed in real-time by consumers, and then stored or forwarded to other AWS services for further processing or storage.

### **Scaling and Fault Tolerance**

- **Auto Scaling**: Kinesis can automatically adjust the number of shards based on throughput needs, ensuring scalability.
- **Data Replication**: Data records are replicated across multiple availability zones within a region to provide high availability and fault tolerance.
- **Checkpointing**: Consumers like KCL and AWS Lambda can checkpoint their progress, enabling them to resume processing from the correct point in the event of a failure.

### **Security**

- **Encryption**: Data at rest can be encrypted using AWS KMS, and data in transit can be secured using HTTPS.
- **Access Control**: IAM policies control access to the Kinesis Data Streams, ensuring that only authorized producers and consumers can interact with the stream.
- **VPC Endpoints**: Kinesis can be accessed within a VPC using VPC endpoints for enhanced security.

### Architectural Diagram

Here’s a high-level view of how these components interact:

```
+------------------+    +----------------------+    +---------------------+
|                  |    |                      |    |                     |
|    Producers     | -> | Kinesis Data Stream  | -> |   Consumers          |
|                  |    |    (Shards)          |    |  (Lambda, KCL, KDA,  |
|  (Web apps, IoT, |    |                      |    |   Custom Apps)       |
|  Servers, etc.)  |    +----------------------+    +---------------------+
|                  |    |                      |    |                     |
+------------------+    +----------------------+    +---------------------+
                               |
                               |
                               V
                     +---------------------+
                     |                     |
                     |  AWS Integration    |
                     |  (S3, Redshift,     |
                     |  DynamoDB, ES, etc.)|
                     |                     |
                     +---------------------+
```