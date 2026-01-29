# Contributing to Claude Skills Template

Thank you for your interest in contributing! This guide will help you use this template and contribute improvements.

## Table of Contents

1. [How to Use This Template](#how-to-use-this-template)
2. [Creating Your Own Skills](#creating-your-own-skills)
3. [Contributing to This Template](#contributing-to-this-template)
4. [Code of Conduct](#code-of-conduct)
5. [Getting Help](#getting-help)

## How to Use This Template

### Quick Start

1. **Clone or Fork**
   ```bash
   git clone https://github.com/your-org/claude-skills-template.git
   cd claude-skills-template
   ```

2. **Review Documentation**
   - Read [QUICKSTART.md](QUICKSTART.md) for a 10-minute introduction
   - Check [reference.md](reference.md) for detailed technical docs
   - Browse [examples.md](examples.md) for patterns and ideas

3. **Explore Examples**
   ```bash
   cd examples
   ls -la
   ```
   Review the example skills to understand structure and patterns.

4. **Create Your First Skill**
   - Copy `SKILL.md` template
   - Follow the QUICKSTART guide
   - Test with Claude

### Using the Template Files

**Core Templates:**
- `SKILL.md`: Main template for creating new skills
- `templates/template.md`: Alternative template format
- `scripts/helper.py`: Python utilities for skill management
- `scripts/validate.sh`: Validation script for skill files

**Example Skills:**
Use these as references:
- `examples/text-summarizer/`: Simple, single-purpose skill
- `examples/api-documentation-generator/`: Complex, multi-step skill
- `examples/code-review-assistant/`: Analysis and feedback skill
- `examples/archunit-architecture-tester/`: Specialized technical skill

## Creating Your Own Skills

### Step-by-Step Process

#### 1. Plan Your Skill

Before writing, consider:
- **Purpose**: What specific problem does it solve?
- **Audience**: Who will use it?
- **Scope**: What's included and excluded?
- **Prerequisites**: What knowledge or tools are needed?

#### 2. Create Skill Directory

```bash
mkdir my-skill-name
cd my-skill-name
```

#### 3. Copy Template

```bash
cp ../SKILL.md ./SKILL.md
```

#### 4. Fill in Metadata

Edit the YAML frontmatter:

```yaml
---
name: my-skill-name
version: 1.0.0
description: Brief one-line description of what it does
author: Your Name or Team
tags: [category, technology, use-case]
license: MIT
created: 2024-01-01
updated: 2024-01-01
category: development
---
```

#### 5. Write Instructions

Follow these guidelines:
- Use clear, action-oriented language
- Number steps for sequential processes
- Include decision criteria
- Add error handling
- Keep it concise

#### 6. Add Examples

Include at least 2 examples:
- Basic/common case
- Advanced/edge case
- Show input and expected output
- Use realistic scenarios

#### 7. Test Thoroughly

- Use your skill with Claude multiple times
- Try different scenarios
- Test edge cases
- Get feedback from others

#### 8. Document Additional Details

Add optional but helpful sections:
- Best practices
- Common mistakes
- Troubleshooting
- Related skills
- Version history

### Skill Quality Checklist

Before considering your skill complete:

**Metadata:**
- [ ] Name is descriptive and uses kebab-case
- [ ] Version follows semantic versioning
- [ ] Description is clear and concise
- [ ] Tags are relevant and aid discovery
- [ ] All required fields are present

**Content:**
- [ ] Overview clearly explains purpose
- [ ] Instructions are step-by-step and actionable
- [ ] At least 2 examples are included
- [ ] Error handling is addressed
- [ ] Examples show realistic usage

**Quality:**
- [ ] Instructions are clear and unambiguous
- [ ] Examples work as shown
- [ ] No typos or grammatical errors
- [ ] Formatting is consistent
- [ ] Links work correctly

**Testing:**
- [ ] Tested with Claude successfully
- [ ] Tested with different inputs
- [ ] Edge cases considered
- [ ] Peer reviewed by at least one other person

## Contributing to This Template

We welcome contributions to improve this template!

### Types of Contributions

1. **Bug Fixes**
   - Typos or errors in documentation
   - Broken examples
   - Incorrect instructions

2. **Improvements**
   - Better examples
   - Clearer documentation
   - Additional helper scripts
   - Better templates

3. **New Example Skills**
   - Skills demonstrating new patterns
   - Skills for different domains
   - Skills showcasing best practices

4. **Documentation**
   - Expanded guides
   - Video tutorials
   - Translations
   - FAQ entries

### Contribution Process

#### 1. Fork and Clone

```bash
git fork https://github.com/your-org/claude-skills-template.git
git clone https://github.com/your-username/claude-skills-template.git
cd claude-skills-template
```

#### 2. Create a Branch

```bash
git checkout -b feature/my-contribution
```

Use branch naming conventions:
- `feature/description` for new features
- `fix/description` for bug fixes
- `docs/description` for documentation
- `example/skill-name` for new example skills

#### 3. Make Your Changes

- Follow existing code style
- Update relevant documentation
- Test your changes
- Keep commits focused and atomic

#### 4. Test Your Changes

For documentation:
- Proofread carefully
- Check all links work
- Verify formatting

For example skills:
- Test skill works with Claude
- Verify all examples
- Check metadata is complete

For scripts:
- Run tests if available
- Test manually
- Document any dependencies

#### 5. Commit Your Changes

Write clear commit messages:

```bash
git add .
git commit -m "feat: add example skill for data validation"
```

Follow conventional commits format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance

#### 6. Push and Create Pull Request

```bash
git push origin feature/my-contribution
```

Then create a pull request with:
- Clear title
- Description of changes
- Why the change is needed
- Any breaking changes
- Screenshots (if relevant)

### Pull Request Guidelines

**Good PR:**
- Focused on a single concern
- Includes tests/validation
- Updates documentation
- Has clear description
- Follows template conventions

**PR Template:**

```markdown
## Description
Brief description of changes

## Motivation
Why this change is needed

## Changes
- Change 1
- Change 2
- Change 3

## Testing
How you tested these changes

## Checklist
- [ ] Documentation updated
- [ ] Examples tested
- [ ] Follows template conventions
- [ ] No breaking changes (or documented)
```

### Review Process

1. **Automated Checks**: Basic validation runs automatically
2. **Peer Review**: At least one maintainer reviews
3. **Feedback**: Address any comments or questions
4. **Approval**: Once approved, changes are merged
5. **Release**: Changes included in next release

### Coding Standards

**Markdown:**
- Use ATX-style headers (`#` not `===`)
- Wrap lines at 100 characters where reasonable
- Use fenced code blocks with language specifiers
- Keep hierarchy logical (H1 → H2 → H3)

**YAML:**
- Use 2 spaces for indentation
- Quote strings with special characters
- Keep metadata alphabetically organized (when sensible)
- Use lowercase for tags

**Python (for scripts):**
- Follow PEP 8
- Include docstrings
- Handle errors gracefully
- Type hints for functions

**Shell Scripts:**
- Use `#!/bin/bash`
- Include usage comments
- Exit with appropriate codes
- Quote variables

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive experience for everyone.

### Our Standards

**Positive behaviors:**
- Using welcoming and inclusive language
- Respecting differing viewpoints
- Accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy

**Unacceptable behaviors:**
- Harassment or discriminatory language
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Unprofessional conduct

### Enforcement

Violations can be reported to [contact email]. All complaints will be reviewed and investigated.

## Getting Help

### Questions About Using the Template

- Check [QUICKSTART.md](QUICKSTART.md)
- Review [reference.md](reference.md)
- Look at example skills
- Search existing issues

### Questions About Contributing

- Check this document
- Review existing PRs
- Open a discussion issue
- Ask in pull request

### Reporting Issues

When opening an issue:

1. **Search first**: Check if already reported
2. **Use template**: Follow issue template
3. **Be specific**: Provide details
4. **Include context**: Version, environment, etc.
5. **Be respectful**: Follow code of conduct

**Bug Report Template:**

```markdown
## Description
Clear description of the bug

## To Reproduce
Steps to reproduce:
1. Step 1
2. Step 2
3. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., macOS 14]
- Claude version: [if relevant]
- Template version: [e.g., 1.0.0]

## Additional Context
Any other relevant information
```

**Feature Request Template:**

```markdown
## Feature Description
Clear description of proposed feature

## Motivation
Why this feature is needed

## Proposed Solution
How you envision it working

## Alternatives Considered
Other approaches you've thought about

## Additional Context
Any other relevant information
```

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in relevant documentation

Thank you for helping make this template better!

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

## Questions?

If you have questions not covered here:
- Open a discussion issue
- Check the documentation
- Reach out to maintainers

We're here to help!
