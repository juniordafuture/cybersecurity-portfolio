# Week 01 Notes — Linux Fundamentals & Threat Pipeline

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S01 · S02 · S03 · TLAB-01

---

## Key Concepts

This week introduced the foundational Linux command-line skills required for cybersecurity operations. Practitioners must develop fluency with the Linux file system hierarchy, file permission model, and shell pipeline syntax before advancing to offensive or defensive tooling (Shotts, 2019). Session 01 focused on filesystem reconnaissance — navigating directories, locating hidden files, and capturing environment variables that may contain sensitive credential material. The discovery.txt artifact documented the operator's token value, mission secret, and all traversed paths, demonstrating a complete reconnaissance workflow.

Session 02 introduced system hardening through permission control. The chmod and chown commands were applied to /etc/shadow to restrict read access to the root and shadow groups, reducing the attack surface exposed to unprivileged processes (National Institute of Standards and Technology [NIST], 2022). The .ssh directory and authorized_keys file were also locked to owner-only permissions, enforcing the principle of least privilege on the host's authentication infrastructure.

Session 03 and TLAB-01 synthesized the week's skills into a threat pipeline. Log data was processed through a shell pipeline using grep, sort, and uniq to extract and deduplicate attacker IP addresses into threat_ips.txt. The final_threat_report.txt artifact confirmed that all three pipeline stages — IP extraction, deduplication, and permission hardening — were completed successfully.

## Tools Used

- `ls`, `find`, `cat`, `env` — filesystem reconnaissance
- `chmod`, `chown` — permission hardening
- `grep`, `sort`, `uniq` — log pipeline and threat extraction
- `git add`, `git commit`, `git push` — artifact versioning

## References

National Institute of Standards and Technology. (2022). *Guide to general server security* (SP 800-123). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-123

Shotts, W. (2019). *The Linux command line: A complete introduction* (2nd ed.). No Starch Press.
