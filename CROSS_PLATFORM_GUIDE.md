# Using claude-config Across Platforms

Purpose: Make this configuration predictable in different hosts (CLI agents, Claude Desktop, local shells, CI).

What varies by host:
- Preambles: Some hosts require short preambles before tool calls.
- Commits: Some hosts restrict `git commit` without approval.
- Custom Commands: `/...` commands are advisory unless implemented by the host.
- Hooks: `.claude/hooks.json` does not run unless a runner integrates it.
- MCP Servers: Online Mode required; if unavailable, pause and request guidance.
- Paths: Machine-specific paths need adjustment.

Baseline behavior (always okay):
- Ask clarifying questions before coding; avoid assumptions.
- Keep responses concise and structured.
- Plan → implement; verify with tests/docs when applicable.
- Treat custom commands and hooks as guidance when no runner exists.

MCP unavailability handling:
1. Pause and notify that MCP/runner is unavailable; do not continue offline.
2. Collect minimal diagnostics (versions, auth status) to aid resolution.
3. Resume once runner and required servers are available and approved.

Integration options:
- Shell scripts under `scripts/workflows/` that implement each command.
- Claude Desktop custom commands mapped to the markdown specs.
- CI jobs (GitHub Actions) invoking these flows on PRs.

See also:
- CLAUDE.md → Platform Compatibility
- .claude/settings.json → policyCompatibility
- .claude/commands/README.md
