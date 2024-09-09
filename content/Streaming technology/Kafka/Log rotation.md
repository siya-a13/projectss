---
longform:
  format: single
  title: Log rotation
title: Log rotation
---

###  **Retention Policy**

Kafka provides different ways to manage how long messages are retained. There are two main types of retention policies:

- **Time-Based Retention (`log.retention.ms`)**: This policy allows you to specify how long Kafka should retain messages in a topic before they are eligible for deletion. For example, you might configure Kafka to keep messages for 7 days. After this period, the messages are eligible for deletion, even if they haven’t reached the segment size limit.
    
- **Size-Based Retention (`log.retention.bytes`)**: This policy controls how much total disk space the logs for a topic can use. If the total size of the log segments in a topic exceeds this limit, older segments are deleted to free up space. This ensures that the disk usage doesn’t exceed the configured limit.
    

### **Log Cleaner**

The log cleaner is a background process in Kafka responsible for cleaning up old messages that are no longer needed based on the configured retention policies. It handles:

- **Compaction**: In addition to retention based on time or size, Kafka supports log compaction. Log compaction ensures that Kafka retains the latest message for each key in a topic, even if messages are older than the retention period. This is useful for scenarios where you want to keep the latest state of a record rather than all historical messages.