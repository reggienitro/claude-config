#!/usr/bin/env python3
"""
Project Creation Script with Enhanced Type Safety
Creates new projects from templates following organization standards
"""

import os
import shutil
import argparse
import subprocess
import datetime
import json
from pathlib import Path
from typing import Dict, List, Optional, Union, Tuple, Any
from dataclasses import dataclass
from enum import Enum

class ProjectCategory(Enum):
    """Valid project categories"""
    CLAUDE_TOOLS = 'claude-tools'
    AUTOMATION_TOOLS = 'automation-tools'
    ML_PROJECTS = 'ml-projects'

@dataclass
class ProjectConfig:
    """Configuration for a new project"""
    name: str
    category: ProjectCategory
    template: str
    description: str = ""
    git_init: bool = True
    create_readme: bool = True

class ProjectCreator:
    """Create new projects from templates with type safety"""
    
    def __init__(self) -> None:
        self.base_path: Path = Path.home() / "AI projects"
        self.templates_path: Path = Path.home() / "claude-config" / ".claude" / "templates"
        self.categories: Dict[str, str] = {
            ProjectCategory.CLAUDE_TOOLS.value: 'Claude Code utilities and extensions',
            ProjectCategory.AUTOMATION_TOOLS.value: 'Automation and productivity tools', 
            ProjectCategory.ML_PROJECTS.value: 'Machine learning and AI projects'
        }
        
    def validate_category(self, category: str) -> ProjectCategory:
        """Validate and convert string to ProjectCategory enum"""
        try:
            return ProjectCategory(category)
        except ValueError:
            valid_categories = [c.value for c in ProjectCategory]
            raise ValueError(f"Category must be one of: {valid_categories}")
    
    def create_project(
        self, 
        name: str, 
        category: str, 
        template: str, 
        description: str = ""
    ) -> Path:
        """Create a new project from template with type validation"""
        
        # Validate and convert category
        category_enum: ProjectCategory = self.validate_category(category)
        
        # Create project path
        project_path: Path = self.base_path / category_enum.value / name
        
        if project_path.exists():
            raise ValueError(f"Project already exists: {project_path}")
        
        print(f"🚀 Creating project: {name}")
        print(f"📁 Category: {category_enum.value}")
        print(f"📋 Template: {template}")
        print(f"📍 Location: {project_path}")
        
        # Create directory structure
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Copy template files if template exists
        template_path: Path = self.templates_path / template
        if template_path.exists():
            self._copy_template(template_path, project_path)
        else:
            self._create_default_structure(project_path)
        
        # Create CLAUDE.md with project info
        self._create_claude_md(project_path, name, category_enum, description)
        
        # Initialize git if requested
        self._init_git(project_path)
        
        # Update registry
        self._update_registry(name, category_enum, project_path)
        
        print(f"✅ Project created successfully!")
        return project_path
    
    def _copy_template(self, template_path: Path, project_path: Path) -> None:
        """Copy template files to project directory"""
        for item in template_path.iterdir():
            if item.name == '.git':
                continue
            
            dest: Path = project_path / item.name
            if item.is_dir():
                shutil.copytree(item, dest, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest)
    
    def _create_default_structure(self, project_path: Path) -> None:
        """Create default project structure"""
        directories: List[str] = ['src', 'tests', 'docs', 'configs']
        for dir_name in directories:
            (project_path / dir_name).mkdir(exist_ok=True)
        
        # Create basic README
        readme_content: str = f"""# {project_path.name}

## Overview
{project_path.name} project

## Setup
```bash
# Installation instructions here
```

## Usage
```bash
# Usage examples here
```

## Development
Created: {datetime.datetime.now().strftime('%Y-%m-%d')}
"""
        (project_path / 'README.md').write_text(readme_content)
    
    def _create_claude_md(
        self, 
        project_path: Path, 
        name: str, 
        category: ProjectCategory, 
        description: str
    ) -> None:
        """Create project-specific CLAUDE.md file"""
        claude_content: str = f"""# Project: {name}

## Category
{category.value}

## Description
{description or f"A {category.value} project"}

## Project Structure
```
{name}/
├── src/         # Source code
├── tests/       # Test files
├── docs/        # Documentation
└── configs/     # Configuration files
```

## Development Guidelines
- Follow Python type hints for all functions
- Write comprehensive tests
- Document all public APIs
- Use semantic versioning

## Status
- Created: {datetime.datetime.now().strftime('%Y-%m-%d')}
- Phase: PLANNING
"""
        (project_path / 'CLAUDE.md').write_text(claude_content)
    
    def _init_git(self, project_path: Path) -> None:
        """Initialize git repository"""
        try:
            subprocess.run(['git', 'init'], cwd=project_path, capture_output=True)
            
            # Create .gitignore
            gitignore_content: str = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv
.env

# IDE
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# Project
*.log
dist/
build/
*.egg-info/
.pytest_cache/
.mypy_cache/
"""
            (project_path / '.gitignore').write_text(gitignore_content)
            
            subprocess.run(['git', 'add', '.'], cwd=project_path, capture_output=True)
            subprocess.run(
                ['git', 'commit', '-m', 'Initial commit'], 
                cwd=project_path, 
                capture_output=True
            )
        except Exception as e:
            print(f"⚠️  Git initialization failed: {e}")
    
    def _update_registry(
        self, 
        name: str, 
        category: ProjectCategory, 
        project_path: Path
    ) -> None:
        """Update project registry"""
        registry_file: Path = self.base_path / 'project-registry.json'
        
        registry: Dict[str, Any] = {}
        if registry_file.exists():
            registry = json.loads(registry_file.read_text())
        
        registry[name] = {
            'category': category.value,
            'path': str(project_path),
            'created': datetime.datetime.now().isoformat(),
            'status': 'active'
        }
        
        registry_file.write_text(json.dumps(registry, indent=2))
    
    def list_projects(self) -> Dict[str, List[str]]:
        """List all existing projects by category"""
        projects: Dict[str, List[str]] = {
            category.value: [] for category in ProjectCategory
        }
        
        for category in ProjectCategory:
            category_path: Path = self.base_path / category.value
            if category_path.exists():
                projects[category.value] = [
                    p.name for p in category_path.iterdir() if p.is_dir()
                ]
        
        return projects
    
    def get_project_info(self, name: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific project"""
        registry_file: Path = self.base_path / 'project-registry.json'
        
        if not registry_file.exists():
            return None
        
        registry: Dict[str, Any] = json.loads(registry_file.read_text())
        return registry.get(name)

def main() -> None:
    """Main entry point with type-safe argument parsing"""
    parser = argparse.ArgumentParser(
        description='Create new projects with enhanced type safety'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new project')
    create_parser.add_argument('name', type=str, help='Project name')
    create_parser.add_argument(
        '--category', 
        type=str,
        choices=[c.value for c in ProjectCategory],
        required=True,
        help='Project category'
    )
    create_parser.add_argument(
        '--template', 
        type=str,
        default='default',
        help='Template to use'
    )
    create_parser.add_argument(
        '--description', 
        type=str,
        default='',
        help='Project description'
    )
    
    # List command
    subparsers.add_parser('list', help='List all projects')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Get project information')
    info_parser.add_argument('name', type=str, help='Project name')
    
    args = parser.parse_args()
    
    creator = ProjectCreator()
    
    if args.command == 'create':
        try:
            path: Path = creator.create_project(
                args.name,
                args.category,
                args.template,
                args.description
            )
            print(f"\n📂 Project created at: {path}")
        except Exception as e:
            print(f"❌ Error: {e}")
            exit(1)
    
    elif args.command == 'list':
        projects: Dict[str, List[str]] = creator.list_projects()
        for category, project_list in projects.items():
            if project_list:
                print(f"\n📁 {category}:")
                for project in project_list:
                    print(f"  • {project}")
    
    elif args.command == 'info':
        info: Optional[Dict[str, Any]] = creator.get_project_info(args.name)
        if info:
            print(f"\n📋 Project: {args.name}")
            for key, value in info.items():
                print(f"  {key}: {value}")
        else:
            print(f"❌ Project not found: {args.name}")
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()