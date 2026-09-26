# The Six-Part Prompt Format — Content Rules

## 1. Role
- Name a specific expert: discipline + seniority + relevant specialism.
- Add one or two qualities the task rewards (rigour, plain-language clarity, standards compliance).
- Weak: "You are an AI assistant." Strong: "You are a senior software architect and technical writer experienced in Claude Code skills and prompt design."

## 2. Context
Answer four questions in two to six sentences:
1. What is the situation or background?
2. Why is the output needed (its purpose)?
3. Who will read or use it, and at what level of expertise?
4. What inputs will the AI receive (pasted text, files, data)?

## 3. Task and Commands
- Numbered steps, one action each, imperative mood ("Analyse…", "Write…", "Compute…").
- Make each step verifiable: counts, word limits, named standards, required sections.
- Include decision branches where the input may vary ("If the source has no examples, create one").
- End with a self-check step.

## 4. Pitfalls to Avoid
Every line begins "Do not". Include all prohibitions from the draft, then add the relevant items below.

**Pitfall bank by task type**
- Writing/documents: filler and clichés; unsupported claims; fabricated citations or statistics; inconsistent terminology; exceeding length limits.
- Code/software: placeholder or mock code; untested assumptions about libraries or versions; removing existing functionality; hard-coded secrets; ignoring error handling.
- Analysis/research: presenting assumptions as findings; mixing units; unstated sources; overconfident conclusions from thin data.
- Conversion/restructuring tasks (e.g. prompt to skill, format to format): dropping source constraints; adding unrequested features; changing intent; leaving placeholders.
- Academic work: non-standard referencing; plagiarism-risk paraphrasing; claims beyond the evidence.
- Presentations/visuals: overcrowded slides; decorative content without purpose; inconsistent styling.

## 5. Examples and Response Format
- State the exact output structure: sections in order, headings, bullets vs prose, length, file type.
- Give an example or skeleton when the shape is not obvious. Keep examples short and representative.
- If the user supplied examples, keep them verbatim.

## 6. Closing question
End the prompt with exactly this line, and nothing after it:

Do you have any questions to ask me that will help you respond appropriately?