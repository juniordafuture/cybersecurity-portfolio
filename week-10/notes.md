# Week 10 — Web Application Exploitation

**Date:** May 2026
**Program:** Knowledge House Cybersecurity Fellowship

## Summary

This week focused on web application attack techniques including SQL injection,
cross-site scripting (XSS), and directory traversal. Students used Burp Suite
and manual testing methods to identify and exploit common OWASP Top 10
vulnerabilities within a controlled Docker-based target environment
(Stuttard & Pinto, 2011).

## Tools & Commands Used

- `burpsuite` — intercept and modify HTTP requests
- `sqlmap -u <url> --dbs` — automated SQL injection enumeration
- `curl -X POST` — manual HTTP request crafting
- `nikto -h <target>` — web server vulnerability scanner
- `gobuster dir -u <url> -w <wordlist>` — directory and file brute-forcing
- `wfuzz` — web fuzzer for parameter discovery
- `docker ps` / `docker exec` — interact with vulnerable container targets

## Key Takeaways

Web application vulnerabilities remain among the most prevalent attack vectors
in real-world engagements. SQL injection can lead to full database compromise
while XSS enables session hijacking and credential theft. Defensive measures
include input validation, parameterized queries, Content Security Policy (CSP)
headers, and regular web application scanning as part of a secure SDLC
(Stuttard & Pinto, 2011). TLAB 10 (Operation Phantom Pursuit) reinforced
these skills through hands-on exploitation of a live Docker web target.

## References

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.

Stuttard, D., & Pinto, M. (2011). *The web application hacker's handbook: Finding and exploiting security flaws* (2nd ed.). Wiley.
