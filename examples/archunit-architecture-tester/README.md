# ArchUnit Architecture Tester

Transform natural language architecture rules into executable ArchUnit tests.

## Overview

This skill helps Java developers enforce architectural constraints by converting natural language descriptions of architecture rules into executable ArchUnit test code.

## What is ArchUnit?

ArchUnit is a Java library for checking the architecture of Java code. It allows you to define and test architectural rules as unit tests, ensuring your codebase adheres to defined architectural patterns.

## Key Features

- Converts plain English architecture rules to Java test code
- Supports common patterns: layering, naming, annotations, dependencies
- Generates fully documented test classes with rationale
- Includes examples and best practices
- Handles complex layered architectures

## Prerequisites

Your Java project needs:

```xml
<!-- Maven -->
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>1.2.1</version>
    <scope>test</scope>
</dependency>
```

```groovy
// Gradle
testImplementation 'com.tngtech.archunit:archunit-junit5:1.2.1'
```

## Quick Start

1. **Describe your architecture rule** in natural language:
   ```
   "Services should not depend on controllers"
   ```

2. **Use this skill** to generate the ArchUnit test

3. **Add the test** to your test suite

4. **Run tests** as part of your build

5. **Fix violations** or adjust rules as needed

## Common Use Cases

### Layer Enforcement
- Ensure controllers don't bypass services
- Prevent repositories from calling external APIs
- Validate clean architecture boundaries

### Naming Conventions
- Repository interfaces end with "Repository"
- Controller classes end with "Controller"
- DTOs end with "DTO"

### Annotation Rules
- All REST controllers have @RestController
- All services have @Service
- All entities have @Entity

### Package Structure
- Prevent circular dependencies
- Enforce package hierarchies
- Validate module boundaries

## Example Usage

**Input:**
> "Repository classes should only be accessed by services, not by controllers"

**Output:**
```java
@Test
void repositories_should_only_be_accessed_by_services() {
    JavaClasses importedClasses = new ClassFileImporter()
        .importPackages("com.example");
    
    ArchRule rule = classes()
        .that().resideInAPackage("..repository..")
        .should().onlyBeAccessed().byAnyPackage("..service..");
    
    rule.check(importedClasses);
}
```

## Benefits

- **Automated Enforcement**: Architecture rules are checked automatically
- **Living Documentation**: Tests serve as documentation of architectural decisions
- **Early Detection**: Catch violations during development, not in code review
- **Consistent Quality**: Ensure all team members follow the same patterns
- **Refactoring Safety**: Prevent accidental architecture degradation

## Resources

- See [SKILL.md](SKILL.md) for detailed instructions
- See [examples.md](examples.md) for more patterns
- [ArchUnit Documentation](https://www.archunit.org)

## When to Use

Use this skill when you:
- Need to enforce architectural patterns
- Want to prevent common architecture violations
- Are implementing layered, hexagonal, or clean architecture
- Need to onboard developers to your architecture
- Want architecture rules as executable tests

## Integration

Add to your CI/CD pipeline:

```yaml
# GitHub Actions
- name: Run Architecture Tests
  run: ./mvnw test -Dtest=*ArchitectureTest
```

```yaml
# GitLab CI
test:architecture:
  script:
    - ./gradlew test --tests '*ArchitectureTest'
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
```

## License

MIT
