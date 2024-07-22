---
title: Amazon DynamoDB Accelerator (DAX)
---
## What is DAX?

 - Fully-managed high available , seamless  in-memory cache for DynamoDB
- Microseconds latency for cached reads & queries
- Doesn't require application logic modification (compatible with existing DynamoDB APIs)
- Solves the "Hot Key" problem (too many reads)
- 5 minutes TTL for cache (default)
- Up to 10 nodes in the cluster
- Multi-AZ (3 nodes minimum recommended for production)
- Secure (Encryption at rest with KMS. VPC, IAM, Cloudtrail).

## When should I use it?

- Consistently/Burst Traffic on the same set of keys
- Require microsecond response times
- Your use case can tolerate eventual consistency
- When your application is read intensive and not write intensive.
