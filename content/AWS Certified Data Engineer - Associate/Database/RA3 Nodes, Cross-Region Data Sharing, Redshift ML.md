---
title: RA3 Nodes, Cross-Region Data Sharing, Redshift ML
---
## RA3 Nodes:

RA3 nodes are a type of node in Amazon Redshift that introduce managed storage and compute separation, providing increased flexibility and cost efficiency for data warehousing workloads. Here are key aspects of RA3 nodes:

#### **Managed Storage and Compute Separation**:

- RA3 nodes decouple storage and compute, allowing you to independently scale and manage each resource according to your workload requirements.

- Compute resources are dedicated to query processing, while storage is managed separately using managed storage volumes (MSVs).
#### **Managed Storage Volumes (MSVs)**:

- RA3 nodes use MSVs to store data. These volumes are backed by Amazon S3 and are automatically managed by Redshift.

- MSVs allow you to scale storage capacity independently of compute resources, optimizing costs by paying only for the storage capacity you use.
#### **Performance and Flexibility**:

- RA3 nodes are designed to improve performance by dynamically managing data placement and utilizing caching mechanisms to reduce query latency.

- They offer flexibility in scaling compute resources up or down independently of storage, enabling you to adapt to changing workload demands without downtime.

## Cross-Region Data Sharing:

Cross-Region Data Sharing in Amazon Redshift enables you to securely and efficiently share data across different AWS regions without the need for data replication. Key features include:

#### **Secure Data Sharing**:

- Data can be shared across AWS accounts and regions securely using Redshift-managed IAM roles and encrypted data transfer.

- This eliminates the need for data movement or replication, reducing complexity and operational overhead.
#### **Granular Data Control**:

- You can selectively share specific databases, schemas, or tables with other AWS accounts in different regions.

- Fine-grained access controls ensure that data access is restricted to authorized users and applications.

#### **Efficient Data Access**:

- Shared data can be accessed directly from the consumer cluster in the recipient AWS region, providing low-latency access to data without additional data transfer costs.

- Consumers can query shared data seamlessly as if it were local to their own Redshift cluster.

## Redshift ML:

Redshift ML integrates machine learning capabilities directly into Amazon Redshift, enabling data analysts to build, train, and deploy machine learning models using SQL commands. Key aspects include:

#### **SQL-Based Machine Learning**:

- Redshift ML allows you to use familiar SQL syntax to create and manage machine learning models directly within your Redshift clusters.

- You can train models using SQL commands without needing to move data to external systems or use complex data pipelines.

#### **Integration with SageMaker**:

- Under the hood, Redshift ML leverages Amazon SageMaker for model training and deployment, ensuring scalability, performance, and integration with the broader AWS ecosystem.

- Models trained using Redshift ML can be deployed directly into Redshift for inference, allowing seamless integration of machine learning insights into your data warehouse workflows.