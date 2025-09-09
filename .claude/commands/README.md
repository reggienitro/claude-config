# Custom Commands Guide

These commands are specifications, not automatically executable in every environment. They require a host runner (e.g., Claude Desktop custom commands, a shell wrapper, or CI scripts).

Commands defined:
- /safe-commit "message": Quality-checked commits
- /status-check: System verification
- /quick-spec "idea": Rapid project specification
- /morning-standup: Session initialization
- /end-of-day: Session wrap-up

How to use across platforms:
- No runner available: Treat these as documented workflows; execute equivalent steps manually.
- With a runner: Map each command to a script or workflow. Example:
  - /safe-commit → runs tests, lint, doc checks, then `git commit` with message.
  - /status-check → runs environment and repo checks; prints summary.

Recommended mapping (example):
- `scripts/workflows/safe_commit.sh`
- `scripts/workflows/status_check.sh`
- `scripts/workflows/morning_standup.sh`
- `scripts/workflows/end_of_day.sh`

Note: See CLAUDE.md → Platform Compatibility for behavior adaptations (preambles, commit policy, MCP availability).

