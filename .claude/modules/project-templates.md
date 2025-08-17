# Project Templates & Examples

## Project Templates

### Python ML Project
```python
# Standard imports
import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Project structure
project/
├── data/
├── models/
├── notebooks/
├── src/
├── tests/
└── configs/
```

### Web Application
```javascript
// React/Next.js structure
app/
├── components/
├── pages/
├── styles/
├── utils/
├── hooks/
└── tests/
```

### Article-to-Audio Project
```bash
# Authentication workflow
./article2audio-enhanced --signup --email "user@example.com" --display-name "Name"
./article2audio-enhanced --signin --email "user@example.com"
./article2audio-enhanced --user-info

# Convert with cloud sync
./article2audio-enhanced "https://example.com/article" --save --voice christopher

# Test integration
python3 test_integration.py
python3 test_basic_supabase.py
```

#### Audio Project Structure
```
claude-tools/article-to-audio-extension/
├── article2audio-enhanced         # Main conversion tool
├── enhanced-server.py            # Backend server
├── supabase_integration.py       # Database integration
├── test-files/                   # Audio test samples
└── tests/                        # Integration tests
```

## Multi-Device Sync

### Repository Structure
```
~/AI projects/
├── claude-tools/          # Custom tools and extensions
├── mcp-servers/           # MCP server configurations
├── scripts/               # Utility and automation scripts
│   ├── database/          # DB management and migrations
│   ├── utilities/         # General utility scripts
│   └── testing/           # Test scripts and verification
├── ml-projects/           # Machine learning projects
└── automation-tools/      # Workflow automation

~/model-finetuning-project/ (Legacy - being reorganized)
├── CLAUDE.md (project-specific overrides)
├── repos/ (cloned projects)
└── requirements/ (requirements documentation)
```

### Syncing Across Devices
1. Push CLAUDE.md and configs to GitHub
2. Clone on new device
3. Symlink or copy CLAUDE.md to appropriate locations
4. Install required MCP servers

## Development Tools
- Git and GitHub CLI (`gh`) for version control
- Multiple language environments (Python, Node.js, etc.)
- Testing frameworks appropriate to each project
- Docker for containerization when needed

## Project-Specific Instructions

### Model Fine-Tuning Projects
When working on ML/AI projects:
1. Always activate the virtual environment first
2. Use appropriate frameworks (LLaMA-Factory for flexibility, specific notebooks for learning)
3. Track experiments with wandb or tensorboard
4. Document hyperparameters and results

### Database Integration Projects
When working with Supabase/database projects:
1. Verify environment variables in `~/.config/api-keys/.env`
2. Test connections before schema operations
3. Use manual schema creation for complex operations
4. Set up automation after successful manual testing
5. Document schema changes and migration paths

### Web Development
1. Check package.json for available scripts
2. Run tests before committing
3. Use conventional commits
4. Follow existing component patterns

### System Configuration
1. MCP configurations sync across devices via this repo
2. CLAUDE.md files should be project-specific
3. Use .env files for API keys (never commit them)