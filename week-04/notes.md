# Week 04 — Vulnerability Scanning

**Date:** February 2026
**Program:** Knowledge House Cybersecurity Fellowship

## Summary

This session introduced automated vulnerability scanning as a method for
identifying known weaknesses in target systems. Students used industry-standard
scanning tools to enumerate vulnerabilities and interpret scan output in the
context of a penetration testing engagement (Kennedy et al., 2011).

## Tools & Commands Used

- `nmap --script vuln` — Nmap vulnerability scripts
- `searchsploit <keyword>` — search Exploit-DB locally
- `msfconsole` — launch Metasploit Framework
- `use auxiliary/scanner/` — Metasploit auxiliary scanning modules
- `db_nmap` — run Nmap scans from within Metasploit

## Key Takeaways

Vulnerability scanning bridges the gap between passive reconnaissance and
active exploitation by identifying specific weaknesses that may be leveraged
during an engagement. The Common Vulnerability Scoring System (CVSS) provides
a standardized method for rating the severity of discovered vulnerabilities,
allowing testers to prioritize findings by risk level. Scan results must
always be validated manually to reduce false positives before reporting.

## References

Kennedy, D., O'Gorman, J., Kearns, D., & Aharoni, M. (2011). *Metasploit: The penetration tester's guide*. No Starch Press.

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.
