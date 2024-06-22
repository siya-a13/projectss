---
title: MYSQL Container
---
# Commands

Pull MYSQL image version 8.4.0 and run as a container .

```
docker run --name mysql -e MYSQL_ROOT_PASSWORD=secret_pwd -d mysql:8.4.0
```

# MYSQL Container Login

Login to MYSQL container .

```
docker exec -it mysql mysql -uroot -p
```

# MYSQL Container Logs

```
docker container logs mysql
```