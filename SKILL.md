---
name: skill-template-creation
version: 1.0.0
description: Create Claude Skills in the user's current workspace using templates and best practices
author: Claude Skills Team
tags: [skill-creation, template, automation, development]
category: development
license: MIT
created: 2024-01-01
updated: 2024-01-01
---

# Skill Template Creation

## Overview

This skill enables Claude to create well-structured Claude Skills directly in the **user's current workspace** (their active working directory or repository). It follows established templates, best practices, and documentation standards to ensure consistent skill structure, proper metadata, and comprehensive documentation for every skill created.

## Purpose

Help users create professional Claude Skills by:
- Generating skill files in the user's current working directory
- Following the SKILL-Template.md structure consistently
- Including proper YAML frontmatter metadata
- Providing clear, actionable instructions and examples

## When to Use

- User requests creation of a new Claude Skill
- User wants to automate a task using a custom skill
- User needs a skill template for their project
- User wants to add Claude Skills to their existing repository

## Output Location

**IMPORTANT:** All skills created using this template should be saved in the **user's current workspace** - their active working directory or repository. The skill files should be created:

1. **In the user's current directory** - If the user is working in a specific project folder
2. **In a specified subdirectory** - If the user requests a specific location (e.g., `.claude/skills/` or `skills/`)
3. **As a standalone skill folder** - Create a dedicated directory for the skill (e.g., `my-skill-name/SKILL.md`)

## Instructions

### Step 1: Understand User Requirements

Before creating a skill, gather the following information from the user:
- **Skill purpose**: What task or workflow should the skill accomplish?
- **Target audience**: Who will use this skill?
- **Inputs**: What information does the skill need?
- **Outputs**: What should the skill produce?
- **Constraints**: Any specific limitations or requirements?

### Step 2: Review Template and References

Study the template and reference documentation to ensure compliance:

| Resource | Location | Purpose |
|----------|----------|---------|
| Skill Template | `SKILL-Template.md` | Structure and format reference |
| Examples | `examples.md` | Pattern examples and use cases |
| Reference Guide | `reference.md` | Comprehensive technical documentation |
| Example Skills | `examples/` directory | Complete skill implementations |

### Step 3: Design the Skill Structure

Plan the skill before creating files:

1. **Choose a descriptive name** (kebab-case, e.g., `api-documentation-generator`)
2. **Define the category** (development, documentation, testing, analysis, utility)
3. **List relevant tags** for discoverability
4. **Outline the main steps** the skill will perform
5. **Identify 2-3 concrete examples** to demonstrate usage

### Step 4: Create the Skill File

Create the skill in the **user's current workspace** with this structure:

```
<user-workspace>/
└── <skill-name>/
    ├── SKILL.md          # Main skill document (required)
    ├── examples.md       # Extended examples (optional)
    └── README.md         # Skill documentation (optional)
```

**For single-file skills**, create directly in the workspace:
```
<user-workspace>/
└── <skill-name>.md
```

### Step 5: Write YAML Frontmatter

Include proper metadata at the top of SKILL.md:

```yaml
---
name: skill-name-here
version: 1.0.0
description: Brief one-line description of what the skill does
author: Author Name
tags: [relevant, tags, here]
category: development
license: MIT
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Step 6: Write Skill Content

Include these sections in order:

1. **Overview** (2-3 sentences): What the skill does
2. **When to Use**: Clear conditions that trigger skill usage
3. **Instructions**: Step-by-step guidance with specific actions
4. **Examples**: At least 2 practical examples with input/output
5. **Best Practices**: Tips for optimal results
6. **Error Handling**: Common errors and solutions

### Step 7: Validate the Skill

Before finalizing, verify:
- [ ] Name uses kebab-case format
- [ ] Version follows semantic versioning (X.Y.Z)
- [ ] Description is clear and concise
- [ ] All required sections are present (Overview, Instructions, Examples)
- [ ] Instructions are actionable with clear steps
- [ ] Examples show realistic input and expected output
- [ ] No typos or grammatical errors

### Step 8: Save and Confirm

1. Save the skill file(s) in the user's workspace
2. Confirm the file location with the user
3. Provide a summary of what was created
4. Suggest next steps (testing, customization, integration)

## Examples

### Example 1: Creating a Simple Skill

**User Request:** "Create a skill that generates code review checklists"

**Actions:**
1. Create directory `code-review-checklist/` in user's workspace
2. Create `SKILL.md` with proper structure
3. Include examples for different code types (frontend, backend, API)

**Output Location:** `<user-workspace>/code-review-checklist/SKILL.md`

### Example 2: Creating a Skill in Custom Location

**User Request:** "Create a commit message generator skill in my `.claude/skills/` folder"

**Actions:**
1. Create directory `.claude/skills/commit-message-generator/`
2. Create `SKILL.md` with conventional commit format instructions
3. Include examples for different commit types

**Output Location:** `<user-workspace>/.claude/skills/commit-message-generator/SKILL.md`

## Best Practices

1. **Be Specific**: Provide clear, actionable instructions with no ambiguity
2. **Use Templates**: Follow the SKILL-Template.md structure consistently
3. **Include Examples**: Always provide at least 2 realistic examples
4. **Consider Edge Cases**: Address error scenarios and fallback strategies
5. **Keep It Focused**: One skill should accomplish one type of task
6. **Test the Skill**: Verify the skill works as expected before finalizing
7. **Document Dependencies**: Note any required tools, APIs, or prerequisites

## Error Handling

| Error | Solution |
|-------|----------|
| User workspace not clear | Ask user to specify the target directory |
| Skill name conflicts | Suggest alternative names or confirm overwrite |
| Missing required information | Request clarification from user |
| Invalid name format | Convert to kebab-case automatically |

## Notes

- Always create skills in the **user's workspace**, not in this template repository
- If uncertain about location, ask the user to confirm the target directory
- For complex skills, consider splitting into multiple files (main SKILL.md + examples.md)
- Refer to `examples/` directory for complete skill implementations as reference
