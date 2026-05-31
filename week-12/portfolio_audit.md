# Portfolio Audit — Week 12

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Submission:** TLAB-12 · Portfolio Review

---

## Repository Checklist

| Item | Status |
|------|--------|
| Repository is public | ✅ |
| Root README.md present and matches required template | ✅ |
| week-01/ through week-11/ folders present | ✅ |
| Each week folder contains session artifacts | ✅ |
| Each week folder contains a completed notes.md in APA style | ✅ |
| week-12/ contains portfolio_audit.md | ✅ |
| Professional Reflection section completed | ✅ |
| Commit history is clean and readable | ✅ |

---

## Artifact Inventory

### Week 01 — Linux Fundamentals & Threat Pipeline
- `discovery.txt` — filesystem reconnaissance artifact with token value and mission secret
- `harden.sh` — system hardening script with chmod/chown permission controls
- `threat_ips.txt` — deduplicated attacker IP list extracted via shell pipeline
- `final_threat_report.txt` — TLAB-01 capstone confirming full pipeline completion

### Week 02 — Networking & Protocol Analysis
- `network_audit.txt` — ping output confirming 4 packets transmitted, 4 received
- `subnet_blueprint.txt` — ipcalc output with network ID, broadcast, and host range
- `protocol_audit.txt` — ss -tuln, curl -I, and dig outputs
- `tlab_report.txt` — ip route gateway restoration and tcpdump TCP handshake flags

### Week 03 — Python Scripting & Automation
- `port_check.py` — socket-based port scanner with loop and connect_ex logic
- `brute_detector.py` — log parser with file I/O, string match, and report writer
- `system_auditor.py` — subprocess auditor with JSON alert output
- `incident_response.py` + `threat_report.json` — TLAB-03 IR automation capstone

### Week 04 — Containers & Docker
- `sandbox_report.txt` — sandbox configuration and forensic documentation workflow
- `deploy_web.sh` — Docker container deployment automation script
- `docker-compose.yml` — air-gapped multi-container stack with network segmentation
- `hyperstack_audit.json` — TLAB-04 network isolation audit with all six fields

### Week 05 — Active Directory & Identity Management
- `onboard_engineers.ps1` — PowerShell AD user provisioning script
- `gpo_audit.txt` — Group Policy documentation covering gpupdate, LSDOU, and OU scoping
- `tlab5_report.txt` — TLAB-05 unified identity and AD audit report

### Week 06 — Capstone Readiness & The Hardened Outpost
- `readiness_check.log` — self-assessment of five core tool domains with remediation plan
- `practical_exam_report.txt` — S17 exam artifact documenting all commands used
- `HardenedOutpost_SAD.pdf` — Sprint 01 capstone System Architecture Document

### Week 07 — Reconnaissance & Vulnerability Assessment
- `ThreatProfile_CloudNano.md` — OSINT reconnaissance with subdomains, tech stack, exposure points
- `nmap_scan_results.txt` — service version scan of three hosts with theory analysis
- `remediation_plan.md` — risk-based triage of five vulnerabilities with Likelihood × Impact
- `Perimeter_Assessment.md` — TLAB-06 three-phase perimeter assessment report

### Week 08 — Exploitation & Privilege Escalation
- `exploit_verification.png` — Meterpreter session with getuid and sysinfo confirmation
- `escalation_path.txt` — Linux GTFOBins and Windows service hijack escalation chain
- `pivot_success.png` + `Deep_Pivot_Report.md` — TLAB-08 lateral movement operation report

### Week 09 — Web Application Attacks
- `sqli_report.txt` — SQL injection chain: bypass, column enum, table discovery, salary exfil
- `xss_payloads.txt` — Reflected XSS, Stored XSS cookie theft, and CSRF attack documentation
- `api_audit.log` — BOLA ID enumeration and Burp Intruder discount code discovery
- `OmniPortal_Assessment.md` — TLAB-09 chained web attack assessment report

### Week 10 — Digital Forensics & Incident Response
- `collection_log.txt` — live triage with process PID and evidence hashes (MD5 + SHA256)
- `forensic_findings.md` — disk forensics: threat actor, deleted executable, timestamp, persistence
- `attack_timeline.csv` — three-phase attack timeline correlated from multi-source logs
- `Incident_Response_Report.md` — TLAB-10 full investigation: SIEM + memory + disk forensics

### Week 11 — Defense in Depth
- `firewall_config.sh` — iptables DMZ egress filtering script
- `custom_ids.rules` — Suricata IDS signatures for ICMP and Ghost_Bear malware
- `edr_policy.xml` — Sysmon EDR policy detecting ransomware shadow copy deletion
- `TLAB11/Operation_Fortress_Report.md` — three-layer defense architecture report

---

## Professional Reflection

Entering this program, my technical background was limited to general computer use and a surface-level familiarity with the command line. Over the course of eleven weeks, I developed from a user who could navigate a Linux terminal into a practitioner who can build threat pipelines, write Python automation scripts, deploy containerized infrastructure, conduct authorized penetration tests, perform digital forensics on disk images, and design layered defensive architectures. The breadth of that progression is difficult to fully articulate, but the artifact record in this repository demonstrates it concretely.

The single most significant shift in my thinking occurred during Week 07 and Week 08, when the program moved from defensive and administrative work into active reconnaissance and exploitation. Running a live Nmap service version scan, identifying a real vulnerability, and then weaponizing it in a controlled environment forced me to internalize a perspective I had only understood abstractly: that every open port and every unpatched service is a decision with consequences. The exploit_verification.png screenshot — showing an active Meterpreter session with elevated privileges — is not just a lab artifact. It is evidence that the gaps in an organization's patch management and network segmentation policies translate directly into attacker capabilities. That realization changed the way I read every defensive document I touched afterward.

Week 10's forensics and incident response content reinforced a complementary lesson about precision and documentation. The fls and icat workflow for recovering a deleted executable from a disk image required exact inode numbers and produced exact evidence. In a real investigation, a single incorrect command — or an undocumented one — can compromise the integrity of a legal case or allow an attacker to remain undetected. The discipline of recording every command used, hashing every piece of evidence collected, and writing findings in structured, reproducible formats is not bureaucratic overhead. It is the practice that distinguishes a professional analyst from someone who just ran the right tool by accident.

The Defense in Depth week crystallized for me how these skills connect across the program. The iptables egress filter blocks the C2 callback that the Meterpreter session in Week 08 would have used. The Suricata signature detects the web shell traffic that the OmniPortal SQL injection in Week 09 would have enabled. The Sysmon EDR rule catches the "delete shadows" command that follows a successful ransomware deployment. None of these controls exists in isolation — they are a layered response to the attacker's entire kill chain, and understanding the offensive techniques is what makes the defensive configurations meaningful rather than mechanical.

Moving forward, the areas I have identified for continued development are network forensics (particularly PCAP analysis at scale), cloud security architecture, and the formal penetration testing report writing skills needed to communicate findings to a non-technical audience. The readiness_check.log artifact from Week 06 documented these gaps honestly, and the remediation plan I wrote then remains the roadmap I intend to follow into the next phase of the program. This portfolio is not a finished record — it is the foundation of a practice that I intend to keep building.

---

## References

Casey, E. (2011). *Digital evidence and computer crime: Forensic science, computers, and the internet* (3rd ed.). Academic Press.

Cichonski, P., Millar, T., Grance, T., & Scarfone, K. (2012). *Computer security incident handling guide* (SP 800-61 Rev. 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2

Engebretson, P. (2013). *The basics of hacking and penetration testing: Ethical hacking and penetration testing made easy* (2nd ed.). Syngress.

Kennedy, D., O'Gorman, J., Kearns, D., & Aharoni, M. (2011). *Metasploit: The penetration tester's guide*. No Starch Press.

National Institute of Standards and Technology. (2020). *Security and privacy controls for information systems and organizations* (SP 800-53 Rev. 5). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-53r5

OWASP Foundation. (2021). *OWASP Top 10: 2021*. https://owasp.org/Top10/

Shotts, W. (2019). *The Linux command line: A complete introduction* (2nd ed.). No Starch Press.
