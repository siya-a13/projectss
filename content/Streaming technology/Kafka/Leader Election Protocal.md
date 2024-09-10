---
longform:
  format: single
  title: Leader Election Protocal
title: Leader Election Protocal
---
![[Leader Election.png]]

**Controller Election in Quorum**

- **Controller Role**:
    
    - Every controller in the quorum is a voter
- **Failure and Election Process**:
    
    - When the active controller fails:
        - One of the voters attempts to become a candidate for the new leader
        - The candidate requests votes from each voter
- **Election Outcome**:
    
    - If the candidate receives a majority of votes (including its own):
        - The candidate becomes the new leader
    - If no majority is received within a specific timeout:
        - The election process is considered a failure
        - Another voter attempts to become a candidate, and the process repeats
- **Voting Mechanism**:
    
    - The actual voting process is based on Kafka’s voting mechanism, utilizing the concept of epochs

## Why Kraft

Replication via Quorum Replication of Raft Protocol but pull-based like Kafka
protocol.
New protocol for leader election but leverages Kafka's epoch method for voting.
A mix of Raft & Kafka protocols - Kraft