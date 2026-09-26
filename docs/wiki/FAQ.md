# FAQ

## General

**Q: What AI models does this work with?**
A: The enhanced prompts work with any LLM — Claude, ChatGPT, GPT-4, Llama, Gemini, etc. The skill itself runs in Claude Code / OpenCode.

**Q: Is this only for Claude Code?**
A: The skill runs in Claude Code, but the *output prompts* work with any AI model.

**Q: Do I need to install Python?**
A: Only for the validation script (`scripts/check_prompt.py`). The skill itself doesn't require Python.

---

## Installation

**Q: Where should I install — user or project level?**
A: User-level (`~/.claude/skills/`) for personal use across projects. Project-level (`.claude/skills/`) for team sharing via git.

**Q: Can I use it as a git submodule?**
A: Yes, see [Installation](Installation) for submodule commands.

**Q: Skill not showing up?**
A: Restart Claude Code after installation. Verify with `ls ~/.claude/skills/etemi-prompt-enhancer/`.

---

## Usage

**Q: Why does the skill ask clarifying questions?**
A: If your draft has genuine ambiguity (goal, audience, deliverable unclear), the skill asks up to 3 focused questions rather than guessing.

**Q: Can I provide examples in my draft?**
A: Yes! Include examples in your draft — they'll be preserved in Part 5 of the enhanced prompt.

**Q: What if I don't like the enhanced prompt?**
A: You can refine the draft and re-run, or edit the enhanced prompt directly — it's just text.

**Q: Does it work for image generation prompts?**
A: Yes, specify `--target midjourney` or similar in your request.

---

## Validation

**Q: Why does `check_prompt.py` fail on my prompt?**
A: Run it to see specific errors. Common issues:
- Missing part headings
- Parts out of order
- No "Do not ..." items in Pitfalls
- Missing or duplicate closing question
- Unfilled placeholders like `{...}` or `TODO`

**Q: Can I skip validation?**
A: Not recommended — validation catches structural issues that break AI execution.

**Q: How do I fix "Parts 1-5 not in required order"?**
A: Ensure headings appear as: Role → Context → Task → Pitfalls → Examples/Format.

---

## Customization

**Q: Can I change the six-part format?**
A: The format is fixed for consistency across the ecosystem. For different formats, create a new skill.

**Q: How do I add a new pitfall category?**
A: Edit `references/six-part-format.md` → Pitfall bank section.

**Q: Can I modify the closing question?**
A: No — it's a fixed requirement for consistent AI interaction.

---

## Ecosystem

**Q: How does this relate to other Etemi skills?**
A: Part of the [Agentic Engineering Skills](https://github.com/etemigarba/Agentic-Engineering-Skills) ecosystem. Chains with:
- [etemi-create-skill-skill](https://github.com/etemigarba/etemi-create-skill-skill) — create skills from prompts
- [Loop-Engineer-Skill](https://github.com/etemigarba/Loop-Engineer-Skill) — bounded agent loops
- [Systematic-Implementation-Skill](https://github.com/etemigarba/Systematic-Implementation-Skill) — SDLC pipeline

**Q: Can I use this in automated workflows?**
A: Yes, the validation script is CLI-friendly for CI/CD pipelines.

---

## License & Contribution

**Q: Can I use this commercially?**
A: Yes, MIT License allows commercial use, modification, distribution.

**Q: How do I contribute?**
A: See [Contributing](Contributing) — fork, branch, test, PR.

**Q: Who is the author?**
A: Prof. Etemi Joshua Garba, Ethereal Multimedia Technology Ltd.