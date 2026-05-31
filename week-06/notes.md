# Week 06 Notes — Capstone Readiness & The Hardened Outpost

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S16 · S17 · S18

---

## Key Concepts

Week 06 served as the culminating sprint for the first phase of the program, synthesizing all prior skills into a capstone architecture exercise. Session 16 was a structured readiness assessment in which the operator self-evaluated proficiency across five core tool domains and identified a weakest area with a documented remediation plan. This metacognitive exercise reflects the professional practice of continuous skills gap analysis recommended for security practitioners at all levels (CompTIA, 2023).

Session 17 was the practical examination, requiring the operator to locate two hidden .log files, move them to ~/Exam_Submission, apply chmod 444 read-only permissions, and document all commands used in practical_exam_report.txt. The exam tested command fluency under time pressure, mirroring the conditions of a real incident response engagement where accurate command documentation is critical for chain-of-custody integrity (Casey, 2011).

Session 18 produced the capstone artifact: HardenedOutpost_SAD.pdf, a System Architecture Document covering four integrated phases. Phase 1 defined the Active Directory structure with OUs and the PowerShell provisioning script. Phase 2 documented the Linux domain join procedure and sudoers configuration. Phase 3 described the Python auditor script logic. Phase 4 detailed the Docker Compose air-gapped network design. Together these phases demonstrate the ability to design and document a secure, multi-layer enterprise environment from the ground up.

## Tools Used

- Self-assessment checklist (`readiness_check.log`) — skills gap analysis
- `find`, `mv`, `chmod 444` — file location, movement, and permission locking
- Pandoc / LaTeX — SAD document compilation to PDF
- Integrated review of: AD, Linux hardening, Python automation, Docker networking

## References

Casey, E. (2011). *Digital evidence and computer crime: Forensic science, computers, and the internet* (3rd ed.). Academic Press.

CompTIA. (2023). *CompTIA Security+ study guide: Exam SY0-701* (9th ed.). Sybex.
