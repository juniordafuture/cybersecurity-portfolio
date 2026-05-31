# TLAB 10 — Operation Phantom Pursuit
# Week 10 — Knowledge House Cybersecurity Fellowship

## Objective

Conduct a web application penetration test against a Docker-hosted vulnerable
web application, identify exploitable vulnerabilities, and document findings
in a structured report.

## Environment

- Attacker: Kali Linux (Docker container)
- Target: Custom vulnerable web application (Docker container)
- Network: Isolated Docker bridge network

## Steps Performed

1. Ran `nikto -h http://target` to perform initial web server reconnaissance.
2. Used `gobuster dir` with the common.txt wordlist to discover hidden endpoints.
3. Identified login page vulnerable to SQL injection via manual testing.
4. Confirmed SQLi using payload: `' OR '1'='1' -- -`
5. Used `sqlmap` to enumerate databases and extract the user table.
6. Identified reflected XSS in search parameter via `<script>alert(1)</script>`.
7. Documented all findings with request and response captures.

## Findings

| Vulnerability | Severity | Location |
|---|---|---|
| SQL Injection | Critical | /login.php |
| Reflected XSS | High | /search.php |
| Directory Listing | Medium | /uploads/ |
| Outdated Server Header | Low | HTTP Response |

## Conclusion

Operation Phantom Pursuit successfully demonstrated multiple critical web
application vulnerabilities. The exercise reinforced the importance of input
sanitization, prepared statements, and proper server hardening as countermeasures
against common web-based attacks.
