---
title: Amazon DynamoDB - Security
---
## **Encryption at Rest and in Transit**:

DynamoDB supports encryption of data both at rest and in transit. At rest, you can enable server-side encryption using AWS Key Management Service (KMS) keys. In transit, data is encrypted using TLS (Transport Layer Security).

## **Access Control**:

IAM (Identity and Access Management) policies allow you to control who can create, read, update, and delete items in DynamoDB tables. Fine-grained access control can be achieved using IAM policies, conditions, and policies attached to KMS keys.

## **Backup and Restore**:

DynamoDB offers backup and restore capabilities through on-demand and continuous backups. On-demand backups allow you to create full backups of your DynamoDB tables for data archiving and recovery.

