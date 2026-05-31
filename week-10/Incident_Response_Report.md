# INCIDENT RESPONSE REPORT: PHANTOM PURSUIT
**Operator:** dwayne

## PHASE 1: SIEM CORRELATION
* **Initial Alert Source IP:** 203.0.113.99

## PHASE 2: LIVE TRIAGE & CHAIN OF CUSTODY
* **Suspicious Process ID (PID):** 10
* **Evidence SHA256 Hash:** ee0ed88e621f9f9b5bc44672241c060e9dd0e2ce84d25cb51506962a74720887

## PHASE 3: DISK FORENSICS
* **Deleted File Inode Number:** 582
* **Extracted Payload Data:** beacon.exe recovered from inode 582
  on compromised_drive.dd. File identified as a Netcat reverse
  shell beacon configured to connect to C2 server at
  203.0.113.99 on port 4444. Process was actively listening
  as PID 10 on the quarantined host. File was deleted to
  conceal attacker presence but recovered via icat forensic
  extraction from the raw disk image.
