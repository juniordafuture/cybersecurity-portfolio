# Week 10 Notes — Digital Forensics & Incident Response

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S28 · S29 · S30 · TLAB-10

---

## Key Concepts

Week 10 covered the full Digital Forensics and Incident Response (DFIR) lifecycle, from live system triage through disk image analysis and multi-source log correlation. The NIST incident response framework defines four phases — Preparation, Detection and Analysis, Containment/Eradication/Recovery, and Post-Incident Activity — and the week's sessions exercised each phase in sequence (Cichonski et al., 2012). Accurate evidence collection and chain-of-custody documentation are legal requirements in many incident response contexts, making hash verification and timestamped artifact recording non-negotiable practices.

Session 28 introduced live triage methodology. The collection_log.txt artifact recorded the malicious process name and PID identified from the running container, along with the MD5 hash of memory_dump.raw and the SHA256 hash of system_artifacts.zip. Hash verification ensures evidence integrity — any modification to the file after collection would produce a different hash value, invalidating the evidence chain (Casey, 2011). Session 29 performed disk forensics using the Sleuth Kit toolset. The fls command enumerated the inode table of a mounted disk image to locate a deleted executable, and icat extracted the payload contents using the recovered inode number, populating all four fields of forensic_findings.md.

Session 30 and TLAB-10 focused on log correlation using Kibana and a multi-source SIEM environment. The attack_timeline.csv artifact reconstructed a three-phase attack chain — Initial Access from an external IP, Lateral Movement identified via a Windows Security event, and Exfiltration flagged by an anomalous data volume in the firewall log. The Incident_Response_Report.md TLAB capstone combined SIEM analysis, memory forensics, and disk forensics into a unified investigation report.

## Tools Used

- `ps aux`, `netstat`, `lsof` — live process and connection triage
- `md5sum`, `sha256sum` — evidence hash verification
- Sleuth Kit (`fls`, `icat`) — disk image forensics and deleted file recovery
- Kibana / Elasticsearch — SIEM log search and attack timeline correlation

## References

Casey, E. (2011). *Digital evidence and computer crime: Forensic science, computers, and the internet* (3rd ed.). Academic Press.

Cichonski, P., Millar, T., Grance, T., & Scarfone, K. (2012). *Computer security incident handling guide* (SP 800-61 Rev. 2). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r2
