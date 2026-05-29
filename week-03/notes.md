# Week 03 — Reconnaissance & Nmap Scanning

**Date:** February 2026
**Program:** Knowledge House Cybersecurity Fellowship

## Summary

This session focused on the reconnaissance phase of penetration testing,
with hands-on practice using Nmap for network discovery and port scanning.
Reconnaissance is the first phase of the penetration testing lifecycle and
involves gathering information about target systems without triggering
detection (Lyon, 2009).

## Tools & Commands Used

- `nmap -sn <range>` — ping sweep / host discovery
- `nmap -sV <target>` — service and version detection
- `nmap -sS <target>` — stealth SYN scan
- `nmap -O <target>` — OS fingerprinting
- `nmap -A <target>` — aggressive scan (OS, version, scripts)
- `nmap -p- <target>` — scan all 65535 ports
- `nmap --script vuln <target>` — run vulnerability scripts

## Key Takeaways

Nmap is one of the most widely used tools in network security assessments
and is essential knowledge for any penetration tester. The difference
between scan types — TCP connect, SYN stealth, and UDP — determines how
detectable a scan is to intrusion detection systems. Service version
detection with `-sV` provides critical information about potential
vulnerabilities tied to specific software versions running on open ports.

## References

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.

Lyon, G. F. (2009). *Nmap network scanning: The official Nmap project guide to network discovery and security scanning*. Insecure.com LLC.
