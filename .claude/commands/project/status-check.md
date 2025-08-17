# /status-check

Comprehensive project status verification across all systems.

## What it checks:
1. **Git status** - uncommitted changes, branch info
2. **MCP servers** - verify all servers are active and functional
3. **Database connections** - test Supabase, local DBs
4. **Environment variables** - confirm API keys are loaded
5. **Task status** - current tasks and progress
6. **System health** - running processes, disk space

## Usage:
```bash
/status-check
/status-check --verbose  # detailed output
/status-check --fix      # attempt to fix issues found
```

## Checks Performed:

### Git & Version Control
- Current branch and tracking info
- Uncommitted changes
- Unpushed commits
- Repository cleanliness

### MCP Server Health
```bash
# Test each configured server
gh auth status                    # GitHub
python3 -c "import supabase"      # Supabase
# ... other server checks
```

### Database Connectivity
- Supabase connection test
- Local database accessibility
- Schema verification

### Environment Setup
- API keys loaded from ~/.config/api-keys/.env
- Required dependencies installed
- Python virtual environment activated (if applicable)

### Task Management
- Current task-master status
- Pending todos and priorities
- Session continuity files present

## Example Output:
```
🟢 Git: Clean working directory, main branch
🟢 MCP Servers: 12/12 active
🟢 Databases: Supabase connected, local DBs accessible
🟡 Environment: 1 missing API key (EXA_API_KEY)
🟢 Tasks: 3 pending, 1 in progress
🟢 System: All services running

Issues found: 1
Run '/status-check --fix' to attempt automatic resolution
```