---
longform:
  format: single
  title: Basic Commands
title: Basic Commands
---
Here’s a clear explanation of **basic Linux commands** with examples for each:  

---

### **1. `ls` (List Directory Contents)**  
**Purpose:** Lists files and directories in the current folder.  
**Common Options:**  
- `ls -l` → Detailed list (permissions, owner, size, date)  
- `ls -a` → Shows hidden files (starting with `.`)  
- `ls -h` → Human-readable file sizes (KB, MB)  

**Example:**  
```bash
ls -lah  # Lists all files (including hidden) in detailed, readable format
```

---

### **2. `cd` (Change Directory)**  
**Purpose:** Moves you into a different directory.  
**Common Usage:**  
- `cd /path/to/folder` → Absolute path  
- `cd folder_name` → Relative path  
- `cd ..` → Go up one level  
- `cd ~` or `cd` → Go to home directory  

**Example:**  
```bash
cd Documents/Projects  # Enters the "Projects" folder inside "Documents"
```

---

### **3. `mkdir` (Make Directory)**  
**Purpose:** Creates a new directory (folder).  
**Common Options:**  
- `mkdir -p parent/child` → Creates nested directories at once.  

**Example:**  
```bash
mkdir new_folder       # Creates "new_folder"
mkdir -p dir1/dir2     # Creates "dir1" and "dir2" inside it
```

---

### **4. `rm` (Remove Files/Directories)**  
**Purpose:** Deletes files or directories.  
**Common Options:**  
- `rm file.txt` → Deletes a file.  
- `rm -r folder/` → Deletes a directory **recursively** (use with caution!).  
- `rm -f` → Forces deletion (no confirmation).  

**Example:**  
```bash
rm old_file.txt        # Deletes "old_file.txt"
rm -r old_folder/      # Deletes "old_folder" and its contents
```

---

### **5. `cp` (Copy Files/Directories)**  
**Purpose:** Copies files or directories.  
**Common Options:**  
- `cp file.txt new_location/` → Copies a file.  
- `cp -r folder/ backup/` → Copies a directory recursively.  

**Example:**  
```bash
cp notes.txt ~/Backups/  # Copies "notes.txt" to the "Backups" folder
cp -r project/ backup/   # Copies the entire "project" folder
```

---

### **6. `mv` (Move/Rename Files/Directories)**  
**Purpose:** Moves files/directories **or** renames them.  
**Common Usage:**  
- `mv file.txt new_name.txt` → Renames a file.  
- `mv file.txt /target/path/` → Moves a file.  

**Example:**  
```bash
mv old.txt new.txt      # Renames "old.txt" to "new.txt"
mv file.txt ~/Documents/ # Moves "file.txt" to "Documents"
```

---
