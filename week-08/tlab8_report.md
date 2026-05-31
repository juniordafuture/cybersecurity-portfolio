# TLAB 8 — Operation Deep Pivot
# Week 08 — Knowledge House Cybersecurity Fellowship

## Objective

Operation Deep Pivot required students to perform a multi-stage network
reconnaissance and initial exploitation exercise against a layered Docker
target environment, then pivot from the initial foothold to enumerate a
secondary internal network segment.

## Environment

- Attacker: Kali Linux (Docker container)
- Target 1 (DMZ): Ubuntu 20.04 — 192.168.10.50
- Target 2 (Internal): Debian — 10.10.20.30 (reachable via pivot)
- Network: Multi-segment Docker network

## Phase 1: External Recon & Initial Access

1. Ran `nmap -sV -p- 192.168.10.50` — identified vsftpd 2.3.4 on port 21.
2. Searched Metasploit for vsftpd exploit: `search vsftpd`
3. Used `exploit/unix/ftp/vsftpd_234_backdoor` — obtained root shell on Target 1.
4. Enumerated network interfaces: `ifconfig` revealed dual-homed host on 10.10.20.0/24.

## Phase 2: Pivot to Internal Network

1. Backgrounded session and added pivot route: `run post/multi/manage/autoroute`
2. Launched SOCKS proxy: `use auxiliary/server/socks_proxy` on port 1080.
3. Configured proxychains and ran: `proxychains nmap -sT -Pn 10.10.20.0/24`
4. Discovered Target 2 at 10.10.20.30 with port 22 (SSH) and 80 (HTTP) open.
5. Documented all findings with command outputs and session details.

## Results

| Phase | Action | Result |
|---|---|---|
| Recon | nmap scan | vsftpd 2.3.4 identified |
| Exploit | Metasploit module | Root shell on Target 1 |
| Pivot | autoroute + proxychains | Internal subnet enumerated |
| Discovery | nmap via proxy | Target 2 identified |

## Conclusion

Operation Deep Pivot demonstrated a realistic multi-stage attack chain moving
from external reconnaissance through initial compromise to internal network
pivoting. The exercise highlighted the critical importance of network
segmentation and internal monitoring as defensive countermeasures.
