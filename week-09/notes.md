# Week 09 Notes — Web Application Attacks

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S25 · S26 · S27 · TLAB-09

---

## Key Concepts

Week 09 focused on web application attack techniques, covering three of the most prevalent vulnerability classes documented in the OWASP Top 10: SQL Injection, Cross-Site Scripting, and Broken Object Level Authorization (OWASP Foundation, 2021). These vulnerabilities collectively account for a significant proportion of real-world data breaches and application compromises, making their mechanics essential knowledge for both offensive and defensive practitioners.

Session 25 demonstrated SQL Injection through two attack vectors. A classic tautology payload (' OR '1'='1) bypassed authentication entirely by collapsing the WHERE clause logic to always-true. A subsequent UNION-based attack was used to enumerate column count, discover the target table name, and exfiltrate the CEO's exact salary value from the database. The sqli_report.txt artifact documented all four stages with the correct payloads and recovered data, along with a remediation recommendation for parameterized queries (Clarke, 2012).

Sessions 26 and 27 covered client-side and API attack surfaces. The xss_payloads.txt artifact documented a Reflected XSS payload, a Stored XSS attack that captured a session cookie value, and a crafted CSRF URL targeting a $5,000 unauthorized transfer. Session 27 used Burp Suite to perform a Broken Object Level Authorization attack — swapping user IDs in an API request to access the CISO's confidential profile — and Burp Intruder to brute-force a four-digit discount code. The OmniPortal_Assessment.md TLAB capstone chained all three attack classes into a single engagement narrative with remediation recommendations for each finding.

## Tools Used

- SQL tautology and UNION payloads — authentication bypass and data exfiltration
- Browser developer tools — cookie inspection and XSS payload delivery
- Burp Suite (Proxy, Intruder, Repeater) — API manipulation and fuzzing
- `session-submit` — artifact submission

## References

Clarke, J. (2012). *SQL injection attacks and defense* (2nd ed.). Syngress.

OWASP Foundation. (2021). *OWASP Top 10: 2021 — The ten most critical web application security risks*. https://owasp.org/Top10/
