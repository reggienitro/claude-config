#!/usr/bin/env python3
"""
Project Creation Script
Creates new projects from templates following organization standards
"""

import os
import shutil
import argparse
import subprocess
import datetime
from pathlib import Path
from typing import Dict, List

class ProjectCreator:
    """Create new projects from templates"""
    
    def __init__(self):
        self.base_path = Path.home() / "AI projects"
        self.templates_path = Path.home() / "claude-config" / ".claude" / "templates"
        self.categories = {
            'claude-tools': 'Claude Code utilities and extensions',
            'automation-tools': 'Automation and productivity tools', 
            'ml-projects': 'Machine learning and AI projects'
        }
        
    def create_project(self, name: str, category: str, template: str, description: str = ""):
        """Create a new project from template"""
        
        # Validate category
        if category not in self.categories:
            raise ValueError(f"Category must be one of: {list(self.categories.keys())}")
        
        # Create project path
        project_path = self.base_path / category / name
        
        if project_path.exists():
            raise ValueError(f"Project already exists: {project_path}")
        
        print(f"🚀 Creating project: {name}")
        print(f"📁 Category: {category}")
        print(f"📋 Template: {template}")
        print(f"📍 Location: {project_path}")
        
        # Create directory structure
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Copy template files if template exists
        template_path = self.templates_path / template
        if template_path.exists():
            print(f"📄 Copying template files from {template_path}")
            for item in template_path.iterdir():
                if item.is_file():
                    shutil.copy2(item, project_path)
                elif item.is_dir():
                    shutil.copytree(item, project_path / item.name)
        else:
            print(f"ℹ️  Template {template} not found, creating basic structure")
            self._create_basic_structure(project_path)
        
        # Create project-specific files
        self._create_readme(project_path, name, description, category)
        self._create_gitignore(project_path, template)
        self._create_claude_md(project_path, name, category)
        
        # Initialize git
        os.chdir(project_path)
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', f'feat: initial {name} project setup'], check=True)
        
        print(f"✅ Project {name} created successfully!")
        print(f"📍 Location: {project_path}")
        print(f"🔗 Next: cd \"{project_path}\"")
        
        return str(project_path)
    
    def _create_basic_structure(self, project_path: Path):
        """Create basic project structure"""
        dirs = ['src', 'tests', 'docs', 'config']
        for dir_name in dirs:
            (project_path / dir_name).mkdir(exist_ok=True)
            (project_path / dir_name / '.gitkeep').touch()
    
    def _create_readme(self, project_path: Path, name: str, description: str, category: str):
        """Create README.md file"""
        readme_content = f"""# {name.replace('-', ' ').title()}

{description or 'Project description'}

## 🎯 Overview

[Describe what this project does]

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- [Other requirements]

### Installation
```bash
git clone <repository-url>
cd {name}
pip install -r requirements.txt
```

### Usage
```bash
# Basic usage example
python src/main.py
```

## 📁 Project Structure

```
{name}/
├── src/                 # Source code
├── tests/               # Test files
├── docs/                # Documentation
├── config/              # Configuration files
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## 🛠️ Development

### Setup Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running Tests
```bash
pytest tests/
```

### Code Quality
```bash
# Format code
black src/ tests/

# Check types
mypy src/

# Lint code
flake8 src/ tests/
```

## 📊 Status

- 🔄 **Status**: In Development
- 📋 **Category**: {category}
- 🏗️ **Template**: Created from project template
- 📅 **Created**: {datetime.date.today().isoformat()}

## 🤝 Contributing

This is a personal project. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

Private project - All rights reserved.

---

*Created with Claude Code project template*  
*Last Updated: {datetime.date.today().isoformat()}*
"""
        
        with open(project_path / 'README.md', 'w') as f:
            f.write(readme_content)
    
    def _create_gitignore(self, project_path: Path, template: str):
        """Create .gitignore file based on template type"""
        
        base_ignore = """# Environment & Secrets
.env
.env.*
*.pem
*.key
api_keys/
secrets/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
venv/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
logs/
*.log

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
coverage.xml

# Data files
data/
*.db
*.sqlite
*.csv
temp/
tmp/
"""
        
        template_specific = {
            'web-app': """
# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Build outputs
dist/
build/
.next/
""",
            'ml-project': """
# ML Models
models/
*.pkl
*.model
*.h5
*.pt
*.pth

# Jupyter
.ipynb_checkpoints/
*.ipynb

# Data
datasets/
*.parquet
""",
            'cli-tool': """
# Binaries
bin/
*.exe
""",
            'mcp-server': """
# MCP specific
.mcp/
mcp-logs/
"""
        }
        
        gitignore_content = base_ignore + template_specific.get(template, "")
        
        with open(project_path / '.gitignore', 'w') as f:
            f.write(gitignore_content)
    
    def _create_claude_md(self, project_path: Path, name: str, category: str):
        """Create project-specific CLAUDE.md"""
        claude_content = f"""# {name} - Claude Code Configuration

## Project-Specific Settings

This project inherits from the main Claude configuration and adds project-specific customizations.

### Project Info
- **Name**: {name}
- **Category**: {category}
- **Created**: {datetime.date.today().isoformat()}
- **Template**: Auto-generated

### Development Workflow
- Use `/safe-commit` for quality-checked commits
- Follow conventional commit format
- Test before committing
- Document changes in README

### Project-Specific Commands
```bash
# Quick setup
./setup.sh

# Run tests
./test.sh

# Deploy/build
./deploy.sh
```

### Dependencies
- Inherit from main claude-config
- Project-specific dependencies in requirements.txt

### Notes
- Add project-specific development notes here
- Link to related projects
- Document any special setup requirements

---

*Inherits from: ~/claude-config/CLAUDE.md*  
*Last Updated: {datetime.date.today().isoformat()}*
"""
        
        with open(project_path / 'CLAUDE.md', 'w') as f:
            f.write(claude_content)
    
    def list_templates(self):
        """List available templates"""
        if not self.templates_path.exists():
            print("No templates directory found")
            return
        
        templates = [d.name for d in self.templates_path.iterdir() if d.is_dir()]
        if not templates:
            print("No templates available")
            return
        
        print("📋 Available Templates:")
        for template in sorted(templates):
            print(f"  - {template}")
    
    def list_categories(self):
        """List available categories"""
        print("📁 Available Categories:")
        for category, description in self.categories.items():
            print(f"  - {category}: {description}")

def main():
    parser = argparse.ArgumentParser(description='Create new project from template')
    parser.add_argument('name', help='Project name (kebab-case)')
    parser.add_argument('category', choices=['claude-tools', 'automation-tools', 'ml-projects'],
                       help='Project category')
    parser.add_argument('--template', default='basic', 
                       help='Template to use (default: basic)')
    parser.add_argument('--description', default='',
                       help='Project description')
    parser.add_argument('--list-templates', action='store_true',
                       help='List available templates')
    parser.add_argument('--list-categories', action='store_true', 
                       help='List available categories')
    
    args = parser.parse_args()
    
    creator = ProjectCreator()
    
    if args.list_templates:
        creator.list_templates()
        return
    
    if args.list_categories:
        creator.list_categories()
        return
    
    try:
        project_path = creator.create_project(
            args.name, 
            args.category, 
            args.template,
            args.description
        )
        print(f"\\n🎉 Success! Project created at: {project_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())