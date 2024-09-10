---
longform:
  format: single
  title: Controlled Shutdown (CS)
title: Controlled Shutdown (CS)
---
![[controll_shutdown.png]]

**Producer/Consumer Traffic and Leader Election**

- **Producer/Consumer Traffic:**
    
    - **Old Leader**: Continues to handle traffic until new leaders are elected.
    - **New Leaders**: Traffic is then moved to the new leaders.
    - **System Availability**: The system availability is not impacted during this process.
- **Operation Time:**
    
    - **Persist in Zookeeper (ZK)**: Time required to persist metadata in Zookeeper.
    - **Propagate New Leaders**: Time required to propagate new leader information to brokers.
    - **Exclusions**: Does not include the time required for leader election.
    - **Operation Time Complexity**: O(#partitions)