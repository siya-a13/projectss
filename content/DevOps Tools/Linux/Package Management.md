---
longform:
  format: single
  title: Package Management
title: Package Management
---
### **Package Management in Linux**  
Package management refers to installing, updating, configuring, and removing software packages in a Linux system. Different Linux distributions use different package managers, but they generally serve the same purpose:  

1. **Installation** – Adding new software.  
2. **Upgrading** – Keeping software up to date.  
3. **Removal** – Uninstalling unwanted software.  
4. **Dependency Resolution** – Ensuring required libraries are installed.  
5. **Repository Management** – Downloading packages from trusted sources.  

---

## **1. Debian/Ubuntu (APT & DPKG)**
### **`apt` (Advanced Package Tool)**  
The primary high-level package manager for Debian-based systems (Ubuntu, Mint, etc.).  

#### **Key Commands:**  
| Command | Description |
|---------|-------------|
| `sudo apt update` | Updates the package list (does not install updates). |
| `sudo apt upgrade` | Upgrades all installed packages. |
| `sudo apt install <package>` | Installs a package. |
| `sudo apt remove <package>` | Removes a package (keeps config files). |
| `sudo apt purge <package>` | Removes a package + config files. |
| `sudo apt autoremove` | Removes unused dependencies. |
| `sudo apt search <keyword>` | Searches for packages. |
| `sudo apt show <package>` | Displays package details. |

#### **Example:**  
```bash
sudo apt update && sudo apt upgrade -y  # Update & upgrade all packages
sudo apt install nginx                 # Install Nginx web server
sudo apt remove nginx --purge          # Remove Nginx + configs
```

---

### **`dpkg` (Debian Package Manager)**  
A low-level tool for manually installing `.deb` files (does not handle dependencies automatically).  

#### **Key Commands:**  
| Command | Description |
|---------|-------------|
| `sudo dpkg -i <package.deb>` | Installs a `.deb` file. |
| `sudo dpkg -r <package>` | Removes a package (keeps configs). |
| `sudo dpkg -P <package>` | Purges a package + configs. |
| `dpkg -l` | Lists all installed packages. |
| `dpkg -L <package>` | Lists files installed by a package. |

#### **Example:**  
```bash
sudo dpkg -i google-chrome.deb   # Install Chrome manually
sudo dpkg -r google-chrome       # Remove Chrome (keep configs)
```

---

## **2. RHEL/CentOS/Fedora (YUM/DNF & RPM)**
### **`yum` (Yellowdog Updater Modified)**  
The older package manager for RHEL/CentOS 7 (replaced by `dnf` in newer versions).  

#### **Key Commands:**  
| Command | Description |
|---------|-------------|
| `sudo yum install <package>` | Installs a package. |
| `sudo yum remove <package>` | Removes a package. |
| `sudo yum update` | Updates all packages. |
| `sudo yum search <keyword>` | Searches for packages. |
| `sudo yum info <package>` | Shows package details. |

#### **Example:**  
```bash
sudo yum install httpd      # Install Apache web server
sudo yum remove httpd       # Remove Apache
```

---

### **`dnf` (Dandified YUM)**  
The modern replacement for `yum` (used in RHEL 8+, Fedora, CentOS Stream).  

#### **Key Commands:**  
| Command | Description |
|---------|-------------|
| `sudo dnf install <package>` | Installs a package. |
| `sudo dnf remove <package>` | Removes a package. |
| `sudo dnf upgrade` | Upgrades all packages. |
| `sudo dnf search <keyword>` | Searches for packages. |
| `sudo dnf info <package>` | Shows package details. |

#### **Example:**  
```bash
sudo dnf install nginx     # Install Nginx
sudo dnf remove nginx      # Remove Nginx
```

---

### **`rpm` (Red Hat Package Manager)**  
A low-level tool for managing `.rpm` files (does not resolve dependencies automatically).  

#### **Key Commands:**  
| Command | Description |
|---------|-------------|
| `sudo rpm -ivh <package.rpm>` | Installs an RPM file. |
| `sudo rpm -e <package>` | Removes an installed package. |
| `rpm -qa` | Lists all installed RPM packages. |
| `rpm -qi <package>` | Shows package info. |

#### **Example:**  
```bash
sudo rpm -ivh package.rpm   # Install an RPM manually
sudo rpm -e package         # Remove the package
```

---

## **Comparison Table**
| **Feature**       | **APT (Debian/Ubuntu)** | **YUM/DNF (RHEL/Fedora)** | **DPKG/RPM (Low-Level)** |
|------------------|----------------|----------------|----------------|
| **Install**      | `apt install`  | `yum/dnf install` | `dpkg -i` / `rpm -ivh` |
| **Remove**       | `apt remove`   | `yum/dnf remove`  | `dpkg -r` / `rpm -e` |
| **Update**       | `apt update && upgrade` | `yum/dnf update` | N/A |
| **Search**       | `apt search`   | `yum/dnf search` | N/A |
| **Manual File**  | `.deb` (dpkg)  | `.rpm` (rpm)     | Direct install |

---