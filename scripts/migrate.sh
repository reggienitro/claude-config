#!/bin/bash
# Claude Config v2.0 Migration Script
# Helps migrate from v1.x to v2.0 modular system

set -euo pipefail
IFS=$'\n\t'

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging
log() { echo -e "${GREEN}[✓]${NC} $1"; }
warn() { echo -e "${YELLOW}[⚠]${NC} $1"; }
error() { echo -e "${RED}[✗]${NC} $1"; exit 1; }
info() { echo -e "${BLUE}[ℹ]${NC} $1"; }

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
BACKUP_DIR="$REPO_DIR/backups/$(date +%Y%m%d_%H%M%S)"

# Header
echo ""
echo "═══════════════════════════════════════════════════════"
echo "  Claude Config v2.0 Migration Tool"
echo "  Progressive Disclosure Configuration System"
echo "═══════════════════════════════════════════════════════"
echo ""

# Check if we're in the right directory
if [[ ! -f "$REPO_DIR/CLAUDE.md" ]]; then
    error "CLAUDE.md not found. Please run from claude-config directory."
fi

# Create backup directory
mkdir -p "$BACKUP_DIR"
log "Created backup directory: $BACKUP_DIR"

# Step 1: Backup existing configuration
info "Step 1: Backing up existing configuration..."
cp "$REPO_DIR/CLAUDE.md" "$BACKUP_DIR/CLAUDE.md.backup"
[[ -f ~/CLAUDE.md ]] && cp ~/CLAUDE.md "$BACKUP_DIR/HOME_CLAUDE.md.backup"
log "Backed up existing CLAUDE.md files"

# Step 2: Check for existing v2.0 structure
info "Step 2: Checking for existing v2.0 structure..."
if [[ -d "$REPO_DIR/core" ]] && [[ -d "$REPO_DIR/modules" ]]; then
    log "v2.0 structure already exists"
else
    warn "v2.0 structure not found, creating..."
    mkdir -p "$REPO_DIR/core" "$REPO_DIR/modules" "$REPO_DIR/scripts" "$REPO_DIR/docs"
    log "Created v2.0 directory structure"
fi

# Step 3: Analyze current CLAUDE.md for sections to preserve
info "Step 3: Analyzing your current configuration..."
SECTIONS_FOUND=""
[[ $(grep -c "MCP Servers" "$REPO_DIR/CLAUDE.md" 2>/dev/null || echo 0) -gt 0 ]] && SECTIONS_FOUND="${SECTIONS_FOUND}MCP_SERVERS "
[[ $(grep -c "Spec-Driven" "$REPO_DIR/CLAUDE.md" 2>/dev/null || echo 0) -gt 0 ]] && SECTIONS_FOUND="${SECTIONS_FOUND}SPEC_DRIVEN "
[[ $(grep -c "Permission" "$REPO_DIR/CLAUDE.md" 2>/dev/null || echo 0) -gt 0 ]] && SECTIONS_FOUND="${SECTIONS_FOUND}PERMISSIONS "

if [[ -n "$SECTIONS_FOUND" ]]; then
    log "Found sections to preserve: $SECTIONS_FOUND"
fi

# Step 4: Create enhanced CLAUDE.md
info "Step 4: Creating enhanced configuration..."
cat > "$REPO_DIR/CLAUDE-ENHANCED.md" << 'EOF'
# Claude Configuration v2.0 - Enhanced
> This configuration uses the new modular system with progressive disclosure

<!-- Core configuration is in core/CLAUDE-CORE.md -->
<!-- Modules auto-load based on project context -->

## 🎯 Personal Configuration Overrides
<!-- Your personal preferences that override core settings -->

EOF

# Preserve personal sections from original CLAUDE.md
if [[ -n "$SECTIONS_FOUND" ]]; then
    info "Preserving your personal sections..."
    
    # Extract MCP Servers section if it exists
    if [[ "$SECTIONS_FOUND" == *"MCP_SERVERS"* ]]; then
        echo "### MCP Servers Available" >> "$REPO_DIR/CLAUDE-ENHANCED.md"
        sed -n '/MCP Servers Available/,/^##[^#]/p' "$REPO_DIR/CLAUDE.md" | sed '1d;$d' >> "$REPO_DIR/CLAUDE-ENHANCED.md"
        echo "" >> "$REPO_DIR/CLAUDE-ENHANCED.md"
    fi
    
    # Add reference to core
    echo "<!-- Additional configuration loaded from: -->" >> "$REPO_DIR/CLAUDE-ENHANCED.md"
    echo "<!-- - core/CLAUDE-CORE.md (always) -->" >> "$REPO_DIR/CLAUDE-ENHANCED.md"
    echo "<!-- - modules/* (when relevant) -->" >> "$REPO_DIR/CLAUDE-ENHANCED.md"
fi

log "Created CLAUDE-ENHANCED.md with preserved sections"

# Step 5: Offer migration options
echo ""
info "Step 5: Choose migration strategy:"
echo ""
echo "  1) Full Migration - Replace CLAUDE.md with v2.0 system (recommended)"
echo "  2) Preview Only - Keep current setup, just create v2.0 files for review"
echo "  3) Gradual Migration - Add v2.0 sections to existing CLAUDE.md"
echo ""
read -p "Select option (1-3): " MIGRATION_CHOICE

case $MIGRATION_CHOICE in
    1)
        info "Performing full migration..."
        mv "$REPO_DIR/CLAUDE.md" "$REPO_DIR/CLAUDE.md.v1"
        mv "$REPO_DIR/CLAUDE-ENHANCED.md" "$REPO_DIR/CLAUDE.md"
        log "Migration complete! Old config saved as CLAUDE.md.v1"
        ;;
    2)
        info "Preview mode - no changes made to existing files"
        log "Review CLAUDE-ENHANCED.md and modules/ directory"
        ;;
    3)
        info "Adding v2.0 sections to existing CLAUDE.md..."
        echo "" >> "$REPO_DIR/CLAUDE.md"
        echo "# ═══ v2.0 Enhancements Below ═══" >> "$REPO_DIR/CLAUDE.md"
        cat "$REPO_DIR/core/CLAUDE-CORE.md" | sed -n '/Prerequisites Validation Protocol/,/Quick Reference Card/p' >> "$REPO_DIR/CLAUDE.md"
        log "Added core v2.0 sections to existing CLAUDE.md"
        ;;
    *)
        error "Invalid option selected"
        ;;
esac

# Step 6: Set up project detection
info "Step 6: Setting up project detection..."
cat > "$REPO_DIR/scripts/detect-project.sh" << 'DETECT_EOF'
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
DETECT_EOF

chmod +x "$REPO_DIR/scripts/detect-project.sh"
log "Created project detection script"

# Step 7: Final summary
echo ""
echo "═══════════════════════════════════════════════════════"
echo "  Migration Summary"
echo "═══════════════════════════════════════════════════════"
echo ""
log "✅ Backup created in: $BACKUP_DIR"
log "✅ v2.0 structure created:"
echo "    • core/CLAUDE-CORE.md - Base configuration"
echo "    • modules/*.md - Feature-specific modules"
echo "    • scripts/ - Helper scripts"
echo ""

# Next steps
info "Next Steps:"
echo ""
echo "1. Review the new structure:"
echo "   cat core/CLAUDE-CORE.md"
echo ""
echo "2. Test in a project:"
echo "   cd ~/projects/your-project"
echo "   ~/claude-config/scripts/detect-project.sh"
echo ""
echo "3. Commit changes:"
echo "   git add -A"
echo "   git commit -m 'feat: migrate to v2.0 modular system'"
echo "   git push"
echo ""
echo "4. On other devices:"
echo "   git pull"
echo "   ./scripts/migrate.sh"
echo ""

log "Migration tool completed successfully!"
echo ""