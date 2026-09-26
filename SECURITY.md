# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅        |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do not** open a public issue
2. Email details to: **joshua.garba@ethereal.ng**
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will acknowledge receipt within 48 hours and provide a timeline for resolution.

## Security Considerations

This skill:
- Does not execute user-provided code
- Does not make network requests
- Does not access file system beyond reading prompt files for validation
- Uses only Python standard library
- Has no external dependencies

The validation script (`scripts/check_prompt.py`) only reads the provided prompt file and performs regex-based structural checks. It does not evaluate or execute any code within the prompt.

## Dependency Security

No external dependencies — zero supply chain risk.