---
name: code-review-assistant
version: 1.0.0
description: Provide structured, actionable code reviews covering quality, security, performance, and maintainability
author: Claude Skills Template
tags: [code-review, quality, security, best-practices, feedback, development]
category: development
license: MIT
created: 2024-01-01
updated: 2024-01-01
maturity: stable
complexity: medium
estimated_time: "10-30 minutes"
requirements:
  - Code to review (pull request, commit, or file)
  - Context about the project and standards
  - Understanding of the programming language
---

# Code Review Assistant

## Overview

Provide comprehensive, structured code reviews that identify issues, suggest improvements, and recognize good practices. Reviews cover correctness, security, performance, maintainability, and adherence to best practices while providing constructive, actionable feedback.

## Purpose

Effective code reviews improve code quality, catch bugs early, share knowledge, and maintain consistency. This skill ensures thorough, systematic reviews that balance critical feedback with positive reinforcement, helping teams maintain high standards without being overly prescriptive.

## When to Use

Use this skill when you need to:
- Review pull requests before merging
- Conduct security-focused code audits
- Evaluate architectural decisions
- Assess code quality and maintainability
- Provide learning feedback to junior developers
- Ensure compliance with coding standards
- Identify performance bottlenecks
- Review refactoring changes
- Audit third-party code or libraries

## Instructions

### Step 1: Understand the Context

Before reviewing code, gather essential context:

**Change Information:**
- What is being changed and why?
- What problem does this solve?
- Is this a bug fix, feature, refactor, or optimization?
- What files are modified?
- How large is the change (lines of code)?

**Project Context:**
- What programming language(s)?
- What frameworks or libraries are used?
- What are the team's coding standards?
- What is the project's purpose/domain?
- Are there specific security requirements?
- What testing practices are expected?

**Review Scope:**
- Focus area (security, performance, style, architecture)
- Time constraints (quick scan vs. deep review)
- Reviewer relationship (peer, senior, external)

### Step 2: First Pass - High-Level Assessment

Scan the code for overall structure and patterns:

**Architecture & Design:**
- Does the approach make sense?
- Are responsibilities properly separated?
- Is the code in the right place?
- Are there better design patterns to use?
- Does it integrate well with existing code?

**Code Organization:**
- Is the code structure logical?
- Are files/modules appropriately sized?
- Is there clear separation of concerns?
- Are related things grouped together?

**Readability:**
- Is the code self-explanatory?
- Are names clear and descriptive?
- Is complexity manageable?
- Would a new team member understand this?

**Impact Assessment:**
- What could break if this changes?
- Are there potential side effects?
- Is backward compatibility maintained?
- What's the risk level of this change?

### Step 3: Detailed Review - Line by Line

Review code systematically, checking for specific issues:

**Correctness:**
- ✓ Logic is correct for all cases
- ✓ Edge cases are handled
- ✓ Error conditions are managed
- ✓ Input validation is present
- ✓ Null/undefined checks where needed
- ✓ Type handling is correct
- ✓ Calculations are accurate
- ✓ State management is correct

**Security:**
- ✓ Input is sanitized/validated
- ✓ No SQL injection vulnerabilities
- ✓ No XSS (cross-site scripting) risks
- ✓ Authentication/authorization is proper
- ✓ Sensitive data is protected
- ✓ No hardcoded credentials
- ✓ Proper encryption usage
- ✓ CSRF protection where needed
- ✓ Rate limiting considered
- ✓ Access control is enforced

**Performance:**
- ✓ No unnecessary loops or iterations
- ✓ Efficient data structures chosen
- ✓ Database queries are optimized
- ✓ No N+1 query problems
- ✓ Appropriate caching
- ✓ Resource cleanup (connections, files)
- ✓ Memory leaks prevented
- ✓ Async operations used properly
- ✓ Batch operations where appropriate

**Maintainability:**
- ✓ Code is readable and clear
- ✓ Functions/methods are focused
- ✓ Duplication is minimized (DRY)
- ✓ Magic numbers/strings are constants
- ✓ Complex logic has comments
- ✓ API changes are documented
- ✓ Dependencies are minimal
- ✓ Code follows team conventions

**Error Handling:**
- ✓ Exceptions are caught appropriately
- ✓ Error messages are helpful
- ✓ Errors are logged properly
- ✓ Recovery strategies are implemented
- ✓ Resources are cleaned up in error cases
- ✓ User-facing errors are friendly
- ✓ No silent failures

**Testing:**
- ✓ Tests are included for new code
- ✓ Edge cases are tested
- ✓ Happy path is tested
- ✓ Error conditions are tested
- ✓ Test coverage is adequate
- ✓ Tests are maintainable
- ✓ Mock/stub usage is appropriate

### Step 4: Check Language-Specific Best Practices

Review against language-specific idioms and conventions:

**Python:**
- PEP 8 compliance
- Pythonic idioms (list comprehensions, context managers)
- Type hints usage
- Proper use of `with` statements
- Virtual environment dependencies

**JavaScript/TypeScript:**
- ESLint compliance
- Proper async/await usage
- No var usage (const/let)
- TypeScript types are specific
- Promise error handling

**Java:**
- Exception handling patterns
- Stream API usage
- Immutability where appropriate
- Proper resource management (try-with-resources)
- Null handling

**Go:**
- Error handling patterns
- Goroutine management
- Channel usage
- Defer statement usage
- Interface design

**C#:**
- LINQ usage
- IDisposable implementation
- Async/await patterns
- Null reference handling
- Exception types

**Ruby:**
- Rubocop compliance
- Idiomatic Ruby (blocks, symbols)
- Rails conventions
- Gem dependencies

### Step 5: Evaluate Testing

Assess test quality and coverage:

**Test Presence:**
- Are new features tested?
- Are bug fixes verified with tests?
- Are edge cases covered?
- Are integration points tested?

**Test Quality:**
- Tests are clear and focused
- Tests don't duplicate functionality
- Test names describe what's tested
- Tests are fast and reliable
- Mocks are used appropriately
- Tests follow AAA pattern (Arrange, Act, Assert)

**Missing Tests:**
- Critical paths without coverage
- Error handling not tested
- Integration scenarios missing
- Performance tests needed

### Step 6: Review Documentation

Check that code changes include appropriate documentation:

**Code Comments:**
- Complex logic is explained
- Non-obvious decisions are documented
- TODOs are tracked
- Comments are current and accurate
- Public APIs have docstrings/JSDoc

**External Documentation:**
- README is updated if needed
- API docs reflect changes
- Migration guides for breaking changes
- Architecture docs updated
- Configuration examples provided

**Changelog/Commit Messages:**
- Clear description of what changed
- Explanation of why it changed
- References to issues/tickets
- Breaking changes highlighted

### Step 7: Structure Feedback

Organize findings into three priority levels:

**🔴 Critical Issues (Must Fix Before Merge):**
- Security vulnerabilities
- Logic errors/bugs
- Data loss risks
- Breaking changes without migration path
- Major performance problems
- Violations of system requirements

Format:
```
🔴 CRITICAL: [Brief description]
Location: [file:line]
Issue: [Detailed explanation]
Impact: [What could go wrong]
Fix: [Specific suggestion]
```

**🟡 Important Suggestions (Should Address):**
- Code quality improvements
- Maintainability concerns
- Test coverage gaps
- Minor security concerns
- Style guide violations
- Missing documentation
- Potential bugs in edge cases

Format:
```
🟡 SUGGESTION: [Brief description]
Location: [file:line]
Issue: [Explanation]
Reason: [Why this matters]
Suggestion: [How to improve]
```

**⚪ Nitpicks/Optional (Consider):**
- Naming preferences
- Code style details
- Alternative approaches
- Micro-optimizations
- Personal preferences

Format:
```
⚪ NITPICK: [Brief description]
Location: [file:line]
Comment: [Observation]
Alternative: [Optional different approach]
```

**✅ Positive Feedback (Recognize Good Work):**
- Well-designed solutions
- Clear code
- Good test coverage
- Thoughtful error handling
- Performance improvements
- Good documentation

Format:
```
✅ EXCELLENT: [What was done well]
Location: [file:line]
Why: [What makes this good]
```

### Step 8: Provide Summary and Recommendation

Conclude with an overall assessment:

**Review Summary:**
```
Overall Assessment: [Approve / Approve with suggestions / Request changes / Needs major revision]

Critical Issues: [count] - [Must be fixed]
Important Suggestions: [count] - [Should be addressed]
Nitpicks: [count] - [Optional]
Positive Observations: [count]

Code Quality: [Excellent / Good / Adequate / Needs Improvement / Poor]
Test Coverage: [Comprehensive / Good / Adequate / Insufficient / Missing]
Security: [No concerns / Minor concerns / Needs attention / Serious issues]
Performance: [Optimized / Good / Acceptable / Concerns / Issues]

Recommendation: [Merge / Merge after addressing critical issues / Needs revision / Major rework needed]

Next Steps:
1. [Action item]
2. [Action item]
3. [Action item]
```

## Review Types

### Standard Pull Request Review

Focus on:
- Correctness of implementation
- Code quality and style
- Test coverage
- Documentation updates
- Integration with existing code

Tone: Collaborative, constructive

### Security-Focused Review

Focus on:
- Input validation and sanitization
- Authentication and authorization
- Data protection and encryption
- Injection vulnerabilities
- Access control
- Security best practices

Tone: Thorough, cautious

### Architecture Review

Focus on:
- Design patterns and principles
- System integration
- Scalability considerations
- Long-term maintainability
- Technical debt
- Alternative approaches

Tone: Strategic, questioning

### Performance Review

Focus on:
- Algorithm efficiency
- Database query optimization
- Resource usage
- Caching strategies
- Scaling considerations
- Profiling results

Tone: Data-driven, analytical

### Learning/Mentoring Review

Focus on:
- Understanding of concepts
- Best practices
- Alternative approaches
- Learning opportunities
- Explanations and examples

Tone: Educational, encouraging

## Best Practices

### Be Constructive and Kind

✅ **DO:**
- Explain the "why" behind suggestions
- Offer specific, actionable advice
- Recognize good work
- Ask questions to understand intent
- Assume good faith
- Be humble about your own knowledge

❌ **DON'T:**
- Use harsh or demanding language
- Make personal criticisms
- Be dismissive of approaches
- Assume incompetence
- Nitpick excessively
- Block on minor style issues

### Be Specific and Actionable

✅ **Good:**
```
The loop at line 45 iterates over all users to find a match. Consider using a 
Map/dictionary indexed by user ID for O(1) lookup instead of O(n) iteration. 
Example: `userMap.get(userId)` instead of `users.find(u => u.id === userId)`
```

❌ **Vague:**
```
This is slow and should be optimized.
```

### Prioritize Correctly

**Block merging for:**
- Security vulnerabilities
- Data corruption risks
- Breaking production
- Violating legal/compliance requirements

**Don't block merging for:**
- Personal style preferences
- Trivial optimizations
- Minor naming choices
- Alternative approaches that also work

### Balance Thoroughness with Pragmatism

- Large changes need thorough review
- Urgent hotfixes need focused review on critical issues
- Trivial changes (typos, docs) can be lightweight
- Consistent small improvements over time beat perfect code

### Consider the Author

**For Junior Developers:**
- More detailed explanations
- Educational tone
- Encourage questions
- Highlight learning opportunities

**For Senior Developers:**
- More concise feedback
- Focus on high-level concerns
- Trust their judgment on details
- Discuss trade-offs

**For External Contributors:**
- Explain project conventions
- Be especially welcoming
- Provide context about decisions
- Thank them for contribution

## Common Mistakes to Avoid

❌ **Commenting on Every Line**: Focus on important issues, not every minor point

❌ **Style Debates**: Use automated linters; don't debate subjectively in reviews

❌ **Bike-shedding**: Don't spend excessive time on trivial decisions

❌ **Rewriting in Your Style**: Accept different approaches that work

❌ **Being a Blocker**: Distinguish between must-fix and nice-to-have

❌ **Ignoring Context**: Understand constraints (time, resources, requirements)

❌ **Late Mega-Reviews**: Review promptly in multiple smaller passes

❌ **No Positive Feedback**: Recognize good work, not just problems

## Example Review Templates

### Quick Review Template

```markdown
## Review Summary
[Approve/Request Changes]: [One-line overall assessment]

### Critical Issues
- [Issue 1 with location and fix]

### Suggestions
- [Suggestion 1]
- [Suggestion 2]

### Questions
- [Question about approach/implementation]

### Positive
- [Something done well]
```

### Comprehensive Review Template

```markdown
## Code Review: [PR Title]

### Overview
**Change Type**: [Feature/Bug Fix/Refactor/etc.]
**Risk Level**: [Low/Medium/High]
**Review Focus**: [What I focused on]

### Critical Issues 🔴
[None found] OR
1. **[Issue Name]** (`file.js:123`)
   - Issue: [Description]
   - Impact: [What could go wrong]
   - Fix: [Specific solution]

### Important Suggestions 🟡
1. **[Suggestion]** (`file.js:45`)
   - Current: [What's there now]
   - Concern: [Why it matters]
   - Recommendation: [How to improve]

### Nitpicks/Optional ⚪
- [Minor observation]

### Positive Feedback ✅
- [Good practice observed]
- [Well-designed solution]

### Testing
**Coverage**: [Adequate/Needs improvement]
**Suggestions**: [Test improvements needed]

### Documentation
**Status**: [Complete/Needs updates]
**Needed**: [What docs to add/update]

### Summary
**Code Quality**: [Rating]
**Recommendation**: [Approve/Request changes]
**Next Steps**: [What author should do]
```

## Language-Specific Considerations

### Python
- Check PEP 8 compliance
- Verify type hints are used
- Look for Pythonic idioms
- Check for proper exception handling
- Verify requirements.txt updated

### JavaScript/TypeScript
- Check for proper async/await usage
- Verify TypeScript types are specific (not `any`)
- Look for proper error handling in promises
- Check for memory leaks in event listeners
- Verify package.json dependencies

### Java
- Check exception handling patterns
- Verify proper resource management
- Look for appropriate use of streams
- Check for thread safety if concurrent
- Verify proper null handling

### Go
- Check error handling (every error checked)
- Verify proper goroutine management
- Look for channel deadlocks
- Check for race conditions
- Verify proper defer usage

### C#
- Check proper async/await patterns
- Verify IDisposable implementation
- Look for proper LINQ usage
- Check exception types
- Verify nullable reference handling

### Ruby
- Check Rubocop compliance
- Verify idiomatic Ruby usage
- Look for proper Rails conventions
- Check for N+1 queries in Rails
- Verify Gemfile updated

## Security Review Checklist

### Input Validation
- [ ] All user input is validated
- [ ] Whitelist validation used over blacklist
- [ ] Input length limits enforced
- [ ] File upload restrictions in place
- [ ] Type checking performed

### Authentication & Authorization
- [ ] Authentication required for protected endpoints
- [ ] Authorization checks for resource access
- [ ] Session management is secure
- [ ] Password handling follows best practices
- [ ] Multi-factor authentication considered

### Injection Prevention
- [ ] SQL injection prevented (parameterized queries)
- [ ] XSS prevented (output encoding)
- [ ] Command injection prevented
- [ ] LDAP injection prevented
- [ ] XML injection prevented

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] Sensitive data encrypted in transit (HTTPS)
- [ ] Secrets not hardcoded
- [ ] Personal data handling complies with regulations
- [ ] Logging doesn't include sensitive data

### API Security
- [ ] Rate limiting implemented
- [ ] CORS configured properly
- [ ] CSRF protection in place
- [ ] API keys/tokens managed securely
- [ ] Proper HTTP methods used

## Performance Review Checklist

### Algorithm Efficiency
- [ ] Appropriate time complexity (no unnecessary O(n²))
- [ ] Appropriate space complexity
- [ ] Efficient data structures chosen
- [ ] Unnecessary iterations removed

### Database Performance
- [ ] Queries are optimized
- [ ] Indexes exist for common queries
- [ ] N+1 queries avoided
- [ ] Batch operations used where appropriate
- [ ] Connection pooling configured

### Caching
- [ ] Appropriate caching strategy
- [ ] Cache invalidation handled
- [ ] Cache key collisions prevented
- [ ] TTL configured appropriately

### Resource Management
- [ ] Database connections closed
- [ ] File handles released
- [ ] Network connections cleaned up
- [ ] Memory not leaked
- [ ] Async operations used for I/O

## Code Quality Checklist

### Readability
- [ ] Variable names are descriptive
- [ ] Functions have clear, single responsibilities
- [ ] Code is self-documenting
- [ ] Complex logic has explanatory comments
- [ ] Consistent formatting

### Maintainability
- [ ] DRY principle followed (no duplication)
- [ ] SOLID principles followed
- [ ] Functions/methods are reasonably sized
- [ ] Dependencies are minimal
- [ ] Magic numbers extracted to constants

### Error Handling
- [ ] Errors are caught appropriately
- [ ] Error messages are helpful
- [ ] Errors are logged with context
- [ ] User-facing errors are friendly
- [ ] No silent failures

### Testing
- [ ] Unit tests for new functionality
- [ ] Integration tests where appropriate
- [ ] Edge cases tested
- [ ] Error conditions tested
- [ ] Tests are maintainable

## Feedback Examples

### Security Issue

```
🔴 CRITICAL: SQL Injection Vulnerability
Location: `user_controller.py:45`

Issue: The query uses string concatenation with user input:
```python
query = f"SELECT * FROM users WHERE email = '{email}'"
```

Impact: An attacker could inject malicious SQL, potentially accessing or 
modifying any data in the database. Example: email="'; DROP TABLE users--"

Fix: Use parameterized queries:
```python
query = "SELECT * FROM users WHERE email = %s"
cursor.execute(query, (email,))
```

This prevents any user input from being interpreted as SQL commands.
```

### Performance Issue

```
🟡 SUGGESTION: Inefficient Database Query
Location: `order_service.js:78`

Current Code:
```javascript
for (const order of orders) {
  order.user = await User.findById(order.userId);
}
```

Issue: This creates N+1 query problem - one query for orders, then N additional 
queries for users. For 100 orders, this means 101 database queries.

Suggestion: Fetch all users in a single query:
```javascript
const userIds = orders.map(o => o.userId);
const users = await User.find({ _id: { $in: userIds } });
const userMap = new Map(users.map(u => [u._id.toString(), u]));
orders.forEach(order => {
  order.user = userMap.get(order.userId.toString());
});
```

This reduces 101 queries to just 2 queries, significantly improving performance.
```

### Code Quality Suggestion

```
🟡 SUGGESTION: Extract Complex Validation Logic
Location: `payment_processor.java:120-145`

Current: The payment validation logic (25 lines) is embedded directly in the 
processPayment method, making it hard to test and reuse.

Recommendation: Extract to a separate method or class:
```java
public class PaymentValidator {
  public ValidationResult validate(PaymentRequest request) {
    // validation logic here
  }
}
```

Benefits:
- Easier to unit test validation independently
- Can reuse validation in other contexts
- Improves readability of processPayment method
- Single Responsibility Principle
```

### Positive Feedback

```
✅ EXCELLENT: Comprehensive Error Handling
Location: `api_client.ts:89-110`

The error handling in the API client is exemplary:
- Different error types are distinguished (network, timeout, server error)
- Each error type has appropriate retry logic
- Errors are logged with context (request ID, timestamp, endpoint)
- User-facing error messages are clear and actionable
- Original error is preserved for debugging

This makes debugging much easier and provides a better user experience. Great work!
```

## Error Handling

### Unclear Code Intent

When you can't determine what code is supposed to do:

```
❓ QUESTION: Unclear Intent
Location: `service.py:234`

I'm not sure what this section is trying to accomplish:
```python
result = [x for x in data if x not in temp and temp.append(x)]
```

Could you clarify:
1. What is the intended behavior?
2. Is this filtering duplicates? If so, consider using set():
   `result = list(dict.fromkeys(data))`  # preserves order

Would be helpful to add a comment explaining the purpose.
```

### Large Changeset

For very large pull requests:

```
📦 LARGE CHANGESET

This PR changes 2,500+ lines across 30 files, making thorough review difficult.

Recommendations:
1. Consider breaking into smaller, focused PRs
2. For this review, I've focused on:
   - Critical security/correctness issues
   - Architecture/design concerns
   - High-risk changes
3. Detailed code style review may be incomplete

If possible, future PRs would benefit from being < 500 lines for more 
thorough review.
```

### Missing Context

When you need more information:

```
❓ CLARIFICATION NEEDED

To provide a thorough review, I'd appreciate context on:
1. Why was the [specific approach] chosen over [alternative]?
2. How does this interact with the [related system]?
3. Are there performance benchmarks for the new algorithm?
4. Is backward compatibility a concern?

Please update the PR description or add comments explaining these decisions.
```

## Limitations

This skill provides structured guidance but reviewers must:
- Understand the specific programming language and domain
- Have context about project requirements and constraints
- Exercise judgment on issue severity and priorities
- Balance perfectionism with pragmatism
- Adapt feedback style to the team and individual
- Stay current with security vulnerabilities and best practices

## Related Skills

- **Code Formatter**: Automate style consistency
- **Security Auditor**: Deep security-focused analysis
- **Test Coverage Analyzer**: Evaluate test completeness
- **Documentation Generator**: Ensure docs match code

## Version History

- **1.0.0** (2024-01-01): Initial release

## Notes

- Focus on issues that matter; don't be pedantic
- Assume positive intent from the author
- Reviews are collaborative, not adversarial
- Balance speed with thoroughness based on change risk
- Continuous small improvements beat infrequent perfection
- Use automation (linters, formatters) to reduce manual review burden
- Good reviews make code better and developers better
