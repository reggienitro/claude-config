# /safe-commit

Create a comprehensive git commit with automated quality checks.

## Workflow:
1. **Run git status** to show current changes
2. **Check for tests** - ensure test files exist for modified code
3. **Run linting/tests** if package.json or requirements exist
4. **Generate conventional commit message** (feat/fix/docs/style/refactor/test/chore)
5. **Create commit** with proper format including Claude signature
6. **Update task status** if task-master is available

## Usage:
```bash
/safe-commit "implement user authentication"
/safe-commit "fix navigation bug in header component"
/safe-commit "add documentation for API endpoints"
```

## Pre-commit Checks:
- [ ] All files staged appropriately
- [ ] Tests exist for new functionality
- [ ] Linting passes (if configured)
- [ ] No debug code or console.logs
- [ ] Conventional commit format followed
- [ ] Task status updated (if applicable)

## Example Output:
```bash
git add -A
npm run lint  # if package.json exists
npm test      # if tests configured
git commit -m "feat: implement user authentication

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```