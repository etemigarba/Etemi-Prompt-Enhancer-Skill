#!/usr/bin/env python3
"""Unit tests for check_prompt.py validation script."""
import subprocess
import sys
import tempfile
import os
import pytest

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'check_prompt.py')

VALID_PROMPT = """## 1. Role
You are a senior software engineer.

## 2. Context
Background information here.

## 3. Task and Commands
1. Do something.
2. Do another thing.
3. Before responding, check your output against every requirement above.

## 4. Pitfalls to Avoid
- Do not skip steps.
- Do not use placeholder text.

## 5. Examples and Response Format
Output as JSON.

Do you have any questions to ask me that will help you respond appropriately?"""

INVALID_MISSING_PARTS = """## 1. Role
You are a senior software engineer.

## 3. Task and Commands
1. Do something.

## 5. Examples and Response Format
Output as JSON.

Do you have any questions to ask me that will help you respond appropriately?"""

INVALID_WRONG_ORDER = """## 3. Task and Commands
1. Do something.

## 1. Role
You are a senior software engineer.

## 2. Context
Background.

## 4. Pitfalls to Avoid
- Do not skip.

## 5. Examples and Response Format
Output.

Do you have any questions to ask me that will help you respond appropriately?"""

INVALID_NO_DO_NOT = """## 1. Role
You are a senior software engineer.

## 2. Context
Background.

## 3. Task and Commands
1. Do something.

## 4. Pitfalls to Avoid
- Avoid skipping steps.
- Don't use placeholders.

## 5. Examples and Response Format
Output.

Do you have any questions to ask me that will help you respond appropriately?"""

INVALID_MISSING_CLOSING = """## 1. Role
You are a senior software engineer.

## 2. Context
Background.

## 3. Task and Commands
1. Do something.

## 4. Pitfalls to Avoid
- Do not skip.

## 5. Examples and Response Format
Output."""

INVALID_DUPLICATE_CLOSING = """## 1. Role
You are a senior software engineer.

## 2. Context
Background.

## 3. Task and Commands
1. Do something.

## 4. Pitfalls to Avoid
- Do not skip.

## 5. Examples and Response Format
Output.

Do you have any questions to ask me that will help you respond appropriately?
Do you have any questions to ask me that will help you respond appropriately?"""

INVALID_PLACEHOLDERS = """## 1. Role
You are a {specific expert persona}.

## 2. Context
{Background information}.

## 3. Task and Commands
1. {Imperative step}.
2. Before responding, check your output against every requirement above.

## 4. Pitfalls to Avoid
- Do not {prohibition}.

## 5. Examples and Response Format
{Exact structure}.

Do you have any questions to ask me that will help you respond appropriately?"""


def run_check(prompt_text):
    """Run check_prompt.py on given text, return (exit_code, stdout, stderr)."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write(prompt_text)
        f.flush()
        temp_path = f.name
    try:
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, temp_path],
            capture_output=True,
            text=True
        )
        # check_prompt.py prints to stdout, not stderr
        return result.returncode, result.stdout, result.stderr
    finally:
        os.unlink(temp_path)


class TestCheckPrompt:
    def test_valid_prompt_passes(self):
        code, out, err = run_check(VALID_PROMPT)
        assert code == 0
        assert "PASS" in out

    def test_missing_parts_fails(self):
        code, out, err = run_check(INVALID_MISSING_PARTS)
        assert code == 1
        assert "Part 2 heading" in out or "Part 4 heading" in out

    def test_wrong_order_fails(self):
        code, out, err = run_check(INVALID_WRONG_ORDER)
        assert code == 1
        assert "not in the required order" in out

    def test_no_do_not_fails(self):
        code, out, err = run_check(INVALID_NO_DO_NOT)
        assert code == 1
        assert "Do not" in out

    def test_missing_closing_fails(self):
        code, out, err = run_check(INVALID_MISSING_CLOSING)
        assert code == 1
        assert "exact closing question" in out

    def test_duplicate_closing_fails(self):
        code, out, err = run_check(INVALID_DUPLICATE_CLOSING)
        assert code == 1
        assert "more than once" in out

    def test_placeholders_fails(self):
        code, out, err = run_check(INVALID_PLACEHOLDERS)
        assert code == 1
        assert "Unfilled placeholders" in out

    def test_examples_enhanced_prompt(self):
        """Test the actual example file passes."""
        example_path = os.path.join(os.path.dirname(__file__), '..', 'examples', 'enhanced-prompt.md')
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH, example_path],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        assert "PASS" in result.stdout


if __name__ == '__main__':
    pytest.main([__file__, '-v'])