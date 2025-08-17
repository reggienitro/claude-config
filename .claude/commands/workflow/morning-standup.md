# /morning-standup

Daily development session initialization and planning.

## Purpose:
Start each development session with a comprehensive overview of current state, priorities, and planned work. Ensures continuity between sessions and helps identify any issues before starting work.

## Usage:
```bash
/morning-standup
/morning-standup --quick    # abbreviated version
/morning-standup --detailed # full system check
```

## Workflow:
1. **Load session context** - check for continuation files
2. **System health check** - verify all services operational
3. **Review current tasks** - task-master status and priorities  
4. **Check for blockers** - identify anything preventing progress
5. **Plan today's work** - set clear objectives and priorities
6. **Environment prep** - ensure all tools ready

## Checks Performed:

### Session Continuity
- Look for SESSION_HANDOFF_*.md files
- Check SESSION_SUMMARY.md for recent progress
- Review RESTART_PROMPT.txt if present
- Load any project-specific context

### System Status  
- Git repository state (uncommitted changes, branch)
- MCP servers functional (quick connectivity test)
- Database connections active
- API keys and environment variables loaded

### Task Review
```bash
task-master list                    # current tasks
task-master next                    # next priority item
# Review any pending requirements gathering
```

### Development Environment
- Virtual environments activated (if applicable)
- Required dependencies installed
- Development servers ready to start
- Testing frameworks accessible

## Output Format:
```
🌅 MORNING STANDUP - [Date]

📋 SESSION CONTEXT
- Previous session: Article-to-Audio Supabase integration
- Handoff files: SESSION_HANDOFF_BEE_SUPABASE.md found
- Current phase: Schema creation and testing

🔧 SYSTEM STATUS
✅ Git: Clean working directory, main branch  
✅ MCP: 12/12 servers active
✅ Database: Supabase connected
⚠️  Environment: 1 API key missing

📝 TODAY'S PRIORITIES
1. [HIGH] Create Supabase schema via MCP tools
2. [MED] Test full integration workflow  
3. [LOW] Update documentation

🎯 IMMEDIATE NEXT STEPS
- Run: python3 setup_bee_supabase.py
- Create: Database tables via Supabase MCP
- Test: Full article conversion with cloud sync

⚡ READY TO START
All systems operational. Begin with priority task #1.
```

## Benefits:
- **Continuity**: Seamless session transitions
- **Focus**: Clear priorities and next steps
- **Prevention**: Catch issues before they block work
- **Efficiency**: No time wasted on setup/debugging