# /quick-spec

Rapidly generate a project specification from brief description.

## Purpose:
Transform a simple project idea into a structured specification that other AIs can implement from. Uses progressive questioning to build comprehensive requirements without overwhelming the user.

## Usage:
```bash
/quick-spec "build a todo app with user accounts"
/quick-spec "create API for weather data with caching"
/quick-spec "dashboard for monitoring system metrics"
```

## Workflow:
1. **Analyze the input** - identify project type and core functionality
2. **Ask 3-5 key questions** - essential clarifications only
3. **Generate specification** - structured format with:
   - User stories
   - Technical requirements
   - API endpoints (if applicable)
   - Database schema (if applicable)
   - Deployment considerations
4. **Create implementation roadmap** - prioritized task breakdown

## Question Framework:
Instead of asking everything at once, focus on:
- **Core functionality**: What's the main user workflow?
- **Target platform**: Web, mobile, desktop, API?
- **User management**: Authentication needed? User types?
- **Data persistence**: What data needs to be stored?
- **Unique constraints**: Performance, security, integration requirements?

## Output Format:
```markdown
# Project Specification: [Project Name]

## Overview
Brief description and goals

## User Stories
- As a [user type], I want [functionality] so that [benefit]

## Technical Requirements
- Frontend: [React/Vue/etc]
- Backend: [Node.js/Python/etc]
- Database: [PostgreSQL/MongoDB/etc]
- Authentication: [method]
- Deployment: [platform]

## API Endpoints (if applicable)
- GET /api/endpoint - description
- POST /api/endpoint - description

## Database Schema (if applicable)
Tables and relationships

## Implementation Phases
1. Phase 1: Core functionality
2. Phase 2: User management
3. Phase 3: Advanced features

## Definition of Done
- [ ] Functional requirements met
- [ ] Tests written and passing
- [ ] Documentation complete
- [ ] Deployed and accessible
```

## Benefits:
- **Speed**: Get from idea to implementable spec in minutes
- **Completeness**: Ensures nothing critical is missed
- **Transferability**: Other AIs can implement from the spec
- **Flexibility**: Easy to modify and iterate