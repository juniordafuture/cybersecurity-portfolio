# Remediation Plan — CloudNano Corp
**Operator:** Dwayne | Session 21 | W7 | Date: 2026-04-30
**Methodology:** Risk = Likelihood × Impact (not CVSS score alone)

---

## Top 5 Prioritized Vulnerabilities

**1. Unauthenticated AWS S3 Bucket Containing Customer PII [CVSS 9.8]**
Prioritized first because this is an internet-facing cloud asset with no authentication barrier, meaning any attacker can access and exfiltrate real customer PII right now — creating immediate regulatory liability (GDPR/CCPA) and reputational damage for CloudNano.

**2. Remote Code Execution in Apache Struts — Internet-Facing Web Server [CVSS 9.8]**
Prioritized because RCE on a public-facing production server gives an attacker full control of that host with no prior access required, making exploitation both highly likely and catastrophically impactful to business continuity.

**3. SQL Injection in Login Page — Customer Database Portal [CVSS 8.1]**
Prioritized because the login page is directly accessible to the public internet and a successful injection grants an attacker unrestricted read/write access to the customer database, combining high likelihood with maximum data-loss impact.

**4. Cross-Site Scripting (XSS) on Support Forum [CVSS 8.8]**
Prioritized because the support forum is actively used by real customers, and a stored XSS payload can silently steal session tokens or credentials at scale — making the likelihood of exploitation high and the downstream account-takeover impact severe.

**5. Outdated PHP 5.4 on Public Marketing Blog [CVSS 7.5]**
Prioritized because PHP 5.4 reached end-of-life in 2015 and has dozens of known unpatched CVEs; as a public-facing server it is reachable by automated scanners daily, making exploitation likely even without a targeted attacker.

---

## Excluded (Notable)

- **Default Credentials on Internal Router [CVSS 10.0]** — Excluded from top 5 because the device is on an air-gapped network with no physical access available to external attackers, reducing likelihood to near zero despite the maximum severity score.
