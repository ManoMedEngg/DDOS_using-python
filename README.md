# 🛡️ Healthcare DDoS Defense & Awareness Kit

> **"In healthcare, availability isn't just a metric—it's a heartbeat."**

![Healthcare Security Badge](https://img.shields.io/badge/Status-Active-brightgreen) ![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Termux-blue) ![License](https://img.shields.io/badge/License-MIT-orange)

## 🏥 Why Prevent DDoS in the Healthcare Sector?

Distributed Denial of Service (DDoS) attacks are often viewed as mere inconveniences in the tech world. However, in the **Healthcare Sector**, the stakes are exponentially higher.

* **🚑 Life-Critical Systems:** Modern hospitals rely on IoT devices, telemetry, and real-time data transmission. A network outage can sever the connection between a patient monitoring system and the nursing station.
* **📂 Electronic Health Records (EHR):** When doctors cannot access patient history, allergies, or medication lists due to server downtime, treatment is delayed. In emergencies, minutes matter.
* **📞 Emergency Response:** Many VoIP and dispatch systems run on the same network infrastructure. A DDoS attack can jam the lines, preventing ambulances from being dispatched.

**Protecting these networks is not just IT support—it is patient care.**

## 🧠 Awareness: Understanding the Threat

Imagine a hospital entrance designed for ambulances. Now, imagine thousands of fake cars suddenly crowding that entrance, blocking the real ambulances from getting in.

That is a **DDoS attack**.

Attackers flood a network with malicious traffic, overwhelming the servers so legitimate users (doctors, patients, first responders) cannot connect. This tool/guide is designed to help administrators test their resilience or set up defenses against such floods.

## 📋 Requirements

Before installing, ensure you have the following environments set up. This tool is lightweight but requires standard libraries.

* **Python 3.x** (Essential for running the scripts)
* **Git** (To clone the repository)
* **Internet Connection** (For dependency installation)
* **Root/Administrator Privileges** (Required for network manipulation)


## ⚙️ Installation Guide

Choose your operating system below to get started.

### 🐧 Linux (Debian/Ubuntu/Kali)

The native environment for security testing.

1.  **Update your package list:**
    sudo apt update && sudo apt upgrade -y
    
2.  **Install Git and Python:**
    sudo apt install git python3 python3-pip -y
    
3.  **Clone the repository:**
    git clone [https://github.com/ManoMedEngg/DDOS_using-python.git](https://github.com/ManoMedEngg/DDOS_using-python.git)
    
4.  **Enter directory and install requirements:**
    cd DDOS_using-python

    pip3 install -r requirements.txt
    
5.  **Run:**
    python3 main.py
    

### 📱 Termux (Android)

For testing on the go.

1.  **Update Termux:**
    pkg update && pkg upgrade -y
    
2.  **Install dependencies:**
    pkg install git python -y
    
3.  **Clone the repository:**
    git clone [https://github.com/ManoMedEngg/DDOS_using-python.git](https://github.com/ManoMedEngg/DDOS_using-python.git)
    
4.  **Navigate and Install:**
    cd DDOS_using-python

    pip install -r requirements.txt
    
5.  **Run:**
    python main.py
    

### 🪟 Windows

1.  **Install Python:** Download and install Python 3.x from [python.org](https://www.python.org/). *Ensure you check the box "Add Python to PATH" during installation.*
2.  **Download the Source:**
    * Click the green **Code** button -> **Download ZIP**.
    * Extract the ZIP file to your desktop.
3.  **Open Terminal:**
    * Open `cmd` or PowerShell.
    * Navigate to the folder: `cd Desktop/DDOS_using-python`
4.  **Install Requirements:**
    cmd
    pip install -r requirements.txt
5.  **Run:**
    cmd
    python main.py
    
## ⚠️ Disclaimer & Ethical Use

**This project is for educational purposes and stress testing YOUR OWN networks only.**

Using DDoS tools or stress testers on networks you do not own (including hospital networks, government sites, or private servers) is a **criminal offense**. The developers of this repository assume no liability for misuse.

> *Protect the healers, don't harm them.*

