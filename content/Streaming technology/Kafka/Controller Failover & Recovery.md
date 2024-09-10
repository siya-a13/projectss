---
longform:
  format: single
  title: Controller Failover & Recovery
title: Controller Failover & Recovery
---
![[Controller failover & recovery.png]]

**Operation Time During Controller Failover**

- **Operation Time:**
    
    - **Time for New Controller Election**: Duration required to elect a new Kafka Controller.
    - **Time for Loading Metadata**: Duration for the new Controller to load the entire metadata from Zookeeper (ZK).
    - **Time for New Leader Election for Partitions**: Duration required to elect new leaders for partitions.
    - **Time to Persist in Zookeeper (ZK)**: Duration required to persist metadata in Zookeeper.
    - **Time to Propagate New Leaders**: Duration required to propagate new leader information to other brokers.
    f
- **Impact on Kafka Cluster:**
    
    - **Until Metadata Loading is Complete**: The entire Kafka cluster is unavailable.
        - **Loading Time Complexity**: O(#partitions)
    - **Until New Leaders Are Elected**: Partitions PA and PB are unavailable.
        - **Entire Operation Time Complexity**: O(#partitions)