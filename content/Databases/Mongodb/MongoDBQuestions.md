---
longform:
  format: single
  title: MongoDB DBA Questions
title: MongoDB DBA Questions
---
### **Basic Configuration and Logs**

1. What is the purpose of the `db.startup_log.find()` command in MongoDB?
    
2. How do you configure the `logpath`, `datapath`, `port`, and `fork` options in a MongoDB configuration file?
    
---

### **Storage Engines**

1. Compare the WiredTiger and MMAPv1 storage engines in MongoDB.
     
2. What is document-level concurrency, and how does WiredTiger implement it?
    
3. Explain Multi-Version Concurrency Control (MVCC) in MongoDB.
    
4. How does WiredTiger handle compression, and what are the benefits?
    
5. What is a checkpoint in WiredTiger, and why is it important?
    
---

### **Server Status and Monitoring**

6. What information does the `db.serverStatus()` command provide?
    
7. How can you check the storage engine being used in your MongoDB instance using `db.serverStatus()`?
    
---

### **Journaling**

8. What is journaling in MongoDB, and why is it important for durability?
    
9. How does journaling work in WiredTiger?
    
---

### **Locking and Unlocking**

10. What is the purpose of the `db.fsyncLock()` and `db.fsyncUnlock()` commands?
    
11. When would you use these commands in a production environment?
    
---

### **Capped Collections**

12. How do you create a capped collection in MongoDB?
    
13. What are the use cases for capped collections?
    
---

### **Automatic Archival**

14. How can you set up automatic archival in MongoDB?
    
---

### **Document Insertion Time**

15. How can you determine the insertion time of a document using its `_id` field?
    
---

### **TTL Indexes**

16. How do you create a TTL (Time-To-Live) index in MongoDB?
    
17. What is the purpose of the `ttlMonitorSleepSec` parameter, and how can you modify it?
    
---

### **Query Optimization**

18. How can you determine if a query is using an index?
    
19. What do the terms `DocumentsScanned` and `RowsReturned` indicate in the context of query execution?
    
---

### **Indexing Strategies**

20. What is the ESR (Equality, Sort, Range) rule for indexing in MongoDB?
    
21. How does the ESR rule help in optimizing queries?
    

---

### **Replication**

22. How do you set up a replica set in MongoDB?
    
23. What are the key components of a replica set, and how does failover work?
    
---

### **Sharding**

24. Explain the concept of sharding in MongoDB.
    
25. What are the benefits of sharding, and how does it improve performance and scalability?
    
---

## **Sample Follow-Up Questions**

### **Storage Engines**

- Can you switch the storage engine from MMAPv1 to WiredTiger in an existing MongoDB deployment? If yes, how?
    
### **Journaling**

- What happens if journaling is disabled in MongoDB? What are the risks?
    
### **Capped Collections**

- What happens when a capped collection reaches its maximum size or document limit?
    
### **TTL Indexes**

- What happens if the `ttlMonitorSleepSec` parameter is set to a very high value?
    
### **Replication**

- How do you handle a scenario where the primary node in a replica set goes down?
    
### **Sharding**

- What is a shard key, and how do you choose an effective shard key for your data?
    

---

## **Practical Scenarios**

### **Performance Tuning**

- A query is running slowly. How would you diagnose and optimize it?
    
### **Backup and Recovery**

- How would you take a backup of a MongoDB database, and what steps would you follow to restore it?
    
### **Scaling**

- Your MongoDB database is experiencing high read and write traffic. How would you scale it to handle the load?
    
### **Security**

- How do you enable authentication and authorization in MongoDB? What are some best practices for securing a MongoDB deployment?
    
---