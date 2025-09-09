# Claude Configuration v2.0 - Enhanced
> This configuration uses the new modular system with progressive disclosure

<!-- Core configuration is in core/CLAUDE-CORE.md -->
<!-- Modules auto-load based on project context -->

## 🎯 Personal Configuration Overrides
<!-- Your personal preferences that override core settings -->

### MCP Servers Available

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

#### Productivity
- **apple-calendar**: Natural language Apple Calendar management for macOS
- **outlook-mcp**: Comprehensive Microsoft Outlook and Teams integration (75+ tools)
- **outlook-calendar-mcp**: Windows-specific Outlook Calendar integration

#### AI & Knowledge Management
- **beemcp**: Bee.computer lifelogging data access and integration
- **memory**: Persistent context and knowledge storage across sessions

Additional servers can be installed via `mcp-installer`

### Development Tools
- Git and GitHub CLI (`gh`) for version control
- Multiple language environments (Python, Node.js, etc.)
- Testing frameworks appropriate to each project
- Docker for containerization when needed
- **dev-env-health-check** (`dehc`): Environment validation tool
  - Validates MCP servers, API keys, databases
  - Multiple output modes (quick/detailed/comprehensive/JSON)
  - Built-in automation and daily monitoring
  - GitHub: https://github.com/reggienitro/dev-env-health-check

## Project-Specific Instructions
   - Add server to "MCP Servers Available" section above
   - Include category, description, and key capabilities
   - Note any API key requirements
   - Update total count and version number

This ensures all MCP servers are properly documented and tracked in the centralized system.

---

Last updated: 2025-08-13

<!-- Additional configuration loaded from: -->
<!-- - core/CLAUDE-CORE.md (always) -->
<!-- - modules/* (when relevant) -->
