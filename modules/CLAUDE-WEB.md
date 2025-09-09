# CLAUDE-WEB: Web Development Module
> Loaded when package.json detected

## 🌐 Web Architecture Context
```yaml
framework_detection:
  next: "next.config.js"
  react: "React in dependencies"
  vue: "vue in dependencies"
  
build_tools:
  bundler: "auto-detect from scripts"
  test_runner: "auto-detect from scripts"
  formatter: "prettier if available"
  
conventions:
  components: "./components or ./src/components"
  styles: "CSS modules or Tailwind"
  state: "Context or Redux if found"
```

## 📋 Web Development Prerequisites
```bash
# Before web development:
echo "=== WEB DEV PREREQUISITES ==="

# □ Package manager detected?
if [[ -f package-lock.json ]]; then
  echo "✓ Using npm"
elif [[ -f yarn.lock ]]; then  
  echo "✓ Using yarn"
else
  echo "⚠️ No lock file - using npm"
fi

# □ Dependencies installed?
[[ -d node_modules ]] && echo "✓ Dependencies present" || echo "✗ Run npm install"

# □ Scripts available?
[[ -f package.json ]] && grep -q '"dev"' package.json && echo "✓ Dev script found" || echo "✗ No dev script"

# □ Build passing?
npm run build --dry-run 2>/dev/null && echo "✓ Build configured" || echo "⚠️ Build not configured"
```

## 🚫 Web Development Non-Goals
**NEVER without permission:**
- ❌ Upgrade major versions
- ❌ Add new frameworks
- ❌ Modify build configuration
- ❌ Change routing structure
- ❌ Add analytics/tracking
- ❌ Deploy to production

## 🔄 Web Pattern Discovery

### Component Patterns
```javascript
// DISCOVERED PATTERN: Check existing components first
// 1. Find similar component
// 2. Copy structure
// 3. Modify for new use
// 4. Follow same test pattern
```

### State Management Patterns
```javascript
// DISCOVERED PATTERN: Prefer existing state solution
// - Context API if already used
// - Props if simple
// - URL state for navigation
// - Local storage sparingly
```

## 🎯 Web Success Criteria
- ✅ No console errors
- ✅ Responsive design works
- ✅ Accessibility basics met
- ✅ Performance budget maintained
- ✅ Tests pass
- ✅ Linting clean

## 🔧 Web Development Handoff
```markdown
## WEB SESSION HANDOFF
### Dev Server State
- Running on: http://localhost:[port]
- Hot reload: [working/broken]
- Last error: [error message]

### Component Work
- Modified: [components list]
- New routes: [routes list]
- State changes: [what changed]

### Recovery Commands
```bash
npm install
npm run dev
# Open http://localhost:3000
```
```

---
*Module: WEB | Auto-loads when package.json found*