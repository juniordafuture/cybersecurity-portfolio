# S33 — The Last Mile
# Week 11 — Knowledge House Cybersecurity Fellowship

## Session Overview

Session 33 served as the final session of Phase 1, bringing together all
offensive and defensive skills developed throughout the program. Students
conducted a mini end-to-end penetration test, from reconnaissance through
exploitation to post-exploitation and remediation reporting, demonstrating
professional-level workflow and documentation practices (Weidman, 2014).

## Steps Performed

1. Reconnaissance: `nmap -sV -O -A <target>` to fingerprint the target system.
2. Vulnerability identification: Cross-referenced open ports against known CVEs.
3. Exploitation: Selected and configured Metasploit module for identified service.
4. Post-exploitation: Enumerated users, checked sudo rights, reviewed cron jobs.
5. Privilege escalation: Identified SUID binary and escalated to root.
6. Cleanup: Removed dropped artifacts and closed Meterpreter session.
7. Documentation: Compiled full pentest report with findings and recommendations.

## Artifact: Final Pentest Summary

| Phase | Tool Used | Finding |
|---|---|---|
| Recon | nmap | Port 21 (FTP), 22 (SSH), 80 (HTTP) open |
| Exploitation | Metasploit vsftpd 2.3.4 | Remote shell obtained |
| Post-Exploit | Manual enumeration | SUID binary `/usr/bin/find` found |
| PrivEsc | GTFOBins find exploit | Root shell obtained |
| Remediation | Report | Patch FTP, remove SUID from find |

## References

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.

Weidman, G. (2014). *Penetration testing: A hands-on introduction to hacking*. No Starch Press.
