# Claude Config v2.0 - Integration Guide

## Overview
This guide helps you integrate the enhanced v2.0 configuration system into your workflow.

## Core Concepts

### 1. Progressive Disclosure
Instead of loading a massive config file, the system reveals complexity as needed:
- **CLAUDE-CORE.md**: Minimal base configuration
- **Modules**: Load only when relevant (e.g., CLAUDE-WEB.md for web projects)
- **Project Overrides**: Specific to each project

### 2. Configuration as Documentation
The configuration structure itself teaches the AI about your environment:
```yaml
workspace_structure:
  ~/AI projects/: "Primary development"
  ~/projects/: "Active work"
```

### 3. Pattern Discovery Protocol
AI learns from your codebase instead of following static rules:
```markdown
DISCOVERED PATTERN: Error Handling
- Examples: api/users.js:45, api/posts.js:67
- Pattern: try-catch with standard format
- Should follow: Yes
```

## Integration Strategies

### Strategy 1: Full Replacement (Clean Start)
Best for: New setups or major workflow changes

```bash
cd ~/claude-config
./scripts/migrate.sh
# Select option 1: Full Migration
```

### Strategy 2: Gradual Enhancement
Best for: Existing complex configurations

```bash
# Add new sections to existing CLAUDE.md
cat core/CLAUDE-CORE.md | grep -A 20 "Prerequisites Validation" >> ~/CLAUDE.md
cat core/CLAUDE-CORE.md | grep -A 20 "Pattern Discovery" >> ~/CLAUDE.md
```

### Strategy 3: Project-Specific Testing
Best for: Testing before full adoption

```bash
# In a single project
cd ~/projects/test-project
cp ~/claude-config/core/CLAUDE-CORE.md ./CLAUDE.md
ln -s ~/claude-config/modules/CLAUDE-WEB.md .
# Test with this project only
```

## Module Usage

### Auto-Loading Modules
Modules load automatically based on file detection:

| File Detected | Module Loaded | Purpose |
|--------------|---------------|---------|
| package.json | CLAUDE-WEB.md | Web development patterns |
| requirements.txt | CLAUDE-ML.md | Machine learning workflows |
| .env with DB_* | CLAUDE-DATABASE.md | Database operations |
| *.sh files | CLAUDE-AUTOMATION.md | Shell scripting |

### Manual Module Loading
```markdown
<!-- In your CLAUDE.md or CLAUDE-PROJECT.md -->
## Load Additional Modules
- modules/CLAUDE-DOCKER.md
- modules/CLAUDE-TESTING.md
```

## Customization Examples

### Example 1: Adding Company-Specific Module
```bash
cat > ~/claude-config/modules/CLAUDE-COMPANY.md << 'EOF'
# CLAUDE-COMPANY: Acme Corp Standards
> Loaded for all Acme projects

## Code Standards
- Use 2-space indentation
- Prefix all branches with ticket numbers
- All commits must reference JIRA tickets

## Security Requirements
- Never commit .env files
- Use company VPN for deployments
- All APIs require authentication
EOF
```

### Example 2: Project Override
```bash
cat > ~/projects/legacy-app/CLAUDE-PROJECT.md << 'EOF'
# Legacy App Configuration
> Overrides for this specific project

## Special Considerations
- Uses jQuery (don't suggest React)
- PHP 5.6 constraints
- MySQL 5.5 limitations
- No build tools available
EOF
```

### Example 3: Personal Preferences
```bash
cat > ~/claude-config/CLAUDE-PERSONAL.md << 'EOF'
# Personal Preferences
> Always loaded for my sessions

## Communication Style
- Be extremely concise
- Skip explanations unless asked
- Use bullet points always
- Challenge my assumptions

## Workflow
- Always use tmux
- Prefer vim for editing
- Use fish shell syntax
EOF
```

## Prerequisites System

### Understanding Prerequisites
Before any task, the AI validates environment state:

```bash
# Universal checks (always run)
dehc check --mode quick
pwd && git status

# Task-specific (conditional)
[[ -f package.json ]] && npm ls
[[ -d .git ]] && git diff --stat
```

### Custom Prerequisites
Add your own checks:
```markdown
## Project Prerequisites
- [ ] VPN connected: `vpn status`
- [ ] Docker running: `docker ps`
- [ ] Test DB available: `pg_isready`
```

## Pattern Discovery

### How It Works
1. AI encounters unknown pattern
2. Searches for 3+ examples
3. Documents discovered pattern
4. Applies consistently

### Guiding Discovery
```markdown
## Preferred Patterns
Look for patterns in:
- src/components/* for React components
- api/handlers/* for API patterns
- tests/* for testing approach
```

## Session Handoffs

### Creating Handoffs
The AI creates structured handoffs when:
- Session ends
- Context switch needed
- Blocked on issue

### Handoff Template
```markdown
## SESSION HANDOFF 20250109-1530
### Current State
- Task: Implementing user authentication
- Progress: 3/5 subtasks complete
- Location: ~/projects/app

### Key Context
- Using JWT for auth
- PostgreSQL for user storage
- bcrypt for passwords

### Next Steps
1. Add password reset flow
2. Implement 2FA
3. Add session management

### Recovery
cd ~/projects/app
git status
npm test auth.test.js
```

## Troubleshooting

### Issue: Modules Not Loading
```bash
# Check detection
~/claude-config/scripts/detect-project.sh

# Force load in CLAUDE.md
echo "Load: modules/CLAUDE-WEB.md" >> CLAUDE.md
```

### Issue: Conflicts with Existing Config
```bash
# Use backup
cp backups/*/CLAUDE.md.backup ./CLAUDE.md

# Merge manually
diff -u CLAUDE.md core/CLAUDE-CORE.md
```

### Issue: AI Ignoring New Patterns
```markdown
<!-- Be explicit -->
## IMPORTANT: Load v2.0 Configuration
Use pattern discovery protocol
Check prerequisites before tasks
Follow modular loading
```

## Best Practices

### 1. Start Small
- Begin with CLAUDE-CORE.md only
- Add modules as needed
- Create custom modules gradually

### 2. Document Patterns
- When AI discovers patterns, save them
- Build library of patterns over time
- Share patterns across projects

### 3. Regular Updates
```bash
# Weekly sync
git pull
./scripts/migrate.sh
# Review new modules
```

### 4. Project Hygiene
- One CLAUDE-PROJECT.md per project
- Keep project-specific, not general
- Version control with project

## Migration Checklist

- [ ] Backup existing CLAUDE.md
- [ ] Run migration script
- [ ] Test in one project
- [ ] Verify modules load correctly
- [ ] Check prerequisites work
- [ ] Test pattern discovery
- [ ] Create first handoff
- [ ] Commit and push changes
- [ ] Sync to other devices
- [ ] Document custom patterns

## Support

- GitHub Issues: [claude-config/issues](https://github.com/reggienitro/claude-config/issues)
- Documentation: This guide
- Examples: docs/examples/

---
*Integration Guide v1.0 | Part of Claude Config v2.0*