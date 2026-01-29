---
name: archunit-architecture-tester
version: 1.0.0
description: Convert natural language architecture rules into executable ArchUnit tests
author: Claude Skills Template
tags: [java, testing, architecture, archunit, code-generation]
category: testing
license: MIT
created: 2024-01-01
updated: 2024-01-01
maturity: stable
complexity: high
requirements:
  - Java project with ArchUnit dependency
  - Understanding of architecture rules
  - JUnit testing framework
---

# ArchUnit Architecture Tester

## Overview

This skill converts natural language descriptions of software architecture rules into executable ArchUnit test code for Java projects. It helps enforce architectural constraints and design principles through automated testing.

## Purpose

ArchUnit is a Java library for checking architecture characteristics. This skill bridges the gap between architectural decisions (expressed in natural language) and their automated enforcement through tests.

## When to Use

Use this skill when:
- You have architectural rules to enforce (e.g., layering, naming conventions)
- You want to prevent architecture violations in your Java codebase
- You need to codify architecture decisions as tests
- You're implementing hexagonal, onion, or clean architecture patterns
- You want to ensure package dependencies follow defined rules

## Instructions

### Step 1: Understand the Architecture Rule

Analyze the natural language rule to identify:
- **Rule type**: Layer dependency, naming convention, annotation usage, class structure
- **Scope**: Which packages or classes are affected
- **Constraint**: What is allowed or forbidden
- **Exceptions**: Any exemptions to the rule

**Examples of rule types:**
- Layer dependency: "Controllers should only depend on services, not repositories"
- Naming: "All repository classes must end with 'Repository'"
- Annotation: "All REST controllers must be annotated with @RestController"
- Inheritance: "All entities must extend BaseEntity"

### Step 2: Identify ArchUnit Pattern

Map the rule to an ArchUnit pattern:

- **Dependency rules**: `classes().that()...should().dependOn...()`
- **Naming rules**: `classes().that()...should().haveSimpleNameEndingWith()`
- **Annotation rules**: `classes().that().areAnnotatedWith()...should()`
- **Layer rules**: `layeredArchitecture().layer()...mayNotBeAccessedByAnyLayer()`
- **Package rules**: `noClasses().that().resideInAPackage()...should().dependOnClassesThat()`

### Step 3: Generate Test Class Structure

Create a JUnit test class with ArchUnit setup:

```java
@AnalyzeClasses(packages = "com.example")
public class ArchitectureTest {
    // Test methods will go here
}
```

### Step 4: Write Test Method

Generate the test method using ArchUnit DSL:

1. Use descriptive test method name reflecting the rule
2. Define the rule using ArchUnit fluent API
3. Apply the rule to imported classes
4. Add JavaDoc explaining the architectural constraint

### Step 5: Add Context and Documentation

Include:
- JavaDoc describing the rule and rationale
- Comments for complex rules
- Reference to architecture decision records (if applicable)
- Examples of compliant and non-compliant code in comments

### Step 6: Validate Test Syntax

Ensure:
- Correct ArchUnit API usage
- Proper import statements
- Valid package patterns
- Executable test that compiles

## Examples

### Example 1: Layer Dependency Rule

**Natural Language Rule:**
"Service layer classes should not depend on controller layer classes"

**Generated ArchUnit Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

@AnalyzeClasses(packages = "com.example")
public class LayerDependencyArchitectureTest {
    
    /**
     * Architectural Rule: Service Layer Isolation
     * 
     * Services should only depend on other services, repositories, and domain models.
     * They must not depend on controllers to maintain proper layering and prevent
     * circular dependencies.
     * 
     * Rationale: Controllers are the presentation layer and should depend on services,
     * not vice versa. This ensures a unidirectional dependency flow.
     */
    @Test
    void services_should_not_depend_on_controllers() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        ArchRule rule = noClasses()
            .that().resideInAPackage("..service..")
            .should().dependOnClassesThat()
            .resideInAPackage("..controller..");
        
        rule.check(importedClasses);
    }
}
```

### Example 2: Naming Convention Rule

**Natural Language Rule:**
"All repository interfaces must have names ending with 'Repository'"

**Generated ArchUnit Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;

@AnalyzeClasses(packages = "com.example")
public class NamingConventionArchitectureTest {
    
    /**
     * Architectural Rule: Repository Naming Convention
     * 
     * All repository interfaces must follow the naming pattern *Repository to ensure
     * consistency and discoverability across the codebase.
     * 
     * Examples:
     * ✓ UserRepository, OrderRepository, ProductRepository
     * ✗ UserDAO, UserDb, Users
     */
    @Test
    void repository_interfaces_should_have_repository_suffix() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        ArchRule rule = classes()
            .that().resideInAPackage("..repository..")
            .and().areInterfaces()
            .should().haveSimpleNameEndingWith("Repository");
        
        rule.check(importedClasses);
    }
}
```

### Example 3: Annotation Rule

**Natural Language Rule:**
"All classes in the controller package must be annotated with @RestController or @Controller"

**Generated ArchUnit Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RestController;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;

@AnalyzeClasses(packages = "com.example")
public class ControllerAnnotationArchitectureTest {
    
    /**
     * Architectural Rule: Controller Annotation Requirement
     * 
     * All controller classes must be properly annotated to ensure Spring can
     * detect and register them as HTTP request handlers.
     * 
     * Valid annotations: @RestController (for REST APIs), @Controller (for MVC)
     */
    @Test
    void controllers_should_be_annotated() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        ArchRule rule = classes()
            .that().resideInAPackage("..controller..")
            .and().areNotNestedClasses()
            .should().beAnnotatedWith(RestController.class)
            .orShould().beAnnotatedWith(Controller.class);
        
        rule.check(importedClasses);
    }
}
```

### Example 4: Layered Architecture

**Natural Language Rule:**
"Implement a layered architecture with Controller → Service → Repository dependencies. No layer should skip levels or create circular dependencies."

**Generated ArchUnit Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.library.Architectures;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.library.Architectures.layeredArchitecture;

@AnalyzeClasses(packages = "com.example")
public class LayeredArchitectureTest {
    
    /**
     * Architectural Rule: Layered Architecture Pattern
     * 
     * Enforces a strict layered architecture:
     * - Controller layer: HTTP/REST endpoints
     * - Service layer: Business logic
     * - Repository layer: Data access
     * - Domain layer: Domain models
     * 
     * Rules:
     * - Controllers may only access Services
     * - Services may access Repositories and Domain
     * - Repositories may only access Domain
     * - No layer may skip levels
     * - No circular dependencies
     */
    @Test
    void layered_architecture_should_be_respected() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        Architectures.LayeredArchitecture rule = layeredArchitecture()
            .consideringAllDependencies()
            .layer("Controller").definedBy("..controller..")
            .layer("Service").definedBy("..service..")
            .layer("Repository").definedBy("..repository..")
            .layer("Domain").definedBy("..domain..")
            
            .whereLayer("Controller").mayNotBeAccessedByAnyLayer()
            .whereLayer("Service").mayOnlyBeAccessedByLayers("Controller")
            .whereLayer("Repository").mayOnlyBeAccessedByLayers("Service")
            .whereLayer("Domain").mayOnlyBeAccessedByLayers("Repository", "Service", "Controller");
        
        rule.check(importedClasses);
    }
}
```

## Best Practices

1. **One Rule Per Test Method**: Keep test methods focused on a single architectural rule
2. **Descriptive Names**: Use method names that clearly describe the rule being tested
3. **Document Rationale**: Include JavaDoc explaining why the rule exists
4. **Use Constants**: Extract package patterns to constants for reusability
5. **Test Incrementally**: Add rules gradually, don't try to enforce everything at once
6. **Handle Legacy**: Use `.ignoreDependency()` for legacy code you can't fix immediately
7. **Fail Fast**: Run architecture tests early in the build pipeline
8. **Keep Updated**: Review and update rules as architecture evolves

## Error Handling

### Common Errors

**Error:** "Package '..service..' is not contained in ClassFileImporter"
- **Cause**: Package pattern doesn't match actual package structure
- **Solution**: Verify package names and use correct wildcard patterns

**Error:** "Rule violations detected"
- **Cause**: Code violates the architectural rule
- **Solution**: Either fix the code or re-evaluate if the rule is correct

**Error:** "Compilation error: Cannot find symbol"
- **Cause**: Missing ArchUnit dependency or wrong imports
- **Solution**: Add ArchUnit to pom.xml/build.gradle and use correct imports

### Handling Exceptions

For necessary rule violations (e.g., legacy code):

```java
ArchRule rule = noClasses()
    .that().resideInAPackage("..service..")
    .should().dependOnClassesThat()
    .resideInAPackage("..controller..")
    .because("Services should not depend on controllers")
    .ignoreDependency(LegacyService.class, SomeController.class);
```

## Security Considerations

- Architecture rules can enforce security boundaries
- Use rules to prevent sensitive data leakage between layers
- Ensure authentication/authorization layers are properly isolated
- Validate that security annotations are consistently applied

## Performance Notes

- ArchUnit tests analyze bytecode, which can be slow for large codebases
- Use caching: `@AnalyzeClasses(packages = "...", cacheMode = CacheMode.PER_CLASS)`
- Run architecture tests separately from unit tests in CI/CD
- Consider using import options to limit scope when necessary

## Limitations

- Only works for Java codebases
- Requires ArchUnit dependency (adds ~1MB to test classpath)
- Cannot enforce runtime behavior, only static structure
- May need updates when ArchUnit API changes
- Does not replace code review or manual architecture validation

## Related Skills

- **Code Review Assistant**: Complements with human review
- **Test Case Generator**: For generating other types of tests
- **API Documentation Generator**: For documenting architectural decisions

## Version History

- **1.0.0** (2024-01-01): Initial release

## Additional Resources

- [ArchUnit User Guide](https://www.archunit.org/userguide/html/000_Index.html)
- [ArchUnit JavaDoc](https://www.archunit.org/javadoc/0.23.1/)
- [ArchUnit Examples](https://github.com/TNG/ArchUnit-Examples)

## Notes

- Always run these tests as part of your CI/CD pipeline
- Consider creating a separate test class for each architectural concern
- Review and update rules when architectural decisions change
- Use these tests to onboard new team members to architectural patterns
