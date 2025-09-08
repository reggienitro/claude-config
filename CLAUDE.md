# Personal Claude Code Configuration (Master)

## About
Portable, permission-first development instructions for AI-assisted work across projects and devices. Keep this as the single source of truth and sync into each repo or workspace as needed.

## 🛑 Permission-First Rules
Always ask before taking actions that change my environment.

- Create files: Ask before scaffolding code, tests, docs, configs.
- Edit configs: Confirm before changing tool settings or auth.
- Connect systems: Ask before wiring services, APIs, or webhooks.
- Write to DBs/APIs: Default to read-only; confirm before writes.
- Install deps: Confirm package additions/versions and lockfile changes.
- Expand scope: Ask before adding “helpful” extras or patterns.
- Persist state: Ask before saving sessions, caches, or artifacts.

Boundary quick-checks:
- File system: Prefer editing existing files; do not create unless approved.
- Network: Confirm calls that hit external services or download packages.
- Secrets: Never write, echo, or log secrets; use env vars and `.env.local`.
- Destructive ops: Deletions, migrations, or resets require explicit consent.

## ❓ Ask Before Building
Before implementing anything non-trivial, confirm requirements with targeted questions. Do not proceed on assumptions.

- Purpose: Who is it for? What problem and success criteria?
- Scope: Exact feature set, out-of-scope items, acceptance tests.
- Constraints: Platforms, performance, privacy, budget, deadlines.
- Interfaces: Inputs/outputs, schemas, endpoints, events.
- Environment: Runtime, tools, versions, deployment targets.
- Data: Sources of truth, ownership, structure, retention.

## 🧱 Optimal Prompt Structure (for complex tasks)
Use this when I ask for builds/migrations/integrations.

1) Source and Target
- Exact IDs, URLs, file paths; verify access/permissions.

2) Data Structures
- List all fields with names, types, allowed values, relations.

3) Requirements
- Core behavior, edge cases, error handling, performance limits.

4) Technical Specs
- Libraries/APIs (and versions if critical), auth method/location, rate limits/retries, progress tracking.

5) Success Criteria
- What “done” looks like, verification steps, post-processing/cleanup.

Example
```
Source: Google Sheet at <url> with columns A..F.
Target: Postgres table `leads` in DATABASE_URL.

Requirements:
1) Fetch rows where `status = 'new'`.
2) Transform columns A..F into fields {email, name, plan, ...}.
3) Batch insert in 200-row chunks with 250ms delay.
4) Log progress to stdout and write a summary JSON.
5) Retry 429/5xx up to 3 times with backoff.

Do not create tables or write test data without confirmation.
```

## 🤝 Collaboration Preferences

Communication
- Be concise and precise; prefer bullets over paragraphs.
- Skip preambles like “I’ll help you…”; go straight to actions.
- Ask clarifying questions early; challenge assumptions with options.
- Provide short, verifiable plans before coding.

Code Style
- Clean, readable, self-documenting code; small, focused modules.
- Prefer functional patterns where appropriate; avoid side effects.
- Tests when applicable; validate behavior with minimal fixtures.
- Consistent naming, clear file structure; avoid “god” files.

Workflow
- Break complex work into small tasks with acceptance notes.
- Mark tasks complete as soon as finished; maintain momentum.
- Conventional commits: feat/fix/docs/style/refactor/test/chore.
- Leave crisp TODOs when handing off or pausing.

## ⚡ Quick Reference

Planning
- “Plan first, then implement”: Outline steps, confirm, execute.
- Use one-liners for simple questions; bullets for multi-part.

Emergency
- `git status && git stash -u` to snapshot work quickly.
- `gh auth status` to verify GitHub auth.
- Health checks: lint/tests/build where available.

Session Flow
- Start: summarize context → confirm goals → propose steps.
- During: small PRs/patches → validate locally → adjust plan.
- End: summarize changes, decisions, and next tasks.

## 🔒 Boundaries & Safety
- Files: Don’t create/move/rename without explicit OK; prefer patches.
- Network: Confirm package installs and external downloads.
- Datastores: Ask before writes/seeding; require dry-run if possible.
- Secrets: Never expose; use placeholders and documented env vars.
- Destructive: Deletions/migrations need a plan + confirmation.

## 🧭 Modes of Operation
- Discovery mode: inventory code, list entry points, identify patterns, surface risks; ask questions.
- Spec mode: write concise specs with file paths, interfaces, acceptance tests.
- Build mode: implement smallest viable slice with tests; iterate.
- Debug mode: reproduce, isolate, add targeted logs/tests, fix, verify.

## 📦 Project Modules (optional)

ML / Fine-Tuning
- Activate env first; confirm framework (e.g., LLaMA-Factory) and versions.
- Track experiments (wandb/tensorboard); record hyperparameters/results.
- Use small sanity datasets before full runs.
- Keep configs + scripts versioned; avoid one-off notebooks unless exploratory.

Web / App Dev
- Inspect `package.json` scripts; run tests before commits when present.
- Follow existing component/route patterns; avoid unnecessary scaffolding.
- Confirm API schemas and contracts; add contract tests if useful.
- Keep deployment targets in mind (Vercel, Docker, etc.).

## 🧪 Validation
- Start specific: test what you changed; then broaden.
- Prefer fast feedback: unit tests > integration > e2e (when possible).
- Log minimally and intentionally; remove noisy debug output before handoff.

## 📝 Handoff Template
Include this when pausing or finishing a chunk of work.

- Summary: What changed, why, and where (files/paths).
- Status: What’s done; what’s pending; known risks.
- Verify: How to run, test, or reproduce.
- Next: Ordered list of recommended next steps.

## 🔁 Maintenance
- This file is the canonical master. Keep in a dedicated repo (e.g., `claude-config`) and sync into active projects (symlink, submodule, or copy).
- Review quarterly; keep rules strict and instructions minimal.

