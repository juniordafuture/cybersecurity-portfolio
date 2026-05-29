# Week 08 — Password Attacks & Credential Cracking

**Date:** April 2026
**Program:** Knowledge House Cybersecurity Fellowship

## Summary

This session covered credential-based attacks including brute force, dictionary
attacks, and hash cracking techniques. Students practiced using industry-standard
tools to crack password hashes and perform online authentication attacks against
services in a controlled lab environment (Oriyano, 2016).

## Tools & Commands Used

- `hydra -l <user> -P <wordlist> <target> <service>` — online brute force
- `hashcat -m <mode> <hashfile> <wordlist>` — GPU-accelerated hash cracking
- `john <hashfile>` — John the Ripper hash cracking
- `unshadow /etc/passwd /etc/shadow` — prepare Linux hashes for cracking
- `rockyou.txt` — common password wordlist
- `hash-identifier` — identify hash type

## Key Takeaways

Weak and reused passwords remain one of the most exploited vulnerabilities
in real-world breaches, making credential attacks a high-value technique in
penetration testing engagements. The RockYou wordlist demonstrates the
effectiveness of dictionary attacks, as a large percentage of real-world
passwords match commonly used patterns and phrases. Hash cracking speed is
heavily dependent on the hashing algorithm used — modern algorithms such as
bcrypt are intentionally slow to resist offline cracking, while legacy
algorithms like MD5 are cracked almost instantly.

## References

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.

Oriyano, S. P. (2016). *CEH v9: Certified ethical hacker version 9 study guide*. Sybex.
