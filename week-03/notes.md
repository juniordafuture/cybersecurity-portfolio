# Week 03 Notes — Python Scripting & Automation

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S07 · S08 · S09 · TLAB-03

---

## Key Concepts

Week 03 introduced Python as an automation layer for security operations. Security practitioners who can write purpose-built scripts reduce response times and eliminate manual errors in repetitive triage tasks (Seitz, 2021). Session 07 produced port_check.py, a socket-based port scanner that iterates over a list of target IP addresses and attempts a TCP connection to port 22, logging success or failure for each host. This script demonstrated the fundamental loop-and-socket pattern underlying more complex reconnaissance tools.

Session 08 applied file I/O automation to log analysis. The brute_detector.py script opened auth.log, iterated over each line searching for the string "Failed password," and wrote a brute_report.txt summarizing the attack signature count. This workflow mirrors real-world SIEM alert triage, where analysts parse authentication logs to detect credential stuffing and brute-force campaigns (Cichonski et al., 2012).

Session 09 and TLAB-03 elevated the automation to system-level monitoring. The system_auditor.py script used Python's subprocess module to execute shell commands, parsed the output for ALARM conditions, and serialized the findings into a JSON alert structure. The TLAB-03 capstone combined all three patterns — subprocess execution, log parsing, and structured output — into incident_response.py, which extracted attacker IPs from auth.log and wrote them to threat_report.json with an alert type and timestamp.

## Tools Used

- Python `socket` module — TCP port scanning
- Python file I/O (`open`, `readlines`) — log parsing
- Python `subprocess` module — system command execution
- Python `json` module — structured alert output

## References

Cichonski, P., Millar, T., Grance, T., & Scarfone, K. (2012). *Computer security incident handling guide* (SP 800-61 Rev. 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2

Seitz, J. (2021). *Black hat Python: Python programming for hackers and pentesters* (2nd ed.). No Starch Press.
