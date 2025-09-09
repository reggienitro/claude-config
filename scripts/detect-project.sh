#!/bin/bash
# Detects project type and suggests relevant modules

PROJECT_TYPE=""
[[ -f package.json ]] && PROJECT_TYPE="${PROJECT_TYPE}WEB "
[[ -f requirements.txt ]] && PROJECT_TYPE="${PROJECT_TYPE}ML "
[[ -f docker-compose.yml ]] && PROJECT_TYPE="${PROJECT_TYPE}DOCKER "
[[ -n "$(find . -name "*.sh" 2>/dev/null | head -1)" ]] && PROJECT_TYPE="${PROJECT_TYPE}AUTOMATION "

echo "Detected project types: ${PROJECT_TYPE:-NONE}"

for TYPE in $PROJECT_TYPE; do
    MODULE_FILE="$HOME/claude-config/modules/CLAUDE-${TYPE}.md"
    [[ -f "$MODULE_FILE" ]] && echo "Suggested module: $MODULE_FILE"
done
