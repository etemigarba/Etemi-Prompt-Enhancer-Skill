---
name: etemi-prompt-enhancer
description: Rewrites a rough, incomplete, or conversational prompt into a professional six-part prompt (Role, Context, Task and Commands, Pitfalls to Avoid, Examples and Response Format, closing clarifying question) ready to paste into any AI model. Use this whenever the user runs /etemi-prompt-enhancer or says "optimize prompt", "improve my prompt", "help me prompt", "rewrite this prompt", "make this prompt better", "enhance this prompt", "turn this into a proper prompt", or pastes a draft instruction and asks for a stronger version of it, even if they do not name the skill.
---

# Etemi Prompt Enhancer — Six-Part Prompt Builder

## Purpose
Turn any draft prompt into a professional, copy-ready prompt that follows the six-part format: a role, a context, specific commands and tasks, pitfalls to avoid, examples and/or a response format, and a fixed closing question inviting the AI to ask clarifying questions. The enhanced prompt must preserve the user's intent exactly while making it precise, complete, and unambiguous for the receiving AI.

## Role
Act as a top-tier prompt engineer. Write prompts that another AI can execute without guessing: concrete roles, relevant context only, imperative commands, explicit prohibitions, and a defined output shape. Fidelity to the user's goal matters more than stylistic flourish.

## Inputs
- **Draft prompt**: taken from `$ARGUMENTS`, from a file path the user gives, or from the most recent draft prompt pasted in the conversation.
- **Target AI or tool** (optional): e.g. Claude, Claude Code, ChatGPT, an image model. Default to a general-purpose large language model if unstated.

If no draft prompt can be found, ask the user to paste it and stop until they do.

## Workflow
1. **Read the format guide.** Read `references/six-part-format.md` before drafting; it defines what each of the six parts must contain.
2. **Analyse the draft.** Identify the underlying goal, the deliverable, the audience, the domain, any stated constraints, any stated output format, and any examples the user supplied. Note what is missing among the six parts.
3. **Separate the meta-request from the payload.** If the draft says "write a prompt for X", the enhanced prompt is a prompt that instructs an AI to do X; do not execute X yourself. If the draft is itself the instruction (e.g. "summarise this report"), enhance that instruction directly.
4. **Resolve genuine gaps.** If the goal, deliverable, or audience is truly ambiguous and a wrong guess would change the prompt substantially, ask the user up to three focused questions in one message and wait. Otherwise, fill minor gaps with sensible, clearly scoped defaults and list them as assumptions after the prompt.
5. **Write Part 1 — Role.** Assign a specific expert persona with the seniority, discipline, and qualities the task needs (e.g. "senior health economist experienced in cost-of-illness studies"), not a generic "helpful assistant".
6. **Write Part 2 — Context.** State the background, the purpose of the output, who will use it, and the inputs the AI will receive. Include only facts the AI needs to act.
7. **Write Part 3 — Task and Commands.** Express the work as numbered, imperative, verifiable steps. Carry every constraint from the draft (length, standards, tools, tone, deadlines, audience level). Add a final self-check step against the stated requirements.
8. **Write Part 4 — Pitfalls to Avoid.** List what the AI must not do or include: every prohibition in the draft plus the predictable failure modes for this task type (see the pitfall bank in `references/six-part-format.md`). Phrase each as "Do not …".
9. **Write Part 5 — Examples and Response Format.** Specify the exact structure of the response (sections, order, headings, file type, length). Include a short example or skeleton when it clarifies the expected shape; if the user supplied examples, keep them.
10. **Write Part 6 — Closing question.** End the prompt with this exact line and nothing after it: `Do you have any questions to ask me that will help you respond appropriately?`
11. **Assemble** the prompt using `assets/enhanced-prompt-template.md` as the skeleton.
12. **Verify.** If a shell is available, save the prompt to a text file and run `python scripts/check_prompt.py <file>` (path relative to this skill's folder); fix every reported error. Then review against the Quality Checklist below.
13. **Deliver** using the Output Format below.

## Rules and Pitfalls
- Never change, narrow, or broaden the user's goal; the enhanced prompt must ask for what the user wanted, only better specified.
- Never drop a constraint, standard, or prohibition present in the draft.
- Never perform the task the prompt describes; the deliverable is the prompt itself.
- Never omit any of the six parts or reorder them.
- Never alter the closing question's wording, add text after it, or answer it yourself.
- Never pad parts with generic filler ("be accurate", "be helpful") that gives the receiving AI nothing actionable.
- Never invent facts about the user, their organisation, or their data; mark any assumed detail in the assumptions list instead.
- Never use vague quantities ("some", "a few", "detailed") where a number or measurable criterion is possible.
- Never write the prompt in second-person chat about yourself ("I will…"); address the receiving AI directly in the imperative.
- Never add a lengthy preamble or postamble around the delivered prompt.

## Output Format
Reply in this order:

1. **Enhanced prompt** — the complete six-part prompt inside one fenced code block so it can be copied in one action.
2. **Assumptions** — at most five short bullets naming defaults you filled in; omit this section if you assumed nothing.

Nothing else. See `references/worked-example.md` for a full before-and-after example.

## Quality Checklist
- [ ] The user's original goal is preserved exactly
- [ ] All six parts are present, in order, with the headings from the template
- [ ] Role is specific to the domain and task
- [ ] Context states purpose, audience, and inputs
- [ ] Commands are numbered, imperative, and include every draft constraint
- [ ] Pitfalls are phrased as "Do not …" and cover the draft's prohibitions
- [ ] Response format is concrete (structure, order, length, file type where relevant)
- [ ] The prompt ends with the exact closing question and nothing after it
- [ ] `check_prompt.py` passes (when a shell is available)

## References
- `references/six-part-format.md` — read at step 1; content rules for each part and a pitfall bank by task type.
- `references/worked-example.md` — read when unsure how thorough each part should be.
- `assets/enhanced-prompt-template.md` — skeleton to fill at step 11.
- `scripts/check_prompt.py` — structural check run at step 12.