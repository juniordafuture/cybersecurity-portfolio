# Week 04 Notes — Containers & Docker

**Operator:** dwayne  
**Program:** Knowledge House Cybersecurity Fellowship — Sprint 01  
**Sessions:** S10 · S11 · S12 · TLAB-04

---

## Key Concepts

Week 04 introduced container technology as both a deployment platform and a forensic analysis environment. Docker enables operators to build isolated, reproducible application environments using layered images and defined networking, which supports both rapid deployment and controlled security testing (Turnbull, 2018). Session 10 established the sandbox configuration workflow, requiring the operator to document the container environment setup and forensic documentation procedure in sandbox_report.txt.

Session 11 produced deploy_web.sh, an automation script containing the correct docker run command to launch a web container with port mapping and detached execution. Writing deployment logic to a version-controlled shell script enforces infrastructure-as-code practices and creates an auditable record of container configuration decisions (Kim et al., 2021).

Session 12 and TLAB-04 introduced Docker Compose for multi-container orchestration. The docker-compose.yml artifact defined an air-gapped stack in which a WordPress front end was assigned to both a public and a private network, while the database container was restricted to the private network only. The hyperstack_audit.json artifact documented all six required fields confirming that network isolation was tested and the isolation result was recorded honestly as PASSED or FAILED.

## Tools Used

- `docker run`, `docker ps`, `docker exec` — container lifecycle management
- `docker-compose up -d` — multi-container stack orchestration
- Docker `networks:` — network segmentation and isolation
- Shell scripting (`#!/bin/bash`) — deployment automation

## References

Kim, G., Humble, J., Debois, P., Willis, J., & Forsgren, N. (2021). *The DevOps handbook: How to create world-class agility, reliability, and security in technology organizations* (2nd ed.). IT Revolution Press.

Turnbull, J. (2018). *The Docker book: Containerization is the new virtualization* (v18.09). James Turnbull.
