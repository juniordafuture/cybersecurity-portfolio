#!/usr/bin/env python3
import subprocess
import json

print("[*] Initiating Automated Threat Hunt...")

result = subprocess.run(["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"], capture_output=True, text=True)

raw_output = result.stdout
lines = raw_output.split('\n')
attacker_ips = []

for line in lines:
    if line:
        ip = line.split(" ")[10]
        attacker_ips.append(ip)

alert_data = {"alert_type": "Brute Force", "attacker_ips": attacker_ips}

with open("/home/dwayne/threat_report.json", "w") as file:
    json.dump(alert_data, file, indent=4)

print(f"[*] Hunt Complete. Extracted {len(attacker_ips)} attacker IPs to threat_report.json")
