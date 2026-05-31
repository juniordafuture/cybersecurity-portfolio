# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** Dwayne  **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
* **Host 1 (172.88.0.10):** nginx 1.14.2 — HTTP Port 80 — Web Server
* **Host 2 (172.88.0.15):** No open TCP ports detected — Cache Database
* **Host 3 (172.88.0.20):** Apache httpd 2.4.66 — HTTP Port 80 — Web Server

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
* **Web Server 1 Finding (172.88.0.10):** Tool: Nikto — Missing X-Frame-Options header, leaving users vulnerable to clickjacking attacks where malicious sites can embed this server's pages in hidden iframes.
* **Web Server 2 Finding (172.88.0.20):** Tool: Nikto — HTTP TRACE method enabled (OSVDB-877), making the host vulnerable to Cross-Site Tracing (XST) attacks that allow theft of session cookies and authentication headers.

## PHASE 3: RISK TRIAGE
* **Top Priority Remediation:** nginx 1.14.2 Outdated Web Server (172.88.0.10)
* **Justification:** This is the highest risk because the likelihood is high — nginx 1.14.2 is from 2018 with multiple known CVEs — and the impact is critical, as a successful exploit against this internet-facing web server could result in full server compromise and unauthorized access to CloudNano acquisition data.
