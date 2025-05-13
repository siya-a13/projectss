---
longform:
  format: single
  title: Kafka Key Observability Metrices
title: Kafka Key Observability Metrices
---
## 🧭 High-Level Categories

|Layer|Focus|
|---|---|
|Broker|Cluster health, request load|
|Producer|Message throughput, retries|
|Consumer|Lag, processing rates|
|Topic/Partition|Distribution, replication|
|JVM/System|Heap, GC, file descriptors|

---

## 🔧 **1. Kafka Broker Metrics**

These are crucial for **cluster stability** and performance:

|Metric|Description|
|---|---|
|`kafka.server.BrokerTopicMetrics.MessagesInPerSec`|Number of messages received per second|
|`kafka.server.BrokerTopicMetrics.BytesInPerSec` / `BytesOutPerSec`|Ingress and egress throughput|
|`kafka.server.ReplicaManager.PartitionCount`|Number of partitions handled|
|`kafka.server.ReplicaManager.UnderReplicatedPartitions` ⚠️|Should be `0`; indicates replication problems|
|`kafka.controller.KafkaController.ActiveControllerCount`|Should be exactly `1`|
|`kafka.controller.ControllerStats.UncleanLeaderElectionsPerSec` ⚠️|Should be `0`; otherwise may cause data loss|
|`kafka.network.RequestMetrics.RequestsPerSec` (per request type)|Traffic volume for `Produce`, `Fetch`, etc.|
|`kafka.server.ReplicaFetcherManager.MaxLag`|Replication delay between leader and follower|

---

## 🧑‍💻 **2. Producer Metrics**

Monitored per client/application; key for write reliability and performance.

|Metric|Description|
|---|---|
|`record-send-rate`|Records sent per second|
|`record-retry-rate` ⚠️|Number of retries due to transient errors|
|`record-error-rate` ⚠️|Number of failed record sends|
|`request-latency-avg`|Average time to complete a request|
|`batch-size-avg`|Size of message batches|
|`compression-rate-avg`|Efficiency of compression (if enabled)|
|`bufferpool-wait-time-total`|Time producer waits for buffer availability|

---

## 📥 **3. Consumer Metrics**

Vital for detecting **lag**, which indicates whether consumers are keeping up.

|Metric|Description|
|---|---|
|`records-consumed-rate`|Messages consumed per second|
|`fetch-latency-avg`|Average fetch time from broker|
|`fetch-rate`|Number of fetches per second|
|`records-lag` ⚠️|Number of messages behind the head of the partition|
|`records-lag-max` ⚠️|Max lag across partitions|
|`commit-latency-avg`|Offset commit duration|

---

## 📊 **4. Topic and Partition Metrics**

These give insight into **distribution, performance, and durability**.

|Metric|Description|
|---|---|
|Partitions per topic|Should be balanced across brokers|
|Under-replicated partitions ⚠️|Indicates a fault tolerance issue|
|ISR (in-sync replicas) size|Should equal replication factor|
|Log size per partition|Helps with storage forecasting|

---

## ☕ **5. JVM & System Metrics (All Kafka Services)**

Kafka runs on the JVM — so monitor JVM health too:

|Metric|Description|
|---|---|
|Heap usage|Track `MemoryPool` metrics to prevent OOM|
|Garbage collection time (GC count/duration)|Especially `G1` or `OldGen` pauses|
|Thread count|Spike can indicate leaks or deadlocks|
|File descriptors used|Especially on large broker nodes|
|Disk I/O and space usage|Ensure disk isn't bottlenecked or full|
|Network throughput|Helps correlate broker data with infra layer|

---

## 📈 Recommended Tools

- **Prometheus + Grafana** (via JMX Exporter)
- **Confluent Control Center** (for Confluent Kafka)
- **Datadog, New Relic, or Splunk** (for enterprise observability)
- **Burrow or Cruise Control** (consumer lag and rebalance)

---

## 🚨 Alerts You Should Definitely Set

|Alert|Why|
|---|---|
|`UnderReplicatedPartitions > 0`|Risk of data loss|
|`UncleanLeaderElections > 0`|Could indicate broker failures|
|`Consumer Lag consistently increasing`|Consumer may be unhealthy|
|`ActiveControllerCount != 1`|Cluster instability|
|`Broker down`|Availability risk|
|`Heap usage > 85%` or `GC Pause > 2s`|Performance degradation|

---
