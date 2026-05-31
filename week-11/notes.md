# Week 11 Notes — Defense in Depth

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S31 · S32 · S33 · TLAB-11

---

## Key Concepts

Week 11 focused on Defense in Depth (DiD) — the strategy of layering independent security controls so that the failure of any single control does not result in a complete compromise (NIST, 2020). The three sessions each addressed one layer of this architecture: perimeter filtering at the network boundary, signature-based detection at the network perimeter, and behavioral monitoring at the endpoint. Designing controls that operate independently and at different layers of the kill chain ensures that an attacker who bypasses one control still faces additional barriers.

Session 31 produced firewall_config.sh, an iptables script implementing egress filtering for a DMZ web server. The script allowed inbound TCP traffic on ports 80 and 443, blocked all outbound connections to the internal subnet 10.0.5.0/24, and added a specific exception permitting outbound traffic to the database server on port 3306. Egress filtering is a frequently overlooked but critical control — blocking outbound C2 communication can stop an attacker from issuing commands to a compromised host even after initial access is achieved (Cheswick et al., 2003).

Session 32 and Session 33 addressed detection controls. The custom_ids.rules artifact deployed two Suricata signatures: one alerting on ICMP ping traffic targeting the protected server and a second detecting the Ghost_Bear malware scanner's unique HTTP User-Agent string. Session 33 produced an edr_policy.xml Sysmon configuration that triggers on any process creation event where the command line contains "delete shadows" — a direct indicator of ransomware attempting to destroy Volume Shadow Copies. The TLAB-11 Operation Fortress Report integrated all three controls into a unified Defense in Depth narrative covering the C2 egress threat, the web shell detection layer, and the endpoint post-exploitation indicator.

## Tools Used

- `iptables` — network-layer egress filtering and access control
- Suricata rule syntax — network intrusion detection signatures
- Sysmon (`edr_policy.xml`) — endpoint process creation monitoring
- `cat`, `git add/commit/push` — artifact capture and version control

## References

Cheswick, W. R., Bellovin, S. M., & Rubin, A. D. (2003). *Firewalls and internet security: Repelling the wily hacker* (2nd ed.). Addison-Wesley.

National Institute of Standards and Technology. (2020). *Security and privacy controls for information systems and organizations* (SP 800-53 Rev. 5). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-53r5
