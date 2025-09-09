# CLAUDE-ML: Machine Learning Module  
> Loaded when ML/AI projects detected

## 🤖 ML Architecture Context
```yaml
environment_management: "venv or conda"
framework_preference:
  training: "pytorch > tensorflow"
  fine_tuning: "LLaMA-Factory or transformers"
  data: "pandas + numpy"
  
project_structure:
  data/: "raw and processed"
  models/: "saved checkpoints"
  notebooks/: "exploration"
  src/: "training code"
  configs/: "hyperparameters"
```

## 📋 ML Prerequisites Checklist
```bash
# Before ML work:
echo "=== ML PREREQUISITES ==="

# □ Virtual environment active?
[[ -n "$VIRTUAL_ENV" ]] && echo "✓ venv active: $(basename $VIRTUAL_ENV)" || echo "✗ No venv active"

# □ GPU available?
python3 -c "import torch; print(f'✓ GPU: {torch.cuda.is_available()}')" 2>/dev/null || echo "✗ PyTorch not found"

# □ Data present?
[[ -d ./data ]] && echo "✓ Data directory exists" || echo "⚠️ No data directory"

# □ Configs loaded?
[[ -f configs/config.yaml ]] && echo "✓ Config found" || echo "⚠️ No config file"

# □ Tracking setup?
[[ -d .wandb ]] || [[ -d mlruns ]] && echo "✓ Experiment tracking ready" || echo "⚠️ No tracking setup"
```

## 🚫 ML Non-Goals
**NEVER without permission:**
- ❌ Start expensive training runs
- ❌ Download large datasets
- ❌ Modify hyperparameters in active experiments
- ❌ Delete checkpoints or results
- ❌ Share model weights publicly
- ❌ Use production API keys for testing

## 🔄 ML Pattern Discovery

### Training Patterns
```python
# DISCOVERED PATTERN: Standard training loop
# 1. Load config
# 2. Setup wandb/tensorboard
# 3. Initialize model
# 4. Load checkpoint if resuming
# 5. Training loop with validation
# 6. Save best checkpoint
# 7. Log metrics
```

### Data Pipeline Patterns  
```python
# DISCOVERED PATTERN: Data preprocessing
# 1. Raw data validation
# 2. Preprocessing pipeline
# 3. Train/val/test split
# 4. Cache processed data
# 5. DataLoader creation
```

## 🎯 ML Success Criteria
- ✅ Reproducible results (seed set)
- ✅ Metrics logged and tracked
- ✅ Checkpoints saved regularly
- ✅ Memory usage monitored
- ✅ Gradients checked for NaN
- ✅ Validation improving or explained

## 🔧 ML Session Handoff
```markdown
## ML SESSION HANDOFF
### Experiment State
- Experiment ID: [wandb/mlflow ID]
- Epoch: [current/total]
- Best metric: [value @ epoch]
- Last checkpoint: [path]

### Training Status
- Loss: [train/val]
- Learning rate: [current]
- GPU memory: [used/total]
- ETA: [estimated time]

### Recovery Commands
```bash
source venv/bin/activate
export CUDA_VISIBLE_DEVICES=0
python train.py --resume-from [checkpoint]
```
```

---
*Module: ML | Auto-loads when requirements.txt or environment.yml found*