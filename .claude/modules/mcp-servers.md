# MCP Servers Configuration

## Installed Tools & Capabilities

### MCP Servers Available (15 Total)

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

#### Productivity & Calendar
- **apple-calendar**: Natural language Apple Calendar management for macOS
- **outlook-mcp**: Comprehensive Microsoft Outlook and Teams integration (75+ tools)

Additional servers can be installed via `mcp-installer`

## MCP Server API Keys

All API keys stored securely in `~/.config/api-keys/.env`:
- **BEE_API_TOKEN**: Bee.computer lifelogging access
- **GITHUB_PERSONAL_ACCESS_TOKEN**: GitHub repository operations
- **SUPABASE_URL & SUPABASE_KEY**: Database operations and cloud sync
- **SUPABASE_PROJECT_REF**: Project reference for MCP server connection
- **EXA_API_KEY**: Exa semantic search capabilities

Source from environment file for security

## Quick MCP Commands

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

## Adding New MCP Servers Protocol

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

## MCP Server Documentation

Detailed documentation for each server available at:
`~/AI projects/mcp-servers/documentation/individual-servers/`