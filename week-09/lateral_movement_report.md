# Lateral Movement Lab Report
# Week 09 — Knowledge House Cybersecurity Fellowship

## Objective

Demonstrate lateral movement from a compromised DMZ host to an internal
network segment using Metasploit pivot routes and proxychains.

## Environment

- Attacker: Kali Linux (Docker container)
- Initial foothold: Ubuntu target (192.168.1.50)
- Internal target segment: 10.10.20.0/24

## Steps Performed

1. Gained Meterpreter shell on initial Ubuntu target via prior exploit.
2. Ran `ipconfig` to identify dual-homed network interfaces.
3. Added internal subnet route: `run post/multi/manage/autoroute`
4. Launched SOCKS proxy module on port 1080.
5. Configured proxychains.conf to route through 127.0.0.1:1080.
6. Ran `proxychains nmap -sT -Pn 10.10.20.0/24` to enumerate internal hosts.
7. Identified two live hosts on the internal segment.

## Results

Successfully pivoted into the internal network segment without direct
exposure from the attacker machine. Two internal hosts identified and
services enumerated through the pivot tunnel.

## Conclusion

This exercise demonstrated how a single compromised host on a perimeter
network can serve as a gateway into protected internal infrastructure.
Proper network segmentation and east-west traffic monitoring are essential
defensive countermeasures against lateral movement techniques.
