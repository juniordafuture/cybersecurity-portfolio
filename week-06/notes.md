# Week 06 — Privilege Escalation

**Date:** March 2026
**Program:** Knowledge House Cybersecurity Fellowship

## Summary

This session focused on privilege escalation techniques used after gaining
initial access to a target system. Students explored both Linux and Windows
escalation vectors, including misconfigured permissions, SUID binaries, and
weak service configurations (HTB Academy, 2024).

## Tools & Commands Used

- `whoami`, `id` — identify current user and group
- `sudo -l` — list sudo permissions
- `find / -perm -4000 2>/dev/null` — find SUID binaries
- `uname -a` — kernel version information
- `ps aux` — running processes
- `linpeas.sh` — automated Linux privilege escalation script
- `GTFOBins` — reference for exploiting binaries

## Key Takeaways

Privilege escalation is a critical phase in penetration testing because
initial access is rarely obtained with root or administrator-level permissions.
Misconfigured SUID binaries, writable cron jobs, and weak sudo rules are
among the most commonly exploited vectors for local privilege escalation on
Linux systems. Automated tools such as LinPEAS significantly reduce the time
required to enumerate escalation opportunities on a compromised host.

## References

HTB Academy. (2024). *Linux privilege escalation*. Hack The Box. https://academy.hackthebox.com

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.
