# 🛡️ Honeynet Project

A lightweight, professional-grade honeynet built using Docker Compose. This project emulates vulnerable SSH, FTP, and HTTP services to attract attackers, log behavior, and support blue team analysis. Ideal for labs, research, or security monitoring use cases.

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/4952db7a-9587-4584-a630-8ec79182ed87)
![image](https://github.com/user-attachments/assets/45238bf7-3aa5-455f-8d6f-1f6224187c9c)
![image](https://github.com/user-attachments/assets/5d1d29a8-547f-4456-a079-e781531f7982)
![image](https://github.com/user-attachments/assets/f80d7fa1-4d05-42cb-90d1-ee55a48783bd)
![image](https://github.com/user-attachments/assets/1db0aa44-cbb7-4290-9a8d-6b8444e8c14f)
![image](https://github.com/user-attachments/assets/094f8ef7-103f-4825-9939-cf5da20dd79e)
![image](https://github.com/user-attachments/assets/0b59e021-7e50-4ec0-a7c7-62d29ff22b6c)



---

## ✨ Highlights

* Dockerized honeypots: SSH, FTP, HTTP
* Modular architecture: each service runs independently
* Logs attacker interactions in real-time
* SIEM-ready: logs can be forwarded to external systems
* VLAN-ready for isolated deployment

---

## ⚙️ Deployment Guide

### ✅ Requirements

* Ubuntu Server 20.04+
* Docker & Docker Compose
* Root or sudo privileges

### 📦 Installation

```bash
# Install Docker and Docker Compose
sudo apt update && sudo apt install -y docker.io docker-compose

# Clone the honeynet repository
git clone https://github.com/Rzfn2/Honeynet.git
cd honeynet

# Build honeypot containers
sudo docker-compose build

# Start the honeynet
sudo docker-compose up -d
```

### 🔑 SSH Key Setup 

To avoid SSH permission issues during testing:

```bash
# Generate key pair if needed
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
```

---

## 🌐 VLAN Network Isolation

Isolate your honeynet from the host or production environment:

```bash
# Create VLAN interface (e.g. VLAN ID 10)
sudo ip link add link ens33 name ens33.10 type vlan id 10

# Assign IP
sudo ip addr add 192.168.10.1/24 dev ens33.10

# Activate VLAN
sudo ip link set up ens33.10
```

Ensure Docker containers are bridged to this VLAN manually or through custom network configurations.

---

## 🌍 Honeypot Services

| Protocol | Container      | Port |
| -------- | -------------- | ---- |
| SSH      | ssh\_honeypot  | 2222 |
| FTP      | ftp\_honeypot  | 21   |
| HTTP     | http\_honeypot | 8080 |

---

## 🧪 Testing Interaction

From your attacker machine (e.g., Kali Linux):

```bash
# SSH
ssh test@<ip> -p 2222

# FTP
ftp <ip>

# HTTP
curl http://<ip>:8080
```

---

## 📝 Log Files

| Service | Log Path                  |
| ------- | ------------------------- |
| SSH     | audit.log, cmd\_audit.log |
| FTP     | logs/ftp\_audit.log       |
| HTTP    | logs/http\_audit.log      |

Access logs with:

```bash
sudo docker exec -it ssh_honeypot cat audit.log
```

---

## 🔒 Security Recommendations

* Deploy in a VLAN for network isolation
* Restrict outbound container traffic
* Forward logs to ELK/Splunk/SIEM

---

## 🧾 License

MIT License — for academic, SOC testing, and cybersecurity research use only.

---

## 👤 Author

Made by [Abdullah](https://github.com/Rzfn2)

Feedback and professional collaboration are welcome. ⭐
