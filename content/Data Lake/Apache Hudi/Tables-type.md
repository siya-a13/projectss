---
longform:
  format: single
  title: Copy-On-Write
title: Tables-type
---
In Apache Hudi, **COW** (Copy-On-Write) and **MOR** (Merge-On-Read) are two different storage types that determine how data is managed and accessed. Here’s a breakdown of each:

## Copy-On-Write (COW)

![[cow.png]]

- **Definition**: In COW, whenever an update or delete operation occurs, a new version of the data is created. The original data remains unchanged until the new data is fully written.
- **Use Case**: Best suited for workloads where read performance is critical, and updates are less frequent. It’s optimal for batch processing and scenarios where data consistency is paramount.
- **Performance**: Provides faster read operations since data is stored in a format optimized for reading. However, writes may be slower due to the overhead of creating new files.

## Merge On Read (MOR)?

MOR is one of the storage types offered by Hudi. Here's how it works:

![[mor.png]]

- **Data Layout**: In MOR, data is stored in a combination of small columnar files (for efficient querying) and larger log files (for fast writes).
- **Reading**: When you read data, Hudi first retrieves the data from the columnar files and then merges it with any updates from the log files on-the-fly.
- **Benefits**:
    - **Efficient Writes**: You can append data quickly.
    - **Faster Querying**: Optimized for reading without needing to rewrite large datasets frequently.

## Comparission

![[cow-mor.png]]
