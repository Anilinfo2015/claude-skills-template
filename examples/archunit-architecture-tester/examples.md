# ArchUnit Architecture Tester - Examples

Additional examples demonstrating various architecture rule patterns.

## Example 5: Package Dependency Cycle Detection

**Natural Language Rule:**
"Prevent circular dependencies between packages"

**Generated Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.library.dependencies.SlicesRuleDefinition.slices;

@AnalyzeClasses(packages = "com.example")
public class PackageDependencyArchitectureTest {
    
    /**
     * Architectural Rule: No Circular Package Dependencies
     * 
     * Prevents circular dependencies between packages which can lead to:
     * - Difficult testing
     * - Tight coupling
     * - Hard to understand code flow
     * - Build issues
     */
    @Test
    void packages_should_be_free_of_cycles() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        slices()
            .matching("com.example.(*)..")
            .should().beFreeOfCycles()
            .check(importedClasses);
    }
}
```

## Example 6: Field Dependency Rule

**Natural Language Rule:**
"Services should not directly access entity fields; use getters instead"

**Generated Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

@AnalyzeClasses(packages = "com.example")
public class EncapsulationArchitectureTest {
    
    /**
     * Architectural Rule: Encapsulation in Domain Layer
     * 
     * Services should access entity properties through getters, not direct field access.
     * This ensures encapsulation and allows entities to control access to their state.
     */
    @Test
    void services_should_not_access_entity_fields_directly() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        ArchRule rule = noClasses()
            .that().resideInAPackage("..service..")
            .should().accessField(field -> 
                field.getOwner().getPackageName().contains("domain") &&
                !field.getModifiers().contains("PUBLIC")
            );
        
        rule.check(importedClasses);
    }
}
```

## Example 7: Inheritance Rule

**Natural Language Rule:**
"All JPA entities must extend BaseEntity abstract class"

**Generated Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;
import javax.persistence.Entity;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;

@AnalyzeClasses(packages = "com.example")
public class EntityInheritanceArchitectureTest {
    
    /**
     * Architectural Rule: Entity Base Class
     * 
     * All JPA entities must extend BaseEntity to ensure:
     * - Consistent ID generation
     * - Audit fields (createdAt, updatedAt)
     * - Common entity behaviors
     * - Version control for optimistic locking
     */
    @Test
    void jpa_entities_should_extend_base_entity() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        ArchRule rule = classes()
            .that().areAnnotatedWith(Entity.class)
            .should().beAssignableTo(BaseEntity.class)
            .because("all entities must inherit common functionality from BaseEntity");
        
        rule.check(importedClasses);
    }
}
```

## Example 8: Constructor Rule

**Natural Language Rule:**
"DTOs should only have private constructors and use builder pattern"

**Generated Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;
import static com.tngtech.archunit.core.domain.JavaModifier.PRIVATE;

@AnalyzeClasses(packages = "com.example")
public class DtoConstructorArchitectureTest {
    
    /**
     * Architectural Rule: DTO Builder Pattern
     * 
     * DTOs should use the builder pattern with:
     * - Private constructors
     * - Static builder() method
     * - Fluent setter methods in builder
     * 
     * This ensures immutability and clear object creation.
     */
    @Test
    void dtos_should_have_private_constructors() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        ArchRule rule = classes()
            .that().resideInAPackage("..dto..")
            .and().haveSimpleNameEndingWith("DTO")
            .should().haveOnlyPrivateConstructors()
            .because("DTOs should use builder pattern with private constructors");
        
        rule.check(importedClasses);
    }
}
```

## Example 9: Utility Class Rule

**Natural Language Rule:**
"Utility classes should be final and have private constructor"

**Generated Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;
import static com.tngtech.archunit.core.domain.JavaClass.Predicates.resideInAPackage;
import static com.tngtech.archunit.core.domain.JavaModifier.FINAL;

@AnalyzeClasses(packages = "com.example")
public class UtilityClassArchitectureTest {
    
    /**
     * Architectural Rule: Utility Class Design
     * 
     * Utility classes (containing only static methods) should be:
     * - Declared as final (cannot be extended)
     * - Have private constructor (cannot be instantiated)
     * 
     * This prevents misuse and clearly indicates the class's purpose.
     */
    @Test
    void utility_classes_should_be_final_with_private_constructor() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        ArchRule rule = classes()
            .that().resideInAPackage("..util..")
            .and().haveSimpleNameEndingWith("Utils")
            .should().haveModifier(FINAL)
            .andShould().haveOnlyPrivateConstructors()
            .because("utility classes should not be instantiated or extended");
        
        rule.check(importedClasses);
    }
}
```

## Example 10: Spring Component Rule

**Natural Language Rule:**
"Classes in service package should be annotated with @Service, not @Component"

**Generated Test:**

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;
import org.springframework.stereotype.Service;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.classes;

@AnalyzeClasses(packages = "com.example")
public class SpringComponentArchitectureTest {
    
    /**
     * Architectural Rule: Specific Spring Annotations
     * 
     * Service layer classes should use @Service annotation instead of generic
     * @Component for better semantic meaning and easier component scanning.
     */
    @Test
    void services_should_be_annotated_with_service_annotation() {
        JavaClasses importedClasses = new ClassFileImporter()
            .importPackages("com.example");
        
        ArchRule rule = classes()
            .that().resideInAPackage("..service..")
            .and().areNotNestedClasses()
            .and().areNotAnonymousClasses()
            .should().beAnnotatedWith(Service.class)
            .because("services should use @Service for clear semantic meaning");
        
        rule.check(importedClasses);
    }
}
```

## Usage Scenarios

### Scenario 1: Onboarding New Developers

When a new developer joins the team:

1. Show them the architecture test suite
2. Run tests and explain any failures
3. Use test names to explain architectural decisions
4. Reference JavaDoc for detailed rationale

### Scenario 2: Refactoring Legacy Code

When refactoring:

1. Add architecture tests for desired state
2. Mark violations with `.ignoreDependency()` initially
3. Fix violations incrementally
4. Remove ignore statements as you fix code
5. Prevent new violations from being introduced

### Scenario 3: Architecture Decision Review

During architecture reviews:

1. Discuss proposed rule in natural language
2. Convert to ArchUnit test as documentation
3. Run test to validate it catches violations
4. Add test to suite before implementing architecture change

### Scenario 4: CI/CD Integration

In your build pipeline:

```xml
<!-- Maven -->
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <configuration>
                <includes>
                    <include>**/*Test.java</include>
                    <include>**/*ArchitectureTest.java</include>
                </includes>
            </configuration>
        </plugin>
    </plugins>
</build>
```

```groovy
// Gradle
test {
    include '**/*Test.class'
    include '**/*ArchitectureTest.class'
    
    // Fail build on architecture violations
    testLogging {
        events "failed"
        exceptionFormat "full"
    }
}
```

## Advanced Patterns

### Custom Conditions

```java
import com.tngtech.archunit.core.domain.JavaClass;
import com.tngtech.archunit.lang.ArchCondition;
import com.tngtech.archunit.lang.ConditionEvents;

ArchCondition<JavaClass> haveALogger = new ArchCondition<>("have a logger") {
    @Override
    public void check(JavaClass item, ConditionEvents events) {
        boolean hasLogger = item.getFields().stream()
            .anyMatch(field -> field.getRawType().getName().equals("org.slf4j.Logger"));
        
        if (!hasLogger) {
            events.add(SimpleConditionEvent.violated(item, 
                item.getName() + " does not have a logger field"));
        }
    }
};
```

### Freezing Architecture

For existing violations you can't fix immediately:

```java
@Test
void freeze_existing_violations() {
    FreezingArchRule rule = FreezingArchRule.freeze(
        noClasses()
            .that().resideInAPackage("..service..")
            .should().dependOnClassesThat()
            .resideInAPackage("..controller..")
    );
    
    rule.check(importedClasses);
}
```

This allows CI to pass while preventing new violations.

## Tips and Tricks

1. **Start Simple**: Begin with basic rules, add complexity gradually
2. **Use PlantUML**: Generate architecture diagrams from ArchUnit rules
3. **Combine Rules**: Use `.andShould()` and `.orShould()` for complex rules
4. **Test Your Tests**: Intentionally violate rules to ensure tests catch them
5. **Document Exceptions**: When using `.ignoreDependency()`, document why
6. **Regex Patterns**: Use careful regex for package matching
7. **Custom Predicates**: Create reusable predicates for common patterns
8. **Performance**: Cache analysis results for faster test execution

## Troubleshooting

**Tests are slow:**
- Use caching: `@AnalyzeClasses(cacheMode = CacheMode.PER_CLASS)`
- Limit scope of import: `.importPackages()` instead of `.importPath()`
- Run architecture tests in separate test suite

**False positives:**
- Review package patterns for accuracy
- Check for test code being analyzed (exclude it)
- Verify class modifiers and annotations

**Rules not enforced:**
- Ensure tests run in CI/CD
- Verify test discovery configuration
- Check for overly permissive rules
