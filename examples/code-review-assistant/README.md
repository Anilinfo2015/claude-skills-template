# Code Review Assistant

Provide structured, actionable code reviews that improve quality, security, and maintainability.

## Overview

This skill guides you through comprehensive code reviews that go beyond style checking. It helps identify bugs, security vulnerabilities, performance issues, and maintainability concerns while providing constructive feedback that helps developers improve.

## Key Features

- **Multi-dimensional review**: Covers correctness, security, performance, and maintainability
- **Structured feedback**: Organizes findings by priority (Critical/Important/Nitpick)
- **Language-specific checks**: Best practices for Python, JavaScript/TypeScript, Java, Go, C#, Ruby
- **Multiple review types**: Standard PR, security audit, architecture review, performance review, mentoring
- **Actionable suggestions**: Provides specific fixes with code examples
- **Balanced feedback**: Recognizes good work alongside improvement areas

## When to Use

- **Pull request reviews**: Comprehensive review before merging changes
- **Security audits**: Focus on vulnerabilities and security best practices
- **Architecture reviews**: Evaluate design decisions and system integration
- **Performance optimization**: Identify bottlenecks and inefficiencies
- **Code quality checks**: Ensure maintainability and readability
- **Mentoring**: Provide educational feedback to help developers grow
- **Legacy code assessment**: Evaluate technical debt and improvement opportunities

## Quick Example

**Input**: Python code with potential issues

**Output**:
```markdown
## Code Review Summary

### Critical Issues 🔴
1. **SQL Injection Vulnerability** (user_service.py:45)
   - Issue: Query uses string interpolation with user input
   - Impact: Attacker could execute arbitrary SQL
   - Fix: Use parameterized queries with placeholders

### Important Suggestions 🟡
1. **Missing Error Handling** (user_service.py:78)
   - No exception handling for database connection failures
   - Recommendation: Add try-except with proper logging

### Positive Feedback ✅
1. **Excellent Test Coverage** (tests/)
   - Comprehensive unit tests covering edge cases
   - Good use of mocking for external dependencies

**Recommendation**: Request Changes (Fix critical security issue)
**Next Steps**: Fix SQL injection, add error handling, re-request review
```

## Review Categories

### 🔴 Critical Issues (Must Fix)
- Security vulnerabilities
- Logic errors and bugs
- Data loss risks
- Breaking changes without migration
- Major performance problems

### 🟡 Important Suggestions (Should Address)
- Code quality improvements
- Maintainability concerns
- Test coverage gaps
- Minor security concerns
- Missing documentation

### ⚪ Nitpicks (Optional)
- Naming preferences
- Code style details
- Alternative approaches
- Micro-optimizations

### ✅ Positive Feedback (Recognition)
- Well-designed solutions
- Good test coverage
- Clear documentation
- Performance improvements

## What Gets Reviewed

### Correctness
- Logic errors and edge cases
- Error handling
- Input validation
- State management
- Type safety

### Security
- Input sanitization
- SQL injection prevention
- XSS prevention
- Authentication/authorization
- Sensitive data protection
- Access control

### Performance
- Algorithm efficiency
- Database query optimization
- N+1 query problems
- Resource management
- Caching strategies
- Memory leaks

### Maintainability
- Code readability
- DRY principle (no duplication)
- Single responsibility
- Clear naming
- Appropriate comments
- Documentation

### Testing
- Test coverage
- Edge case testing
- Error condition testing
- Test maintainability
- Mock/stub usage

## Review Types

### Standard Pull Request Review
**Focus**: Correctness, code quality, testing, documentation  
**Tone**: Collaborative, constructive  
**Use for**: Regular feature development

### Security-Focused Review
**Focus**: Vulnerabilities, input validation, authentication, encryption  
**Tone**: Thorough, cautious  
**Use for**: Security-critical changes, authentication, payment processing

### Architecture Review
**Focus**: Design patterns, scalability, long-term maintainability  
**Tone**: Strategic, questioning  
**Use for**: Major refactorings, new system components

### Performance Review
**Focus**: Algorithm efficiency, database optimization, resource usage  
**Tone**: Data-driven, analytical  
**Use for**: Performance-critical code, optimization work

### Learning/Mentoring Review
**Focus**: Best practices, learning opportunities, explanations  
**Tone**: Educational, encouraging  
**Use for**: Junior developers, onboarding, skill development

## Language Support

Includes specific best practices and common pitfalls for:

- **Python**: PEP 8, type hints, Pythonic idioms, context managers
- **JavaScript/TypeScript**: ESLint, async/await, type safety, promise handling
- **Java**: Exception handling, streams, resource management, null handling
- **Go**: Error handling, goroutines, channels, defer usage, race conditions
- **C#**: LINQ, IDisposable, async patterns, nullable references
- **Ruby**: Rubocop, idiomatic Ruby, Rails conventions, N+1 queries

## Example Scenarios

### Security Vulnerability Found
```
🔴 CRITICAL: SQL Injection Vulnerability
Location: user_controller.py:45

Issue: Query concatenates user input without sanitization
Impact: Attacker could access or delete any database data
Fix: Use parameterized queries with bound parameters

[Code example showing the fix]
```

### Performance Issue
```
🟡 SUGGESTION: N+1 Query Problem
Location: order_service.js:78

Current: 100 orders = 101 database queries
Recommendation: Batch query with JOIN
Result: Reduces to 1 query, 100x faster

[Code example showing optimization]
```

### Positive Recognition
```
✅ EXCELLENT: Comprehensive Error Handling
Location: payment_processor.java:120

Well-designed error handling with:
- Specific exception types
- Detailed error messages
- Proper resource cleanup
- Retry logic for transient failures

This will make debugging much easier!
```

## Best Practices

### Do's ✅
- Explain the "why" behind suggestions
- Provide specific, actionable advice
- Include code examples for fixes
- Recognize good work
- Ask questions to understand intent
- Prioritize issues appropriately
- Be constructive and kind

### Don'ts ❌
- Don't nitpick excessively on style
- Don't block on personal preferences
- Don't assume incompetence
- Don't be vague ("this is bad")
- Don't debate in code reviews (take offline)
- Don't ignore the business context

## Workflow

1. **Understand Context**: What's being changed and why?
2. **High-Level Review**: Architecture and design approach
3. **Detailed Review**: Line-by-line correctness, security, performance
4. **Check Tests**: Coverage and quality
5. **Review Documentation**: Comments, API docs, README updates
6. **Structure Feedback**: Organize by priority
7. **Provide Summary**: Clear recommendation and next steps

## Review Templates

### Quick Review
```markdown
## Review Summary
[Approve/Request Changes]

### Critical Issues
- [Issue with location and fix]

### Suggestions
- [Improvement suggestion]

### Positive
- [Something done well]
```

### Comprehensive Review
```markdown
## Code Review: [PR Title]

### Overview
**Change Type**: [Feature/Bug Fix/Refactor]
**Risk Level**: [Low/Medium/High]

### Critical Issues 🔴
[Detailed issues with fixes]

### Important Suggestions 🟡
[Quality improvements]

### Nitpicks ⚪
[Minor observations]

### Positive Feedback ✅
[Recognition of good work]

### Testing
[Test coverage assessment]

### Summary
**Recommendation**: [Approve/Request Changes]
**Next Steps**: [Action items]
```

## Quality Checks

Every review should verify:
- ✓ Code is correct for all cases
- ✓ Security vulnerabilities are addressed
- ✓ Performance is acceptable
- ✓ Code is maintainable and readable
- ✓ Tests cover new functionality
- ✓ Documentation is updated
- ✓ Error handling is comprehensive

## Integration

Works well with:
- **Git workflows**: GitHub, GitLab, Bitbucket PR reviews
- **CI/CD pipelines**: Automated quality gates
- **Code quality tools**: Complements linters and static analyzers
- **Team standards**: Enforces coding conventions
- **Security tools**: Enhances automated security scanning

## Tips for Best Results

1. **Provide context**: Share project requirements and constraints
2. **Specify focus**: Security audit vs. quick review vs. architecture review
3. **Include relevant code**: Surrounding context helps understand design
4. **Mention team standards**: Reference style guides or conventions
5. **Indicate author level**: Junior vs. senior affects feedback style
6. **Set priority**: Urgent hotfix vs. regular feature affects depth

## Limitations

- Requires human judgment on issue severity
- Cannot fully assess business logic correctness
- May not catch all security vulnerabilities
- Depends on reviewer's domain knowledge
- Cannot replace automated testing and security scanning
- Effectiveness varies with code complexity and context

## Related Skills

- **Test Generator**: Create tests for reviewed code
- **Security Auditor**: Deep security analysis
- **Code Formatter**: Automated style fixes
- **Documentation Generator**: Update docs for changes
- **Refactoring Assistant**: Implement suggested improvements

## Getting Started

### Basic Usage

1. Provide the code to review (file, diff, or PR link)
2. Specify review type if not standard (security, performance, etc.)
3. Include context about the change
4. Review the structured feedback
5. Address critical issues and key suggestions

### Advanced Usage

- Focus on specific concerns (e.g., "review security only")
- Request mentoring-style feedback for learning
- Compare multiple implementation approaches
- Assess technical debt in legacy code
- Evaluate third-party code or dependencies

## Examples

See [examples.md](examples.md) for detailed examples including:
- Python security review with SQL injection
- JavaScript performance review with N+1 queries
- Java architecture review of service layer
- TypeScript code quality review
- Go concurrency review
- Different review types comparison
- Common review scenarios (hotfix, large refactor, junior developer)

## Additional Resources

See [SKILL.md](SKILL.md) for:
- Complete step-by-step instructions
- Detailed checklists for each review aspect
- Language-specific considerations
- Security review checklist
- Performance review checklist
- Code quality checklist
- Feedback templates and examples

## License

MIT

---

**Note**: This skill provides guidance for human code reviews. It complements but does not replace:
- Automated testing
- Static analysis tools (linters, type checkers)
- Security scanning tools
- Code formatters
- CI/CD pipelines

Use in combination with automated tools for comprehensive quality assurance.
