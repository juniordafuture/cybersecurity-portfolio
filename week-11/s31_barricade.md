# S31 — The Barricade
# Week 11 — Knowledge House Cybersecurity Fellowship

## Session Overview

Session 31 focused on host-based defensive hardening, specifically building
a "barricade" of security controls on a Linux system to prevent unauthorized
access and detect intrusion attempts. Students applied layered security
principles including firewall rules, service minimization, and audit logging
(NIST, 2020).

## Steps Performed

1. Disabled and removed unnecessary services: `systemctl disable <service>`
2. Configured UFW firewall rules to allow only SSH (port 22) and deny all else.
3. Enabled and configured `auditd` to log authentication events and file access.
4. Installed and configured `fail2ban` with a 3-attempt SSH ban policy.
5. Set password policy via `/etc/security/pwquality.conf` (minlen=12, complexity).
6. Verified hardening with a simulated brute-force attempt and confirmed ban.

## Artifact

```bash
# UFW Status after hardening
Status: active
To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
80/tcp                     DENY        Anywhere
443/tcp                    DENY        Anywhere

# fail2ban status
Status for the jail: sshd
|- Filter:  Currently failed: 0 | Total failed: 3
`- Actions: Currently banned: 1 | Total banned: 1
```

## References

National Institute of Standards and Technology. (2020). *Security and privacy
controls for information systems and organizations* (NIST SP 800-53 Rev. 5).
https://doi.org/10.6028/NIST.SP.800-53r5

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.
