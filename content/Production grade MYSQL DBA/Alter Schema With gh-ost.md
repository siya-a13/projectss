---
longform:
  format: single
  title: Alter Schema With gh-ost
title: Alter Schema With gh-ost
---
# Download Binary

```
wget https://github.com/github/gh-ost/releases/download/v1.1.0/gh -ost_1.1.0_amd64.deb
```
# Install

```
sudo dpkg -i gh-ost_1.1.0_amd64.deb
```

# Set global variable

```
SHOW VARIABLES LIKE '%binlog_row_image%';
```
# Command

Run the ghost in background

```
  
nohup gh-ost --host=myhost.com --user=root --password='demopassword' --database=django360 --table=users --alter="ADD COLUMN enc_uid_test VARCHAR(225)" --discard-foreign-keys --skip-foreign-key-checks --postpone-cut-over-flag-file=./ghost-postpone.flag --chunk-size=1000 --allow-on-master --execute gh-ost.log 2>&1 &

```

### **How to Dynamically Configure `gh-ost` During a Migration**

`gh-ost` allows **runtime adjustments** without stopping/restarting the process. Below are key methods to dynamically control its behavior:

---

## **1. Throttling (Pause/Resume)**

#### **Pause Migration Temporarily**

```
echo 'throttle' | nc -U /tmp/gh-ost.scalenut_prod.analysis_competitor.sock
```

- Useful when the database is under heavy load.
- `gh-ost` will stop copying rows but continue applying binlog events.

#### **Resume Migration**

```
echo 'no-throttle' | nc -U /tmp/gh-ost.scalenut_prod.analysis_competitor.sock
```

## **2. Adjust Replication Lag Threshold**

#### **Increase Max Lag Tolerance (Default: 1500ms)**

```
echo 'max-lag-millis=3000' | nc -U /tmp/gh-ost.scalenut_prod.analysis_competitor.sock
```

- If replicas are lagging, this prevents `gh-ost` from auto-throttling.
#### **Check Current Lag Settings**

```
echo 'status' | nc -U /tmp/gh-ost.scalenut_prod.analysis_competitor.sock | grep max-lag
```

## **3. Force Cut-Over (Immediate Table Swap)**

```
echo 'cut-over' | nc -U /tmp/gh-ost.scalenut_prod.analysis_competitor.sock
```

- **Use with caution!** Ensures the migration completes immediately.
- Only works if `postpone-cut-over-flag-file` is **not set**.

## **4. Change Chunk Size (Row Copy Speed)**

```
echo 'chunk-size=500' | nc -U /tmp/gh-ost.scalenut_prod.analysis_competitor.sock
```

- Default: `1000` rows per transaction.
- Lower = less impact on DB, but slower migration.

## **5. Enable/Enable Postpone Cut-Over**

#### **Delay Cut-Over (Manual Control)**

```
touch /path/to/ghost-postpone.flag  # File must match `--postpone-cut-over-flag-file`
```

- `gh-ost` will wait **indefinitely** until the file is removed.
#### **Allow Cut-Over to Proceed**

```
rm /path/to/ghost-postpone.flag
```

## **6. Dynamic Query Checks (For Critical Load)**

```
echo 'critical-load=Threads_running:50' | nc -U /tmp/gh-ost.sock
```

- If `Threads_running > 50`, `gh-ost` auto-throttles.
## **7. Check Current Configuration**

```
echo 'show status' | nc -U /tmp/gh-ost.scalenut_prod.analysis_competitor.sock
```

## **8. Abort Migration (Emergency Stop)**

```
echo 'panic' | nc -U /tmp/gh-ost.scalenut_prod.analysis_competitor.sock
```

- **Kills `gh-ost` immediately** (leaves ghost table behind).
- Clean up manually:

```
DROP TABLE IF EXISTS `_analysis_competitor_gho`;
```