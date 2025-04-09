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
CREATE USER 'slave_user'@'10.0.40.14' IDENTIFIED BY 'slavedba@321#=hu>A>f-IU';

ALTER USER 'slave_user'@'10.0.40.14' IDENTIFIED WITH mysql_native_password BY 'slavedba@321#=hu>A>f-IU';

GRANT REPLICATION SLAVE ON *.* TO 'slave_user'@'10.0.40.14';

FLUSH PRIVILEGES;

```

# Start Replication

```
CHANGE MASTER TO MASTER_HOST = '172.16.3.227', MASTER_USER = 'slave_user', MASTER_PASSWORD = 'slavedba@321#=hu>A>f-IU', MASTER_LOG_FILE = 'mysql-bin.000552', MASTER_LOG_POS = 322450 ; 
```
