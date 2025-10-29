# container-vuln-scan-automation

This project demonstrates **automated container image vulnerability scanning** using [Trivy](https://aquasecurity.github.io/trivy/) and Python.

## Features
- Scans container images and exports vulnerabilities to CSV
- Supports filtering by image name and severity
- Simple, reproducible workflow for DevSecOps or security testing labs

## Quick Start
1. Install [Trivy](https://aquasecurity.github.io/trivy/)
2. Clone this repo
3. Run the scanner:
   ```bash
   python scripts/trivy_scan.py nginx:latest


