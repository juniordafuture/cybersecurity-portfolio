# TLAB 11 — Operation Fortress
# Week 11 — Knowledge House Cybersecurity Fellowship

## Objective

Operation Fortress challenged students to both attack a target system and
harden it against future compromise. This dual-perspective lab required
executing an exploitation chain, documenting findings, and then applying
defensive controls to remediate each identified vulnerability.

## Environment

- Attacker: Kali Linux (Docker container)
- Target: Ubuntu 20.04 (Docker container, intentionally misconfigured)
- Network: Isolated Docker bridge network

## Phase 1: Attack

1. Ran `nmap -sV -p- <target>` — identified open ports 22, 80, 6200.
2. Researched port 6200 — identified as vsftpd 2.3.4 backdoor (CVE-2011-2523).
3. Launched Metasploit module: `use exploit/unix/ftp/vsftpd_234_backdoor`
4. Set `RHOSTS` to target IP and ran exploit — obtained root shell.
5. Enumerated system: found world-writable `/etc/cron.d/` and weak SSH config.
6. Documented all findings with command output.

## Phase 2: Fortify

1. Patched vsftpd: `sudo apt remove vsftpd && sudo apt install vsftpd=3.0.5`
2. Hardened SSH: disabled root login and password auth in `/etc/ssh/sshd_config`.
3. Corrected cron directory permissions: `chmod 755 /etc/cron.d/`
4. Enabled UFW and set deny-all default policy with explicit allow rules.
5. Installed and initialized Tripwire for ongoing file integrity monitoring.
6. Verified all remediations by re-running the nmap scan and exploit attempt.

## Results

The exploit attempt post-hardening returned no session, confirming successful
remediation. All identified vulnerabilities were patched, permissions corrected,
and monitoring controls deployed.

## Conclusion

Operation Fortress demonstrated the full professional cycle of a security
engagement: identify, exploit, document, and remediate. The dual-role exercise
built both offensive technical skill and the defensive mindset required in
modern cybersecurity roles.
