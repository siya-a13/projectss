---
longform:
  format: single
  title: Text Processing
title: Text Processing
---

### 1. **`grep`** – _Search for Patterns_

- **Purpose**: Searches for specific patterns in text using regular expressions.
    
- **Basic Usage**:
    
    ```bash
    grep "pattern" filename
    ```
    
- **Example**:
    
    ```bash
    grep "error" server.log
    ```
    
    Finds all lines in `server.log` that contain the word “error”.
    

---

### 2. **`awk`** – _Pattern Scanning and Processing_

- **Purpose**: A powerful programming language for pattern scanning, text manipulation, and reporting.
    
- **Basic Usage**:
    
    ```bash
    awk '{print $1}' filename
    ```
    
- **Example**:
    
    ```bash
    awk '/error/ {print $2}' server.log
    ```
    
    Prints the second field of lines that contain “error”.
    

---

### 3. **`sed`** – _Stream Editor_

- **Purpose**: Edits text in a stream, often used for substitution or deletion.
    
- **Basic Usage**:
    
    ```bash
    sed 's/old/new/' filename
    ```
    
- **Example**:
    
    ```bash
    sed 's/error/issue/' server.log
    ```
    
    Replaces the first occurrence of "error" with "issue" in each line.
    

---

### 4. **`cut`** – _Extract Columns from Text_

- **Purpose**: Removes sections (fields or columns) from each line of input.
    
- **Basic Usage**:
    
    ```bash
    cut -d':' -f1 /etc/passwd
    ```
    
- **Example**:  
    Outputs the first field (username) from `/etc/passwd`.
    

---

### 5. **`sort`** – _Sort Lines of Text Files_

- **Purpose**: Sorts lines in text files alphabetically or numerically.
    
- **Basic Usage**:
    
    ```bash
    sort filename
    ```
    
- **Example**:
    
    ```bash
    sort -n numbers.txt
    ```
    
    Sorts numbers in ascending numerical order.
    

---

### 6. **`uniq`** – _Report or Filter Repeated Lines_

- **Purpose**: Removes or displays duplicate lines (only works on sorted data).
    
- **Basic Usage**:
    
    ```bash
    uniq filename
    ```
    
- **Example**:
    
    ```bash
    sort data.txt | uniq -c
    ```
    
    Sorts the file and shows each line's frequency of occurrence.