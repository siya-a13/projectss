---
longform:
  format: single
  title: Container setup
title: Container setup
---
## Launch container

```
docker run -d --name postgres -e POSTGRES_USER=deepak -e POSTGRES_PASSWORD=password123 -e POSTGRES_DB=test -p 5432:5432 -v $(pwd)/data:/var/lib/postgresql/data postgres:latest
```

## Login to postgresql


```
docker exec -it postgres psql --dbname=test --username=deepak --password
```