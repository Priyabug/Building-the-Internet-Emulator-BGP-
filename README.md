# 🚀 Building the Internet Emulator

## 📌 Description
**Border Gateway Protocol (BGP)** is the standard exterior gateway protocol designed to exchange routing and reachability information among **autonomous systems (AS)** on the Internet. It is the *glue* of the Internet and a fundamental part of its infrastructure.
## Project Components

The project provides fundamental Internet components implemented as Python classes, including:

- Internet exchanges  
- Autonomous systems (AS)  
- BGP routers  
- DNS infrastructure  
- A range of other services  

These components serve as modular building blocks that users can assemble to construct their own programmable Internet emulations.

---

## 🛠️ Languages and Utilities Used
- 🐍 **Python**
- 🖥️ **Bash**
- 📦 **Docker and Docker Compose**
- 🌍 **BIRD Internet Routing Daemon**
- 📡 **tcpdump**
- 🏗️ **Linux Command-Line Utilities**
- 🌐 **SEED Internet Emulator Web Interface**
- 🏴‍☠️ **Ubuntu 20.04 VM**

---

## 💻 Environments Used
- 🏢 **Windows 10** *(21H2)*

---

## 📜 Program Walk-through

### 🔹 Task 1: Stub Autonomous System
- **Task 1.a:** Understanding **AS-155’s BGP Configuration**
- **Task 1.b:** Observing **BGP UPDATE Messages**
- **Task 1.c:** Experimenting with **Large Communities**
- **Task 1.d:** Configuring **AS-180**

### 🔹 Task 2: Transit Autonomous System
- **Task 2.a:** Experimenting with **IBGP**
- **Task 2.b:** Experimenting with **IGP**

### 🔹 Task 3: Path Selection

### 🔹 Task 4: IP Anycast




---

### 🌐 Key Learnings:

- Understood how **stub** and **transit** ASes are configured and how they influence BGP routing behavior.
- Simulated **prefix hijacking attacks**, demonstrating BGP’s vulnerabilities and the consequences of malicious route advertisement.
- Analyzed **BGP path selection**, **UPDATE messages**, **IBGP vs. EBGP**, and the use of **Large Communities** for advanced policy control.
- Explored the real-world application of **IP Anycast**, showcasing how the same IP can be advertised from multiple geographic locations.

---

### 🔐 Security Insight:

BGP is powerful—but not without flaws. Through this lab, we learned:

- How **misconfigurations** or **malicious behavior** can lead to **route hijacking** or **traffic interception**.
- The importance of deploying **RPKI (Resource Public Key Infrastructure)** and **BGP monitoring tools** to improve routing security.
- The need for **coordination among network operators** to ensure a resilient Internet backbone.

## ✅ Conclusion

This lab provided a comprehensive hands-on exploration of the **Border Gateway Protocol (BGP)**—the protocol that binds the global Internet together by enabling communication between Autonomous Systems (ASes).

---





