---
longform:
  format: single
  title: File Permissions
title: File Permissions
---
# Linux File Permissions Explained

File permissions in Linux are a fundamental security feature that controls access to files and directories. Here's a comprehensive explanation:

## Basic Permission System

Linux uses three types of permissions for each file and directory:

1. **Read (r)** - Allows viewing/reading file contents or listing directory contents
2. **Write (w)** - Allows modifying file contents or adding/removing files in directories
3. **Execute (x)** - Allows running a file as a program or accessing contents of a directory

## Permission Classes

Permissions are assigned to three classes of users:

1. **Owner (u)** - The user who owns the file
2. **Group (g)** - Members of the file's group
3. **Others (o)** - All other users

## Viewing Permissions

Use `ls -l` to view permissions:

```
-rwxr-xr-- 1 user group 2048 Jan 1 10:00 file.txt
```

The permission string (`-rwxr-xr--`) breaks down as:
- First character: file type (`-` for regular file, `d` for directory)
- Next 3: owner permissions (`rwx`)
- Next 3: group permissions (`r-x`)
- Last 3: others permissions (`r--`)

## Numeric (Octal) Representation

Each permission has a numeric value:
- Read (r) = 4
- Write (w) = 2
- Execute (x) = 1

These are added together for each class:
- `rwxr-xr--` becomes 754 (7 for owner, 5 for group, 4 for others)

## Changing Permissions

Use `chmod` to change permissions:

1. Symbolic mode:
   ```bash
   chmod u+x file.txt      # Add execute for owner
   chmod g-w file.txt      # Remove write for group
   chmod o=r file.txt      # Set others to read-only
   chmod a+x file.txt      # Add execute for all (a = all)
   ```

2. Numeric mode:
   ```bash
   chmod 755 file.txt      # rwxr-xr-x
   chmod 644 file.txt      # rw-r--r--
   ```

## Changing Ownership

Use `chown` and `chgrp` to change owner and group:
```bash
chown user file.txt        # Change owner
chown user:group file.txt  # Change both owner and group
chgrp group file.txt       # Change group only
```

## Special Permissions

1. **Set User ID (SUID) (s)** - When set on executable, runs with owner's privileges
   - Numeric: 4000 (e.g., `chmod 4755 file`)

2. **Set Group ID (SGID) (s)** - For executables: runs with group's privileges. For directories: new files inherit group
   - Numeric: 2000 (e.g., `chmod 2755 file`)

3. **Sticky Bit (t)** - On directories, restricts file deletion to owner (common on /tmp)
   - Numeric: 1000 (e.g., `chmod 1777 directory`)

## Default Permissions (umask)

The `umask` determines default permissions for new files:
```bash
umask 022      # Common setting (files: 644, dirs: 755)
umask -S       # View current umask in symbolic form
```

## Access Control Lists (ACLs)

For more granular control beyond standard permissions:
```bash
setfacl -m u:username:rwx file.txt  # Add ACL entry
getfacl file.txt                    # View ACLs
```

## Important Considerations

1. Directory permissions affect file access within them
2. Root user (superuser) bypasses all permission checks
3. Permissions are checked in order: owner > group > others
4. Write permission on a directory is needed to delete files in it, even if you own the files

Understanding and properly configuring file permissions is crucial for Linux system security and proper functioning of services.