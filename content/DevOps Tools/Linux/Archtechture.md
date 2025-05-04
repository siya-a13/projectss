---
longform:
  format: single
  title: Archtechture
title: Archtechture
---
![[architechture.webp]]


### **1. Hardware**  
- Physical components: CPU, RAM, storage, network devices, etc.  
- Linux supports multiple architectures (x86, ARM, RISC-V, etc.).  

### **2. Kernel (Core of Linux)**  
- Monolithic kernel handling:  
  - **Process management** (scheduling, multitasking)  
  - **Memory management** (RAM, virtual memory)  
  - **Device drivers** (communication with hardware)  
  - **File systems** (ext4, Btrfs, XFS, etc.)  
  - **Networking** (TCP/IP stack, firewalls)  
- Loadable kernel modules (drivers can be added/removed dynamically).  

### **3. Shell (Command Interpreter)**  
- Acts as a bridge between users and the kernel.  
- Common shells: **Bash (Bourne Again Shell), Zsh, Fish**.  
- Accepts commands, executes programs, and returns output.  

### **4. Applications (User Space)**  
- End-user software (e.g., web browsers, text editors, servers).  
- Can be CLI-based (like `vim`, `grep`) or GUI-based (like Firefox, LibreOffice).  
- Relies on system libraries (e.g., `glibc`, `GTK`, `Qt`) for functionality.  

