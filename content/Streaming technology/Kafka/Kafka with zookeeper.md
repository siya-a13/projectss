---
longform:
  format: single
  title: Kafka with zookeeper
title: Kafka with zookeeper
---
Zookeeper plays a crucial role in managing and coordinating Apache Kafka, particularly in older versions where Kafka relies on Zookeeper for several key tasks. Here’s a breakdown of what Zookeeper does for Kafka:

1. **Cluster Metadata Management**: Zookeeper maintains information about the Kafka cluster's structure, including the brokers and their respective partitions. It helps Kafka brokers discover each other and coordinate their activities.
    
2. **Leader Election**: For each partition in Kafka, there is a leader broker and several follower brokers. Zookeeper is responsible for electing the leader for each partition and ensuring that the leader is consistently chosen. If the leader fails, Zookeeper helps in electing a new leader from the followers.
    
3. **Configuration Management**: Zookeeper stores and manages the configuration data of Kafka topics, including settings related to replication, partitions, and topic properties. This centralized configuration helps Kafka brokers stay in sync.
    
4. **Synchronization**: Kafka uses Zookeeper to synchronize activities between brokers. For example, it helps ensure that changes in metadata are propagated across all brokers in the cluster.
    
5. **Broker Management**: Zookeeper keeps track of which brokers are alive and available. It monitors brokers and helps manage their lifecycle, ensuring that the cluster remains consistent and robust in the face of broker failures.
    
6. **Quorum Management**: Zookeeper is used to manage the quorum needed for various Kafka operations. This ensures that operations like leader election and partition assignments are carried out consistently across the cluster.
    
7. **Offset Management (for Kafka 0.8.x and earlier)**: In earlier versions of Kafka, Zookeeper was used to manage consumer group offsets. This included tracking which messages had been consumed and managing the progress of consumer groups.
    

It’s worth noting that in recent versions of Kafka, efforts have been made to reduce Zookeeper's role through the development of Kafka’s own consensus mechanism, known as KRaft (Kafka Raft Metadata Mode). This aims to simplify the architecture by removing the dependency on Zookeeper for cluster metadata management and coordination. However, Zookeeper remains integral to many Kafka deployments and versions.