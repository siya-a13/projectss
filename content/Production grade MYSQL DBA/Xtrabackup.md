---
longform:
  format: single
  title: Xtrabackup
title: Xtrabackup
---
# Installing Percona XtraBackup on Ubuntu 20.04

Follow these steps to install Percona XtraBackup on Ubuntu 20.04:

## 1. Update the Package List

First, ensure your package list is up to date:

```
sudo apt update
```

## 2. Install Dependencies

Install the necessary dependencies for Percona XtraBackup:

```
sudo apt install -y lsb-release wget gnupg2
```

## 3. Add Percona Repository

Add the Percona APT repository to your system:

```
wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
sudo dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb
```

## 4. Update the Package List Again

After adding the repository, update the package list:

```
sudo apt update
```

## 5. Install Percona XtraBackup

Now, install Percona XtraBackup:

```
sudo apt install -y percona-xtrabackup-80

```

## 6. Verify the Installation

To verify that Percona XtraBackup is installed correctly, you can check the version:

```
xtrabackup --version
```

## 7. (Optional) Install qpress for Compression

If you plan to use compression with XtraBackup, you can install qpress:

```
sudo apt install -y qpress
```

## 8. Start Using Percona XtraBackup

You can now start using Percona XtraBackup to create backups of your MySQL or Percona Server databases.

### Example Backup Command

To create a full backup of your database:

```
xtrabackup --backup --user=your_db_user --password=your_db_password --target-dir=/path/to/backup
```

# Backup
### **1. Take a Full Backup**

A full backup is the base backup from which incremental backups are created.

```
xtrabackup --backup --user=your_db_user --password=your_db_password --target-dir=/path/to/full-backup
```

### **2. Take an Incremental Backup**

An incremental backup only backs up the changes since the last backup (full or incremental).

```
xtrabackup --backup --user=your_db_user --password=your_db_password --target-dir=/path/to/incremental-backup --incremental-basedir=/path/to/full-backup
```

# Restore

### **1. Prepare the Backups**

Before restoring, you need to **prepare** the backups. This step applies the transaction logs to make the backups consistent.

#### **Prepare the Full Backup**

```
xtrabackup --prepare --apply-log-only --target-dir=/path/to/full-backup
```

#### **Prepare the Incremental Backup**

Apply the incremental backup to the full backup:

```
xtrabackup --prepare --apply-log-only --target-dir=/path/to/full-backup --incremental-dir=/path/to/incremental-backup
```

- Repeat this step for each incremental backup, ensuring you apply them in the correct order.

#### **Final Prepare**

After applying all incremental backups, perform a final prepare on the full backup:

```
xtrabackup --prepare --target-dir=/path/to/full-backup
```

### **4. Restore the Backup**

To restore the backup, stop the MySQL/Percona Server, move the existing data directory, and copy the prepared backup to the data directory.

#### **Stop MySQL/Percona Server**

```
sudo systemctl stop mysql
```

#### **Move Existing Data Directory**

Move the existing data directory to a backup location (optional but recommended):

```
sudo mv /var/lib/mysql /var/lib/mysql-backup
```