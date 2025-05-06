---
longform:
  format: single
  title: Networking Commands
title: Networking Commands
---
### **Networking Commands in Linux**  
Networking commands help you **configure, troubleshoot, and monitor** network connections. Below are the most essential commands:

---

## **1. `ifconfig` (Interface Configuration) – *Legacy***  
Displays and configures **network interfaces** (deprecated in favor of `ip`).  

### **Usage:**  
```bash
ifconfig          # Show all active interfaces
ifconfig eth0     # Show details of eth0
ifconfig eth0 up  # Enable eth0
ifconfig eth0 down # Disable eth0
```
### **Key Output Fields:**  
- `inet` → IPv4 address  
- `inet6` → IPv6 address  
- `RX/TX packets` → Received/Transmitted data  

⚠️ **Note:** `ifconfig` is outdated; use `ip` instead.

---

## **2. `ip` (Modern Replacement for `ifconfig`)**  
The **recommended** tool for managing network interfaces, routes, and addresses.  

### **Common Subcommands:**  
| Command | Description |
|---------|-------------|
| `ip addr` or `ip a` | Show IP addresses of all interfaces |
| `ip link` | List network interfaces (up/down status) |
| `ip route` | Display routing table |
| `ip neigh` | Show ARP table (MAC ↔ IP mapping) |

### **Examples:**  
```bash
ip addr show eth0    # Show IP of eth0  
ip link set eth0 up  # Enable eth0  
ip route add default via 192.168.1.1  # Set default gateway  
```

---

## **3. `netstat` (Network Statistics) – *Legacy***  
Shows **network connections, routing tables, and listening ports**.  

### **Common Flags:**  
| Flag | Description |
|------|-------------|
| `-t` | TCP connections |
| `-u` | UDP connections |
| `-l` | Listening ports |
| `-n` | Show numerical addresses (no DNS resolution) |
| `-p` | Show process using the port |

### **Examples:**  
```bash
netstat -tulnp    # List all listening TCP/UDP ports  
netstat -r        # Show routing table (same as `route -n`)  
```
⚠️ **Note:** `ss` (Socket Statistics) is the modern replacement.

---

## **4. `ping` (Test Network Connectivity)**  
Checks if a remote host is reachable using **ICMP packets**.  

### **Usage:**  
```bash
ping google.com       # Continuous ping (Ctrl+C to stop)  
ping -c 4 google.com  # Send 4 packets and stop  
```
### **Key Output:**  
- **`time=`** → Round-trip time (latency)  
- **`TTL=`** → Time To Live (prevents infinite loops)  

---

## **5. `traceroute` (Trace Network Path to a Host)**  
Shows the **route (hops)** taken by packets to reach a destination.  

### **Usage:**  
```bash
traceroute google.com  
```
### **Key Output:**  
- Each line represents a **hop** (router/gateway).  
- `* * *` means a hop didn’t respond (firewall blocking ICMP).  

📌 **Alternative:**  
```bash
tracepath google.com  # Works without root privileges  
```

---

## **Comparison Table**  
| **Command** | **Purpose** | **Replacement (Modern)** |
|------------|------------|------------------------|
| `ifconfig` | Show/set interfaces | `ip addr`, `ip link` |
| `netstat`  | Show connections/ports | `ss` |
| `route`    | Show routing table | `ip route` |
| `arp`      | Show ARP cache | `ip neigh` |

---
