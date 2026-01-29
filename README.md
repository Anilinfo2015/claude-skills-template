# Claude Skills Template

A comprehensive template and reference implementation for creating Claude Skills based on Anthropic's best practices.

## 🚀 Overview

This template provides everything you need to create, organize, and manage Claude Skills - structured documents that enhance Claude's capabilities by providing specialized knowledge, workflows, and instructions for specific tasks.

## ✨ Features

- **Complete Template Structure**: Ready-to-use templates with YAML frontmatter
- **Comprehensive Documentation**: Detailed guides for all skill levels
- **Practical Examples**: 4 fully-implemented example skills demonstrating different patterns
- **Validation Tools**: Python and Shell scripts for validating skill compliance
- **Best Practices**: Enterprise governance guidelines and quality standards
- **Quick Start Guide**: Get your first skill running in 10 minutes

## 📁 Repository Structure

```
claude-skills-template/
├── SKILL.md                    # Main skill template
├── QUICKSTART.md              # 10-minute getting started guide
├── reference.md               # Comprehensive technical documentation
├── examples.md                # Skill pattern examples
├── ENTERPRISE.md              # Enterprise governance guide
├── CONTRIBUTING.md            # How to use and contribute
├── config.json                # Configuration schema
├── scripts/
│   ├── helper.py             # Python utilities for skill management
│   └── validate.sh           # Bash validation script
├── templates/
│   ├── template.md           # Alternative skill template
│   └── output.json           # JSON schema template
├── tests/
│   └── test_skill.py         # Unit tests for helper utilities
├── assets/
│   └── README.md             # Assets organization guide
└── examples/
    ├── archunit-architecture-tester/    # Convert natural language to ArchUnit tests
    ├── text-summarizer/                 # Intelligent text summarization
    ├── api-documentation-generator/     # Generate API docs from code
    └── code-review-assistant/           # Structured code review feedback
```

## 🎯 Example Skills

### 1. ArchUnit Architecture Tester
Converts natural language architecture rules into executable ArchUnit tests for Java projects.

**Pattern**: Natural language to code conversion  
**Complexity**: High  
**Use Case**: Architecture validation, testing

[View Skill](examples/archunit-architecture-tester/) | [Examples](examples/archunit-architecture-tester/examples.md)

### 2. Text Summarizer
Simple text summarization skill for condensing content while preserving key information.

**Pattern**: Single-purpose transformation  
**Complexity**: Low  
**Use Case**: Content processing, documentation

[View Skill](examples/text-summarizer/) | [Examples](examples/text-summarizer/examples.md)

### 3. API Documentation Generator
Generates comprehensive API documentation from source code and comments.

**Pattern**: Multi-step generation workflow  
**Complexity**: Medium  
**Use Case**: Documentation automation

[View Skill](examples/api-documentation-generator/) | [Examples](examples/api-documentation-generator/examples.md)

### 4. Code Review Assistant
Provides structured code review feedback following best practices.

**Pattern**: Analysis and feedback  
**Complexity**: Medium  
**Use Case**: Code quality, peer review

[View Skill](examples/code-review-assistant/) | [Examples](examples/code-review-assistant/examples.md)

## 🏁 Quick Start

### 1. Clone or Fork

```bash
git clone https://github.com/your-org/claude-skills-template.git
cd claude-skills-template
```

### 2. Read the Quickstart

Start with [QUICKSTART.md](QUICKSTART.md) for a 10-minute introduction to creating your first skill.

### 3. Explore Examples

Browse the [examples/](examples/) directory to see different skill patterns in action.

### 4. Create Your First Skill

Use the helper script to generate a new skill:

```bash
python scripts/helper.py create my-skill-name ./my-skills "Your Name" development
```

Or copy the template manually:

```bash
cp SKILL.md my-skill/SKILL.md
# Edit and customize
```

### 5. Validate Your Skill

```bash
# Validate single skill
./scripts/validate.sh my-skill/SKILL.md

# Validate all skills in a directory
./scripts/validate.sh
```

## 📚 Documentation

### Getting Started
- [QUICKSTART.md](QUICKSTART.md) - Create your first skill in 10 minutes
- [SKILL.md](SKILL.md) - Main template with all sections

### Technical Reference
- [reference.md](reference.md) - Comprehensive technical documentation
- [examples.md](examples.md) - Pattern examples and use cases
- [config.json](config.json) - Configuration schema and options

### Advanced Topics
- [ENTERPRISE.md](ENTERPRISE.md) - Enterprise governance and best practices
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

## 🛠️ Helper Tools

### Python Helper (`scripts/helper.py`)

```bash
# Validate a skill
python scripts/helper.py validate path/to/SKILL.md

# Generate catalog of skills
python scripts/helper.py catalog ./skills markdown

# Create new skill from template
python scripts/helper.py create skill-name ./output "Author" category
```

### Bash Validator (`scripts/validate.sh`)

```bash
# Validate specific skill
./scripts/validate.sh examples/text-summarizer/SKILL.md

# Validate all skills
./scripts/validate.sh
```

## 📋 Skill Structure

Every skill follows this structure:

```markdown
---
name: skill-name
version: 1.0.0
description: Brief one-line description
author: Your Name
tags: [category, technology, use-case]
category: development
license: MIT
created: 2024-01-01
updated: 2024-01-01
---

# Skill Name

## Overview
[Brief overview]

## When to Use
[Usage criteria]

## Instructions
[Step-by-step instructions]

## Examples
[Practical examples]

## Best Practices
[Tips and guidelines]

## Error Handling
[Error scenarios and solutions]
```

## 🎨 Skill Patterns

### Simple Task Pattern
- Single, focused purpose
- Clear input/output
- Minimal decision points
- Example: [Text Summarizer](examples/text-summarizer/)

### Workflow Pattern
- Multiple sequential steps
- Complex output generation
- Validation and quality checks
- Example: [API Documentation Generator](examples/api-documentation-generator/)

### Analysis Pattern
- Analytical evaluation
- Structured feedback format
- Prioritized recommendations
- Example: [Code Review Assistant](examples/code-review-assistant/)

### Specialized Technical Pattern
- Domain-specific knowledge
- Code generation
- Technical validation
- Example: [ArchUnit Architecture Tester](examples/archunit-architecture-tester/)

## 🏢 Enterprise Use

For organizations deploying Claude Skills at scale:

- **Governance Framework**: Standards and approval processes
- **Quality Standards**: Documentation and code quality requirements
- **Security and Compliance**: Review checklists and compliance tiers
- **Organization and Discovery**: Catalog and search capabilities
- **Monitoring and Metrics**: Usage tracking and reporting

See [ENTERPRISE.md](ENTERPRISE.md) for the complete enterprise governance guide.

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- How to use this template
- Creating your own skills
- Contributing improvements
- Code of conduct
- Getting help

### Types of Contributions

- 🐛 Bug fixes and corrections
- 📚 Documentation improvements
- 🎯 New example skills
- 🔧 Helper tools and utilities
- 💡 Best practice additions

## 📖 Learning Path

**Beginners:**
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Study [text-summarizer](examples/text-summarizer/) example
3. Create your first simple skill

**Intermediate:**
4. Review [reference.md](reference.md)
5. Study [api-documentation-generator](examples/api-documentation-generator/)
6. Create a multi-step workflow skill

**Advanced:**
7. Read [ENTERPRISE.md](ENTERPRISE.md)
8. Study [archunit-architecture-tester](examples/archunit-architecture-tester/)
9. Build domain-specific skills

## 🔍 Key Concepts

### Progressive Disclosure
Skills use a two-layer approach:
- **Metadata layer** (YAML frontmatter): Always loaded for discovery
- **Instruction layer**: Loaded on-demand when skill is activated

### Quality Principles
1. **Clarity**: Easy to understand and follow
2. **Conciseness**: No unnecessary complexity
3. **Completeness**: Cover the full workflow
4. **Consistency**: Follow established patterns
5. **Currency**: Regularly updated

### Best Practices
- Use action-oriented language
- Provide concrete examples
- Include error handling
- Document security considerations
- Keep instructions focused

## 🧪 Testing

Run the test suite:

```bash
# Install dependencies
pip install pyyaml

# Run tests
python -m pytest tests/
```

Validate all example skills:

```bash
./scripts/validate.sh
```

## 📊 Skill Quality Checklist

Before considering your skill complete:

**Metadata:**
- [ ] Name uses kebab-case
- [ ] Version follows semver
- [ ] Description is clear and concise
- [ ] Tags aid discovery
- [ ] All required fields present

**Content:**
- [ ] Overview explains purpose
- [ ] Instructions are step-by-step
- [ ] At least 2 examples included
- [ ] Error handling addressed
- [ ] Examples show realistic usage

**Quality:**
- [ ] Instructions are unambiguous
- [ ] Examples work as shown
- [ ] No typos or errors
- [ ] Formatting is consistent
- [ ] Tested with Claude

## 🔗 Additional Resources

- [Anthropic Documentation](https://docs.anthropic.com/)
- [Claude API Reference](https://docs.anthropic.com/claude/reference)
- [Prompt Engineering Guide](https://www.anthropic.com/index/prompting-guide)

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

This template is based on:
- Anthropic's official Claude Skills documentation
- Best practices from the Claude community
- Enterprise implementation patterns

## 💬 Questions or Feedback?

- Open an [Issue](https://github.com/your-org/claude-skills-template/issues)
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- Review existing skills for examples

---

**Ready to get started?** → Read the [QUICKSTART](QUICKSTART.md) guide and create your first skill in 10 minutes!
