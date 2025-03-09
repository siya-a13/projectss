---
longform:
  format: single
  title: DBA Commands
title: DBACommands
---
# To get the size of all databases in MySQL in GB, you can use the following query:

```
SELECT table_schema AS database_name,
       ROUND(SUM(data_length + index_length) / 1024 / 1024 / 1024, 2) AS size_in_GB
FROM information_schema.tables
GROUP BY table_schema;
```

# Create root user

```
CREATE USER 'dba'@'%' IDENTIFIED BY '7(/1+HQo1Z7*?/_)';

GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' WITH GRANT OPTION;

GRANT CREATE USER ON *.* TO 'dba'@'%';

FLUSH PRIVILEGES

mysql -u dba -p'7(/1+HQo1Z7*?/_)'

```


# Backup

```
nohup mydumper --threads 2 --user root --password 'V6j$&=hu>A>f-IU' --database 'webtune_prod' --compress --verbose 3 --compress-protocol --outputdir /home/ubuntu/backup > mydumper_output.log 2>&1 &
```
# Restore

```
nohup myloader -d /home/ubuntu/percona/fbackup -u dba -p '7(/1+HQo1Z7*?/_)' --host 10.0.3.28 --overwrite-tables --verbose 3 --threads 3 > myloader.log 2>&1 &
```
# Show All Tables row count


```
SELECT 
    TABLE_NAME, 
    TABLE_ROWS 
FROM 
    INFORMATION_SCHEMA.TABLES 
WHERE 
    TABLE_SCHEMA = 'scalenut';
```

# Migrate Users

```
mysqldump -uroot -p --exclude-databases=% --users > all-users_privileges-timestamp.sql
```

```
mysql --user=dba --host 10.0.3.28 --password < all-users_privileges-timestamp.sql
```

#### Ref - https://stackoverflow.com/questions/3982299/using-mysqldump-and-database-users
# my.cnf

```
[client]
#password = your_password
port = 3306
socket = /var/run/mysqld/mysqld.sock

[mysqld]
port = 3306
bind-address = 0.0.0.0
datadir = /var/lib/mysql
socket = /var/run/mysqld/mysqld.sock
pid-file = /var/run/mysqld/mysqld.pid
sql_mode = ''
#skip-grant-tables
binlog_format=ROW
collation-server = utf8_general_ci
init-connect='SET NAMES utf8'
character-set-server = utf8

collation-server = utf8mb4_0900_ai_ci 
character-set-server = utf8mb4 
init-connect='SET NAMES utf8mb4'


#skip-grant-tables = FALSE
log-raw = OFF
local-infile = 1
master-info-repository = TABLE
plugin-load = validate_password.so
validate-password = FORCE_PLUS_PERMANENT
validate-password-policy = STRONG
validate-password-special-char-count = 1
validate-password-number-count = 1
validate-password-mixed-case-count = 1
validate-password-length = 14
skip-symbolic-links = YES

# Logging configuration.
log-error = /var/log/mysql/mysql.err

# Slow query log configuration.
slow_query_log = 1
slow_query_log_file = /var/log/mysql/mysql-slow.log
long_query_time = 2


# Replication
server-id = 1

log_bin = mysql-bin
log-bin-index = mysql-bin.index
#expire_logs_days = 5
max_binlog_size = 100M
binlog_format = MIXED

#binlog_do_db = monitoring


# Disabling symbolic-links is recommended to prevent assorted security risks
#symbolic-links = 0

# User is ignored when systemd is used (fedora >= 15).
user = mysql

# http://dev.mysql.com/doc/refman/5.5/en/performance-schema.html
#;performance_schema

# Memory settings.
key_buffer_size = 256M
max_allowed_packet = 1G
table_open_cache = 256
sort_buffer_size = 1M
read_buffer_size = 1M
read_rnd_buffer_size = 4M
myisam_sort_buffer_size = 64M
thread_cache_size = 8
#query_cache_type = 0
#query_cache_size = 16M
#query_cache_limit = 1M
max_connections = 151
tmp_table_size = 16M
max_heap_table_size = 16M
group_concat_max_len = 1024
join_buffer_size = 262144

# Other settings.
wait_timeout = 28800
interactive_timeout = 28800
net_read_timeout = 3600
net_write_timeout = 3600
lower_case_table_names = 0
event_scheduler = OFF

# InnoDB settings.
#innodb_large_prefix = 1
#innodb_file_format = barracuda
innodb_file_per_table = 1
innodb_buffer_pool_size = 256M
innodb_log_file_size = 64M
innodb_log_buffer_size = 8M
innodb_flush_log_at_trx_commit = 1
innodb_lock_wait_timeout = 50

[mysqldump]
max_allowed_packet = 200M

[mysqld_safe]
pid-file = /var/run/mysqld/mysqld.pid

```


```
SHOW CREATE TABLE writer_generates;

ALTER TABLE writer_generates 
CONVERT TO CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

```

# Mysql-8 config

```

[client]
# password = your_password
port = 3306
socket = /var/run/mysqld/mysqld.sock

[mysqld]
port = 3306
bind-address = 0.0.0.0
datadir = /var/lib/mysql
socket = /var/run/mysqld/mysqld.sock
pid-file = /var/run/mysqld/mysqld.pid
sql_mode = ''
gtid-mode = ON
enforce-gtid-consistency
# skip-grant-tables = FALSE
log-raw = OFF
# local-infile = 0
master-info-repository = TABLE
# plugin-load = validate_password.so
# validate-password = FORCE_PLUS_PERMANENT
# validate-password-policy = STRONG
# validate-password-special-char-count = 1
# validate-password-number-count = 1
# validate-password-mixed-case-count = 1
# validate-password-length = 14
skip-symbolic-links = YES

# Logging configuration
log-error = /var/log/mysql/mysql.err

# Slow query log configuration
slow_query_log = 1
slow_query_log_file = /var/log/mysql/mysql-slow.log
long_query_time = 10

# Replication
server-id = 1
log_bin = mysql-bin
log-bin-index = mysql-bin.index
expire_logs_days = 10
max_binlog_size = 134217728
binlog_format = MIXED
# binlog_do_db = webtune_prod

# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links = 0

# User is ignored when systemd is used (fedora >= 15).
user = mysql

# http://dev.mysql.com/doc/refman/5.5/en/performance-schema.html
; performance_schema

# Memory settings
key_buffer_size = 1G
max_allowed_packet = 2G
table_open_cache = 6000
sort_buffer_size = 262144
read_buffer_size = 262144
read_rnd_buffer_size = 524288
myisam_sort_buffer_size = 64M
thread_cache_size = 27
# query_cache_type = 1
# query_cache_size = 1162006528
# query_cache_limit = 1048576
max_connections = 2000
tmp_table_size = 16777216
max_heap_table_size = 16777216
group_concat_max_len = 1024
join_buffer_size = 262144

# Other settings
wait_timeout = 28800
lower_case_table_names = 0
event_scheduler = OFF

# InnoDB settings
# innodb_large_prefix = 1
# innodb_file_format = barracuda
innodb_file_per_table = 1
innodb_buffer_pool_size = 20G
innodb_log_file_size = 1G
innodb_log_buffer_size = 1G
innodb_flush_log_at_trx_commit = 1
innodb_lock_wait_timeout = 50

[mysqldump]
quick
max_allowed_packet = 1G

[mysqld_safe]
pid-file = /var/run/mysqld/mysqld.pid

```


# Server Copy

```
scp backup/* ubuntu@20.246.107.58:/home/ubuntu/backup
```

```
scp -i /home/ubuntu/ssh-scalenut-nonprod-key.pem backup/* ubuntu@10.0.16.5:/home/ubuntu/backup
```