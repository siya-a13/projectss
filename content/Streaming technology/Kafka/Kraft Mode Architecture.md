---
longform:
  format: single
  title: Kraft Protocol
title: Kraft Mode Architecture
---
![[Krafpt_protocal.png]]

**Metadata Storage and Management**

- **Internal Topic for Metadata**: `__cluster_metadata`
- **Latest Metadata Tracked By**: Offset
- **Topic Configuration**:
    - 1 Partition
- **Metadata Partition/Log**:
    - Each controller will have a replica of this partition
    
- **Example (Kafka Topic Creation)**:
	- Metadata might be represented as:
	
```
{
  "topicId": "AAm]KnzO",
  "partitionId": 0,
  "leader": "2",
  "ISR": "[0,1,2]"
}
```

- **Snapshot Management**:
    - Metadata partition periodically abridged by snapshots
- **Data Retention Policy**: Snapshot
- Metadata replication via event-source storage model rather than RPC call in zookeeper base model.
- No more divergent view among controller.

## Controller failure scenario in kraft

![[metadata_cache.png]]

**Broker Nodes: Observers**

- **Role**:
    - Called observers
    - Cannot become the active controller if the current controller fails
- **Responsibilities**:
    - Replicate the metadata topic
    - Replicate metadata
    - Required for ISR (In-Sync Replicas) and leader information
- **Consistency**:
    - Ensures no divergent views between controller and broker
    - Eliminates the need for additional RPC (Remote Procedure Call) calls
- **Configuration**:
    - Can be configured to become a controller later, if needed