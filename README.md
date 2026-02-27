# 🔐 Privilege Escalation Monitoring Investigation

## Overview

A host-based threat detection investigation focused on identifying and analyzing a cron-based persistence mechanism on a Linux system. A long-running background process (`sleep 9999`) was discovered, configured to restart automatically via a cron job every five minutes.

## Key Findings

- Unauthorized cron job executing `sleep 9999` every 5 minutes
- Persistence mechanism operating under standard user privileges
- No privilege escalation or lateral movement observed
- System authentication controls remained intact

## Environment

| Detail             | Value                                   |
| ------------------ | --------------------------------------- |
| OS                 | Kali Linux                              |
| Platform           | UTM (macOS Host)                        |
| Investigation Type | Host-based Threat Detection             |
| Tools Used         | `ps`, `pstree`, `crontab`, `journalctl` |

## Repository Structure

```
├── investigation-report.md     # Full investigation report
├── Scripts/
│   └── sudo_log_parser.py      # Parses auth logs for sudo authentication failures
├── Screenshots/
│   ├── suspicious-process-ps.png
│   ├── process-tree.png
│   └── cron-persistence.png
├── logs/
│   └── sample_auth.log         # Sample authentication log for analysis
└── README.md
```

## Script Usage

```bash
cd Scripts
python3 sudo_log_parser.py
```

The script parses `logs/sample_auth.log` for sudo authentication failures and flags users with 3+ failed attempts as potential privilege escalation indicators.

## Skills Demonstrated

- Linux process inspection and analysis (`ps`, `pstree`)
- Scheduled task investigation (`crontab`)
- Persistence mechanism identification
- Log analysis and threat detection
- Incident documentation and remediation planning
