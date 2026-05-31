# Week 09 — Network Pivoting & Lateral Movement

**Date:** April 2026
**Program:** Knowledge House Cybersecurity Fellowship

## Summary

This week introduced the concept of network pivoting as a post-exploitation
technique used to move laterally through a target network after initial
compromise. Students explored how attackers leverage a foothold on one
machine to reach otherwise inaccessible network segments, simulating
real-world internal network traversal scenarios (Engebretson, 2013).

## Tools & Commands Used

- `route add` — add routes through a compromised session in Metasploit
- `portfwd add` — port forwarding through a Meterpreter session
- `auxiliary/server/socks_proxy` — set up a SOCKS proxy for pivoting
- `proxychains nmap` — run nmap through a proxy tunnel
- `ipconfig` / `ifconfig` — discover internal network interfaces
- `arp -a` — enumerate hosts on adjacent subnets
- `netstat -ano` — identify listening services and connections

## Key Takeaways

Pivoting is a critical post-exploitation skill that demonstrates the real
danger of a single compromised host within a segmented network. By routing
traffic through a Meterpreter session, a tester can enumerate and attack
internal systems that have no direct exposure to the internet. Understanding
pivoting techniques also informs network defenders on the importance of
micro-segmentation, host-based firewalls, and monitoring east-west traffic
within an enterprise environment (Engebretson, 2013).

## References

Engebretson, P. (2013). *The basics of hacking and penetration testing: Ethical hacking and penetration testing made easy* (2nd ed.). Syngress.

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.
