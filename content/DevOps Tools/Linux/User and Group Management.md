---
longform:
  format: single
  title: User and Group Management
title: User and Group Management
---
# Linux User and Group Management

User and group management is fundamental to Linux system administration, controlling access to files, directories, and system resources. Here's a comprehensive guide:

## User Management

### 1. Viewing Users
```bash
cat /etc/passwd         # List all users
getent passwd           # Alternative method
id username             # Show user details
whoami                  # Show current user
```

### 2. Creating Users
```bash
useradd username        # Basic user creation
useradd -m username    # Create with home directory
useradd -G group1,group2 username  # Add to supplementary groups
useradd -s /bin/bash username  # Set default shell
useradd -u 1005 username  # Specify UID
```

### 3. Modifying Users
```bash
usermod -aG sudo username  # Add to sudo group
usermod -s /bin/zsh username  # Change shell
usermod -L username      # Lock account
usermod -U username      # Unlock account
usermod -d /new/home username  # Change home directory
```

### 4. Deleting Users
```bash
userdel username        # Delete user (keeps home dir)
userdel -r username     # Delete user and home directory
```

### 5. Password Management
```bash
passwd username         # Set/change password
passwd -l username      # Lock password
passwd -u username      # Unlock password
passwd -e username      # Expire password (force change)
chage -l username       # View password aging info
```

## Group Management

### 1. Viewing Groups
```bash
cat /etc/group          # List all groups
getent group            # Alternative method
groups username         # Show user's groups
```

### 2. Creating Groups
```bash
groupadd groupname      # Create new group
groupadd -g 1005 groupname  # Create with specific GID
```

### 3. Modifying Groups
```bash
groupmod -n newname oldname  # Rename group
groupmod -g 1006 groupname  # Change GID
```

### 4. Deleting Groups
```bash
groupdel groupname      # Delete group
```

### 5. Managing Group Memberships
```bash
gpasswd -a user group   # Add user to group
gpasswd -d user group   # Remove user from group
usermod -aG group1,group2 user  # Add to multiple groups
```

## Important Files

1. **/etc/passwd** - User account information
   - Format: `username:x:UID:GID:description:homedir:shell`

2. **/etc/shadow** - Encrypted passwords and aging info (root only)

3. **/etc/group** - Group definitions
   - Format: `groupname:x:GID:members`

4. **/etc/gshadow** - Secure group information (root only)

## Special Users

1. **Root (UID 0)** - Superuser with full system access
2. **System Users (UID 1-999)** - For services/daemons (varies by distro)
3. **Regular Users (UID 1000+)** - Normal user accounts

## Best Practices

1. Use `-aG` with `usermod` to append groups rather than replace
2. Always use `visudo` to edit sudoers file
3. Regularly audit users with `last`, `who`, and `w` commands
4. Set appropriate password policies in `/etc/login.defs`
5. Use `adduser` instead of `useradd` on Debian-based systems (more user-friendly)

## Sudo Privileges

To grant administrative privileges:
```bash
usermod -aG sudo username  # Debian/Ubuntu
usermod -aG wheel username # RHEL/CentOS
```

Then edit sudoers file safely:
```bash
visudo
# Add line: username ALL=(ALL) ALL
```

## User Environment

User-specific configuration files:
- `~/.bashrc` - Shell configuration
- `~/.profile` - Login configuration
- `~/.ssh/` - SSH keys and config

## Practical Examples

1. Create a developer user with home directory and add to appropriate groups:
```bash
useradd -m -G developers,sudo -s /bin/bash devuser
passwd devuser
```

2. Find all users belonging to a specific group:
```bash
getent group developers | cut -d: -f4
```

3. List all users with UID ≥ 1000 (normal users):
```bash
awk -F: '$3 >= 1000 {print $1}' /etc/passwd
```

4. Set password expiration policy:
```bash
chage -M 90 -W 7 username  # Expire after 90 days, warn 7 days before
```

Proper user and group management is essential for system security and resource access control in Linux environments.