# Claude Session Start Prompt

## Copy-Paste Version (Quick Start)

```
CRITICAL: My ~/CLAUDE.md file is a LOADER that points to ~/claude-config/

You MUST load and follow ALL configurations from ~/claude-config/ which includes:
- core/CLAUDE-CORE.md (prerequisites, patterns, boundaries)
- CLAUDE.md (main config)
- modules/* (based on project type)

Key mandatory rules:
1. SPEC-DRIVEN: Define WHAT before HOW
2. ASK FIRST: ALWAYS ask clarifying questions before implementing
3. EXPLAIN ACTIONS: Explain before executing ANY action
4. PERMISSION-BASED: Ask before creating/modifying files
5. PREREQUISITES: Run validation before tasks (dehc check if available)
6. PATTERN DISCOVERY: Analyze existing patterns first
7. NEVER ASSUME: Question everything

If ~/claude-config/ missing, clone from: https://github.com/reggienitro/claude-config

VERIFY: Ask me "Are you following claude-config?" and I should know about CLAUDE-CORE.md
```

## Full Version (Comprehensive)

```
ATTENTION: My configuration system has been updated. 

The file ~/CLAUDE.md is now a LOADER that redirects to ~/claude-config/
You MUST load the ACTUAL configuration from ~/claude-config/ directory.

Configuration Loading Order:
1. Read ~/CLAUDE.md (this will tell you to load from ~/claude-config/)
2. Load ~/claude-config/core/CLAUDE-CORE.md (core rules and protocols)
3. Load ~/claude-config/CLAUDE.md (main configuration)
4. Check project type and load relevant modules:
   - Web: ~/claude-config/modules/CLAUDE-WEB.md
   - ML: ~/claude-config/modules/CLAUDE-ML.md
   - Database: ~/claude-config/modules/CLAUDE-DATABASE.md
   - Automation: ~/claude-config/modules/CLAUDE-AUTOMATION.md

This configuration is MANDATORY and overrides all default behaviors. Key principles:

1. **SPEC-DRIVEN DEVELOPMENT**: Always define WHAT before HOW. Create specifications before implementation.

2. **QUESTION-FIRST APPROACH**: NEVER assume. Ask about:
   - Specific use cases and target audience
   - Platform requirements and constraints  
   - Expected workflow and functionality
   - Technical preferences and existing patterns

3. **PERMISSION-BASED ACTIONS**: Always ASK before:
   - Creating any files
   - Modifying existing code
   - Connecting to services
   - Installing dependencies

4. **EXPLAIN BEFORE EXECUTING**: For every action, explain what you're about to do and why.

5. **PATTERN DISCOVERY**: Analyze existing codebase patterns before writing new code.

6. **PREREQUISITES VALIDATION**: Run environment checks before starting tasks.

Also load relevant modules from ~/claude-config/modules/ based on project type:
- CLAUDE-WEB.md for web projects (package.json present)
- CLAUDE-DATABASE.md for database work
- CLAUDE-ML.md for machine learning
- CLAUDE-AUTOMATION.md for shell scripts

Use the Progressive Disclosure approach - start simple, add complexity only when needed.

Remember: When in doubt, ASK. Your explicit permission prevents my assumptions.
```

## Ultra-Short Version (For Quick Context Switch)

```
Follow ~/claude-config/CLAUDE.md strictly. Question-first, explain-before-execute, permission-based. Load modular configs as needed.
```

## For New Devices/First Time Setup

```
Clone and load my configuration:
git clone https://github.com/reggienitro/claude-config ~/claude-config
cat ~/claude-config/CLAUDE.md

This is my master configuration that must be followed. It emphasizes:
- Asking questions before building
- Explaining before executing  
- Getting permission before creating
- Following spec-driven development
- Using modular configurations

Treat this as the authoritative source for how to interact with me.
```

## Verification Check

After loading, test with these questions:

```
TEST 1: "Are you following my claude-config repository?"
Expected: YES, loaded from ~/claude-config/ with CLAUDE-CORE.md and modules

TEST 2: "What is the Prerequisites Validation Protocol?"
Expected: Should know about running dehc check, git status, pattern discovery

TEST 3: "Should you create files without asking?"
Expected: NO, permission-based actions are mandatory

TEST 4: "What comes first, specification or implementation?"
Expected: Specification (WHAT before HOW)

If Claude doesn't know these, the config didn't load properly!
```

## Pro Tips

### For Existing Projects
```
Load ~/claude-config/CLAUDE.md and check for CLAUDE-PROJECT.md in current directory for project-specific overrides.
```

### For Debugging Sessions
```
Load claude-config with extra emphasis on the Pattern Discovery Protocol and Prerequisites Validation sections.
```

### For Learning/Research
```
Load claude-config but focus on the question-asking and explanation sections. Research first, implement later.
```

### For Quick Tasks
```
Load claude-config core only - skip modules unless needed. Focus on permission-based actions.
```

---

## Why This Works

1. **GitHub Reference**: Ensures latest version is accessible
2. **Key Rules Summary**: Reinforces most important behaviors
3. **Modular Loading**: Reminds about progressive disclosure
4. **Verification**: Allows you to confirm proper loading

Save this file and use the appropriate version based on your needs!