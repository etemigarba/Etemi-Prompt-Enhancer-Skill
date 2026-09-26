# Usage Guide

## Basic Usage

### Via Slash Command
```
/etemi-prompt-enhancer Write a prompt for converting a prompt to a Claude Code skill
```

### Via Natural Language
Simply paste your draft prompt and ask:
> "Optimize this prompt for me"

Or use any trigger phrase:
- "improve my prompt"
- "help me prompt"
- "rewrite this prompt"
- "make this prompt better"
- "enhance this prompt"
- "turn this into a proper prompt"

### From File
```
/etemi-prompt-enhancer @path/to/draft-prompt.txt
```

## Input Formats

### Direct Text
```
/etemi-prompt-enhancer Summarize this report in 3 bullet points for executives
```

### Multi-line Prompt
```
/etemi-prompt-enhancer
Write a comprehensive code review checklist for Python projects.
Include security, performance, and style checks.
Target audience: senior developers.
Output as markdown with checkboxes.
```

### With Target AI Specification
```
/etemi-prompt-enhancer --target claude-code
Create a skill for automated testing.
```

## Output

The skill returns:

1. **Enhanced Prompt** — Complete six-part prompt in a fenced code block
2. **Assumptions** — Up to 5 bullets listing any defaults filled in

### Example Output

```
## 1. Role
You are a senior Python developer and code review specialist with expertise in security auditing, performance optimization, and PEP 8 compliance.

## 2. Context
A development team needs a standardized code review checklist for Python pull requests. The checklist will be used by senior and mid-level developers during PR reviews. Inputs include the PR diff, linked issue, and any CI results.

## 3. Task and Commands
1. Create a markdown checklist with categories: Security, Performance, Style, Testing, Documentation.
2. Each category must have 5-8 specific, verifiable check items.
3. Include a "Critical" subsection for security items that block merge.
4. Add a self-check step: verify all items are actionable and non-redundant.
5. Output as GitHub-flavored markdown with checkboxes.

## 4. Pitfalls to Avoid
- Do not include vague items like "code looks good" without measurable criteria.
- Do not omit security checks for common vulnerabilities (SQL injection, XSS, path traversal).
- Do not add items that cannot be verified from a diff alone.
- Do not use placeholder text or TODO markers.

## 5. Examples and Response Format
Output structure:
### Security (Critical)
- [ ] No hardcoded secrets or API keys
- [ ] Parameterized queries used for all SQL
...

### Performance
- [ ] No N+1 query patterns in loops
...

Do you have any questions to ask me that will help you respond appropriately?
```

## Advanced Usage

### Chaining with Other Skills

Use output from this skill as input to [etemi-create-skill-skill](https://github.com/etemigarba/etemi-create-skill-skill):

```
/etemi-prompt-enhancer Create a skill for generating API documentation
→ Copy enhanced prompt →
/etemi-create-skill-skill [paste enhanced prompt]
```

### Batch Processing

Create a script to enhance multiple prompts:

```bash
#!/bin/bash
for prompt in prompts/*.txt; do
  /etemi-prompt-enhancer "$(cat "$prompt")" > "enhanced/$(basename "$prompt")"
done
```

## Tips for Best Results

1. **Be Specific**: Include target audience, output format, constraints
2. **Provide Examples**: If you have a preferred output style, include a sample
3. **State Constraints**: Word limits, required sections, forbidden patterns
4. **Clarify Ambiguity**: The skill will ask up to 3 clarifying questions if needed

## Common Patterns

| Task Type | Good Input | Enhanced Output Includes |
|-----------|------------|-------------------------|
| Code generation | "Write a REST API" | Role: senior backend engineer; Context: framework, auth, specs; Tasks: numbered endpoints |
| Documentation | "Document this function" | Role: technical writer; Context: audience, format; Tasks: sections, examples |
| Analysis | "Analyze this data" | Role: data scientist; Context: data shape, questions; Tasks: methods, visualizations |
| Conversion | "Convert to TypeScript" | Role: TS expert; Context: source code, target version; Tasks: types, interfaces |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Skill not triggering | Check installation path; restart Claude Code |
| Validation fails | Run `python scripts/check_prompt.py` on output to see errors |
| Output missing parts | Ensure draft has clear goal; skill asks clarifying questions if needed |
| Placeholder errors | Skill fills gaps with assumptions; review assumptions list |