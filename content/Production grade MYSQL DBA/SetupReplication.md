---
longform:
  format: single
  title: SetupReplication
title: SetupReplication
---
# Reset root user password

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'A$Ea`LQCd+CD5_=^';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

```
# Create a replication user

```
CREATE USER 'slave_user'@'10.0.40.5' IDENTIFIED BY 'slavedba@321#';

ALTER USER 'slave_user'@'10.0.40.5' IDENTIFIED WITH mysql_native_password BY 'slavedba@321#';

GRANT REPLICATION SLAVE ON *.* TO 'slave_user'@'10.0.40.5';

FLUSH PRIVILEGES;

```

# Start Replication

```
CHANGE MASTER TO MASTER_HOST = '10.0.40.4', MASTER_USER = 'slave_user', MASTER_PASSWORD = 'slavedba@321#', MASTER_LOG_FILE = 'mysql-bin.000013', MASTER_LOG_POS = 405 ; 
```
