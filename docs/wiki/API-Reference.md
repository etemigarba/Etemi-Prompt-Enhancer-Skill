# API Reference

## Validation Script: `scripts/check_prompt.py`

### Usage

```bash
python scripts/check_prompt.py <prompt-file>
```

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | PASS — all structural checks passed |
| 1 | FAIL — one or more errors (printed to stderr) |

### Checks Performed

1. **Parts 1-5 Headings Present** — Each part heading found with correct keyword
2. **Parts in Order** — Parts 1-5 appear in sequence
3. **Pitfalls Format** — Part 4 contains at least one "Do not ..." item
4. **Closing Question** — Exact closing question at end, appears exactly once
5. **No Placeholders** — No `{...}`, `TODO`, `TBD`, `[add details]` remaining

### Error Messages

| Error | Cause |
|-------|-------|
| `Part N heading (containing '...') not found` | Missing or malformed part heading |
| `Parts 1-5 are not in the required order` | Parts appear out of sequence |
| `Pitfalls section has no 'Do not ...' items` | Part 4 missing prohibitions |
| `Prompt must end with the exact closing question` | Missing or extra text after closing |
| `Closing question appears more than once` | Duplicate closing question |
| `Unfilled placeholders found: [...]` | Template placeholders not replaced |

### Example

```bash
$ python scripts/check_prompt.py examples/enhanced-prompt.md
PASS: six-part structure verified.
$ echo $?
0

$ python scripts/check_prompt.py examples/basic-prompt.md
ERROR: Part 1 heading (containing 'role') not found.
ERROR: Part 2 heading (containing 'context') not found.
ERROR: Part 3 heading (containing 'task') not found.
ERROR: Part 4 heading (containing 'pitfall') not found.
ERROR: Part 5 heading (containing 'example') not found.
ERROR: Prompt must end with the exact closing question and nothing after it.
$ echo $?
1
```

## Skill Interface

### Trigger Detection

The skill activates when user message matches:

```python
TRIGGERS = [
    "/etemi-prompt-enhancer",
    "optimize prompt",
    "improve my prompt",
    "help me prompt",
    "rewrite this prompt",
    "make this prompt better",
    "enhance this prompt",
    "turn this into a proper prompt",
]
```

### Input Extraction

```python
# Priority order:
# 1. $ARGUMENTS (slash command args)
# 2. File path mentioned in message
# 3. Most recent draft prompt in conversation
```

### Output Format

```markdown
## 1. Role
...

## 2. Context
...

## 3. Task and Commands
1. ...
2. ...
3. Before responding, check your output against every requirement above.

## 4. Pitfalls to Avoid
- Do not ...
- Do not ...

## 5. Examples and Response Format
...

Do you have any questions to ask me that will help you respond appropriately?
```

**Assumptions** (optional):
- Assumption 1
- Assumption 2

## Template Variables

`assets/enhanced-prompt-template.md` uses these placeholders:

| Placeholder | Description |
|-------------|-------------|
| `{specific expert persona...}` | Role definition |
| `{Background...}` | Context definition |
| `{Imperative, verifiable step.}` | Task step (repeatable) |
| `{prohibition from the draft}` | Draft prohibition |
| `{predictable failure mode...}` | Task-type pitfall |
| `{Exact structure...}` | Output format spec |
| `{Optional short example...}` | Example/skeleton |

## Integration

### As Module

```python
from scripts.check_prompt import main
import sys

sys.argv = ['check_prompt.py', 'prompt.md']
result = main()  # Returns 0 or 1
```

### In CI/CD

```yaml
- name: Validate Prompts
  run: |
    python scripts/check_prompt.py examples/enhanced-prompt.md
    python -m pytest tests/
```