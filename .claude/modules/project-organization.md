# Project Organization & Filing Standards

## 📁 Master Directory Structure

```
~/AI projects/
├── claude-tools/          # Claude Code utilities and extensions
├── mcp-servers/           # MCP server configurations and documentation
├── ml-projects/           # Machine learning and model fine-tuning
├── automation-tools/      # Workflow automation and productivity tools
├── scripts/               # Utility and automation scripts
│   ├── database/          # DB management and migrations
│   ├── utilities/         # General utility scripts
│   └── testing/           # Test scripts and verification
└── repos/                 # External repositories and forks

~/model-finetuning-project/ # Legacy directory (being reorganized)
~/claude-config/            # This configuration system
```

## 🎯 Project Filing Rules

### **1. New Project Categorization**
When creating a new project, place it in the appropriate category:

- **claude-tools/** - Tools that enhance Claude Code workflows
- **ml-projects/** - Machine learning, AI training, model work
- **automation-tools/** - Productivity automation, scripting systems
- **repos/** - External projects, forks, experiments

### **2. Project Structure Standards**
Every project should have:
```
project-name/
├── README.md              # Project overview and quick start
├── CLAUDE.md              # Project-specific Claude instructions (optional)
├── src/                   # Source code
├── tests/                 # Test files
├── docs/                  # Documentation
├── configs/               # Configuration files
├── .env.example           # Environment variables template
└── .gitignore             # Git ignore rules
```

### **3. File Naming Conventions**
- **Scripts**: `kebab-case.py`, `setup-database.py`
- **Classes**: `PascalCase.py`, `DatabaseManager.py`
- **Configs**: `snake_case.json`, `api_keys.env`
- **Docs**: `UPPER_CASE.md` for important docs, `lower-case.md` for guides
- **No spaces in filenames** - use dashes or underscores

### **4. Code Organization Rules**
- **No giant files** - Split functionality into focused modules
- **Maximum 200 lines per file** unless absolutely necessary
- **One class per file** for complex classes
- **Group related functions** in utility modules
- **Separate concerns** - don't mix UI and business logic

## 📋 Git Workflow Standards

### **Commit Message Format**
Use conventional commits:
```
feat: add user authentication system
fix: resolve database connection timeout
docs: update API documentation
style: format code with black
refactor: extract payment logic into service
test: add integration tests for auth
chore: update dependencies
```

### **Branch Management**
- **main** - Production-ready code
- **develop** - Integration branch for features
- **feature/description** - New features
- **fix/description** - Bug fixes
- **hotfix/description** - Critical production fixes

### **Commit Frequency**
- Commit early, commit often
- Each commit should be a logical unit of work
- Test before committing
- Use `/safe-commit` command for quality checks

## 🔧 Development Workflow

### **Starting New Projects**
```bash
# 1. Create in appropriate category
mkdir -p "~/AI projects/claude-tools/project-name"
cd "~/AI projects/claude-tools/project-name"

# 2. Initialize structure
mkdir -p {src,tests,docs,configs}
touch README.md .gitignore

# 3. Copy configuration
cp ~/claude-config/CLAUDE.md ./CLAUDE.md

# 4. Initialize git
git init
git add .
git commit -m "feat: initial project setup"

# 5. Create remote (if needed)
gh repo create project-name --private
git remote add origin git@github.com:username/project-name.git
git push -u origin main
```

### **Daily Development**
```bash
# Morning routine
/morning-standup
git status
git pull

# During development
# - Commit frequently with clear messages
# - Use /safe-commit for quality checks
# - Test before committing

# End of day
/end-of-day
git push
```

## 📊 Project Status Tracking

### **README.md Requirements**
Every project README must include:
```markdown
# Project Name
Brief description of what it does

## Status
- ✅ Core functionality complete
- 🔄 Testing in progress  
- 📌 Documentation pending

## Quick Start
Basic usage instructions

## Dependencies
List of requirements

## API Keys
Required environment variables (never include actual keys)
```

### **Project Lifecycle States**
- 🔬 **Experiment** - Testing ideas, may be deleted
- 🚧 **Development** - Active development
- ✅ **Complete** - Functional, may need maintenance
- 📦 **Archive** - No longer active, kept for reference
- 🗑️ **Deprecated** - Should be removed

## 🔒 Security & Privacy Standards

### **API Key Management**
- Store in `~/.config/api-keys/.env`
- Use `.env.example` files in projects
- Never commit actual keys to git
- Use different keys for different environments

### **Sensitive Data Rules**
- No personal data in repositories
- No API keys, passwords, or tokens in code
- Use environment variables for all secrets
- Review commits before pushing

### **Code Security**
- Validate all inputs
- Use parameterized queries for databases
- Review generated code for security issues
- Follow principle of least privilege

## 📈 Maintenance Protocols

### **Weekly Maintenance**
- Review and clean up experiment projects
- Update dependencies in active projects
- Backup important data
- Check API key rotation schedule

### **Monthly Reviews**
- Archive completed projects
- Update documentation
- Review and optimize project structure
- Clean up unused files

### **Quarterly Audits**
- Full security review of all projects
- Consolidate similar projects
- Update project categorization
- Review and update this organization guide

## 🎯 Quality Standards

### **Code Quality Checklist**
- [ ] Tests pass
- [ ] Linting passes
- [ ] Documentation updated
- [ ] No debug code or console.logs
- [ ] Follows project conventions
- [ ] Security considerations addressed
- [ ] API keys not committed

### **Project Health Indicators**
- ✅ Recent commits (active development)
- ✅ Tests passing
- ✅ Documentation up to date
- ✅ Dependencies up to date
- ✅ No security vulnerabilities

## 🚀 Project Templates

### **Quick Setup Commands**
```bash
# Claude tool project
./add-project.sh ~/new-tool claude-tools "Description of tool"

# ML project  
./add-project.sh ~/ml-experiment ml-projects "ML experiment description"

# Automation tool
./add-project.sh ~/automation-script automation-tools "Automation description"
```

### **Template Files**
Templates available in `/Users/aettefagh/claude-config/.claude/templates/`:
- `python-project/` - Python project with testing setup
- `web-app/` - Web application with React/Next.js
- `cli-tool/` - Command-line tool with argparse
- `mcp-server/` - MCP server development template

---

**Last Updated**: 2025-08-17  
**Version**: 1.0  
**Next Review**: 2025-09-17