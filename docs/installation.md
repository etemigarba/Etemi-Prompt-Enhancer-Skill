# Installation Guide

## Prerequisites

- **Python 3.8+** (for validation script)
- **Claude Code**, **OpenCode**, or compatible AI coding agent
- No external Python packages required (stdlib only)

## Installation Methods

### Method 1: User-Level Installation (Recommended)

```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill
cp -r etemi-prompt-enhancer ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/etemi-prompt-enhancer/
```

### Method 2: Project-Level Installation

```bash
# In your project root
mkdir -p .claude/skills
cp -r etemi-prompt-enhancer .claude/skills/
```

### Method 3: Git Submodule (For Teams)

```bash
# Add as submodule
git submodule add https://github.com/etemigarba/etemi-prompt-enhancer.git .claude/skills/etemi-prompt-enhancer
git submodule update --init --recursive
```

## Verification

After installation, verify the skill loads correctly:

```bash
# Check skill structure
ls ~/.claude/skills/etemi-prompt-enhancer/
# Should show: SKILL.md assets/ references/ scripts/

# Test validation script
python ~/.claude/skills/etemi-prompt-enhancer/scripts/check_prompt.py \
  ~/.claude/skills/etemi-prompt-enhancer/examples/enhanced-prompt.md
# Should output: "PASS: six-part structure verified."
```

## Configuration

No additional configuration required. The skill activates automatically when you use trigger phrases.

### Trigger Phrases

The skill responds to:
- `/etemi-prompt-enhancer`
- "optimize prompt"
- "improve my prompt"
- "help me prompt"
- "rewrite this prompt"
- "make this prompt better"
- "enhance this prompt"
- "turn this into a proper prompt"

## Updating

```bash
# User-level
cd ~/.claude/skills/etemi-prompt-enhancer && git pull

# Project-level
cd .claude/skills/etemi-prompt-enhancer && git pull

# Submodule
git submodule update --remote .claude/skills/etemi-prompt-enhancer
```

## Uninstallation

```bash
# User-level
rm -rf ~/.claude/skills/etemi-prompt-enhancer

# Project-level
rm -rf .claude/skills/etemi-prompt-enhancer

# Submodule
git submodule deinit .claude/skills/etemi-prompt-enhancer
git rm .claude/skills/etemi-prompt-enhancer
rm -rf .git/modules/.claude/skills/etemi-prompt-enhancer
```