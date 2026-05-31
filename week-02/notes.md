# Week 02 Notes — Networking & Protocol Analysis

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S04 · S05 · S06 · TLAB-02

---

## Key Concepts

Week 02 established the networking foundations required for both offensive reconnaissance and defensive monitoring. A thorough understanding of the OSI model and TCP/IP protocol suite enables analysts to interpret traffic patterns, identify anomalous behavior, and design segmented network architectures (Tanenbaum & Wetherall, 2021). Session 04 focused on interface configuration and connectivity verification, using ip addr and ping to restore a downed network adapter and confirm four-packet bidirectional communication, which was documented in network_audit.txt.

Session 05 introduced subnetting and CIDR notation. The ipcalc tool was used to compute network boundaries — including the network ID, broadcast address, and usable host range — for a given subnet mask (RFC 1518, 1993). This subnet_blueprint.txt artifact is foundational for designing segmented environments such as the air-gapped Docker stacks introduced in Week 04.

Session 06 and TLAB-02 examined layer-4 through layer-7 protocols in live traffic. The ss -tuln command enumerated all listening sockets, curl -I retrieved HTTP response headers to fingerprint web services, and dig resolved DNS records to identify domain infrastructure. The tlab_report.txt artifact captured the restored default gateway from ip route output and a tcpdump snippet confirming the TCP three-way handshake — [S], [S.], and [.] flags — verifying that connection state was fully restored.

## Tools Used

- `ip addr`, `ip route`, `ping` — interface and connectivity management
- `ipcalc` — subnet and CIDR calculation
- `ss -tuln` — socket and port enumeration
- `curl -I` — HTTP header fingerprinting
- `dig` — DNS record resolution
- `tcpdump` — packet capture and handshake analysis

## References

Rekhter, Y., & Li, T. (1993). *An architecture for IP address allocation with CIDR* (RFC 1518). Internet Engineering Task Force. https://www.rfc-editor.org/rfc/rfc1518

Tanenbaum, A. S., & Wetherall, D. J. (2021). *Computer networks* (6th ed.). Pearson.
