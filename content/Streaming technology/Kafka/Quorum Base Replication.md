---
longform:
  format: single
  title: Quorum Controller
title: Quorum Controller
---
![[Quorum Controller.png]]

**Quorum-Based Replication**

- **Quorum Definition**:
    
    - Based on majority instead of requiring all nodes
- **Replication Mechanism**:
    
    - **Quorum Replication**: Pull-based
    - Leader handles all write operations
    - Followers make fetch requests to the leader (pull-based)
- **Commit Process**:
    
    - The leader commits a write after receiving acknowledgments (acks) from a majority of followers, including itself
    - **Ack**: Request for the next write from a follower
- **Trade-offs**:
    
    - Balances between replication latency and delivery guarantee
- **ISR Concept**:
    
    - New concept of ISR (In-Sync Replicas) introduced for controller replicas
- **Protocol Implementation**:
    
    - Implemented by the Raft protocol

#### To tolerate N failures, a quorum need to have
2N + 1 replicas