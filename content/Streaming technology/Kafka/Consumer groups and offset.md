---
longform:
  format: single
  title: Consumer groups and offset
title: Consumer groups and offset
---
![[consumer-groups.png]]

**Consumer Groups**: Consumers read data as part of a consumer group. Each consumer in a group exclusively reads from specific partitions, ensuring no overlap. The number of consumers cannot exceed the number of partitions, as this would leave some consumers inactive.

**Offsets Management**: Kafka tracks the offset, or the last record read by each consumer group, storing this information in a special Kafka topic called `__consumer_offsets`. Consumers should commit their offsets after processing data. If a consumer fails, it can resume from the last committed offset, ensuring no data is missed.