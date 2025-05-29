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

![image](https://github.com/user-attachments/assets/a7d2334e-edd0-417e-a6dc-7d6487c7a0b2)


---

# 🚀 Getting Started

## ✅ Step 1: Install the Necessary Software

To run the emulator, ensure the following are installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3](https://www.python.org/downloads/)

---

## 📂 Step 2: Set Up the Project

To enable the emulator code:

1. Add the project's root folder to the `PYTHONPATH` environment variable.
2. Run the following command inside the root directory to temporarily set it:

   ```bash
   source development.env

## 🌐 Step 3: Set Up the Proxy (Optional)

> _Only needed if you're having issues downloading Docker images (e.g., you're in Mainland China)._

The emulator pulls Docker images from Docker Hub. If you encounter **slow** or **failed** downloads:

- **Use a Docker Hub proxy**  
  📘 Follow the [proxy setup instructions](#) to configure your environment.

- **If proxies are slow or unreliable**, we recommend building the Docker images **locally**.  
  🛠️ Follow the [local build instructions](#) to build images directly on your machine.

---

✅ **If you're not facing any Docker Hub access issues, you can safely skip this step.**



## 🛠️ Languages and Utilities Used
- 🐍 **Python**
- 🖥️ **Bash**
- 📦 **Docker and Docker Compose**
- 🌍 **BIRD Internet Routing Daemon**
- 📡 **tcpdump**
- 🏗️ **Linux Command-Line Utilities**
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

## Key Learnings from Internet Emulation Lab

- **Understanding of Realistic Internet Modeling**  
  Learned how to emulate real-world Internet environments by modeling components such as ASes, IXes, DNS servers, and blockchain networks.

- **Limitations of GUI-Based Emulation Tools**  
  Gained insight into the limitations of traditional GUI emulators like GNS3 and Packet Tracer, especially for large-scale or specialized networks.

- **Benefits of Code-Based Emulation**  
  Discovered that code-driven emulators offer better flexibility, scalability, and automation for network design and experimentation.

- **Docker and SDK Integration**  
  Understood how to use Docker and a custom SDK to create lightweight, programmable virtual network nodes.

- **Hands-on with Internet Protocols and Infrastructure**  
  Acquired practical experience configuring and testing key Internet protocols (e.g., DNS, BGP) in an emulated environment.

- **Network Customization and Automation**  
  Learned to define network topologies programmatically, enabling repeatable and customizable network scenarios.

- **Emulation of Advanced Network Use Cases**  
  Gained knowledge in simulating complex use cases like cybersecurity attacks and blockchain mining in a controlled environment.

- **Component-Based Network Design Philosophy**  
  Learned the benefits of abstracting network functions into components, promoting modular and reusable network designs.

- **Scalability and Reusability in Emulation Environments**  
  Understood how programmatic emulation allows for scalable, resource-efficient setups that can be reused across multiple scenarios.


---


## ✅ Conclusion

This lab provided a comprehensive hands-on exploration of the **Border Gateway Protocol (BGP)**—the protocol that binds the global Internet together by enabling communication between Autonomous Systems (ASes).

---





