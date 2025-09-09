# CLAUDE-CORE: Foundational Configuration
> Progressive disclosure configuration - Start here, expand as needed

## 🎯 Core Philosophy
**Configuration as Living Documentation** - This config teaches through structure, not just instructions.

## 🧬 Project Architecture DNA
<!-- This section implicitly teaches AI about your environment through structure -->
```yaml
environment:
  type: "personal-development"
  approach: "spec-driven"
  philosophy: "define-what-before-how"
  
workspace_structure:
  ~/AI projects/: "Primary development"
  ~/projects/: "Active work"
  ~/.config/: "System configurations"
  
decision_hierarchy:
  1: "User explicit request"
  2: "Project specification"  
  3: "Existing patterns in codebase"
  4: "This configuration"
  5: "AI best judgment"
```

## 🚦 Prerequisites Validation Protocol
**BEFORE ANY TASK: Run this checklist**

### Universal Prerequisites
```bash
# □ Environment ready?
dehc check --mode quick || echo "⚠️ Environment issues detected"

# □ In correct directory?
pwd && git status --short

# □ Dependencies current?
[[ -f package.json ]] && npm ls --depth=0 2>/dev/null | head -5

# □ Clean working tree?
git diff --stat
```

### Task-Specific Prerequisites
- **Before Creating Files**: `ls -la` target directory exists?
- **Before Database Work**: Environment variables loaded?
- **Before Testing**: Test framework installed?
- **Before Building**: Build config present?

## 🎭 Pattern Discovery Protocol
**When encountering unknown codebase patterns:**

### Phase 1: Observe
```markdown
1. Find 3+ examples of similar code
2. Extract common patterns:
   - Naming conventions
   - File organization  
   - Import structure
   - Error handling
   - Testing approach
```

### Phase 2: Document
```markdown
DISCOVERED PATTERN: [Name]
- Examples found: [files]
- Pattern structure: [description]
- Should follow: [yes/no + reasoning]
```

### Phase 3: Apply
- Follow discovered patterns unless explicitly told otherwise
- Document deviations with reasoning

## ⛔ Out of Scope Boundaries
**These are EXPLICIT NON-GOALS - Do not attempt:**

### Never Automatically
- ❌ Create documentation unless requested
- ❌ Refactor working code without permission
- ❌ Add features beyond requirements
- ❌ Optimize without metrics
- ❌ Deploy or publish anything
- ❌ Modify git history
- ❌ Change project configuration files
- ❌ Install new dependencies without approval

### Always Require Permission For
- 🔐 Any .env or secrets handling
- 📁 Creating new directories
- 🔗 External service connections
- 📦 Package installations
- 🗃️ Database schema changes

## 🔄 Session Continuation Architecture

### Handoff Creation Protocol
When session ends or context switches needed:

```markdown
## SESSION HANDOFF [timestamp]
### Current State
- Working directory: [pwd]
- Task objective: [what we're building]
- Completion status: [X/Y tasks done]

### Critical Context
- Key decisions made: [list]
- Blockers encountered: [list]
- Next immediate step: [specific action]

### Recovery Commands
```bash
cd [directory]
git status
[specific state check commands]
```

### Do Not Repeat
- Already tried: [failed approaches]
- Already decided: [settled questions]
```

### Handoff Recovery Protocol
When resuming work:

1. **Load handoff**: Read SESSION_HANDOFF_*.md
2. **Verify state**: Run recovery commands
3. **Announce resume**: "Resuming [task] from [status]"
4. **Continue forward**: Don't repeat completed work

## 🧩 Modular Configuration Loading

### Configuration Hierarchy
```
CLAUDE-CORE.md (this file - always loaded)
├── CLAUDE-PROJECT.md (project-specific overrides)
├── modules/
│   ├── CLAUDE-ML.md (when ML detected)
│   ├── CLAUDE-WEB.md (when web framework detected)
│   ├── CLAUDE-DATABASE.md (when database detected)
│   └── CLAUDE-TESTING.md (when tests detected)
└── CLAUDE-LOCAL.md (personal, never committed)
```

### Auto-Load Triggers
- Detect `requirements.txt` → Load CLAUDE-ML.md
- Detect `package.json` → Load CLAUDE-WEB.md  
- Detect `.env` with DB vars → Load CLAUDE-DATABASE.md
- Detect `test/` directory → Load CLAUDE-TESTING.md

## 💬 Communication Contract

### Response Hierarchy
1. **Answer questions first** - Before any action
2. **Explain before executing** - What and why
3. **Validate prerequisites** - Run checklist
4. **Execute with feedback** - Show progress
5. **Confirm completion** - With verification

### Cognitive Load Management
- One question at a time
- Default suggestions provided
- Escape hatches for experts
- Progressive complexity revelation

## 🎯 Success Validation Framework

### Definition of "Done"
A task is ONLY complete when:
- ✅ Explicitly requested functionality works
- ✅ No errors in execution
- ✅ Tests pass (if applicable)
- ✅ Follows discovered patterns
- ✅ Prerequisites remain valid
- ✅ No new warnings introduced

### Incomplete State Handling
If blocked or partially complete:
- 🔶 Mark exact stopping point
- 🔶 Document what remains
- 🔶 Create continuation handoff
- 🔶 Request human intervention

## 🔍 Learning Mode Instructions

### When You Don't Know
1. **Admit uncertainty**: "I need to understand X first"
2. **Research phase**: Use tools to investigate
3. **Present findings**: "Based on analysis..."
4. **Confirm approach**: "Should I proceed with..."
5. **Document learning**: Add to pattern discovery

### Continuous Improvement
- Log discovered patterns → Future sessions benefit
- Track common issues → Build prerequisites
- Note user preferences → Refine approach

---

## Quick Reference Card
```bash
# Start work
dehc check --mode quick && pwd

# Save state
echo "## SESSION [$(date +%Y%m%d-%H%M%S)]" > SESSION_HANDOFF.md

# Load features
[[ -f CLAUDE-PROJECT.md ]] && echo "Project config loaded"

# Validate
git status --short && npm test
```

---
*CLAUDE-CORE v2.0 | Progressive Disclosure Configuration*
*Next: Load CLAUDE-PROJECT.md for specific configurations*