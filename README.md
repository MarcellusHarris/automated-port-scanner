# Automated Port Scanner & Vulnerability Assessment

This project presents a Python-based port scanning tool designed to automate the discovery of open ports on a target system. It uses the `nmap` Python module to identify active services and analyze potential vulnerabilities. This project was presented at BootCon in front of an audience of over 300 attendees.

---

#Objective

To develop a Python script that automates the process of scanning open ports and assists in basic vulnerability assessment.

---

#Prerequisites

- Python 3.11.4 or later
- Nmap 7.94 or later
- Target IP address (e.g., local device like a PlayStation 5)

Install the required library using:

```bash
pip install python-nmap

---

Vulnerability Assessment: dnscat2
Demonstrated how dnscat2 can be used to establish covert C2 channels via DNS traffic.

Used a demo to show how unauthorized access could be obtained over port 53.

Discussed how attackers could use this technique to extract data or control systems.

---

Potential Threats
Remote control over systems (e.g., PlayStation 5)

Theft of sensitive personal information (login credentials, payment data)

System crashes or permanent damage due to exploitation

Mitigations
Use IDS/IPS (e.g., Snort) to monitor DNS traffic

Block abnormal DNS requests at the firewall level

Use network segmentation and access controls

