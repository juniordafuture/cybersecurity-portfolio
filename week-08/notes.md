# Week 08 Notes — Exploitation & Privilege Escalation

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S22 · S23 · S24 · TLAB-08

---

## Key Concepts

Week 08 moved from assessment into active exploitation, covering the full post-compromise lifecycle from initial access through lateral movement. The Metasploit Framework provides a structured environment for exploit development, payload delivery, and post-exploitation operations, and is the industry-standard tool for authorized penetration testing engagements (Kennedy et al., 2011). Session 22 produced exploit_verification.png, a screenshot confirming an active Meterpreter session with getuid output showing elevated access and sysinfo output identifying the target machine.

Session 23 addressed post-exploitation privilege escalation on both Linux and Windows platforms. On Linux, GTFOBins was used to identify a SUID binary that could be abused to spawn a root shell. On Windows, WinPEAS enumerated a service with an unquoted executable path in a world-writable directory, and msfvenom generated a malicious service binary to replace it, achieving nt authority\system access. The escalation_path.txt artifact documented all four required fields: vulnerable service name, writable path, exact msfvenom command, and the confirming whoami output.

Session 24 and TLAB-08 introduced pivoting and lateral movement through internal network segments. Metasploit's autoroute module established a routing table entry for the internal subnet, and proxychains tunneled an nmap scan through the active session to reach 10.0.9.50, discovering an open Redis port on the isolated segment. The Deep_Pivot_Report.md capstone documented all four phases of the operation chain from initial GTFOBins escalation through the confirmed internal network scan.

## Tools Used

- `msfconsole`, Metasploit modules — exploit delivery and session management
- `meterpreter` — post-exploitation shell and command execution
- GTFOBins — Linux SUID binary abuse for privilege escalation
- `WinPEAS` — Windows privilege escalation enumeration
- `msfvenom` — custom payload generation
- `autoroute`, `proxychains`, `nmap` — network pivoting and internal scanning

## References

Kennedy, D., O'Gorman, J., Kearns, D., & Aharoni, M. (2011). *Metasploit: The penetration tester's guide*. No Starch Press.

Walter, J. (2020). *Penetration testing: A hands-on introduction to hacking*. No Starch Press.
