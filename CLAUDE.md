# Personal Claude Code Configuration

## About Me
Personal development environment optimized for AI-assisted development workflows across multiple devices.

## Import Modules
- [@.claude/modules/workflow-patterns.md](.claude/modules/workflow-patterns.md)
- [@.claude/modules/mcp-servers.md](.claude/modules/mcp-servers.md)
- [@.claude/modules/project-templates.md](.claude/modules/project-templates.md)
- [@.claude/modules/project-organization.md](.claude/modules/project-organization.md)

## 🚨 CRITICAL: ASK QUESTIONS BEFORE BUILDING
**MANDATORY FOR ALL PROJECT/APP DEVELOPMENT:**
- **ALWAYS ASK CLARIFYING QUESTIONS** before starting any implementation
- **NEVER assume requirements** - ask about functionality, user experience, technical constraints, deployment targets
- **Question everything**: What's the specific use case? What's the target audience? What platforms? What's the expected workflow?
- **Stop and ask** rather than making assumptions about features, UI/UX, or technical architecture
- **This is mandatory** - I'd rather answer 10 questions than debug wrong assumptions or rebuild incorrectly

## Core Principles

### Communication Style
- Be concise but precise - I prefer explanations of what's being done
- Planning, structuring, and strategizing before building anything is essential
- Make it a high priority to ask clarifying questions to better refine projects
- Skip preambles like "I'll help you..." or "Let me..."
- Use bullet points for multiple items
- One-line answers are perfect for simple questions
- **Challenge my thinking** - Present alternatives and explain your reasoning

### Code Style Preferences
- Write clean, self-documenting code
- Comments are appreciated to explain and document
- Prefer functional approaches where appropriate
- Test-driven development when applicable
- Commit often, unit and regression test often
- Employ good file structure and naming conventions

### Workflow Preferences
- Break complex tasks into subtasks immediately
- Mark tasks complete as soon as finished
- Create comprehensive git commits with clear messages
- Use conventional commit format: feat/fix/docs/style/refactor/test/chore

## Quick Reference

### Custom Commands Available
- `/safe-commit "message"` - Automated quality checks + commit
- `/status-check` - Comprehensive system verification
- `/quick-spec "idea"` - Rapid project specification generation
- `/morning-standup` - Daily session initialization
- `/end-of-day` - Session wrap-up with handoff preparation

### Emergency Commands
```bash
task-master next                    # Get next priority task
python3 setup_bee_supabase.py      # Verify database connections
git status && git stash            # Save work quickly
gh auth status                     # Check GitHub connection
```

### Most-Used Workflows
1. **New Project**: `/quick-spec` → requirements gathering → implementation
2. **Daily Dev**: `/morning-standup` → code → `/safe-commit` → `/end-of-day`
3. **Session Recovery**: Check SESSION_HANDOFF_*.md → `/status-check`

### Task Management (via Task Master)
- Use `task-master` commands for project organization
- Parse PRDs with `task-master parse-prd`
- Track progress with `task-master list` and `task-master next`
- Expand tasks with `task-master expand --research`

## Multi-Device Sync

### This Repository
- **GitHub**: https://github.com/reggienitro/claude-config
- **Purpose**: Sync Claude configuration across devices
- **Usage**: Clone → copy CLAUDE.md to project → customize as needed

### Syncing Process
```bash
# On new device
git clone https://github.com/reggienitro/claude-config.git
cd claude-config
cp CLAUDE.md /path/to/project/

# To update
git pull && cp CLAUDE.md /path/to/project/
```

## Security & Privacy

### API Key Management
- Store in ~/.config/api-keys/.env
- Never commit API keys
- Use different keys for different environments
- Rotate keys regularly

### Code Security
- Review generated code for security issues
- Don't blindly execute suggested commands
- Be cautious with file system operations
- Validate all inputs

---

---

**Last updated**: 2025-08-17  
**Version**: 2.1 (Post-Reorganization)  
**Total MCP Servers**: 12 (All Documented)  
**Custom Commands**: 5  
**Major Projects**: Reorganized & Following Standards