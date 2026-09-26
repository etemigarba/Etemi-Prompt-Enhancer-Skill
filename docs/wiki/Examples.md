# Examples

## Example 1: Basic Prompt Enhancement

### Input (Draft)
```
Write a prompt for converting a prompt to a Claude Code skill.
```

### Enhanced Output
See [enhanced-prompt.md](../examples/enhanced-prompt.md) for the full six-part result.

---

## Example 2: Code Generation Task

### Input (Draft)
```
Create a Python function that validates email addresses using regex.
```

### Enhanced Output Structure
```
## 1. Role
You are a senior Python developer with expertise in input validation, regex patterns, and RFC 5322 compliance.

## 2. Context
A web application needs robust email validation for user registration. The function will be called on every signup. Input: raw email string. Output: boolean or validated email object.

## 3. Task and Commands
1. Write a function `validate_email(email: str) -> bool` using regex.
2. Pattern must comply with RFC 5322 practical subset (no exotic edge cases).
3. Handle None/empty input gracefully.
4. Include docstring with examples.
5. Add type hints.
6. Before responding, verify against RFC 5322 test cases.

## 4. Pitfalls to Avoid
- Do not use overly permissive regex (e.g., `.+@.+\..+`).
- Do not reject valid addresses with +tags, subdomains, or new TLDs.
- Do not hardcode TLD lists.
- Do not omit None/empty checks.
- Do not use placeholder regex.

## 5. Examples and Response Format
```python
def validate_email(email: str) -> bool:
    """Validate email per RFC 5322 practical subset.
    
    >>> validate_email("user@example.com")
    True
    >>> validate_email("invalid")
    False
    """
    ...
```

Do you have any questions to ask me that will help you respond appropriately?
```

---

## Example 3: Documentation Task

### Input (Draft)
```
Document the REST API endpoints for user management.
```

### Enhanced Output Structure
```
## 1. Role
You are a senior technical writer and API documentation specialist experienced with OpenAPI 3.0 and developer portal standards.

## 2. Context
A SaaS platform needs public API documentation for user management endpoints (CRUD + auth). Audience: external developers integrating with the API. Input: existing endpoint list and auth scheme.

## 3. Task and Commands
1. Create OpenAPI 3.0 spec for /users/* endpoints.
2. Include: GET/POST /users, GET/PUT/DELETE /users/{id}, POST /auth/login, POST /auth/refresh.
3. Document request/response schemas with examples.
4. Add authentication scheme (Bearer JWT).
5. Include error responses (400, 401, 404, 422, 500).
6. Before responding, validate spec with `swagger-codegen validate`.

## 4. Pitfalls to Avoid
- Do not omit required fields in schemas.
- Do not use placeholder example values.
- Do not forget to document rate limits.
- Do not assume prior knowledge of auth flow.

## 5. Examples and Response Format
Output: `openapi.yaml` with:
- info, servers, security schemes
- paths with all operations
- components/schemas for User, Error, TokenResponse
- examples for each response

Do you have any questions to ask me that will help you respond appropriately?
```

---

## Example 4: Analysis Task

### Input (Draft)
```
Analyze the performance bottleneck in this database query.
```

### Enhanced Output Structure
```
## 1. Role
You are a senior database engineer and performance analyst with expertise in PostgreSQL query optimization, execution plans, and indexing strategies.

## 2. Context
A production query is exceeding 5s p95 latency. The query, schema, EXPLAIN ANALYZE output, and table statistics will be provided. Output must be actionable optimization steps.

## 3. Task and Commands
1. Analyze EXPLAIN ANALYZE output for actual vs estimated rows.
2. Identify sequential scans, expensive joins, missing indexes.
3. Propose up to 3 index recommendations with CREATE INDEX statements.
4. Estimate impact using `pg_stat_statements` if available.
5. Provide before/after comparison template.
6. Before responding, verify each recommendation reduces cost.

## 4. Pitfalls to Avoid
- Do not suggest indexes without checking write overhead.
- Do not ignore correlation between columns.
- Do not recommend partitioning without data volume justification.
- Do not present assumptions as measured findings.

## 5. Examples and Response Format
```
### Findings
- Seq scan on users (1.2M rows) — missing index on status
- Nested loop join — consider hash join via enable_nestloop=off

### Recommendations
1. CREATE INDEX CONCURRENTLY idx_users_status ON users(status) WHERE status='active';
...

### Validation Template
| Metric | Before | After | Target |
|--------|--------|-------|--------|
| p95 latency | 5.2s | ? | <500ms |
```

Do you have any questions to ask me that will help you respond appropriately?
```