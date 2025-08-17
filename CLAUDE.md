# Personal Claude Code Configuration

## About Me
This is a personal development environment optimized for AI-assisted development workflows across multiple devices.

## Core Development Principles

### Communication Style
- Be concise but precise - I prefer explanations of what's being done as I am no code wizard. I especially appreciate planning, structuring, and strategizing before building anything, and constantly referring back to the actual project plan. Make it a high priority to ask me clarifying or other sorts of questions to better refine our projects.
- Skip preambles like "I'll help you..." or "Let me..."
- Use bullet points for multiple items
- One-line answers are perfect for simple questions
- **Challenge my thinking** - If you think I'm wrong or there's a better approach, speak up! Present alternatives and explain your reasoning. I value constructive pushback

### 🚨 CRITICAL: ASK QUESTIONS BEFORE BUILDING
**MANDATORY FOR ALL PROJECT/APP DEVELOPMENT:**
- **ALWAYS ASK CLARIFYING QUESTIONS** before starting any implementation
- **NEVER assume requirements** - ask about functionality, user experience, technical constraints, deployment targets
- **Question everything**: What's the specific use case? What's the target audience? What platforms? What's the expected workflow?
- **Stop and ask** rather than making assumptions about features, UI/UX, or technical architecture
- **This is mandatory** - I'd rather answer 10 questions than debug wrong assumptions or rebuild incorrectly

### Code Style Preferences
- Write clean, self-documenting code
- Comments are appreciated to explain and document
- Prefer functional approaches where appropriate
- Test-driven development when applicable
- Commit often, unit and regression test often
- Employ good file structure and naming conventions, do not dump giant lines into one file

### Workflow Preferences
- Break complex tasks into subtasks immediately
- Mark tasks complete as soon as finished
- Create comprehensive git commits with clear messages
- Use conventional commit format: feat/fix/docs/style/refactor/test/chore

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

## Installed Tools & Capabilities

### Task Management (via Task Master)
- Use `task-master` commands for project organization
- Parse PRDs with `task-master parse-prd`
- Track progress with `task-master list` and `task-master next`
- Expand tasks with `task-master expand --research`

### MCP Servers Available (12 Total)

#### Core Infrastructure
- **filesystem**: Local file operations
- **web-search**: Real-time web information
- **mcp-installer**: Package management for MCP servers
- **mcp-tts**: Text-to-speech functionality

#### Development & Collaboration
- **github**: Repository management, issues, PRs, workflow automation
- **supabase**: Database operations, real-time subscriptions, auth, storage
- **exa-search**: Advanced semantic web search and content extraction
- **playwright**: Browser automation, web scraping, UI testing

#### AI & Knowledge Management
- **bee**: Bee AI framework
- **beemcp**: Bee.computer lifelogging data access
- **memory**: Persistent context and knowledge storage across sessions
- **task-master-ai**: Project and task management with PRD parsing
- **bee-supabase**: Integration between Bee.computer data and Supabase database

Additional servers can be installed via `mcp-installer`

### Development Tools
- Git and GitHub CLI (`gh`) for version control
- Multiple language environments (Python, Node.js, etc.)
- Testing frameworks appropriate to each project
- Docker for containerization when needed

## Project-Specific Instructions

### Model Fine-Tuning Projects
When working on ML/AI projects:
1. Always activate the virtual environment first
2. Use appropriate frameworks (LLaMA-Factory for flexibility, specific notebooks for learning)
3. Track experiments with wandb or tensorboard
4. Document hyperparameters and results

### Database Integration Projects
When working with Supabase/database projects:
1. Verify environment variables in `~/.config/api-keys/.env`
2. Test connections before schema operations
3. Use manual schema creation for complex operations
4. Set up automation after successful manual testing
5. Document schema changes and migration paths

### Web Development
1. Check package.json for available scripts
2. Run tests before committing
3. Use conventional commits
4. Follow existing component patterns

### System Configuration
1. MCP configurations sync across devices via this repo
2. CLAUDE.md files should be project-specific
3. Use .env files for API keys (never commit them)

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

### Database Management Workflows

#### Supabase Schema Setup
```bash
# Create schema via Supabase dashboard
# 1. Go to https://supabase.com/dashboard
# 2. Navigate to SQL Editor
# 3. Execute schema file
# 4. Verify with setup script
python3 setup_bee_supabase.py
```

#### Database Migration Pattern
```bash
# Standard migration workflow
python3 setup_database.py              # Verify connectivity
python3 execute_schema.py               # Apply schema changes
python3 verify_schema.py               # Confirm success
```

#### Data Sync Operations
```bash
# Bee data dumps to Supabase
python3 bee_supabase_agent.py --status          # Check status
python3 bee_supabase_agent.py                   # Run daily dump
python3 bee_supabase_agent.py --backfill 7      # Backfill last 7 days
python3 schedule_bee_dumps.py --create-cron     # Setup automation
```

## Multi-Device Sync

### Repository Structure
```
~/AI projects/
├── claude-tools/          # Custom tools and extensions
├── mcp-servers/           # MCP server configurations
├── scripts/               # Utility and automation scripts
│   ├── database/          # DB management and migrations
│   ├── utilities/         # General utility scripts
│   └── testing/           # Test scripts and verification
├── ml-projects/           # Machine learning projects
└── automation-tools/      # Workflow automation

~/model-finetuning-project/ (Legacy - being reorganized)
├── CLAUDE.md (project-specific overrides)
├── repos/ (cloned projects)
└── requirements/ (requirements documentation)
```

### Syncing Across Devices
1. Push CLAUDE.md and configs to GitHub
2. Clone on new device
3. Symlink or copy CLAUDE.md to appropriate locations
4. Install required MCP servers

## Security & Privacy

### API Key Management
- Store in .env files or secure key management
- Never commit API keys
- Use different keys for different environments
- Rotate keys regularly

### MCP Server API Keys
All API keys stored securely in `~/.config/api-keys/.env`:
- **BEE_API_TOKEN**: Bee.computer lifelogging access
- **GITHUB_PERSONAL_ACCESS_TOKEN**: GitHub repository operations
- **SUPABASE_URL & SUPABASE_KEY**: Database operations and cloud sync
- **SUPABASE_PROJECT_REF**: Project reference for MCP server connection
- **EXA_API_KEY**: Exa semantic search capabilities

Source from environment file for security

### Code Security
- Review generated code for security issues
- Don't blindly execute suggested commands
- Be cautious with file system operations
- Validate all inputs

## Shortcuts & Aliases

### Common Commands
```bash
# Task management
alias tn='task-master next'
alias tl='task-master list'
alias td='task-master set-status --status=done --id='

# Git shortcuts
alias gs='git status'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline'
```

### Claude Code Commands
- `/clear` - Clear context between tasks
- `/plan` - Enter planning mode
- `/architect` - System design mode
- `/requirements-start` - Begin requirements gathering
- `/requirements-status` - Check requirements progress
- `/remind` - Remind AI to follow rules

### Session Continuation Protocol

When resuming work on long-running projects:

#### Continuation Commands
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

#### Session Recovery Keywords
- **"continuation prompt"** - Load previous session context
- **"handoff"** - Transfer between AI sessions with state
- **"resume from"** - Continue specific project tasks
- **"status check"** - Verify current system state

#### Context Files
- `SESSION_HANDOFF_*.md` - Detailed session transfer docs
- `SESSION_SUMMARY.md` - High-level progress summary
- `RESTART_PROMPT.txt` - Quick continuation context

#### Example Session Handoff Content
Recent project handoffs include:
- **Bee Supabase Integration**: Complete data pipeline with daily automation setup
- **Article-to-Audio + Supabase**: Full cloud integration with user accounts and sync
- **MCP Server Configurations**: Cross-device tool synchronization

#### Post-Session Verification Checklist
- [ ] Check MCP servers are active and functional
- [ ] Verify database connections and schema state
- [ ] Test critical workflows end-to-end
- [ ] Confirm environment variables and credentials
- [ ] Review any pending tasks or blockers

## Project Templates

### Python ML Project
```python
# Standard imports
import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Project structure
project/
├── data/
├── models/
├── notebooks/
├── src/
├── tests/
└── configs/
```

### Web Application
```javascript
// React/Next.js structure
app/
├── components/
├── pages/
├── styles/
├── utils/
├── hooks/
└── tests/
```

### Article-to-Audio Project
```bash
# Authentication workflow
./article2audio-enhanced --signup --email "user@example.com" --display-name "Name"
./article2audio-enhanced --signin --email "user@example.com"
./article2audio-enhanced --user-info

# Convert with cloud sync
./article2audio-enhanced "https://example.com/article" --save --voice christopher

# Test integration
python3 test_integration.py
python3 test_basic_supabase.py
```

#### Audio Project Structure
```
claude-tools/article-to-audio-extension/
├── article2audio-enhanced         # Main conversion tool
├── enhanced-server.py            # Backend server
├── supabase_integration.py       # Database integration
├── test-files/                   # Audio test samples
└── tests/                        # Integration tests
```

## Notes & Reminders

- This file is loaded automatically by Claude Code
- Project-specific CLAUDE.md files override these defaults
- Update this file as preferences evolve
- Keep security in mind - this file may be read by AI

## Debug Mode

When debugging is needed:
1. Enable verbose logging
2. Use step-by-step execution
3. Document findings in task notes
4. Create test cases for bugs found

## MCP Servers Reference

### Quick MCP Commands
```bash
# Test GitHub connection
gh auth status

# Test Supabase connection
python3 -c "from supabase import create_client; print('Connected')"

# List all installed MCP servers
cat ~/AI\ projects/mcp-servers/installed/installed-servers.json

# View MCP server documentation
ls ~/AI\ projects/mcp-servers/documentation/individual-servers/
```

### MCP Server Documentation
Detailed documentation for each server available at:
`~/AI projects/mcp-servers/documentation/individual-servers/`

### Adding New MCP Servers Protocol
When installing or discovering new MCP servers, follow this documentation process:

1. **Install & Configure Server**
   ```bash
   # Install the server
   npx @anaisbetts/mcp-installer install <server-name>
   # or specific installation method
   
   # Add to Claude desktop config
   # Configure API keys in ~/.config/api-keys/.env if needed
   ```

2. **Test Server Functionality**
   ```bash
   # Test the server works
   # Document any API key requirements
   # Verify all core features function
   ```

3. **Create Documentation Files**
   ```bash
   # Create individual server documentation
   ~/AI projects/mcp-servers/documentation/individual-servers/<server-name>.md
   
   # Include: Overview, Capabilities, Configuration, Use Cases, Status
   ```

4. **Update Tracking Files**
   ```bash
   # Add to installed servers JSON
   ~/AI projects/mcp-servers/installed/installed-servers.json
   
   # Update main README
   ~/AI projects/mcp-servers/README.md
   
   # Update this CLAUDE.md file's MCP server list
   ```

5. **Update Central Documentation**
   - Add server to "MCP Servers Available" section above
   - Include category, description, and key capabilities
   - Note any API key requirements
   - Update total count and version number

This ensures all MCP servers are properly documented and tracked in the centralized system.

---

Last updated: 2025-08-13
Version: 1.2