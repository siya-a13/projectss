---
longform:
  format: single
  title: Container setup
---
## Command

- Spin up mongo container

```
docker run -d --name mongodb-standalone -p 27017:27017 \ -e MONGO_INITDB_ROOT_USERNAME=root \ -e MONGO_INITDB_ROOT_PASSWORD=password \ -v /Users/deepaknishad/mongo/data:/data/db mongo
```

- Create collection of name ec2

```
db.createCollection("ec2”)
```

- Find all the document inside ec2 collection

```
db.ec2.find().pretty()
```

- Find all document inside ec2 with environment : staging and lob : sales

```
db.ec2.find({ environment: "staging", lob: "sales" }).pretty()
```