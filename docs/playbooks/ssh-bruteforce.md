# SSH Brute Force Response Playbook

## Detection
- Suricata alert: "SSH Brute Force Attempt"
- Multiple failed logins in auth.log

## Investigation
```bash
bash scripts/analysis/investigate-ip.sh <ATTACKER_IP>
grep "Failed password" /var/log/auth.log | grep <ATTACKER_IP>
```

## Response
```bash
# Block the attacker
bash scripts/operations/block-ip.sh <ATTACKER_IP> --reason "SSH brute force"

# Check for successful logins
grep "Accepted" /var/log/auth.log | grep <ATTACKER_IP>
```

## Recovery
- Review compromised accounts
- Rotate credentials
- Update AIDE baseline
