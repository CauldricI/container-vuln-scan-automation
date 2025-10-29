#!/usr/bin/env python3
import subprocess, json, pandas as pd, sys

def run_trivy(image="nginx:latest"):
    print(f"Scanning {image}...")
    result = subprocess.run(["trivy", "image", "--quiet", "--format", "json", image],
                            capture_output=True, text=True)
    data = json.loads(result.stdout)
    vulns = []
    for r in data.get("Results", []):
        for v in r.get("Vulnerabilities", []):
            vulns.append({
                "Target": r.get("Target"),
                "Severity": v.get("Severity"),
                "CVE": v.get("VulnerabilityID"),
                "PkgName": v.get("PkgName"),
                "InstalledVersion": v.get("InstalledVersion"),
                "FixedVersion": v.get("FixedVersion"),
            })
    df = pd.DataFrame(vulns)
    df.to_csv("scan_results.csv", index=False)
    print(f"Saved {len(df)} findings → scan_results.csv")

if __name__ == "__main__":
    image = sys.argv[1] if len(sys.argv) > 1 else "nginx:latest"
    run_trivy(image)
