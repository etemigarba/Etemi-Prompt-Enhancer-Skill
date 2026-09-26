#!/usr/bin/env python3
"""Structural check for a six-part enhanced prompt. Standard library only.

Usage: python check_prompt.py <prompt-file>
Exit code 0 = pass, 1 = errors found.
"""
import re
import sys

CLOSING = "Do you have any questions to ask me that will help you respond appropriately?"
PARTS = [
    ("1", r"role"),
    ("2", r"context"),
    ("3", r"task"),
    ("4", r"pitfall"),
    ("5", r"(example|format)"),
]
PLACEHOLDER_RE = re.compile(r"\{[^{}\n]{3,}\}|\bTODO\b|\bTBD\b|\[add details\]", re.I)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    with open(sys.argv[1], encoding="utf-8") as f:
        text = f.read().strip()
    errors = []

    # A heading is a short line such as "## 1. Role" or "**3) Task and Commands**".
    positions = []
    for num, word in PARTS:
        pat = re.compile(rf"^[ \t]*#*[ \t]*\**{num}[.)][ \t]*\**(?=[^\n]{{0,50}}$)[^\n]*{word}[^\n]*$", re.I | re.M)
        m = pat.search(text)
        if not m:
            errors.append(f"Part {num} heading (containing '{word}') not found.")
        else:
            positions.append((m.start(), m.end()))
    if len(positions) == len(PARTS) and positions != sorted(positions):
        errors.append("Parts 1-5 are not in the required order.")

    if len(positions) == len(PARTS):
        pit_body = text[positions[3][1]:positions[4][0]]
        if not re.search(r"^[ \t]*[-*][ \t]*Do not\b", pit_body, re.M):
            errors.append("Pitfalls section has no 'Do not ...' items.")

    if not text.endswith(CLOSING):
        errors.append("Prompt must end with the exact closing question and nothing after it.")
    elif text.count(CLOSING) > 1:
        errors.append("Closing question appears more than once.")

    ph = PLACEHOLDER_RE.findall(text)
    if ph:
        errors.append(f"Unfilled placeholders found: {ph[:3]}")

    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1
    print("PASS: six-part structure verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())