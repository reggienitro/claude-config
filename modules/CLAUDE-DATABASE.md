# CLAUDE-DATABASE: Database Operations Module
> Loaded when database work detected

## 🗄️ Database Architecture Context
```yaml
primary_database: "supabase"
local_testing: "sqlite"
orm_preference: "none - raw SQL preferred"
migration_tool: "manual versioned scripts"

connection_sources:
  production: "~/.config/api-keys/.env"
  testing: ".env.test"
  
patterns:
  schema_location: "./schemas/"
  migration_location: "./migrations/"
  seed_location: "./seeds/"
```

## 📋 Database Prerequisites Checklist
```bash
# Before ANY database operation:
echo "=== DATABASE PREREQUISITES ==="

# □ Environment variables loaded?
[[ -n "$SUPABASE_URL" ]] && echo "✓ Supabase URL found" || echo "✗ Missing SUPABASE_URL"
[[ -n "$SUPABASE_KEY" ]] && echo "✓ Supabase key found" || echo "✗ Missing SUPABASE_KEY"

# □ Can connect?
python3 -c "from supabase import create_client; print('✓ Connection test passed')" 2>/dev/null || echo "✗ Connection failed"

# □ Schema current?
[[ -f schemas/current.sql ]] && echo "✓ Schema file exists" || echo "✗ No schema file"

# □ Backup exists?
ls -la backups/*.sql 2>/dev/null | tail -1 || echo "⚠️ No recent backups"
```

## 🚫 Database Non-Goals
**NEVER without explicit permission:**
- ❌ DROP any table or database
- ❌ TRUNCATE production tables
- ❌ Modify schema in production
- ❌ Share connection strings
- ❌ Run migrations without backup
- ❌ Access production without announcement

## 🔄 Database Operation Patterns

### Pattern: Safe Schema Modification
```python
# DISCOVERED PATTERN: Always test locally first
# 1. Create schema change script
# 2. Test on local SQLite
# 3. Review with EXPLAIN
# 4. Apply to Supabase
# 5. Verify with health check
```

### Pattern: Data Migration Flow
```bash
# DISCOVERED PATTERN: Backup-Modify-Verify
backup_current()
apply_migration()
verify_integrity()
checkpoint_or_rollback()
```

## 🎯 Database Success Criteria
- ✅ All queries EXPLAIN-ed before execution
- ✅ Transactions used for multi-step operations
- ✅ Foreign keys maintained
- ✅ Indexes verified for performance
- ✅ No N+1 query problems
- ✅ Connection pools managed

## 🔧 Database Handoff Template
```markdown
## DATABASE SESSION HANDOFF
### Connection State
- Database: [name]
- Schema version: [version]
- Last migration: [file]

### Pending Operations
- [ ] Uncommitted transaction: [details]
- [ ] Schema changes staged: [list]
- [ ] Data verification needed: [tables]

### Recovery SQL
```sql
-- Verify state
SELECT version FROM schema_versions ORDER BY id DESC LIMIT 1;
-- Check integrity  
SELECT COUNT(*) FROM information_schema.tables;
```
```

---
*Module: DATABASE | Auto-loads when .env contains DB vars*