---
title: Amazon DynamoDB - Time To Live (TTL)
---
## What is TTL?

- Time to Live
- Feature that allows automatic removal of individual items
- Dashboard app that only cares about the current day..
- Reduces cost, can make some q's more efficient
- Totally free, does not consume write throughput
- TTL happens automatically
- Must be epoch in SECONDS, N type
- TTL can take 48 hours or more - don't rely on it though