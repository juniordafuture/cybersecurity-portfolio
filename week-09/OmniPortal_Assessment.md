==================================================
TLAB9: OPERATION OMNI-PORTAL ASSESSMENT REPORT
==================================================

PHASE 1 — BREAKING THE GATE (SQLi)
* Target URL: http://127.0.0.1:8090/login
* SQLi Payload Used: ' OR 1=1 --
* Result: Successfully bypassed login authentication
  and gained access to the portal including the
  "View My Orders" link and auth_token cookie.

PHASE 2 — POISONING THE WELL (Stored XSS)
* Target URL: http://127.0.0.1:8090/support
* XSS Payload Used: <script>alert(document.cookie)</script>
* Auth Token Captured: auth_token=SUPPORT_TIER_1_SECRET_TOKEN
* Result: Payload permanently stored on Support Board.
  Fires every time any user visits the page, stealing
  their session cookie.

PHASE 3 — DEEP DATA MINING (API BOLA)
* Targeted Endpoint: http://127.0.0.1:8090/api/v2/orders/501
* Confidential Order Found: Order ID 501
* Order Details: Confidential Server Lease
* Amount: $15,000.00
* Result: Successfully exfiltrated private financial
  data belonging to another account via ID enumeration.

PHASE 4 — REMEDIATION
* SQLi Fix: Use parameterized queries and prepared
  statements. Never concatenate user input directly
  into SQL queries. This separates code from data,
  making injection impossible regardless of input.

* XSS Fix: Sanitize and escape all user input before
  rendering it on the page. Implement Content Security
  Policy (CSP) headers to prevent unauthorized script
  execution. Never render raw user input as HTML.

* API BOLA Fix: Implement proper authorization checks
  on every API endpoint. Verify that the requesting
  user's session token matches the owner of the
  requested order ID before returning any data.
  Never rely on obscurity of IDs alone for security.
