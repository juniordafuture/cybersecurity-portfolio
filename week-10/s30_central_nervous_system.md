# S30 — The Central Nervous System
# Week 10 — Knowledge House Cybersecurity Fellowship

## Session Overview

This session examined the infrastructure underlying enterprise security
operations, including Security Information and Event Management (SIEM) systems,
log aggregation pipelines, and centralized monitoring architectures. Students
analyzed how a SOC collects, correlates, and responds to security telemetry
from across an organization (Chuvakin et al., 2013).

## Key Concepts Covered

- SIEM architecture: data ingestion, normalization, correlation rules, alerting
- Log sources: firewalls, IDS/IPS, endpoints, authentication systems
- Use cases: detecting brute force, privilege escalation, lateral movement
- Splunk basics: search queries, dashboards, alert creation
- Log forwarding with syslog and Beats agents

## Lab Activity

Students configured a mock log pipeline and wrote Splunk search queries to
detect simulated attack patterns including failed login bursts and suspicious
outbound connections. Queries were documented and validated against synthetic
log data.

## References

Chuvakin, A., Schmidt, K., & Phillips, C. (2013). *Logging and log management:
The authoritative guide to understanding the concepts surrounding logging and
log management*. Syngress.

Knowledge House. (2026). *Cybersecurity fellowship program curriculum*. Knowledge House.
