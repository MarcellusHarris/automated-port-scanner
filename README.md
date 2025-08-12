# Automated Port Scanner & Vulnerability Assessment
**Live Demo:**  
[https://marcellusharris.github.io/automated-port-scanner/](https://marcellusharris.github.io/automated-port-scanner/)
![Python](https://img.shields.io/badge/Python-3.11-blue)![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Security](https://img.shields.io/badge/Security-DNS%20C2%20Demo-red)
![Presented at BootCon](https://img.shields.io/badge/Presented-BootCon-blueviolet)

This project presents a Python-based port scanning tool designed to automate the discovery of open ports on a target system. It uses the `nmap` Python module to identify active services and analyze potential vulnerabilities. This project was presented at BootCon in front of an audience of over 300 attendees.

---

## Objective

To develop a Python script that automates the process of scanning open ports and assists in basic vulnerability assessment.

---

## Features

- Fast TCP port scanning using `python-nmap`
-  Integrated basic vulnerability awareness and analysis
-  Terminal-based interface for quick testing
-  Covert DNS C2 demo using `dnscat2`
-  Real-world threat simulation (tested on devices like PlayStation 5)
-  Defensive insights: IDS, firewalls, and segmentation best practices
-  Includes screenshot for visual appeal


## Prerequisites

- Python 3.11.4 or later  
- Nmap 7.94 or later  
- Target IP address (e.g., local device like a PlayStation 5)

Install the required library using:
```bash
pip install python-nmap

- Block abnormal DNS requests at the firewall level  
- Use network segmentation and access control

![Demo Screenshot](screenshot.png)
## Vulnerabilxity Assessment: dnscat2

Demonstrated how **dnscat2** can be used to establish covert C2 channels via DNS traffic.

Used a live demo to show how unauthorized access could be obtained over port 53.

Discussed how attackers could use this technique to extract data or control systems in stealth.

---

## Potential Threats

- Remote control over systems (e.g., PlayStation 5)  
- Theft of sensitive personal information (login credentials, payment data)  
- System crashes or permanent damage due to exploitation  

---

## Mitigations

- Use IDS/IPS (e.g., Snort) to monitor DNS traffic  
- Block abnormal DNS requests at the firewall level  
- Use network segmentation and access controls  
 
