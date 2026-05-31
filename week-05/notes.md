# Week 05 Notes — Active Directory & Identity Management

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S13 · S14 · TLAB-05

---

## Key Concepts

Week 05 focused on Windows Active Directory (AD) as the identity and access management backbone of enterprise environments. Active Directory's hierarchical structure of domains, organizational units (OUs), and Group Policy Objects (GPOs) provides centralized control over authentication, authorization, and configuration enforcement across all domain-joined systems (Microsoft, 2023). Understanding AD is essential for both offensive and defensive practitioners, as it represents the primary target for lateral movement and privilege escalation in real-world intrusions.

Session 13 produced onboard_engineers.ps1, a PowerShell script that automated the creation of new user accounts in the Engineering OU using a for loop and the New-ADUser cmdlet. The script used the correct -Path parameter pointing to OU=Engineering,DC=titan,DC=local and set -ChangePasswordAtLogon $true, enforcing a credential reset on first login. Automating user provisioning reduces human error and creates a consistent, auditable onboarding process (Campbell, 2022).

Session 14 and TLAB-05 examined Group Policy as a configuration enforcement mechanism. The gpo_audit.txt artifact documented the three required concepts: the gpupdate /force command used to immediately apply policy changes, the LSDOU processing order (Local, Site, Domain, OU) that determines which GPO wins in a conflict, and the rationale for scoping a Lockout Policy to the Engineering OU rather than the domain root.

## Tools Used

- `New-ADUser` — PowerShell AD user provisioning
- `gpupdate /force` — immediate Group Policy application
- Group Policy Management Console (GPMC) — policy creation and linking
- Active Directory Users and Computers (ADUC) — OU and user management

## References

Campbell, D. (2022). *Mastering Active Directory: Design, deploy, and protect Active Directory Domain Services for Windows Server 2022* (3rd ed.). Packt Publishing.

Microsoft. (2023). *Active Directory Domain Services overview*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview
