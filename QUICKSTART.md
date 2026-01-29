# Claude Skills Quickstart Guide

Get started creating your first Claude skill in 10 minutes.

## Table of Contents

1. [What You'll Build](#what-youll-build)
2. [Prerequisites](#prerequisites)
3. [Step 1: Create Skill File](#step-1-create-skill-file)
4. [Step 2: Add Metadata](#step-2-add-metadata)
5. [Step 3: Write Instructions](#step-3-write-instructions)
6. [Step 4: Add Examples](#step-4-add-examples)
7. [Step 5: Test Your Skill](#step-5-test-your-skill)
8. [Next Steps](#next-steps)

## What You'll Build

A simple "Commit Message Generator" skill that creates standardized Git commit messages following conventional commit format.

**Learning Goals:**
- Understand skill structure
- Write effective instructions
- Create practical examples
- Test and refine a skill

**Time Required:** ~10 minutes

## Prerequisites

- Text editor
- Basic understanding of markdown
- Familiarity with Git commits (for this example)

## Step 1: Create Skill File

Create a new directory and file:

```bash
mkdir commit-message-generator
cd commit-message-generator
touch SKILL.md
```

Open `SKILL.md` in your text editor.

## Step 2: Add Metadata

Add YAML frontmatter at the top of the file:

```markdown
---
name: commit-message-generator
version: 1.0.0
description: Generate conventional commit messages from code changes
author: Your Name
tags: [git, commit, automation, development]
category: development
license: MIT
created: 2024-01-01
---
```

**Key Points:**
- `name`: Use lowercase with hyphens (kebab-case)
- `version`: Follow semantic versioning (major.minor.patch)
- `description`: One clear sentence explaining what it does
- `tags`: Help with discoverability

## Step 3: Write Instructions

Add the main skill content:

```markdown
# Commit Message Generator

## Overview

Generate well-formatted commit messages following the Conventional Commits specification.

## When to Use

Use this skill when:
- You've made code changes and need to commit
- You want consistent, standardized commit messages
- You need to convey changes clearly to your team

## Instructions

### Step 1: Analyze Changes

Review the code changes and identify:
- What was changed (files, functions, features)
- Why the change was made (purpose)
- Impact of the change (breaking, feature, fix)

### Step 2: Determine Commit Type

Select the appropriate type:
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **style**: Formatting, no code change
- **refactor**: Code restructuring, no behavior change
- **test**: Adding or updating tests
- **chore**: Maintenance, dependencies, config

### Step 3: Identify Scope (Optional)

Determine the component affected:
- Module name (e.g., auth, api, ui)
- Feature area (e.g., user-profile, checkout)
- Keep it brief and lowercase

### Step 4: Write Description

Create a concise description (50 chars or less):
- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter
- No period at the end
- Be specific but brief

### Step 5: Add Body (If Needed)

For complex changes, add body with:
- More detailed explanation
- Motivation for the change
- Contrast with previous behavior
- Wrap at 72 characters

### Step 6: Note Breaking Changes

If breaking change:
- Add `BREAKING CHANGE:` footer
- Explain what breaks
- Describe migration path

### Step 7: Format Message

Combine into final format:
```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```
```

**Key Points:**
- Each step is actionable
- Clear decision criteria
- Specific examples
- Handles edge cases

## Step 4: Add Examples

Add practical examples:

```markdown
## Examples

### Example 1: Simple Feature

**Changes:**
- Added new user authentication endpoint
- Created login handler
- Added tests

**Generated Commit:**
```
feat(auth): add user login endpoint

Implements POST /api/auth/login with JWT token generation.
Includes validation for email and password fields.
```

### Example 2: Bug Fix

**Changes:**
- Fixed null pointer exception in user profile
- Added null check

**Generated Commit:**
```
fix(profile): prevent crash when user data is missing

Added null check before accessing user.email property.
Fixes issue #123.
```

### Example 3: Breaking Change

**Changes:**
- Changed API response format from XML to JSON
- Updated all endpoints

**Generated Commit:**
```
feat(api): migrate response format to JSON

Changed all API endpoints to return JSON instead of XML
for better client compatibility and reduced payload size.

BREAKING CHANGE: All API responses now return JSON.
Clients must update Accept headers and parsing logic.
Migration guide: docs/api-migration-v2.md
```

### Example 4: Documentation

**Changes:**
- Updated README with new installation steps
- Added troubleshooting section

**Generated Commit:**
```
docs: update installation instructions

Added npm alternative installation method and
troubleshooting section for common setup issues.
```
```

**Key Points:**
- Real-world scenarios
- Show input (changes) and output (commit)
- Cover different types
- Include edge cases

## Step 5: Test Your Skill

### 5.1 Self-Test

Try using your skill with Claude:

1. Describe some code changes
2. Ask Claude to use the commit-message-generator skill
3. Verify the output follows the format
4. Check for clarity and accuracy

### 5.2 Refine

Based on testing:
- Are instructions clear?
- Do examples cover common cases?
- Is anything confusing or missing?
- Could steps be simplified?

### 5.3 Add Best Practices and Notes

Add any learnings:

```markdown
## Best Practices

1. **Be Specific**: "fix login bug" → "fix password validation in login"
2. **Keep Description Short**: Aim for 50 characters or less
3. **Use Imperative Mood**: "add feature" not "added feature"
4. **Reference Issues**: Include issue numbers when relevant
5. **One Concern Per Commit**: Split unrelated changes into separate commits

## Common Mistakes

- ❌ "Updated files" → Too vague
- ❌ "Fixed bug" → What bug?
- ❌ "Added new feature for users to login and register" → Too long
- ✅ "feat(auth): add user registration endpoint" → Clear and concise

## Notes

- This skill follows [Conventional Commits 1.0.0](https://www.conventionalcommits.org/)
- Commit messages are for humans - prioritize clarity
- When in doubt, err on the side of more detail
```

## Your Complete Skill

Here's what your complete `SKILL.md` should look like:

```markdown
---
name: commit-message-generator
version: 1.0.0
description: Generate conventional commit messages from code changes
author: Your Name
tags: [git, commit, automation, development]
category: development
license: MIT
created: 2024-01-01
---

# Commit Message Generator

## Overview

Generate well-formatted commit messages following the Conventional Commits specification.

## When to Use

Use this skill when:
- You've made code changes and need to commit
- You want consistent, standardized commit messages
- You need to convey changes clearly to your team

[... rest of the skill content ...]
```

## Next Steps

### Enhance Your Skill

1. **Add Validation Section**
   ```markdown
   ## Validation
   
   Verify your commit message:
   - [ ] Type is one of the standard types
   - [ ] Description is under 50 characters
   - [ ] Uses imperative mood
   - [ ] Scope is relevant and lowercase
   - [ ] Breaking changes are documented
   ```

2. **Create Templates Directory**
   ```bash
   mkdir templates
   ```
   
   Add `templates/commit-template.txt`:
   ```
   <type>(<scope>): <description>
   
   [Body - explain what and why]
   
   [Footer - breaking changes, issues]
   ```

3. **Add Helper Script**
   ```bash
   mkdir scripts
   ```
   
   Add `scripts/validate-commit.sh`:
   ```bash
   #!/bin/bash
   # Validate commit message format
   # Usage: ./validate-commit.sh "feat(api): add endpoint"
   
   message=$1
   pattern='^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .{1,50}$'
   
   if [[ $message =~ $pattern ]]; then
     echo "✓ Valid commit message"
     exit 0
   else
     echo "✗ Invalid commit message format"
     exit 1
   fi
   ```

### Create More Skills

Try creating skills for:
- Code review checklist
- Bug report generator
- PR description creator
- Release notes generator

### Explore Example Skills

Check out the complete example skills:
- [examples/archunit-architecture-tester/](examples/archunit-architecture-tester/)
- [examples/text-summarizer/](examples/text-summarizer/)
- [examples/api-documentation-generator/](examples/api-documentation-generator/)
- [examples/code-review-assistant/](examples/code-review-assistant/)

### Learn More

- **[reference.md](reference.md)**: Detailed technical documentation
- **[examples.md](examples.md)**: More skill patterns and examples
- **[ENTERPRISE.md](ENTERPRISE.md)**: Governance for larger teams
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Share your skills

## Tips for Success

1. **Start Simple**: Begin with straightforward, single-purpose skills
2. **Test Thoroughly**: Use your skill multiple times with different scenarios
3. **Iterate**: Refine based on real usage
4. **Document Well**: Future you will thank present you
5. **Share**: Contributing helps everyone improve

## Getting Help

- Review existing skills for patterns
- Check the reference guide for details
- Test incrementally as you build
- Keep instructions clear and concise

## Congratulations! 🎉

You've created your first Claude skill! You now understand:
- Skill structure and metadata
- How to write effective instructions
- Creating useful examples
- Testing and refinement

Start building more skills to automate your workflows and share knowledge with your team.
