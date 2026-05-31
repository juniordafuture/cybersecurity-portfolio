# OPERATION FORTRESS REPORT
# Defense in Depth Architecture

## LAYER 1 — THE FIREWALL (Egress Filtering)
* Threat: Attacker C2 subnet 198.51.100.0/24
* iptables Rule Deployed:
  iptables -A OUTPUT -d 198.51.100.0/24 -j DROP
* Purpose: Blocks all outbound communication to the
  attacker's Command and Control infrastructure.

## LAYER 2 — THE TRIPWIRE (IDS Signature)
* Threat: Web shell exploit string cmd=whoami
* Suricata Rule Deployed:
  alert tcp any any -> any 80 (msg:"Web Shell cmd=whoami Detected"; content:"cmd=whoami"; sid:1000003; rev:1;)
* Purpose: Detects web shell exploitation attempts
  crossing the network perimeter on port 80.

## LAYER 3 — THE ENDPOINT (Sysmon EDR Policy)
* Threat: Post-exploitation payload download via curl
* Sysmon XML Rule Deployed:
  <CommandLine condition="contains">curl http://198.51.100.5</CommandLine>
* Purpose: Catches post-exploitation payload downloads
  executing natively on the Linux host.
