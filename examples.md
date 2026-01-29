# Claude Skills Examples

This document provides practical examples of different skill patterns and use cases.

## Table of Contents

1. [Simple Task Skill](#simple-task-skill)
2. [Multi-Step Workflow Skill](#multi-step-workflow-skill)
3. [Code Analysis Skill](#code-analysis-skill)
4. [Documentation Generation Skill](#documentation-generation-skill)
5. [Testing and Validation Skill](#testing-and-validation-skill)
6. [Conditional Logic Skill](#conditional-logic-skill)
7. [Data Transformation Skill](#data-transformation-skill)
8. [Review and Feedback Skill](#review-and-feedback-skill)

---

## Simple Task Skill

A basic skill for a straightforward, single-purpose task.

### Example: Text Summarizer

```markdown
---
name: text-summarizer
version: 1.0.0
description: Summarize text to specified length and style
tags: [text-processing, summarization, utility]
---

# Text Summarizer

## Overview

Condense text while preserving key information and main points.

## When to Use

- Text exceeds desired length
- Need executive summary
- Creating abstract or overview

## Instructions

### Step 1: Analyze Content

Read the input text and identify:
- Main topic or thesis
- Key supporting points (3-5 major ideas)
- Critical data or conclusions

### Step 2: Determine Target Length

Confirm desired summary length:
- Brief: 2-3 sentences
- Standard: 1 paragraph (4-6 sentences)
- Extended: 2-3 paragraphs

### Step 3: Generate Summary

Create summary that:
- Captures main thesis in first sentence
- Includes essential supporting points
- Maintains original tone and intent
- Omits minor details and examples

## Examples

### Example 1: Brief Summary

**Input:** [500-word article about climate change]
**Output:** "Climate change is accelerating due to increased greenhouse gas emissions, 
with global temperatures rising 1.1°C since pre-industrial times. Scientists warn 
that without immediate action to reduce emissions, we face severe ecological and 
economic consequences by 2050."

### Example 2: Standard Summary

**Input:** [2000-word research paper]
**Output:** [150-word summary preserving methodology and findings]
```

**Usage Pattern:**
- Single, focused task
- Clear input/output
- Minimal decision points

---

## Multi-Step Workflow Skill

Skills that guide through complex, sequential processes.

### Example: API Documentation Generator

```markdown
---
name: api-doc-generator
version: 1.0.0
description: Generate comprehensive API documentation from code
tags: [documentation, api, automation]
---

# API Documentation Generator

## Overview

Create standardized API documentation from source code and comments.

## Instructions

### Step 1: Extract API Definitions

Parse source files to identify:
- Endpoint paths and HTTP methods
- Request parameters and body schemas
- Response formats and status codes
- Authentication requirements

### Step 2: Extract Documentation

From comments and docstrings, extract:
- Endpoint purpose and description
- Parameter descriptions and constraints
- Example requests and responses
- Error conditions and codes

### Step 3: Organize Documentation

Group endpoints by:
- Resource type (users, orders, products)
- Functionality (authentication, CRUD operations)
- API version

### Step 4: Generate Output

Create documentation with:
- Table of contents
- Authentication section
- Endpoint reference (one per endpoint)
- Common errors section
- Example workflows

### Step 5: Validate

Verify documentation includes:
- All public endpoints
- Complete parameter descriptions
- Valid example requests/responses
- Current version information

## Output Format

\`\`\`markdown
# API Documentation v1.0

## Authentication
[Auth details]

## Endpoints

### GET /api/users
**Description:** Retrieve user list
**Parameters:**
- page (integer, optional): Page number (default: 1)
- limit (integer, optional): Results per page (default: 20)

**Response:**
\`\`\`json
{
  "users": [...],
  "total": 150,
  "page": 1
}
\`\`\`
```

**Usage Pattern:**
- Sequential steps with dependencies
- Complex output generation
- Validation and quality checks

---

## Code Analysis Skill

Skills for examining and evaluating code.

### Example: Code Review Assistant

```markdown
---
name: code-review-assistant
version: 1.0.0
description: Provide structured code review feedback
tags: [code-review, quality, best-practices]
---

# Code Review Assistant

## Instructions

### Step 1: Understand Context

Review:
- Pull request description
- Related issues or tickets
- Changed files and diff

### Step 2: Check Code Quality

Evaluate:
- **Correctness**: Logic errors, edge cases
- **Performance**: Algorithmic efficiency, resource usage
- **Security**: Input validation, auth checks, data exposure
- **Maintainability**: Readability, naming, structure

### Step 3: Verify Standards

Check adherence to:
- Language conventions and style guide
- Project patterns and architecture
- Testing requirements
- Documentation standards

### Step 4: Provide Feedback

Structure comments as:

**Critical Issues** (must fix):
- Security vulnerabilities
- Logic errors
- Breaking changes

**Suggestions** (should consider):
- Performance improvements
- Code clarity
- Better patterns

**Nitpicks** (optional):
- Style preferences
- Minor optimizations

### Step 5: Summarize

Provide:
- Overall assessment (approve/request changes)
- Key themes
- Learning opportunities

## Example Output

**Critical Issues:**
1. Line 45: SQL injection vulnerability - use parameterized queries
2. Line 78: Null pointer exception possible when user is undefined

**Suggestions:**
1. Lines 30-60: Consider extracting to separate function for clarity
2. Line 92: Use Array.map() instead of forEach for functional approach

**Positive Notes:**
- Good test coverage (85%)
- Clear variable naming
- Proper error handling in API calls
```

**Usage Pattern:**
- Analytical evaluation
- Structured feedback format
- Prioritized recommendations

---

## Documentation Generation Skill

Skills that create structured documentation.

### Example: README Generator

```markdown
---
name: readme-generator
version: 1.0.0
description: Generate comprehensive README files for projects
tags: [documentation, readme, automation]
---

# README Generator

## Instructions

### Step 1: Gather Project Information

Identify:
- Project name and purpose
- Key features
- Technology stack
- Target audience

### Step 2: Analyze Codebase

Extract:
- Installation requirements
- Configuration options
- Main entry points
- Example usage from tests/examples

### Step 3: Generate Structure

Create sections:
1. Title and description
2. Features
3. Installation
4. Usage
5. Configuration
6. API Reference (if applicable)
7. Contributing
8. License

### Step 4: Add Details

For each section:
- Use clear, concise language
- Include code examples
- Add badges (build status, version)
- Link to additional resources

## Template

\`\`\`markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\`\`\`bash
npm install project-name
\`\`\`

## Usage

\`\`\`javascript
const project = require('project-name');
// Example code
\`\`\`

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| opt1   | str  | "value" | Description |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT
\`\`\`
```

**Usage Pattern:**
- Template-based generation
- Information extraction
- Standardized output format

---

## Testing and Validation Skill

Skills for verifying correctness and quality.

### Example: Test Case Generator

```markdown
---
name: test-case-generator
version: 1.0.0
description: Generate comprehensive test cases from requirements
tags: [testing, quality-assurance, automation]
---

# Test Case Generator

## Instructions

### Step 1: Analyze Requirements

Identify:
- Core functionality
- Input parameters and types
- Expected outputs
- Edge cases and constraints

### Step 2: Design Test Cases

Create tests for:
- **Happy path**: Standard, expected usage
- **Edge cases**: Boundary values, empty inputs
- **Error cases**: Invalid inputs, exceptions
- **Integration**: Interactions with dependencies

### Step 3: Structure Tests

For each test case:
- Clear description
- Setup/preconditions
- Input data
- Expected output
- Assertions

### Step 4: Generate Code

Output in appropriate testing framework:
- Jest/Mocha (JavaScript)
- pytest (Python)
- JUnit (Java)

## Example

**Function to test:**
```python
def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

**Generated tests:**
```python
def test_divide_positive_numbers():
    assert divide(10, 2) == 5

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5

def test_divide_by_one():
    assert divide(10, 1) == 10

def test_divide_zero_dividend():
    assert divide(0, 5) == 0

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_float_result():
    assert abs(divide(10, 3) - 3.333) < 0.001
```
```

**Usage Pattern:**
- Requirement analysis
- Systematic coverage
- Code generation

---

## Conditional Logic Skill

Skills with branching logic based on context.

### Example: Error Handler

```markdown
---
name: error-handler
version: 1.0.0
description: Diagnose and handle errors with appropriate strategies
tags: [error-handling, debugging, troubleshooting]
---

# Error Handler

## Instructions

### Step 1: Classify Error

Determine error type:

**If** syntax error:
- Identify location and type
- Explain the syntax rule violated
- Provide corrected code

**Else if** runtime error:
- Analyze stack trace
- Identify root cause
- Suggest fix and prevention

**Else if** logical error:
- Review expected vs actual behavior
- Trace data flow
- Identify incorrect logic

**Else if** configuration error:
- Check configuration files
- Verify environment variables
- Validate dependencies

### Step 2: Assess Severity

**Critical** (system down):
- Immediate fix required
- Provide hotfix solution
- Plan long-term fix

**High** (feature broken):
- Fix in current sprint
- Provide workaround
- Add tests

**Medium** (degraded performance):
- Schedule fix
- Monitor impact
- Document issue

**Low** (minor issue):
- Add to backlog
- Document for future
- Consider if fix needed

### Step 3: Provide Solution

Based on error type and severity:
1. Immediate action to take
2. Code fix or configuration change
3. Testing to verify fix
4. Prevention for future

## Example

**Error:**
```
TypeError: Cannot read property 'name' of undefined
  at getUsername (app.js:15)
```

**Analysis:**
- Type: Runtime error
- Severity: High
- Cause: Accessing property on undefined object

**Solution:**
```javascript
// Before
function getUsername(user) {
  return user.name;
}

// After
function getUsername(user) {
  if (!user) {
    throw new Error('User object is required');
  }
  return user.name;
}

// Or with optional chaining
function getUsername(user) {
  return user?.name ?? 'Anonymous';
}
```
```

**Usage Pattern:**
- Decision trees
- Context-dependent actions
- Multiple outcome paths

---

## Data Transformation Skill

Skills for converting data between formats.

### Example: Schema Converter

```markdown
---
name: schema-converter
version: 1.0.0
description: Convert data schemas between different formats
tags: [data, schema, conversion]
---

# Schema Converter

## Instructions

### Step 1: Parse Source Schema

Identify source format:
- JSON Schema
- OpenAPI/Swagger
- GraphQL Schema
- Database DDL
- TypeScript interfaces

Extract:
- Field names and types
- Constraints (required, min/max, pattern)
- Nested structures
- Relationships

### Step 2: Map Types

Convert types to target format:

| JSON Schema | TypeScript | Python | SQL |
|-------------|------------|--------|-----|
| string      | string     | str    | VARCHAR |
| number      | number     | float  | DECIMAL |
| integer     | number     | int    | INTEGER |
| boolean     | boolean    | bool   | BOOLEAN |
| array       | T[]        | List[T]| JSON |
| object      | interface  | Dict   | JSON |

### Step 3: Generate Target Schema

Create valid schema in target format:
- Apply naming conventions
- Add required metadata
- Include documentation
- Validate output

## Example

**Input (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "id": {"type": "integer"},
    "name": {"type": "string", "minLength": 1},
    "email": {"type": "string", "format": "email"},
    "active": {"type": "boolean"}
  },
  "required": ["id", "name", "email"]
}
```

**Output (TypeScript):**
```typescript
interface User {
  id: number;
  name: string;
  email: string;
  active?: boolean;
}
```

**Output (Python):**
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    name: str
    email: str
    active: Optional[bool] = None
```
```

**Usage Pattern:**
- Format detection
- Type mapping
- Structure preservation

---

## Review and Feedback Skill

Skills for evaluating and providing constructive feedback.

### Example: Document Reviewer

```markdown
---
name: document-reviewer
version: 1.0.0
description: Review documents for clarity, accuracy, and completeness
tags: [review, documentation, quality]
---

# Document Reviewer

## Instructions

### Step 1: Read for Understanding

First pass:
- Understand overall purpose
- Identify target audience
- Note structure and flow

### Step 2: Evaluate Content

Check for:
- **Accuracy**: Facts, examples, technical details
- **Completeness**: All topics covered, no gaps
- **Clarity**: Easy to understand, no ambiguity
- **Conciseness**: No unnecessary verbosity

### Step 3: Review Structure

Assess:
- Logical organization
- Appropriate heading hierarchy
- Smooth transitions
- Table of contents (if needed)

### Step 4: Check Style

Verify:
- Consistent terminology
- Appropriate tone for audience
- Grammar and spelling
- Formatting consistency

### Step 5: Provide Feedback

Structure as:

**Strengths:**
- What works well
- Effective sections

**Content Issues:**
- Missing information
- Incorrect details
- Unclear sections

**Structural Improvements:**
- Organization changes
- Better flow
- Section additions/removals

**Style Suggestions:**
- Wording improvements
- Formatting tweaks
- Consistency fixes

## Example Output

**Strengths:**
- Clear introduction that sets context
- Good use of examples in section 3
- Helpful diagrams

**Content Issues:**
1. Section 2.1: Missing explanation of authentication flow
2. Section 4: Example code has syntax error
3. Prerequisites section incomplete - missing Node.js version

**Structural Improvements:**
1. Move "Common Errors" section before "Advanced Usage"
2. Split section 5 into two separate sections
3. Add troubleshooting section

**Style Suggestions:**
1. Use consistent heading style (sentence case vs title case)
2. Replace passive voice in instructions ("The file is opened" → "Open the file")
3. Fix inconsistent code formatting
```

**Usage Pattern:**
- Multi-criteria evaluation
- Structured feedback
- Actionable recommendations

---

## Skill Composition Example

Skills can reference and build on each other:

```markdown
---
name: full-stack-feature-builder
version: 1.0.0
description: Build complete feature from spec to deployment
tags: [development, full-stack, automation]
dependencies:
  - api-endpoint-generator
  - database-schema-creator
  - test-case-generator
  - api-doc-generator
---

# Full Stack Feature Builder

## Overview

Build a complete feature including database, API, tests, and documentation.

## Instructions

### Step 1: Database Schema
Apply **database-schema-creator** skill to:
- Design schema from requirements
- Generate migration files
- Create seed data

### Step 2: API Implementation
Apply **api-endpoint-generator** skill to:
- Create endpoint handlers
- Implement business logic
- Add validation

### Step 3: Testing
Apply **test-case-generator** skill to:
- Generate unit tests
- Create integration tests
- Add E2E tests

### Step 4: Documentation
Apply **api-doc-generator** skill to:
- Generate API documentation
- Create usage examples
- Update README

### Step 5: Review
Apply **code-review-assistant** skill to:
- Review generated code
- Check for issues
- Validate completeness
```

This demonstrates how simple skills can be composed into powerful workflows.

---

## Additional Resources

- See [examples/](examples/) directory for complete skill implementations
- Review [reference.md](reference.md) for detailed technical documentation
- Check [QUICKSTART.md](QUICKSTART.md) for getting started guide
