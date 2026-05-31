# S32 — The Tripwire
# Week 11 — Knowledge House Cybersecurity Fellowship

## Session Overview

Session 32 introduced file integrity monitoring (FIM) as a detection control
to identify unauthorized changes to critical system files. Students configured
Tripwire to establish a baseline and detect simulated tampering, modeling
real-world intrusion detection workflows (Kim & Solomon, 2018).

## Steps Performed

1. Installed Tripwire: `sudo apt install tripwire`
2. Initialized the Tripwire database: `sudo tripwire --init`
3. Ran a baseline integrity check: `sudo tripwire --check`
4. Simulated file tampering by modifying `/etc/passwd`.
5. Re-ran integrity check and confirmed Tripwire flagged the modification.
6. Reviewed violation report and documented the flagged change.
7. Updated the database after confirming the change: `sudo tripwire --update`

## Artifact

```
Tripwire Integrity Check Report

Object Summary:
----------------
Modified:  /etc/passwd
  Property: SHA-256 hash changed
  Old: a3f9c2e1d7b84f0c...
  New: 7d21bc4e90f13a8d...

Total violations found: 1
```

## References

Kim, D., & Solomon, M. G. (2018). *Fundamentals of information systems security*
(3rd ed.). Jones & Bartlett Learning.

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.
