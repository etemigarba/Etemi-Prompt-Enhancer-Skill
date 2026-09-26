# Contributing Guide

Thank you for contributing to Etemi Prompt Enhancer!

## Quick Start

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run validation: `python scripts/check_prompt.py examples/enhanced-prompt.md`
5. Run tests: `python -m pytest tests/`
6. Commit: `git commit -m 'Add amazing feature'`
7. Push: `git push origin feature/amazing-feature`
8. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/etemigarba/etemi-prompt-enhancer.git
cd etemi-prompt-enhancer
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -e .[dev]
```

## Code Standards

- **Python**: PEP 8, type hints where practical
- **Markdown**: GitHub-flavored, consistent heading levels
- **Commits**: Conventional commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`)

## Validation Requirements

All enhanced prompts must pass:

```bash
python scripts/check_prompt.py <prompt-file>
# Must exit with code 0
```

## Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_check_prompt.py::test_valid_prompt -v
```

## Adding Examples

1. Add draft prompt to `examples/`
2. Generate enhanced version using the skill
3. Validate: `python scripts/check_prompt.py examples/your-enhanced.md`
4. Both files should be included in PR

## Updating References

When modifying the six-part format:
1. Update `references/six-part-format.md`
2. Update `references/worked-example.md` if format changes
3. Update `assets/enhanced-prompt-template.md` if structure changes
4. Regenerate `examples/enhanced-prompt.md`
5. Run validation on all examples

## Pull Request Checklist

- [ ] All validation checks pass
- [ ] Tests pass
- [ ] Documentation updated if needed
- [ ] CHANGELOG.md updated
- [ ] No placeholder text in committed files
- [ ] Commit messages follow conventional format

## Reporting Issues

Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) for:
- Validation script false positives/negatives
- Skill trigger failures
- Output format issues
- Documentation errors

## Feature Requests

Open an issue with:
- Clear problem statement
- Proposed solution
- Example input/output if applicable
- Relation to existing skills ecosystem

## License

By contributing, you agree your contributions will be licensed under the MIT License.