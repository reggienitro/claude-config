# Workflow Patterns & Automation

## 🎯 AI Collaboration Principles

### 1. Preparation and Planning Framework
- Establish project structure before coding
- Strategic discussion before implementation
- Break complex problems into focused tasks
- Document decisions throughout

### 2. Context Management Strategy
- Descriptive naming that communicates purpose
- Modular, focused file organization
- Keep conversations topic-focused
- Use appropriate interaction modes

### 3. Validation and Quality Assurance
- Test-driven validation of generated code
- Understand code, don't just accept it
- Use debugging when AI gets stuck
- Provide current docs for new tech

### 4. Iterative Development and Safety
- Commit frequently for safe experimentation
- Maintain custom instructions based on experience
- Provide runtime feedback to AI
- Version control discipline

### 5. Human-AI Collaboration Boundaries
- Recognize AI strengths and limitations
- Maintain human oversight for debugging
- Use AI as collaborative partner, not replacement
- Bridge AI knowledge gaps with context

## 📋 Requirements Gathering Principles

### Progressive Context Building
- Always analyze existing codebase before asking questions
- Build understanding progressively (structure → patterns → specifics)
- Use discovered context to inform better questions

### Structured Information Gathering
- Break requirements into discrete phases
- Use defaults to reduce cognitive load
- Ask one question at a time, not multiple
- Progress tracking between sessions

### AI Guidance and Boundaries
- Clear rules for AI behavior (use `/remind` if needed)
- Prevent implementation until requirements complete
- Force focus on single topics/features
- Maintain session continuity

### Documentation as Foundation
- Generate specs that other AIs can implement from
- Include specific file paths and patterns
- Link requirements to implementation artifacts
- Maintain searchable requirement history

## Common Workflows

### Starting a New Project
```bash
# Initialize project structure
mkdir -p {src,tests,docs,configs}
task-master init
# Create initial PRD and parse it
task-master parse-prd docs/prd.md
```

### Daily Development Flow
```bash
# Start of session
task-master next
# During work
task-master update-subtask --id=<id> --prompt="progress notes"
# Complete task
task-master set-status --id=<id> --status=done
# Commit changes
git add -A && git commit -m "feat: complete task <id>"
```

### Requirements Gathering Flow
```bash
# Start new requirement
/requirements-start add user authentication
# Continue gathering if interrupted
/requirements-status
# View all requirements
/requirements-list
```

### Debugging Protocol
1. Read error messages carefully
2. Check logs if available
3. Use appropriate debugging tools (debugger, print statements, etc.)
4. Document the solution in task notes

### Code Review Checklist
- [ ] Tests pass
- [ ] Linting passes
- [ ] Documentation updated
- [ ] No console.logs or debug code
- [ ] Follows project conventions
- [ ] Security considerations addressed

## Database Management Workflows

### Supabase Schema Setup
```bash
# Create schema via Supabase dashboard
# 1. Go to https://supabase.com/dashboard
# 2. Navigate to SQL Editor
# 3. Execute schema file
# 4. Verify with setup script
python3 setup_bee_supabase.py
```

### Database Migration Pattern
```bash
# Standard migration workflow
python3 setup_database.py              # Verify connectivity
python3 execute_schema.py               # Apply schema changes
python3 verify_schema.py               # Confirm success
```

### Data Sync Operations
```bash
# Bee data dumps to Supabase
python3 bee_supabase_agent.py --status          # Check status
python3 bee_supabase_agent.py                   # Run daily dump
python3 bee_supabase_agent.py --backfill 7      # Backfill last 7 days
python3 schedule_bee_dumps.py --create-cron     # Setup automation
```

## Session Continuation Protocol

### Continuation Commands
```bash
# Navigate to project
cd /Users/aettefagh/model-finetuning-project

# Check current state
ls -la bee_* supabase_*
python3 setup_bee_supabase.py

# Resume specific workflows
python3 bee_supabase_agent.py --status     # Check data sync status
python3 test_supabase_connection.py        # Verify connections
```

### Session Recovery Keywords
- **"continuation prompt"** - Load previous session context
- **"handoff"** - Transfer between AI sessions with state
- **"resume from"** - Continue specific project tasks
- **"status check"** - Verify current system state

### Context Files
- `SESSION_HANDOFF_*.md` - Detailed session transfer docs
- `SESSION_SUMMARY.md` - High-level progress summary
- `RESTART_PROMPT.txt` - Quick continuation context

### Example Session Handoff Content
Recent project handoffs include:
- **Bee Supabase Integration**: Complete data pipeline with daily automation setup
- **Article-to-Audio + Supabase**: Full cloud integration with user accounts and sync
- **MCP Server Configurations**: Cross-device tool synchronization

### Post-Session Verification Checklist
- [ ] Check MCP servers are active and functional
- [ ] Verify database connections and schema state
- [ ] Test critical workflows end-to-end
- [ ] Confirm environment variables and credentials
- [ ] Review any pending tasks or blockers