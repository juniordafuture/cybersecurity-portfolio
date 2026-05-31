# Week 07 Notes — Reconnaissance & Vulnerability Assessment

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S19 · S20 · S21 · TLAB-06

---

## Key Concepts

Week 07 introduced the reconnaissance and vulnerability assessment phase of the penetration testing lifecycle. Effective reconnaissance transforms public information into actionable intelligence, allowing operators to map an organization's external attack surface before a single packet is sent (Engebretson, 2013). Session 19 used Sublist3r for subdomain enumeration and Shodan for passive service fingerprinting on the CloudNano target, producing ThreatProfile_CloudNano.md with at least two discovered subdomains, two identified technologies, and three documented exposure points with real-world risk explanations.

Session 20 applied active scanning techniques using Nmap's -sV flag to perform service version detection against three target hosts. The nmap_scan_results.txt artifact documented all open ports and exact service versions for each host, along with two theory questions addressing why version detection is critical for vulnerability matching and how version information informs exploit selection. Accurate service enumeration directly enables the vulnerability triage performed in Session 21 (Lyon, 2009).

Session 21 and TLAB-06 completed the assessment cycle with risk-based triage. The remediation_plan.md artifact selected five vulnerabilities from Nikto output and justified each selection with explicit reference to both Likelihood and Impact — moving beyond CVSS scores to demonstrate analytical reasoning. The Perimeter_Assessment.md TLAB artifact synthesized all three phases: Nmap host discovery, Nikto web server findings, and a prioritized remediation recommendation with a full Likelihood × Impact justification.

## Tools Used

- `sublist3r` — subdomain enumeration
- `shodan` — passive service and infrastructure fingerprinting
- `nmap -sV` — active port and service version scanning
- `nikto` — web server vulnerability scanning

## References

Engebretson, P. (2013). *The basics of hacking and penetration testing: Ethical hacking and penetration testing made easy* (2nd ed.). Syngress.

Lyon, G. F. (2009). *Nmap network scanning: The official Nmap project guide to network discovery and security scanning*. Insecure.com LLC.
