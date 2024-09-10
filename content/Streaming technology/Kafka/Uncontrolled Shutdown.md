---
longform:
  format: single
  title: Uncontrolled Shutdown (CS)
title: Uncontrolled Shutdown
---
![[Uncontrolled_shutdown.png]]

**Impact of Leader Election on Partitions**

- **Until New Leaders Are Elected:**
    
    - **Partitions PA and PB**: These partitions are unavailable.
    - **Producer/Consumer Traffic**: Traffic to and from these partitions will be impacted.
- **Operation Time:**
    
    - **Time for Leader Election**: Duration required to elect new leaders.
    - **Time to Persist in Zookeeper (ZK)**: Duration required to persist metadata in Zookeeper.
    - **Time to Propagate New Leaders and ISR**: Duration required to propagate new leader information and In-Sync Replicas (ISR) to brokers.
    - **Operation Time Complexity**: O(#partitions)