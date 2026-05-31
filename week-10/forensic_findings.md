# FORENSIC FINDINGS REPORT (THE MALWARE AUTOPSY)

### WHO:
* Threat Actor: Unknown APT operator who deployed
  rootkit_beacon.exe inside TitanCorp network using
  a social engineering lure disguised as Resume.exe

### WHAT:
* Deleted Executable: Resume.exe (inode 582,
  recovered from ~/DFIR_Evidence/compromised_drive.dd)
* Active Hidden Process: rootkit_beacon.exe PID: 4444
* Classification: Hidden rootkit beacon with no
  visible window running on port 4444

### WHEN:
* Infection Timestamp: 2026-05-26 13:31
* Evidence Source: DFIR_Evidence disk image
* Memory Artifact: memdump.raw (5MB active capture)

### HOW:
* Persistence Mechanism: Rootkit deployed as a hidden
  process with NO_WINDOW flag to avoid detection.
  Resume.exe was deleted after execution to destroy
  evidence of initial infection. Active C2 beacon
  maintained on port 4444 for remote command and
  control communications.
