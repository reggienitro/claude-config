# Claude Configuration Changelog

## [2.1] - 2025-08-17 - Post-Reorganization Update

### Added
- Complete documentation for all 12 MCP servers:
  - mcp-tts (text-to-speech)
  - bee (AI framework)
  - filesystem (file operations)
  - web-search (web search capabilities)
- New project organization module (`project-organization.md`)
- Comprehensive filing standards and directory structure
- Project backlog system

### Changed
- Updated version to 2.1 (Post-Reorganization)
- All MCP servers now fully documented
- Confirmed 12 active MCP servers with complete documentation

### Reorganized
- **model-finetuning-project**: Cleaned from 117 files to 10 core files
- **bee-supabase-integration**: Moved to `~/AI projects/automation-tools/` (72+ files)
- **article-to-audio**: Confirmed in `~/AI projects/claude-tools/`
- **health-integration**: Moved to `~/AI projects/automation-tools/`

### Project Structure Now Follows
- Clear categorization: claude-tools, ml-projects, automation-tools
- Maximum 200 lines per file guideline
- Proper separation of concerns
- Consistent naming conventions

## [2.0] - 2025-08-17 - Modular Configuration

### Added
- Modular configuration system with importable modules
- Separate modules for:
  - workflow-patterns.md
  - mcp-servers.md
  - project-templates.md
  - project-organization.md

### Changed
- Converted monolithic CLAUDE.md to modular structure
- Improved maintainability and organization

## [1.0] - 2025-08-01 - Initial Configuration

### Initial Setup
- Base configuration structure
- MCP server integration
- Custom commands
- Development workflow patterns

---

*This changelog follows [Keep a Changelog](https://keepachangelog.com/) format*