---
longform:
  format: single
  title: Ordering Guarantee
title: Ordering Guarantee
---
### **Ordering Guarantee Using Key**

![[Kafka-Guarantee-Ordering.png]]

In Kafka, messages are written to topics and each topic is divided into partitions. Each partition is an ordered log of messages. Kafka guarantees that messages with the same key are written to the same partition. This ensures that the order of messages with the same key is preserved. Here's how it works:

- **Partitioning**: When you produce a message to Kafka, you can specify a key. Kafka uses this key to determine the partition to which the message will be written. This ensures that all messages with the same key go to the same partition.
- **Ordering**: Within a partition, Kafka maintains the order of messages. Thus, if you produce several messages with the same key, Kafka will ensure they are written in the order they were received. However, ordering between different keys or across partitions is not guaranteed.