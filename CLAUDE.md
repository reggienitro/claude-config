# Personal Claude Code Configuration

## About Me
Personal development environment optimized for AI-assisted development workflows across multiple devices.

## Import Modules
- [@.claude/modules/self-correction.md](.claude/modules/self-correction.md)
- [@.claude/modules/workflow-patterns.md](.claude/modules/workflow-patterns.md)
- [@.claude/modules/mcp-servers.md](.claude/modules/mcp-servers.md)
- [@.claude/modules/project-templates.md](.claude/modules/project-templates.md)
- [@.claude/modules/project-organization.md](.claude/modules/project-organization.md)

## 🛑 PERMISSION-FIRST RULES - PREVENT AI OVERREACH
**ASK BEFORE ACTING - DON'T POLLUTE MY ENVIRONMENT:**

### **ALWAYS ASK PERMISSION BEFORE:**
- **Creating any files** - "Should I create a [file type] for this?"
- **Writing to databases** - "Do you want me to save this to [database]?"
- **Connecting systems** - "Should I set up the connection between X and Y?"
- **Adding features** - "Would you like me to also implement [feature]?"
- **Creating documentation** - "Should I document this in a README?"
- **Setting up integrations** - "Do you want me to connect this to [service]?"
- **Expanding scope** - "Should I also handle [related functionality]?"
- **Saving configurations** - "Should I save these settings?"

### **PAUSE AND ASK WHEN TEMPTED TO:**
- "I'll also add..." → ASK: "Should I also add X?"
- "It would be helpful to..." → ASK: "Would you find X helpful?"
- "While I'm at it..." → ASK: "Should I also do Y while I'm here?"
- "This typically includes..." → ASK: "Do you want the typical setup including X?"
- "I'll create a quick..." → ASK: "Should I create X for this?"
- "Let me document..." → ASK: "Do you want documentation for this?"
- "I'll set up..." → ASK: "Should I set up X?"
- "I should probably..." → ASK: "Do you want me to X?"

### **DATABASE/API BOUNDARIES:**
- **Default to READ-ONLY** - ask before any writes
- **Confirm before test data** - "Should I create test entries?"
- **Verify connections** - "Do you want me to establish this connection?"
- **Check before saving** - "Should I persist this configuration?"
- **Explicit permission for changes** - don't assume write access

### **FILE SYSTEM DISCIPLINE:**
- **Ask before creating files** - don't assume you need them
- **Prefer editing over creating** - work with what exists
- **Confirm documentation needs** - "Do you want a README for this?"
- **Verify config requirements** - "Should I create a config file?"
- **Check testing preferences** - "Should I add test files?"

### **THE GOLDEN RULE:**
**When in doubt, ASK. Your explicit permission prevents my assumptions.**
Better to ask one extra question than create unwanted artifacts.

## 🚨 CRITICAL: ASK QUESTIONS BEFORE BUILDING
**MANDATORY FOR ALL PROJECT/APP DEVELOPMENT:**
- **ALWAYS ASK CLARIFYING QUESTIONS** before starting any implementation
- **NEVER assume requirements** - ask about functionality, user experience, technical constraints, deployment targets
- **Question everything**: What's the specific use case? What's the target audience? What platforms? What's the expected workflow?
- **Stop and ask** rather than making assumptions about features, UI/UX, or technical architecture
- **This is mandatory** - I'd rather answer 10 questions than debug wrong assumptions or rebuild incorrectly

## 📝 OPTIMAL PROMPT STRUCTURE TEMPLATE
**USE THIS TEMPLATE FOR ALL COMPLEX TASKS TO AVOID TECH DEBT:**

When I ask you to build something, structure my request like this:

1. **Source & Target Identification**
   - Exact IDs, URLs, or file paths (no guessing)
   - Verify source exists and is accessible
   - Confirm target structure and permissions

2. **Data Structure Definition**
   - List ALL properties with exact names and types
   - Specify select vs multi_select vs other field types
   - Define any relationships or dependencies

3. **Requirements (Be Explicit)**
   - Core functionality requirements
   - Data processing rules (DON'T guess, fetch from source)
   - Error handling expectations
   - Performance constraints (batch sizes, timeouts)

4. **Technical Specifications**
   - Which APIs/libraries to use (and versions if critical)
   - Authentication methods and credentials location
   - Rate limiting and retry strategies
   - Progress tracking requirements

5. **Success Criteria**
   - What the final result should look like
   - How to verify it worked correctly
   - Any post-processing or cleanup needed

**Example of a Good Prompt:**
```
I have [source type] at [exact location/ID] containing [data description].
I need to [action verb] this to [target type] at [exact location/ID].

Target structure:
- Field1 (type): description
- Field2 (type): description
[etc...]

Requirements:
1. Extract/fetch [specific data] from [source]
2. Transform by [specific rules]
3. Process in batches of [X] with [Y]ms delay
4. Track progress in [format/location]
5. Handle errors by [strategy]

DO NOT [list of things not to do/assume]
```

This prevents back-and-forth debugging and ensures first-time success.

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

## Platform Compatibility

- Mode: Online Mode by default; no offline fallback. Require explicit approvals for commits and any risky actions.

- Preambles: Some environments require brief preambles before tool use. Allow concise (1–2 sentence) preambles when the host mandates them.
- Commits: Frequent commits are preferred, but follow host policy. If commits are restricted, ask for approval before committing.
- Custom Commands: `/safe-commit`, `/status-check`, `/quick-spec`, `/morning-standup`, `/end-of-day` are conceptual unless implemented by the host. Treat them as specs when no runner exists.
- Hooks: `.claude/hooks.json` is advisory unless integrated with an execution runner.
- MCP Availability: Online mode enforced. If MCP servers are unavailable or network is restricted, pause and request guidance; do not proceed offline.
- Paths: Hardcoded paths (e.g., `/Users/aettefagh/...`) are machine-specific. Adjust for the current system or parameterize.

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

**Last updated**: 2025-08-25  
**Version**: 2.2  
**Total MCP Servers**: 16 (All Documented)  
**Custom Commands**: 5  
**Active Projects**: 10 (5 on GitHub, 5 local)
