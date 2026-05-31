# Portfolio Audit — Phase 1 TEPP Final Submission

**Student:** Dwayne Saxton
**Program:** Knowledge House Cybersecurity Fellowship — Phase 1
**Date:** May 2026
**Repository:** https://github.com/juniordafuture/cybersecurity-portfolio

---

## Section 1: Repository Structure Audit

The following table documents the completion status of each weekly folder
in the portfolio repository.

| Week | Topic | Folder Present | notes.md | Artifacts |
|---|---|---|---|---|
| Week 01 | Linux Fundamentals | ✅ | ✅ | discovery.txt, harden.sh, threat_ips.txt, final_threat_report.txt |
| Week 02 | Networking & Subnetting | ✅ | ✅ | network_audit.txt, protocol_audit.txt, subnet_blueprint.txt, tlab_report.txt |
| Week 03 | Python for Security | ✅ | ✅ | brute_detector.py, incident_response.py, port_check.py, system_auditor.py, threat_report.json |
| Week 04 | Docker & Containers | ✅ | ✅ | deploy_web.sh, docker-compose.yml, hyperstack_audit.json, sandbox_report.txt |
| Week 05 | Metasploit Framework | ✅ | ✅ | notes only |
| Week 06 | Privilege Escalation | ✅ | ✅ | notes only |
| Week 07 | Web Application Security | ✅ | ✅ | notes only |
| Week 08 | Password Attacks & Deep Network | ✅ | ✅ | s24_deep_network.md, tlab8_report.md |
| Week 09 | Network Pivoting & Lateral Movement | ✅ | ✅ | pivot_routes.txt, lateral_movement_report.md |
| Week 10 | Web App Exploitation | ✅ | ✅ | s30_central_nervous_system.md, tlab10_report.md |
| Week 11 | Advanced Exploitation & Hardening | ✅ | ✅ | s31_barricade.md, s32_tripwire.md, s33_last_mile.md, tlab11_report.md |

---

## Section 2: Skill Progression Summary

Phase 1 of the Knowledge House Cybersecurity Fellowship covered the core
foundations of offensive and defensive security across eleven weeks. The
curriculum progressed systematically from Linux fundamentals and networking
principles through Python scripting, containerization, and advanced
penetration testing techniques (Knowledge House, 2026).

Weeks 1 through 4 established the technical foundation required for all
subsequent coursework. Linux command-line proficiency, TCP/IP networking,
Docker containerization, and Python scripting are universally applicable
skills across both offensive and defensive security roles. These early
weeks required the most deliberate practice as they formed the prerequisite
basis for all later lab environments (Engebretson, 2013).

Weeks 5 through 8 introduced the offensive security methodology in earnest.
The Metasploit Framework, privilege escalation techniques, web application
vulnerabilities, and credential attacks represent the core toolkit of a
penetration tester. Each week built on the previous, culminating in TLAB 8
(Operation Deep Pivot), which required chaining multiple techniques
into a realistic multi-stage engagement (Kennedy et al., 2011).

Weeks 9 through 11 pushed into advanced territory including network
pivoting, SIEM and log analysis, and full-cycle exploitation with defensive
hardening. TLAB 11 (Operation Fortress) was the most complex lab of the
phase, requiring students to both compromise and remediate a target system,
demonstrating the dual perspective essential to professional security work
(Seitz, 2021).

---

## Section 3: Tools & Technologies Mastered

The following tools were used across Phase 1 labs and sessions:

- **Reconnaissance:** nmap, netdiscover, theHarvester, Shodan, Sublist3r
- **Exploitation:** Metasploit Framework, msfvenom, sqlmap, Burp Suite
- **Post-Exploitation:** Meterpreter, autoroute, proxychains, GTFOBins
- **Web Application:** nikto, gobuster, wfuzz, curl
- **Defensive:** auditd, fail2ban, UFW/iptables, Tripwire, Splunk
- **Scripting:** Bash, Python (socket, subprocess, os modules)
- **Infrastructure:** Docker, Docker Compose, VirtualBox, Linux (Ubuntu/Debian/Kali)
- **Version Control:** Git, GitHub

---

## Section 4: Professional Reflection

Entering the Knowledge House Cybersecurity Fellowship, the foundational
goal was to transition from general IT familiarity into a structured,
skills-based cybersecurity practice. Phase 1 delivered that foundation
in a way that was both technically rigorous and professionally relevant.

The most significant personal growth came through the hands-on lab
environments. Reading about SQL injection or buffer overflows is
fundamentally different from executing these techniques in a controlled
Docker environment and seeing the results in real time. This experiential
learning approach, grounded in actual tooling used by security professionals,
accelerates competency development in a way that traditional coursework
alone cannot replicate (Kolb, 1984).

The progression from defender to attacker and back again—most clearly
demonstrated in TLAB 11 (Operation Fortress)—was transformative. Understanding
how an attacker thinks, what paths they exploit, and what artifacts they
leave behind directly informs how to build better defenses. This dual
perspective is increasingly recognized as essential in modern security
operations (Weidman, 2014).

Professionally, Phase 1 reinforced that cybersecurity is not a destination
but a continuous discipline. Threat actors evolve, new vulnerabilities
emerge, and defensive tools must adapt. The habits developed in this
phase—documenting work thoroughly, committing incrementally, writing
clearly, and approaching problems methodically—are as important to a
long-term career as any specific technical skill. These practices will
continue to guide work in Phase 2 and beyond.

---

## References

Engebretson, P. (2013). *The basics of hacking and penetration testing:
Ethical hacking and penetration testing made easy* (2nd ed.). Syngress.

Kennedy, D., O'Gorman, J., Kearns, D., & Aharoni, M. (2011). *Metasploit:
The penetration tester's guide*. No Starch Press.

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*.
Knowledge House.

Kolb, D. A. (1984). *Experiential learning: Experience as the source of
learning and development*. Prentice Hall.

Seitz, J. (2021). *Black hat Python: Python programming for hackers and
pentesters* (2nd ed.). No Starch Press.

Weidman, G. (2014). *Penetration testing: A hands-on introduction to
hacking*. No Starch Press.
