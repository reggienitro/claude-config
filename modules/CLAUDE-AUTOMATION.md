# CLAUDE-AUTOMATION: Shell Scripts & Workflow Module
> Loaded when shell scripts or automation detected

## 🤖 Automation Architecture Context
```yaml
scripting_preference: "bash with error handling"
scheduling: "cron for recurring tasks"
orchestration: "shell scripts with logging"

conventions:
  scripts_location: "./scripts or ./automation"
  logs_location: "~/.local/logs or ./logs"
  config_location: "~/.config or ./config"
  
error_handling:
  style: "set -euo pipefail"
  logging: "structured with timestamps"
  notifications: "optional email/slack"
```

## 📋 Automation Prerequisites Checklist
```bash
# Before automation work:
echo "=== AUTOMATION PREREQUISITES ==="

# □ Shell environment?
echo "✓ Shell: $SHELL ($(bash --version | head -1))"

# □ Required tools installed?
command -v jq >/dev/null && echo "✓ jq installed" || echo "✗ jq missing"
command -v curl >/dev/null && echo "✓ curl installed" || echo "✗ curl missing"
command -v gh >/dev/null && echo "✓ GitHub CLI installed" || echo "⚠️ gh missing"

# □ Permissions correct?
[[ -w ~/.local/logs ]] && echo "✓ Log directory writable" || echo "⚠️ Cannot write logs"

# □ Cron accessible?
crontab -l >/dev/null 2>&1 && echo "✓ Cron access" || echo "⚠️ No cron access"
```

## 🚫 Automation Non-Goals
**NEVER without permission:**
- ❌ Modify system files (/etc, /usr)
- ❌ Create system services
- ❌ Add to user startup/login
- ❌ Schedule destructive operations
- ❌ Access sensitive credentials
- ❌ Create infinite loops without safeguards

## 🔄 Automation Patterns

### Shell Script Pattern
```bash
#!/bin/bash
# DISCOVERED PATTERN: Defensive scripting
set -euo pipefail  # Exit on error, undefined vars, pipe failures
IFS=$'\n\t'        # Safe field splitting

# Logging setup
LOG_FILE="${LOG_FILE:-~/.local/logs/$(basename $0).log}"
log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

# Error handling
trap 'log "ERROR: Script failed at line $LINENO"' ERR

# Main logic with validation
main() {
    log "Starting $(basename $0)"
    # Validate prerequisites
    # Execute operations
    # Verify success
    log "Completed successfully"
}

main "$@"
```

### Cron Job Pattern
```bash
# DISCOVERED PATTERN: Robust cron entries
# Include PATH, error handling, logging
PATH=/usr/local/bin:/usr/bin:/bin
SHELL=/bin/bash
MAILTO=""

# Daily at 9 AM with logging
0 9 * * * /path/to/script.sh >> ~/.local/logs/cron.log 2>&1
```

## 🎯 Automation Success Criteria
- ✅ Idempotent (safe to run multiple times)
- ✅ Proper error handling and recovery
- ✅ Comprehensive logging
- ✅ Validation before destructive ops
- ✅ Rollback capability for changes
- ✅ Performance monitoring included

## 🔧 Automation Handoff Template
```markdown
## AUTOMATION SESSION HANDOFF
### Active Scripts
- Running: [script names and PIDs]
- Scheduled: [cron jobs list]
- Last run: [timestamps and results]

### Configuration State
- Environment vars: [required vars]
- Config files: [locations]
- Dependencies: [external tools]

### Recovery Commands
```bash
# Check running scripts
ps aux | grep -E "script1|script2"

# Verify cron
crontab -l

# Check recent logs
tail -50 ~/.local/logs/*.log
```
```

---
*Module: AUTOMATION | Auto-loads when *.sh files detected*