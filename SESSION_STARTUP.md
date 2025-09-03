# Claude Session Startup Guide

## Quick Start for New Sessions

### Standard Opening Prompt:
```
"Load my configuration from /Users/aettefagh/claude-config/CLAUDE.md with modules in .claude/modules/. I have 12 MCP servers configured and 5 custom commands available. Follow my development principles especially the requirement to ask clarifying questions before building anything."
```

### Verification Commands:
```bash
# Test custom commands
/status-check

# Verify key MCP servers
gh auth status
```

### New Project Setup:
```bash
# Initialize new project structure
mkdir -p {src,tests,docs,configs}

# Copy config to project
cp /Users/aettefagh/claude-config/CLAUDE.md ./

# Initialize git if needed
git init
```

### MCP Unavailable (Online Mode Enforced)
If MCP servers or custom command runners are unavailable:
1. Pause work and request guidance. Do not proceed offline.
2. Perform minimal verification only (collect diagnostics): `git status`, `python3 -V`, `node -v`, `gh auth status`.
3. Capture runner/server logs or errors and surface them for resolution.
4. Resume only after an MCP runner and required servers are available and approved.

## Emergency Recovery
If configuration isn't working:
1. `git pull` in `/Users/aettefagh/claude-config/`
2. Copy CLAUDE.md to current project
3. Restart Claude session with config prompt above
