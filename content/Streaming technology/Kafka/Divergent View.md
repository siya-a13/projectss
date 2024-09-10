---
longform:
  format: single
  title: Divergent View
title: Divergent View
---
![[zookeeper-controller-updated.jpg]]

**Communication to Kafka (K)**

- **Sources of Communication:**
    
    - **Controller**
    - **Brokers**
    - **Kafka Clients**: Producers, consumers, `kafka-acls.sh`, etc.
- **Changes in Client Communication:**
    
    - **Previous Method**: Communication load from Kafka clients was managed through Zookeeper (ZK) using the `-zookeeper` flag.
    - **Current Method**: Communication is now directed to brokers using the `-bootstrap-server` flag, which specifies a list of brokers.
- **Broker Responsibilities:**
    
    - Brokers now maintain In-Sync Replicas (ISR) information, which is updated by controllers through RPC (Remote Procedure Call).
- **Metadata Synchronization Issues:**
    
    - **Controller & Kafka**: Metadata views between the Controller and Kafka may not be in sync.
        - **Client Impact**: Client requests may timeout if Zookeeper does not have the latest ISR information.
    - **Controller & Brokers**: Metadata views between the Controller and brokers may also be out of sync.
        - **Broker Impact**: Brokers will update ISR information only after the new ISR is persisted to Zookeeper. Client requests may timeout if brokers do not have the latest ISR information.