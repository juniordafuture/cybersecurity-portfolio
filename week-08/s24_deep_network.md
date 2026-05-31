# S24 — The Deep Network
# Week 08 — Knowledge House Cybersecurity Fellowship

## Session Overview

Session 24 explored advanced network reconnaissance techniques and deep
packet inspection to map complex multi-segment target environments. Students
used passive and active scanning strategies to build a comprehensive picture
of a target network's topology, services, and potential attack surfaces
(McNab, 2016).

## Tools & Commands Used

- `nmap -sV -O -A --traceroute <target>` — full service and OS fingerprinting
- `nmap -sn 192.168.0.0/24` — host discovery ping sweep
- `wireshark` — passive packet capture and protocol analysis
- `netdiscover -r 192.168.0.0/16` — ARP-based host discovery
- `dig` / `nslookup` — DNS enumeration
- `whois <target>` — domain registration information gathering
- `theHarvester -d <domain> -b google` — OSINT email and subdomain harvesting

## Steps Performed

1. Performed ping sweep to identify live hosts across the target subnet.
2. Ran full port scan with service version detection on discovered hosts.
3. Captured traffic in Wireshark to identify unencrypted protocols in use.
4. Performed DNS enumeration to map subdomains and mail servers.
5. Cross-referenced findings to build a network map of the target environment.

## Artifact: Network Recon Summary

```
Target Network: 192.168.10.0/24
Live Hosts Discovered: 4

Host: 192.168.10.1   | Role: Gateway    | Ports: 80, 443, 22
Host: 192.168.10.10  | Role: Web Server | Ports: 80, 443, 8080
Host: 192.168.10.20  | Role: DB Server  | Ports: 3306, 22
Host: 192.168.10.50  | Role: Workstation| Ports: 22, 139, 445

OS Fingerprint (10.10): Linux 4.x (Ubuntu)
OS Fingerprint (10.20): Linux 5.x (Debian)
```

## References

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.

McNab, C. (2016). *Network security assessment: Know your network* (3rd ed.). O'Reilly Media.
