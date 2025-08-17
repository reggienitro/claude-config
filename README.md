# Claude Configuration Sync

Personal Claude Code configuration files for cross-device synchronization.

## Files

- `CLAUDE.md` - Main Claude Code configuration with personal preferences, workflows, and project instructions

## Usage

### On a new device:
```bash
git clone https://github.com/reggienitro/claude-config.git
cd claude-config
cp CLAUDE.md /path/to/your/project/
```

### To update configuration:
```bash
# Make changes to CLAUDE.md
git add CLAUDE.md
git commit -m "Update Claude configuration"
git push
```

### To sync changes on other devices:
```bash
git pull
cp CLAUDE.md /path/to/your/project/
```

## Features

- Cross-device Claude Code configuration sync
- Personal development workflow preferences
- MCP server configurations
- Project-specific instructions
- Session continuation protocols