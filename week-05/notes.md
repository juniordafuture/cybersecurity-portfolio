# Week 05 — Metasploit Framework

**Date:** February 2026
**Program:** Knowledge House Cybersecurity Fellowship

## Summary

This session provided hands-on experience with the Metasploit Framework,
one of the most widely used penetration testing platforms in the industry.
Students practiced identifying, selecting, and configuring exploits to
compromise vulnerable target systems in a controlled lab environment
(Kennedy et al., 2011).

## Tools & Commands Used

- `msfconsole` — launch Metasploit
- `search <term>` — search for modules
- `use <module>` — select a module
- `show options` — display required configuration
- `set RHOSTS <ip>` — set target IP
- `set LHOST <ip>` — set listener IP
- `set payload <payload>` — select payload
- `exploit` / `run` — launch the exploit
- `sessions -l` — list active sessions
- `sessions -i <id>` — interact with a session

## Key Takeaways

The Metasploit Framework streamlines the exploitation process by providing
a structured interface to thousands of known exploits and payloads. Understanding
the relationship between exploits, payloads, and listeners is fundamental to
achieving reliable remote code execution during an engagement. Post-exploitation
modules within Metasploit allow testers to escalate privileges, extract
credentials, and maintain persistence after initial access is gained.

## References

Kennedy, D., O'Gorman, J., Kearns, D., & Aharoni, M. (2011). *Metasploit: The penetration tester's guide*. No Starch Press.

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.
