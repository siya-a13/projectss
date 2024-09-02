---
longform:
  format: single
  title: Amazon S3 - Replication
---
AWS S3 replication is a feature that allows you to automatically and asynchronously replicate objects across different S3 buckets. This is useful for scenarios like disaster recovery, data sovereignty requirements, or low-latency access in different regions.

![[s3-replication.png]]

### Types of Replication in S3:

1. **Cross-Region Replication (CRR)**:
    
    - Replicates objects from one bucket to another bucket in a different AWS region.
    - Useful for reducing latency by placing data closer to users in different regions, meeting compliance requirements for data storage, and disaster recovery.
2. **Same-Region Replication (SRR)**:
    
    - Replicates objects from one bucket to another bucket within the same AWS region.
    - Useful for creating backups, or managing data across different business units or teams within the same region.
### Key Features:

- **Bidirectional Replication**: You can configure replication rules that replicate objects from Bucket A to Bucket B and vice versa.
- **Prefix or Tag-Based Filtering**: You can replicate only a subset of objects by filtering based on object prefixes or tags.
- **Replication Time Control (RTC)**: Guarantees that 99.99% of objects are replicated within 15 minutes.

### How to Set Up S3 Replication:

1. **Enable Versioning**:
    
    - Both source and destination buckets must have versioning enabled.
2. **Create an IAM Role**:
    
    - The IAM role needs permission to read from the source bucket and write to the destination bucket.
3. **Set Up a Replication Rule**:
    
    - Define the source bucket, destination bucket, replication rule (e.g., replicate all objects, or based on specific prefixes/tags), and enable options like RTC if needed.
4. **Monitor Replication**:
    
    - Use CloudWatch metrics to monitor the replication status and troubleshoot issues if any arise.

### Considerations:

- **Replication is one-way by default**: Objects in the destination bucket are not replicated back to the source bucket.
- **Storage Class**: You can choose to replicate objects into a different storage class (e.g., Standard to Standard-IA) in the destination bucket.
- **Cost**: You incur costs for both storage in the destination bucket and the replication traffic.
