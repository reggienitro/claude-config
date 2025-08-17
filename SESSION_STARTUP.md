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

## Emergency Recovery
If configuration isn't working:
1. `git pull` in `/Users/aettefagh/claude-config/`
2. Copy CLAUDE.md to current project
3. Restart Claude session with config prompt above