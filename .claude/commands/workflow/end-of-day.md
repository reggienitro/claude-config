# /end-of-day

Session wrap-up with state preservation and handoff preparation.

## Purpose:
Properly conclude development sessions by creating comprehensive handoff documentation, committing work, and preparing for seamless continuation in the next session.

## Usage:
```bash
/end-of-day
/end-of-day --quick     # minimal handoff
/end-of-day --detailed  # comprehensive documentation
```

## Workflow:
1. **Commit current work** - ensure no work is lost
2. **Document session progress** - what was accomplished
3. **Identify current state** - where we left off
4. **Note blockers/issues** - anything preventing progress
5. **Plan next session** - clear starting point
6. **Create handoff files** - for session continuity

## Tasks Performed:

### Code Preservation
```bash
git status                          # show current changes
git add -A                          # stage all changes
git commit -m "work in progress: [description]

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Progress Documentation
- Update task-master status for completed/in-progress items
- Document what was accomplished this session
- Note any architectural decisions made
- Record any new dependencies or configurations added

### State Capture
- Current branch and repository state
- Running processes or services
- Database schema state
- Environment variables and configurations
- Open files and current working directory

### Issue Tracking
- Any errors encountered and resolutions attempted
- Blockers that need resolution
- Missing dependencies or configurations
- Questions that need answering before proceeding

### Next Session Preparation
- Clear starting point and first task
- Required commands to resume work
- Expected time to complete current task
- Any research or preparation needed

## Output Files Created:

### SESSION_HANDOFF_[PROJECT].md
Comprehensive technical handoff including:
- Current state analysis
- Files created/modified this session
- Technical architecture notes
- Immediate next steps
- Known issues and solutions

### SESSION_SUMMARY.md
High-level progress summary:
- What was accomplished
- Current status
- Next priorities
- Timeline estimates

### RESTART_PROMPT.txt
Quick continuation prompt:
- Brief context for next session
- Key commands to run
- Current focus area

## Example Output:
```
🌙 END OF DAY WRAP-UP - [Date]

📊 SESSION SUMMARY
- Duration: 3.5 hours
- Tasks completed: 2/3 planned
- Files modified: 8 files
- Commits: 3 commits

✅ ACCOMPLISHED TODAY
- ✓ Modularized CLAUDE.md configuration
- ✓ Created 5 custom commands
- ⏳ Quality hooks implementation (75% complete)

💾 STATE PRESERVED
- Current branch: feature/modular-config
- Working directory: clean
- Next task: Add pre-commit hooks configuration

📋 HANDOFF FILES CREATED
- SESSION_HANDOFF_CLAUDE_CONFIG.md
- SESSION_SUMMARY.md  
- RESTART_PROMPT.txt

🎯 NEXT SESSION START
Run: cd /Users/aettefagh/claude-config && /morning-standup
Focus: Complete quality hooks and test configuration

✨ Session successfully wrapped up. Ready for next continuation.
```

## Benefits:
- **Zero work loss**: All progress preserved
- **Smooth continuity**: Next session starts immediately
- **Context preservation**: No re-learning required
- **Issue tracking**: Problems documented for resolution