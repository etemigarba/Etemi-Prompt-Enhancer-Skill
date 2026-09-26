# Etemi Prompt Enhancer Wiki

## Home

Welcome to the Etemi Prompt Enhancer wiki! This skill transforms rough prompts into professional six-part structured prompts for any AI model.

### Quick Links

- [Installation](Installation)
- [Usage Guide](Usage-Guide)
- [API Reference](API-Reference)
- [Examples](Examples)
- [FAQ](FAQ)

---

## Installation

### Prerequisites

- Python 3.8+
- Claude Code / OpenCode / compatible AI agent
- No external dependencies

### User-Level Install

```bash
mkdir -p ~/.claude/skills
cp -r etemi-prompt-enhancer ~/.claude/skills/
```

### Project-Level Install

```bash
mkdir -p .claude/skills
cp -r etemi-prompt-enhancer .claude/skills/
```

### Verify

```bash
python ~/.claude/skills/etemi-prompt-enhancer/scripts/check_prompt.py \
  ~/.claude/skills/etemi-prompt-enhancer/examples/enhanced-prompt.md
# PASS: six-part structure verified.
```

---

## Usage-Guide

### Trigger Phrases

- `/etemi-prompt-enhancer`
- "optimize prompt"
- "improve my prompt"
- "help me prompt"
- "rewrite this prompt"
- "make this prompt better"
- "enhance this prompt"
- "turn this into a proper prompt"

### Basic Example

**Input:**
```
/etemi-prompt-enhancer Write a prompt for code review
```

**Output:** Six-part prompt with Role, Context, Tasks, Pitfalls, Format, Closing Question

### Advanced

- Chain with [etemi-create-skill-skill](https://github.com/etemigarba/etemi-create-skill-skill)
- Batch process multiple prompts
- Specify target AI: `--target claude-code`

---

## API-Reference

### Validation Script

```bash
python scripts/check_prompt.py <file>
```

**Exit codes:** 0=pass, 1=fail

**Checks:** 5 parts present, correct order, pitfalls format, closing question, no placeholders

### Skill Interface

Activates on trigger phrases, extracts input from `$ARGUMENTS`, file path, or recent conversation.

---

## Examples

### Example 1: Code Generation

**Draft:** "Write a Python function to parse JSON"

**Enhanced:** [View full example](https://github.com/etemigarba/etemi-prompt-enhancer/blob/main/examples/enhanced-prompt.md)

### Example 2: Documentation

**Draft:** "Document this API endpoint"

**Enhanced:** Includes Role: technical writer, Context: audience=developers, Tasks: numbered sections

---

## FAQ

**Q: Does it work with ChatGPT?**
A: Yes, the enhanced prompts work with any LLM.

**Q: Can I customize the six parts?**
A: The format is fixed for consistency. Modify `references/six-part-format.md` for content rules.

**Q: Why does validation fail on my prompt?**
A: Run `python scripts/check_prompt.py your-prompt.md` to see specific errors.

**Q: How do I add a new pitfall type?**
A: Edit `references/six-part-format.md` pitfall bank section.

**Q: Can I use this in CI/CD?**
A: Yes, the validation script is designed for automation. See [API Reference](API-Reference).