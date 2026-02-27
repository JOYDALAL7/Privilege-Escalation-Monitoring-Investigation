# Privilege-Escalation-Monitoring-Investigation

## Environment

- Operating System: Kali Linux
- Platform: UTM (macOS Host)
- Host Type: Linux Endpoint
- User Context: kali
- Investigation Type: Host-based Threat Detection
- Tools Used: ps, pstree, crontab, journalctl

---

## Incident Summary

During routine host monitoring, a long-running background process was identified

that did not align with normal user activity. Further investigation revealed

the presence of a scheduled cron job designed to repeatedly execute the process,

indicating a persistence mechanism.

---

## Detection

Suspicious activity was detected through manual process inspection. A background

process running with an unusually long execution time raised concerns of potential

persistence or misuse of system resources.

---

## Process Analysis

### Process Identification

The following command was used to identify suspicious processes:

ps aux | grep sleep

The output confirmed the presence of a long-running `sleep 9999` process executing

under the current user context.

---

### Process Lineage Analysis

To analyze the process hierarchy and determine how the process was spawned, the

following command was used:

pstree -p | grep sleep

The output showed a standalone `sleep` process, suggesting it was not launched

interactively and may be associated with scheduled execution.

---

## Persistence Investigation

### Cron Job Inspection

To determine whether the process was configured for persistence, the user crontab

was inspected using:

crontab -l

The following cron entry was discovered:

_/5 _ \* \* \* /bin/sleep 9999

This configuration causes the `sleep 9999` command to execute every five minutes,

ensuring persistence of the process.

---

## Findings

- A long-running background process was active on the system
- The process was configured to restart automatically using cron
- The persistence mechanism did not require elevated privileges
- No successful privilege escalation or lateral movement was observed
- The behavior is consistent with basic persistence techniques

---

## Impact Assessment

No direct system compromise was observed. However, unauthorized persistence poses

potential risks, including resource abuse, execution of malicious payloads, and

reduced visibility into host activity.

---

## Mitigation & Remediation

- Remove unauthorized cron jobs
- Terminate suspicious background processes
- Restrict cron usage to trusted users
- Monitor scheduled tasks regularly
- Implement host-based intrusion detection
- Configure alerts for persistence mechanisms

---

## Lessons Learned

This investigation demonstrates the importance of host-level monitoring,

scheduled task inspection, and understanding common persistence techniques used

by attackers.

---

## Evidence

### Suspicious Process Detection

![Suspicious Process](screenshots/suspicious-process-ps.png)

### Process Tree Analysis

![Process Tree](screenshots/process-tree.png)

### Cron-Based Persistence

## ![Cron Persistence](screenshots/cron-persistence.png)

## Conclusion

The investigation successfully identified a cron-based persistence mechanism

responsible for maintaining a long-running background process. The issue was

1. contained, documented, and remediation steps were identified to prevent recurrence.
