# Changelog

All notable changes to this project will be documented in this format.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-09-26

### Added
- Initial release of Etemi Prompt Enhancer skill
- Six-part prompt format: Role, Context, Task & Commands, Pitfalls, Examples/Format, Closing Question
- Validation script `scripts/check_prompt.py` with structural checks
- Template-driven prompt generation via `assets/enhanced-prompt-template.md`
- Comprehensive reference documentation in `references/`
- Worked example showing before/after transformation
- Example prompts in `examples/`
- Unit tests for validation script in `tests/`
- Full documentation in `docs/` and GitHub Wiki
- GitHub Actions CI workflow for automated validation
- MIT License with explicit permission for adoption/editing/refactoring
- PyPI package configuration (`pyproject.toml`, `setup.py`)

### Features
- Zero external dependencies (stdlib only)
- Trigger phrases: `/etemi-prompt-enhancer`, "optimize prompt", "improve my prompt", etc.
- Automatic gap resolution with assumptions tracking
- Pitfall bank by task type (writing, code, analysis, conversion, academic, presentations)
- Integration with Agentic Engineering Skills ecosystem
- Compatible with any LLM (Claude, ChatGPT, etc.)

### Documentation
- Installation guide (user-level, project-level, submodule)
- Usage guide with examples
- API reference for validation script and skill interface
- Contributing guidelines
- FAQ wiki page
- Cross-references to related repositories

## [Unreleased]

### Planned
- Additional worked examples for different task types
- Extended pitfall bank for domain-specific tasks
- Performance benchmarks for validation script
- Web-based playground for prompt enhancement