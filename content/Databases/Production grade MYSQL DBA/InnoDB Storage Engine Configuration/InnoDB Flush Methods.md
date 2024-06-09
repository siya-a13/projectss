---
title: InnoDB Flush Methods
---
- InnoDB performs certain tasks in background , including flushing of dirty pages from the buffer pool - modified pages that are not yet written to the data files on disk.
- **innodb_flush_method**  - system variable
- **fsync** - Default flush method, flush data , metadata , log files causes *double buffering* 
- **O_DSYNC** - flush only data files but causes *double buffering
- **O_DIRECT** - flush only data files, uses fsync with no *double buffering*, read write directly goes to disk.
- **O_DIRECT_NO_FSYNC** - O_DIRECT but skip fsync, not good for XFS FS.

## Recommendations ?
- When you have heavy write use **O_DIRECT_NO_FSYNC**
- Use either **O_DIRECT** or **O_DIRECT_NO_FSYNC**