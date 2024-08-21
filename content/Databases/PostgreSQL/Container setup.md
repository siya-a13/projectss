---
longform:
  format: single
  title: Container setup
title: Container setup
---
## Launch container

```
docker run -d \ --name postgres-container \ -e POSTGRES_USER=your_username \ -e POSTGRES_PASSWORD=your_password \ -e POSTGRES_DB=your_database \ -p 5432:5432 \ -v $(pwd)/data:/var/lib/postgresql/data \ postgres:latest
```

## Login to postgresql


```
docker exec -it postgres psql --dbname=test --username=deepak --password
```