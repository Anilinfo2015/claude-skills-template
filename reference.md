# Claude Skills Reference Guide

## Table of Contents

1. [Introduction](#introduction)
2. [What are Claude Skills?](#what-are-claude-skills)
3. [Architecture and Design](#architecture-and-design)
4. [Skill Structure](#skill-structure)
5. [YAML Frontmatter](#yaml-frontmatter)
6. [Writing Effective Skills](#writing-effective-skills)
7. [Progressive Disclosure](#progressive-disclosure)
8. [Best Practices](#best-practices)
9. [Integration Patterns](#integration-patterns)
10. [Advanced Topics](#advanced-topics)

## Introduction

This reference guide provides comprehensive technical documentation for creating, organizing, and using Claude Skills. Skills are structured documents that enhance Claude's capabilities by providing specialized knowledge, workflows, and instructions for specific tasks.

## What are Claude Skills?

Claude Skills are markdown documents with YAML frontmatter that contain:

- **Metadata**: Information about the skill (name, version, description, etc.)
- **Instructions**: Step-by-step guidance for accomplishing specific tasks
- **Examples**: Practical demonstrations of the skill in action
- **Context**: Relevant information needed to execute the skill effectively

### Key Benefits

1. **Reusability**: Package complex workflows for repeated use
2. **Consistency**: Ensure standardized approaches to common tasks
3. **Knowledge Sharing**: Distribute expertise across teams
4. **Efficiency**: Reduce repetitive explanations and instructions
5. **Scalability**: Build libraries of organizational knowledge

## Architecture and Design

### Progressive Disclosure Pattern

Skills follow a progressive disclosure pattern optimized for LLM context management:

1. **Metadata Layer** (Always Loaded)
   - YAML frontmatter with name, description, tags
   - Lightweight (~100-200 tokens)
   - Enables skill discovery and selection

2. **Instruction Layer** (Loaded On-Demand)
   - Detailed instructions and examples
   - Loaded only when skill is activated
   - Optimizes context window usage

### File Organization

```
skill-name/
├── SKILL.md           # Main skill document
├── examples.md        # Extended examples (optional)
├── templates/         # Template files (optional)
├── scripts/          # Helper scripts (optional)
└── README.md         # Skill documentation (optional)
```

## Skill Structure

### Basic Template

```markdown
---
name: skill-name
version: 1.0.0
description: Brief one-line description
author: Author Name
tags: [tag1, tag2, tag3]
---

# Skill Name

## Overview
[Brief overview]

## Instructions
[Step-by-step instructions]

## Examples
[Practical examples]
```

### Sections Breakdown

#### 1. Overview
- **Purpose**: 2-3 sentences explaining what the skill does
- **Scope**: What the skill covers and doesn't cover
- **Prerequisites**: Required knowledge or tools

#### 2. When to Use
- Clear conditions that trigger skill usage
- Use cases and scenarios
- Decision criteria

#### 3. Instructions
- Numbered steps for clarity
- Action-oriented language
- Clear success criteria for each step

#### 4. Examples
- Real-world scenarios
- Input/output pairs
- Edge cases and variations

#### 5. Best Practices
- Tips for optimal results
- Common pitfalls to avoid
- Performance considerations

#### 6. Error Handling
- Expected errors and solutions
- Fallback strategies
- Validation approaches

## YAML Frontmatter

### Required Fields

```yaml
name: skill-identifier           # Lowercase with hyphens
version: 1.0.0                   # Semantic versioning
description: Brief description   # One-line summary
```

### Recommended Fields

```yaml
author: Author Name or Team
tags: [category, technology, use-case]
license: MIT
created: 2024-01-01
updated: 2024-01-01
category: development | documentation | testing | analysis
```

### Optional Fields

```yaml
requirements:
  - Requirement 1
  - Requirement 2
dependencies:
  - other-skill-name
related_skills:
  - related-skill-1
  - related-skill-2
maturity: experimental | stable | deprecated
complexity: low | medium | high
estimated_time: "5-10 minutes"
```

## Writing Effective Skills

### Instruction Design Principles

#### 1. Clarity
- Use simple, direct language
- Avoid ambiguity
- Define technical terms

#### 2. Conciseness
- Remove unnecessary words
- Focus on essential information
- Use bullet points for lists

#### 3. Actionability
- Start with action verbs
- Provide specific steps
- Include measurable outcomes

#### 4. Context-Awareness
- Provide necessary context
- Don't overload with background
- Link to additional resources

### Example Quality Guidelines

**Good Example:**
```markdown
### Step 1: Validate Input

Check that the input meets these criteria:
- Contains at least one code block
- Uses supported language syntax
- Has clear function boundaries

If validation fails, request clarification.
```

**Poor Example:**
```markdown
### Step 1: Do Validation

You should probably check the input to make sure it's okay.
Maybe look at it and see if it seems right.
```

## Progressive Disclosure

### Implementation Strategy

1. **Skill Discovery**
   ```yaml
   # Lightweight metadata for browsing
   name: api-doc-generator
   description: Generate API documentation from code
   tags: [documentation, api, automation]
   ```

2. **Skill Activation**
   ```markdown
   # Load full instructions when needed
   ## Instructions
   [Detailed step-by-step process]
   ```

3. **On-Demand Details**
   ```markdown
   # Link to extended resources
   See examples.md for more scenarios
   See templates/ for output formats
   ```

### Context Management

- Keep core instructions under 2000 tokens
- Move extensive examples to separate files
- Use references instead of duplication
- Provide links to external documentation

## Best Practices

### Content Organization

1. **Hierarchical Structure**
   - Use clear heading hierarchy (H1 → H2 → H3)
   - Group related information
   - Maintain logical flow

2. **Modular Design**
   - Break complex skills into sub-skills
   - Create reusable components
   - Avoid monolithic documents

3. **Version Control**
   - Use semantic versioning
   - Document breaking changes
   - Maintain changelog

### Writing Style

1. **Voice and Tone**
   - Professional but approachable
   - Direct and authoritative
   - Consistent terminology

2. **Formatting**
   - Use code blocks for examples
   - Use tables for comparisons
   - Use callouts for important notes

3. **Examples**
   - Provide realistic scenarios
   - Show input and output
   - Include edge cases

### Testing and Validation

1. **Peer Review**
   - Have others test the skill
   - Gather feedback
   - Iterate based on results

2. **Real-World Testing**
   - Use with actual data
   - Test edge cases
   - Validate outputs

3. **Documentation**
   - Keep examples up-to-date
   - Document known issues
   - Provide troubleshooting tips

## Integration Patterns

### Skill Composition

Skills can reference and compose with other skills:

```markdown
## Prerequisites

This skill builds on:
- [Data Validation Skill](../data-validator/SKILL.md)
- [Error Handling Skill](../error-handler/SKILL.md)

## Instructions

1. First, apply the Data Validation Skill to inputs
2. Process the validated data
3. Use Error Handling Skill for any errors
```

### Workflow Integration

```markdown
## Workflow

This skill is typically used in this sequence:

1. Skill A: Prepare data
2. **This Skill**: Transform data
3. Skill C: Output results
```

### Tool Integration

```markdown
## Tool Requirements

This skill requires access to:
- File system (read/write)
- External API (with authentication)
- Database connection

Verify tool availability before proceeding.
```

## Advanced Topics

### Conditional Logic

```markdown
## Instructions

### Step 1: Determine Approach

**If** input is JSON:
- Parse using JSON schema validation
- Apply JSON-specific transformations

**Else if** input is XML:
- Parse using XML schema validation
- Apply XML-specific transformations

**Else**:
- Request format specification
- Provide format conversion options
```

### Error Recovery

```markdown
## Error Handling

### Recoverable Errors

1. **Invalid Format**
   - Attempt auto-correction
   - Suggest valid formats
   - Request user input

2. **Missing Data**
   - Use default values where appropriate
   - Request required information
   - Proceed with partial data if allowed

### Non-Recoverable Errors

1. **Authentication Failure**
   - Stop execution
   - Report error clearly
   - Suggest remediation

2. **Resource Unavailable**
   - Stop execution
   - Suggest alternatives
   - Log for later retry
```

### Performance Optimization

```markdown
## Performance Considerations

1. **Large Datasets**
   - Process in chunks
   - Use streaming where possible
   - Provide progress updates

2. **Complex Computations**
   - Break into smaller steps
   - Cache intermediate results
   - Parallelize when possible

3. **External Dependencies**
   - Implement timeouts
   - Use retry logic
   - Provide offline fallbacks
```

### Security Patterns

```markdown
## Security Guidelines

### Input Validation

1. **Sanitization**
   - Remove potentially harmful characters
   - Validate against expected patterns
   - Use allowlists over denylists

2. **Authentication**
   - Verify credentials before proceeding
   - Use secure credential storage
   - Implement proper access controls

3. **Data Protection**
   - Encrypt sensitive data
   - Avoid logging secrets
   - Use secure communication channels
```

### Metadata for Discovery

Effective tagging for skill discovery:

```yaml
tags:
  - Primary category (e.g., development, documentation)
  - Technology (e.g., python, javascript, api)
  - Use case (e.g., testing, automation, review)
  - Skill level (e.g., beginner, advanced)
```

### Multi-Language Support

```markdown
## Language Support

This skill supports:
- Python 3.8+
- JavaScript (ES6+)
- TypeScript 4.0+

### Language-Specific Notes

**Python:**
- Use type hints
- Follow PEP 8

**JavaScript:**
- Use modern syntax
- Prefer const/let over var
```

## Conclusion

Effective Claude Skills are:
- **Clear**: Easy to understand and follow
- **Concise**: No unnecessary complexity
- **Complete**: Cover the full workflow
- **Consistent**: Follow established patterns
- **Current**: Regularly updated and maintained

For more examples, see the [examples directory](examples/) and [examples.md](examples.md).

## Additional Resources

- [QUICKSTART.md](QUICKSTART.md) - Getting started guide
- [examples.md](examples.md) - Practical examples
- [ENTERPRISE.md](ENTERPRISE.md) - Enterprise governance
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contributing guidelines
