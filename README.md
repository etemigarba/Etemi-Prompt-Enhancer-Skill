# Etemi Prompt Enhancer

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Skill Version](https://img.shields.io/badge/Skill-1.0.0-orange.svg)](SKILL.md)
[![CI Status](https://github.com/etemigarba/etemi-prompt-enhancer/workflows/Validate/badge.svg)](https://github.com/etemigarba/etemi-prompt-enhancer/actions)
[![GitHub Stars](https://img.shields.io/github/stars/etemigarba/etemi-prompt-enhancer?style=social)](https://github.com/etemigarba/etemi-prompt-enhancer/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/etemigarba/etemi-prompt-enhancer?style=social)](https://github.com/etemigarba/etemi-prompt-enhancer/network)
[![Last Commit](https://img.shields.io/github/last-commit/etemigarba/etemi-prompt-enhancer)](https://github.com/etemigarba/etemi-prompt-enhancer/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/etemigarba/etemi-prompt-enhancer)](https://github.com/etemigarba/etemi-prompt-enhancer)

> **Transform rough prompts into production-ready six-part instructions (Role, Context, Task, Pitfalls, Examples/Format, Clarifying Question) with built-in validation. Zero-dependency Python checker, template-driven, works with any AI model. Part of the Agentic Engineering Skills ecosystem.**

---

## Overview

The **Etemi Prompt Enhancer** is a Claude Code skill that rewrites incomplete, conversational, or rough prompts into professional, six-part structured prompts ready for any AI model. It follows a rigorous format ensuring clarity, completeness, and executability.

### Key Features

- **Six-Part Format**: Role → Context → Task & Commands → Pitfalls → Examples/Format → Clarifying Question
- **Zero Dependencies**: Validation script uses only Python standard library
- **Template-Driven**: Consistent output using `assets/enhanced-prompt-template.md`
- **Automated Validation**: `scripts/check_prompt.py` verifies structure compliance
- **Universal Compatibility**: Works with Claude, ChatGPT, Claude Code, and any LLM
- **Skill Ecosystem**: Integrates with [Agentic Engineering Skills](https://github.com/etemigarba/Agentic-Engineering-Skills), [Loop Engineer](https://github.com/etemigarba/Loop-Engineer-Skill), [Systematic Implementation](https://github.com/etemigarba/Systematic-Implementation-Skill), [Production Ready Workflow](https://github.com/etemigarba/Production-Ready-Workflow-Skill), [Debug and Fix Bugs](https://github.com/etemigarba/Debug-and-Fix-Bugs-Skill), and [Create Skill](https://github.com/etemigarba/etemi-create-skill-skill)

---

## Quick Start

### Installation

```bash
# User-level (recommended)
mkdir -p ~/.claude/skills
cp -r etemi-prompt-enhancer ~/.claude/skills/

# Or project-level
mkdir -p .claude/skills
cp -r etemi-prompt-enhancer .claude/skills/
```

### Usage

Trigger the skill by running `/etemi-prompt-enhancer` or using any of these phrases:
- "optimize prompt"
- "improve my prompt"
- "help me prompt"
- "rewrite this prompt"
- "make this prompt better"
- "enhance this prompt"
- "turn this into a proper prompt"

**Example:**
```
/etemi-prompt-enhancer Write a prompt for converting a prompt to a Claude Code skill
```

---

## Six-Part Format

| Part | Purpose |
|------|---------|
| **1. Role** | Specific expert persona with seniority & discipline |
| **2. Context** | Background, purpose, audience, inputs |
| **3. Task & Commands** | Numbered, imperative, verifiable steps |
| **4. Pitfalls** | "Do not..." prohibitions covering failure modes |
| **5. Examples & Format** | Exact output structure + optional skeleton |
| **6. Closing Question** | Fixed: "Do you have any questions to ask me that will help you respond appropriately?" |

---

## Validation

```bash
# Validate any enhanced prompt
python scripts/check_prompt.py path/to/prompt.md

# Exit code 0 = PASS, 1 = errors with details
```

---

## Repository Structure

```
etemi-prompt-enhancer/
├── SKILL.md                      # Core skill definition
├── assets/
│   └── enhanced-prompt-template.md
├── references/
│   ├── six-part-format.md        # Content rules per part
│   └── worked-example.md         # Before/after example
├── scripts/
│   └── check_prompt.py           # Structural validator
├── examples/
│   ├── basic-prompt.md           # Sample input
│   └── enhanced-prompt.md        # Sample output
├── docs/
│   ├── installation.md
│   ├── usage.md
│   ├── api-reference.md
│   └── contributing.md
└── tests/
    └── test_check_prompt.py      # Unit tests
```

---

## Documentation

- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage.md)
- [API Reference](docs/api-reference.md)
- [Contributing](docs/contributing.md)
- [Wiki](https://github.com/etemigarba/etemi-prompt-enhancer/wiki)

---

## Related Repositories

| Repository | Description |
|------------|-------------|
| [Agentic-Engineering-Skills](https://github.com/etemigarba/Agentic-Engineering-Skills) | 33 technology-agnostic skills across 6 SDLC categories |
| [Loop-Engineer-Skill](https://github.com/etemigarba/Loop-Engineer-Skill) | Bounded, self-correcting agent loops |
| [Systematic-Implementation-Skill](https://github.com/etemigarba/Systematic-Implementation-Skill) | Gate-controlled SDLC meta-skill |
| [Production-Ready-Workflow-Skill](https://github.com/etemigarba/Production-Ready-Workflow-Skill) | Zero-mock-data production hardening |
| [Debug-and-Fix-Bugs-Skill](https://github.com/etemigarba/Debug-and-Fix-Bugs-Skill) | Three-phase debugging with live verification |
| [etemi-create-skill-skill](https://github.com/etemigarba/etemi-create-skill-skill) | Converts prompts/workflows into installable skills |

---

## License

MIT License — Copyright (c) 2026 Prof. Etemi Joshua Garba

No explicit permission required for adoption, editing, and refactoring of the skills.

---

## Author

**Prof. Etemi Joshua Garba**  
Consultant in Software Engineering, AI-Driven Software Engineering, AI-Native Software Development, and Prompt Engineering  
[Ethereal Multimedia Technology Ltd.](https://ethereal.ng/) | [ORCID](https://orcid.org/0000-0001-6707-0220) | [LinkedIn](https://www.linkedin.com/in/ejgarba/)