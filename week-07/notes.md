# Week 07 — Web Application Security

**Date:** March 2026
**Program:** Knowledge House Cybersecurity Fellowship

## Summary

This session introduced web application penetration testing concepts and
common vulnerability classes defined by the OWASP Top 10. Students practiced
identifying and exploiting vulnerabilities including SQL injection and
cross-site scripting in a controlled lab environment (OWASP, 2021).

## Tools & Commands Used

- `curl` — command-line HTTP requests
- `nikto -h <target>` — web server vulnerability scanner
- `gobuster dir -u <url> -w <wordlist>` — directory enumeration
- `sqlmap -u <url>` — automated SQL injection testing
- Browser Developer Tools — inspect requests and responses
- Burp Suite (Community Edition) — HTTP proxy and interceptor

## Key Takeaways

Web applications represent one of the largest attack surfaces in modern
organizations, making web application security testing a core competency for
penetration testers. SQL injection remains one of the most critical and
prevalent vulnerabilities, capable of allowing an attacker to dump entire
databases, bypass authentication, or execute commands on the underlying server.
Directory enumeration with tools like Gobuster reveals hidden endpoints and
administrative panels that are often inadequately protected.

## References

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.

OWASP. (2021). *OWASP top ten*. Open Web Application Security Project. https://owasp.org/www-project-top-ten/
