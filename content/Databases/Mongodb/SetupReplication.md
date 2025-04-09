---
longform:
  format: single
  title: SetupReplication
title: SetupReplication
---
# Check version

```
db.version()
```

# Find Running Queries

```
db.currentOp().inprog.filter(op => op.secs_running > 5)

```

# Find active write operation


```
db.currentOp().inprog.forEach(
   function(d){
     if(d.waitingForLock && d.lockType != "read")
        printjson(d)
     })
```

Refer - https://stackoverflow.com/questions/14970227/how-do-i-view-queries-being-executed-by-my-mongodb

# Handle Race condition in mongo

```
cfg = rs.conf()

## cfg.members = cfg.members.filter(m => m.host !== "10.0.40.11:27017")

cfg.members = [
  {_id: 0, host: "SECONDARY_IP:27017", priority: 2},
  {_id: 1, host: "OTHER_MEMBER_IP:27017", priority: 1}
];

cfg.version += 1

rs.reconfig(cfg, { force: true })

```

## Create User

```
db.createUser({
  user: "myUser",
  pwd: "myPassword",
  roles: [{ role: "readWrite", db: "test" }]
})

db.createUser({
  user: "kefi",
  pwd: "kefi",
  roles: [{ role: "readWrite", db: "kefi_prod" }],
  mechanisms: ["SCRAM-SHA-1", "SCRAM-SHA-256"]
})

```