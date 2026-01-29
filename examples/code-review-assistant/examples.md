# Code Review Assistant - Extended Examples

Real-world code review examples demonstrating different scenarios, languages, and review types.

## Example 1: Python Security Review

### Code Being Reviewed

```python
# user_service.py
def get_user_by_email(email):
    query = f"SELECT * FROM users WHERE email = '{email}'"
    cursor.execute(query)
    return cursor.fetchone()

def update_user_profile(user_id, data):
    user = User.query.get(user_id)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def upload_avatar(file):
    filename = file.filename
    file.save(f"/uploads/avatars/{filename}")
    return filename
```

### Review Feedback

```markdown
## Security Review: User Service Updates

### Critical Issues 🔴

1. **SQL Injection Vulnerability**
   Location: `user_service.py:3`
   
   Issue: The query uses f-string with unsanitized user input:
   ```python
   query = f"SELECT * FROM users WHERE email = '{email}'"
   ```
   
   Impact: An attacker can inject SQL commands. Example:
   `email = "'; DROP TABLE users; --"` would execute arbitrary SQL.
   
   Fix: Use parameterized queries:
   ```python
   query = "SELECT * FROM users WHERE email = %s"
   cursor.execute(query, (email,))
   ```

2. **Mass Assignment Vulnerability**
   Location: `user_service.py:8-10`
   
   Issue: Setting arbitrary attributes from user input allows attackers to 
   modify fields they shouldn't access (e.g., is_admin, password_hash).
   
   Impact: User could elevate privileges or modify sensitive fields.
   
   Fix: Whitelist allowed fields:
   ```python
   allowed_fields = ['name', 'bio', 'avatar_url']
   for key in allowed_fields:
       if key in data:
           setattr(user, key, data[key])
   ```

3. **Path Traversal Vulnerability**
   Location: `user_service.py:14-16`
   
   Issue: Using unsanitized filename allows directory traversal:
   `filename = "../../etc/passwd"` could overwrite system files.
   
   Impact: Attacker could overwrite critical files or access restricted areas.
   
   Fix: Sanitize filename and use secure path joining:
   ```python
   import os
   from werkzeug.utils import secure_filename
   
   safe_filename = secure_filename(file.filename)
   filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
   file.save(filepath)
   ```

### Important Suggestions 🟡

1. **Add Input Validation**
   Location: `user_service.py:2`
   
   Recommendation: Validate email format before query:
   ```python
   import re
   
   def is_valid_email(email):
       pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
       return re.match(pattern, email) is not None
   
   def get_user_by_email(email):
       if not is_valid_email(email):
           raise ValueError("Invalid email format")
       # ... rest of function
   ```

2. **Add File Type Validation**
   Location: `user_service.py:14`
   
   Recommendation: Validate file type and size:
   ```python
   ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
   MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
   
   def allowed_file(filename):
       return '.' in filename and \
              filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
   
   def upload_avatar(file):
       if not allowed_file(file.filename):
           raise ValueError("Invalid file type")
       # Check file size...
   ```

### Summary

**Overall Assessment**: Request Changes (Must fix critical security issues)

**Critical Issues**: 3 - All must be fixed before merge
**Important Suggestions**: 2 - Should be addressed
**Security**: Serious issues - Multiple critical vulnerabilities

**Recommendation**: Do not merge until all critical security issues are resolved.

**Next Steps**:
1. Fix SQL injection with parameterized queries
2. Fix mass assignment with field whitelisting
3. Fix path traversal with filename sanitization
4. Add input validation for email
5. Add file type and size validation
6. Request re-review after fixes
```

## Example 2: JavaScript Performance Review

### Code Being Reviewed

```javascript
// order_processor.js
async function processOrders(orderIds) {
  const results = [];
  
  for (const orderId of orderIds) {
    const order = await Order.findById(orderId);
    const user = await User.findById(order.userId);
    const items = await Item.find({ orderId: order.id });
    
    for (const item of items) {
      const product = await Product.findById(item.productId);
      item.productName = product.name;
      item.productPrice = product.price;
    }
    
    const total = items.reduce((sum, item) => {
      return sum + (item.productPrice * item.quantity);
    }, 0);
    
    results.push({
      order: order,
      user: user,
      items: items,
      total: total
    });
  }
  
  return results;
}
```

### Review Feedback

```markdown
## Performance Review: Order Processing

### Critical Issues 🔴

1. **Severe N+1 Query Problem**
   Location: `order_processor.js:5-7`
   
   Issue: Sequential database queries in loops create massive performance problem.
   
   Current behavior (for 100 orders with 5 items each):
   - 100 queries for orders
   - 100 queries for users  
   - 100 queries for items
   - 500 queries for products
   - **Total: 800 database queries**
   
   Impact: For 100 orders, this takes ~20 seconds. For 1000 orders, could timeout.
   
   Fix: Batch all queries:
   ```javascript
   async function processOrders(orderIds) {
     // Single query for all orders
     const orders = await Order.find({ _id: { $in: orderIds } });
     
     // Single query for all users
     const userIds = [...new Set(orders.map(o => o.userId))];
     const users = await User.find({ _id: { $in: userIds } });
     const userMap = new Map(users.map(u => [u._id.toString(), u]));
     
     // Single query for all items
     const items = await Item.find({ orderId: { $in: orderIds } });
     const itemsByOrder = items.reduce((acc, item) => {
       if (!acc[item.orderId]) acc[item.orderId] = [];
       acc[item.orderId].push(item);
       return acc;
     }, {});
     
     // Single query for all products
     const productIds = [...new Set(items.map(i => i.productId))];
     const products = await Product.find({ _id: { $in: productIds } });
     const productMap = new Map(products.map(p => [p._id.toString(), p]));
     
     // Process in memory
     return orders.map(order => {
       const orderItems = itemsByOrder[order.id] || [];
       orderItems.forEach(item => {
         const product = productMap.get(item.productId.toString());
         item.productName = product.name;
         item.productPrice = product.price;
       });
       
       const total = orderItems.reduce((sum, item) => 
         sum + (item.productPrice * item.quantity), 0
       );
       
       return {
         order: order,
         user: userMap.get(order.userId.toString()),
         items: orderItems,
         total: total
       };
     });
   }
   ```
   
   Result: Reduces 800 queries to just 4, improving from ~20s to ~0.5s

### Important Suggestions 🟡

1. **Add Database Indexes**
   
   Recommendation: Ensure these indexes exist:
   ```javascript
   // In your migration or model definitions
   Order.index({ _id: 1 });
   Item.index({ orderId: 1 });
   Item.index({ productId: 1 });
   User.index({ _id: 1 });
   Product.index({ _id: 1 });
   ```
   
   This ensures fast lookups even with optimized queries.

2. **Add Caching Layer**
   Location: Product lookups
   
   Recommendation: Products probably don't change often. Consider caching:
   ```javascript
   const cache = require('./cache');
   
   async function getProductsWithCache(productIds) {
     const cacheKeys = productIds.map(id => `product:${id}`);
     const cached = await cache.mget(cacheKeys);
     
     const missingIds = productIds.filter((id, idx) => !cached[idx]);
     if (missingIds.length > 0) {
       const products = await Product.find({ _id: { $in: missingIds } });
       await Promise.all(products.map(p => 
         cache.set(`product:${p._id}`, p, 3600) // 1 hour TTL
       ));
       return [...cached.filter(Boolean), ...products];
     }
     
     return cached;
   }
   ```

3. **Add Error Handling**
   
   Current code has no error handling. Consider:
   ```javascript
   async function processOrders(orderIds) {
     try {
       // ... processing logic
     } catch (error) {
       logger.error('Failed to process orders', {
         orderIds,
         error: error.message,
         stack: error.stack
       });
       throw new Error(`Order processing failed: ${error.message}`);
     }
   }
   ```

### Nitpicks ⚪

1. **Variable Naming**
   Location: Line 19
   
   Consider more descriptive name:
   ```javascript
   const total = items.reduce((sum, item) => ...
   // Could be:
   const orderTotal = items.reduce((totalPrice, item) => ...
   ```

### Positive Feedback ✅

1. **Clean Data Structure**
   Location: Lines 23-28
   
   The returned object structure is clean and intuitive. Good separation of 
   concerns with order, user, items, and total clearly defined.

### Summary

**Overall Assessment**: Request Changes (Critical performance issue)

**Critical Issues**: 1 - Must fix N+1 query problem
**Important Suggestions**: 3 - Should address for production readiness
**Code Quality**: Good (once performance fixed)
**Performance**: Critical issues - 40x performance degradation

**Recommendation**: Fix the N+1 query problem before merge. Consider caching 
for additional performance gains.

**Next Steps**:
1. Implement batched queries (reduces 800 queries to 4)
2. Verify database indexes exist
3. Add error handling
4. Consider caching for products (optional but recommended)
5. Performance test with realistic data volumes
```

## Example 3: Java Architecture Review

### Code Being Reviewed

```java
// UserController.java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private EntityManager entityManager;
    
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody User user) {
        // Validate email
        if (!user.getEmail().contains("@")) {
            return ResponseEntity.badRequest().build();
        }
        
        // Hash password
        String hashedPassword = user.getPassword() + "salt123";
        user.setPassword(hashedPassword);
        
        // Save to database
        entityManager.persist(user);
        
        // Send welcome email
        String emailBody = "<html><body>Welcome " + user.getName() + "!</body></html>";
        EmailService.sendEmail(user.getEmail(), "Welcome", emailBody);
        
        // Log to file
        try {
            FileWriter writer = new FileWriter("users.log", true);
            writer.write(user.getEmail() + " registered at " + new Date() + "\n");
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        return ResponseEntity.ok(user);
    }
}
```

### Review Feedback

```markdown
## Architecture Review: User Creation Endpoint

### Critical Issues 🔴

1. **Password Security Flaw**
   Location: `UserController.java:17-18`
   
   Issue: Password "hashing" is just concatenation with a hardcoded salt:
   ```java
   String hashedPassword = user.getPassword() + "salt123";
   ```
   
   Impact: This provides NO security. Passwords are essentially stored in 
   plaintext. A database breach exposes all passwords.
   
   Fix: Use proper password hashing with bcrypt:
   ```java
   import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
   
   private final BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
   
   String hashedPassword = passwordEncoder.encode(user.getPassword());
   user.setPassword(hashedPassword);
   ```

2. **XSS Vulnerability**
   Location: `UserController.java:24`
   
   Issue: User name is directly interpolated into HTML without escaping:
   ```java
   String emailBody = "<html><body>Welcome " + user.getName() + "!</body></html>";
   ```
   
   Impact: If user name contains `<script>alert('xss')</script>`, it executes 
   when email is viewed in HTML-enabled clients.
   
   Fix: Use HTML escaping or template engine:
   ```java
   import org.apache.commons.text.StringEscapeUtils;
   
   String emailBody = "<html><body>Welcome " + 
                      StringEscapeUtils.escapeHtml4(user.getName()) + 
                      "!</body></html>";
   ```

### Important Suggestions 🟡

1. **Separation of Concerns Violation**
   Location: Entire method
   
   Issue: Controller is doing too much:
   - Input validation (line 11)
   - Password hashing (line 17)
   - Database operations (line 21)
   - Email sending (line 24)
   - File logging (lines 27-33)
   
   This violates Single Responsibility Principle and makes testing difficult.
   
   Recommendation: Extract to service layer:
   ```java
   @RestController
   @RequestMapping("/api/users")
   public class UserController {
       
       private final UserService userService;
       
       @Autowired
       public UserController(UserService userService) {
           this.userService = userService;
       }
       
       @PostMapping
       public ResponseEntity<UserResponse> createUser(@Valid @RequestBody CreateUserRequest request) {
           try {
               UserResponse user = userService.createUser(request);
               return ResponseEntity.ok(user);
           } catch (ValidationException e) {
               return ResponseEntity.badRequest().body(new ErrorResponse(e.getMessage()));
           }
       }
   }
   
   @Service
   public class UserService {
       
       private final UserRepository userRepository;
       private final EmailService emailService;
       private final PasswordEncoder passwordEncoder;
       private final UserValidator userValidator;
       
       @Transactional
       public UserResponse createUser(CreateUserRequest request) {
           userValidator.validate(request);
           
           User user = new User();
           user.setEmail(request.getEmail());
           user.setPassword(passwordEncoder.encode(request.getPassword()));
           user.setName(request.getName());
           
           User saved = userRepository.save(user);
           
           emailService.sendWelcomeEmail(saved);
           
           return UserResponse.from(saved);
       }
   }
   ```

2. **Missing Input Validation**
   Location: `UserController.java:11-13`
   
   Issue: Email validation is insufficient (only checks for @). Missing:
   - Proper email format validation
   - Name validation
   - Password strength requirements
   - Duplicate email check
   
   Recommendation: Use Bean Validation:
   ```java
   public class CreateUserRequest {
       @NotNull
       @Email(message = "Email must be valid")
       private String email;
       
       @NotBlank(message = "Name is required")
       @Size(min = 2, max = 100)
       private String name;
       
       @NotNull
       @Size(min = 8, message = "Password must be at least 8 characters")
       @Pattern(regexp = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                message = "Password must contain uppercase, lowercase, digit, and special character")
       private String password;
   }
   
   @PostMapping
   public ResponseEntity<UserResponse> createUser(@Valid @RequestBody CreateUserRequest request) {
       // Validation happens automatically
   }
   ```

3. **Transaction Management Missing**
   Location: Lines 21-24
   
   Issue: No transaction management. If email sending fails after database 
   save, you have inconsistent state (user created but no welcome email).
   
   Recommendation: Use @Transactional and handle email asynchronously:
   ```java
   @Transactional
   public User createUser(CreateUserRequest request) {
       User saved = userRepository.save(user);
       
       // Publish event for async processing
       applicationEventPublisher.publishEvent(new UserCreatedEvent(saved));
       
       return saved;
   }
   
   @EventListener
   @Async
   public void handleUserCreated(UserCreatedEvent event) {
       try {
           emailService.sendWelcomeEmail(event.getUser());
       } catch (Exception e) {
           logger.error("Failed to send welcome email", e);
           // Could retry or alert ops team
       }
   }
   ```

4. **Poor Error Handling**
   Location: Lines 28-32
   
   Issue: Exception is just printed to console. No proper logging, no recovery.
   
   Recommendation: Use proper logging framework:
   ```java
   import org.slf4j.Logger;
   import org.slf4j.LoggerFactory;
   
   private static final Logger logger = LoggerFactory.getLogger(UserController.class);
   
   try {
       // ... file operations
   } catch (IOException e) {
       logger.error("Failed to log user registration", e);
       // Don't fail user creation due to logging failure
   }
   ```

5. **Resource Leak**
   Location: Lines 28-31
   
   Issue: FileWriter is not closed if exception occurs before line 31.
   
   Fix: Use try-with-resources:
   ```java
   try (FileWriter writer = new FileWriter("users.log", true)) {
       writer.write(user.getEmail() + " registered at " + new Date() + "\n");
   } catch (IOException e) {
       logger.error("Failed to log user registration", e);
   }
   ```

6. **Direct EntityManager Usage**
   Location: Line 21
   
   Issue: Using EntityManager directly in controller. Should use Repository pattern.
   
   Recommendation:
   ```java
   public interface UserRepository extends JpaRepository<User, Long> {
       Optional<User> findByEmail(String email);
   }
   
   // In service:
   User saved = userRepository.save(user);
   ```

### Nitpicks ⚪

1. **Return Sensitive Data**
   Location: Line 35
   
   Consider not returning password (even if hashed) in response:
   ```java
   public class UserResponse {
       private Long id;
       private String email;
       private String name;
       // No password field
   }
   ```

2. **Magic String**
   Location: Line 24
   
   Extract to constant:
   ```java
   private static final String WELCOME_EMAIL_SUBJECT = "Welcome";
   ```

### Summary

**Overall Assessment**: Needs Major Revision

**Critical Issues**: 2 - Security vulnerabilities must be fixed
**Important Suggestions**: 6 - Architecture and best practices  
**Code Quality**: Needs Improvement
**Security**: Serious issues
**Architecture**: Needs refactoring

**Recommendation**: Major rework needed before merge

**Next Steps**:
1. Fix password hashing (use BCrypt)
2. Fix XSS vulnerability (escape HTML)
3. Refactor to service layer pattern
4. Add proper input validation with Bean Validation
5. Implement transaction management
6. Use Repository pattern instead of EntityManager
7. Add proper error handling and logging
8. Make email sending asynchronous
9. Add unit tests for UserService
10. Add integration tests for endpoint

This is a good learning opportunity to understand Spring Boot best practices. 
Happy to pair on the refactoring if helpful!
```

## Example 4: TypeScript Code Quality Review

### Code Being Reviewed

```typescript
// payment-processor.ts
export class PaymentProcessor {
  processPayment(amount: any, method: any, userId: any) {
    if (amount <= 0) {
      throw new Error("Invalid amount");
    }
    
    let fee;
    if (method == "credit_card") {
      fee = amount * 0.029 + 0.3;
    } else if (method == "debit_card") {
      fee = amount * 0.019 + 0.25;
    } else if (method == "bank_transfer") {
      fee = 0;
    } else {
      throw new Error("Invalid payment method");
    }
    
    const total = amount + fee;
    
    // Process payment
    const result = this.callPaymentAPI(method, total, userId);
    
    if (result.success) {
      this.saveTransaction(userId, amount, fee, method);
      this.sendEmail(userId, total);
      return { success: true, transactionId: result.id };
    } else {
      return { success: false, error: result.error };
    }
  }
  
  callPaymentAPI(method: any, amount: any, userId: any): any {
    // Implementation
  }
  
  saveTransaction(userId: any, amount: any, fee: any, method: any): void {
    // Implementation
  }
  
  sendEmail(userId: any, amount: any): void {
    // Implementation
  }
}
```

### Review Feedback

```markdown
## Code Quality Review: Payment Processor

### Important Suggestions 🟡

1. **No Type Safety**
   Location: Throughout the file
   
   Issue: Using `any` type everywhere defeats the purpose of TypeScript:
   ```typescript
   processPayment(amount: any, method: any, userId: any)
   ```
   
   This provides no type checking, IDE support, or compile-time error detection.
   
   Recommendation: Use proper types:
   ```typescript
   enum PaymentMethod {
     CREDIT_CARD = 'credit_card',
     DEBIT_CARD = 'debit_card',
     BANK_TRANSFER = 'bank_transfer'
   }
   
   interface PaymentResult {
     success: boolean;
     transactionId?: string;
     error?: string;
   }
   
   interface PaymentAPIResult {
     success: boolean;
     id?: string;
     error?: string;
   }
   
   export class PaymentProcessor {
     processPayment(
       amount: number, 
       method: PaymentMethod, 
       userId: string
     ): PaymentResult {
       // Now TypeScript can catch errors at compile time
     }
   }
   ```

2. **Magic Numbers**
   Location: Lines 9-14
   
   Issue: Fee calculations use hardcoded numbers with no context:
   ```typescript
   fee = amount * 0.029 + 0.3;
   ```
   
   Recommendation: Extract to constants with clear naming:
   ```typescript
   const PAYMENT_FEES = {
     [PaymentMethod.CREDIT_CARD]: {
       percentageFee: 0.029,  // 2.9%
       fixedFee: 0.30         // $0.30
     },
     [PaymentMethod.DEBIT_CARD]: {
       percentageFee: 0.019,  // 1.9%
       fixedFee: 0.25         // $0.25
     },
     [PaymentMethod.BANK_TRANSFER]: {
       percentageFee: 0,
       fixedFee: 0
     }
   } as const;
   
   private calculateFee(amount: number, method: PaymentMethod): number {
     const feeStructure = PAYMENT_FEES[method];
     return amount * feeStructure.percentageFee + feeStructure.fixedFee;
   }
   ```

3. **Using == Instead of ===**
   Location: Lines 9, 11, 13
   
   Issue: Loose equality (==) can cause unexpected type coercion bugs.
   
   Fix: Use strict equality (===) or, better, use enum as shown above:
   ```typescript
   if (method === PaymentMethod.CREDIT_CARD) {
     // ...
   }
   ```

4. **No Error Handling for Async Operations**
   Location: Lines 22, 25, 26
   
   Issue: No try-catch blocks. If any operation fails, unhandled exception crashes.
   
   Recommendation: Add comprehensive error handling:
   ```typescript
   async processPayment(
     amount: number,
     method: PaymentMethod,
     userId: string
   ): Promise<PaymentResult> {
     try {
       this.validatePayment(amount, method);
       
       const fee = this.calculateFee(amount, method);
       const total = amount + fee;
       
       const apiResult = await this.callPaymentAPI(method, total, userId);
       
       if (!apiResult.success) {
         logger.warn('Payment API failed', { userId, method, error: apiResult.error });
         return { success: false, error: apiResult.error };
       }
       
       await Promise.all([
         this.saveTransaction(userId, amount, fee, method, apiResult.id!),
         this.sendEmail(userId, total).catch(err => {
           logger.error('Failed to send confirmation email', { userId, error: err });
           // Don't fail payment due to email error
         })
       ]);
       
       return { success: true, transactionId: apiResult.id! };
       
     } catch (error) {
       logger.error('Payment processing failed', { userId, error });
       return { 
         success: false, 
         error: error instanceof Error ? error.message : 'Unknown error' 
       };
     }
   }
   ```

5. **Missing Input Validation**
   Location: Line 3
   
   Issue: Only validates amount > 0. Missing validations:
   - Maximum amount limits
   - Currency validation
   - Method validity
   - User existence
   
   Recommendation: Add comprehensive validation:
   ```typescript
   private validatePayment(amount: number, method: PaymentMethod, userId: string): void {
     if (amount <= 0) {
       throw new ValidationError('Amount must be greater than zero');
     }
     
     if (amount > 100000) {
       throw new ValidationError('Amount exceeds maximum allowed ($100,000)');
     }
     
     if (!Object.values(PaymentMethod).includes(method)) {
       throw new ValidationError(`Invalid payment method: ${method}`);
     }
     
     if (!userId || userId.trim().length === 0) {
       throw new ValidationError('User ID is required');
     }
   }
   ```

6. **No Logging**
   Location: Throughout
   
   Issue: No logging for debugging or audit trail.
   
   Recommendation: Add structured logging:
   ```typescript
   import { logger } from './logger';
   
   async processPayment(...): Promise<PaymentResult> {
     logger.info('Processing payment', { userId, amount, method });
     
     try {
       // ... processing
       
       logger.info('Payment successful', { 
         userId, 
         transactionId: apiResult.id,
         amount,
         fee 
       });
       
       return { success: true, transactionId: apiResult.id };
     } catch (error) {
       logger.error('Payment failed', { userId, amount, error });
       throw error;
     }
   }
   ```

7. **Synchronous API Call Assumption**
   Location: Line 22
   
   Issue: Code assumes callPaymentAPI is synchronous, but payment APIs are 
   typically async. This could cause issues.
   
   Recommendation: Make async:
   ```typescript
   private async callPaymentAPI(
     method: PaymentMethod,
     amount: number,
     userId: string
   ): Promise<PaymentAPIResult> {
     const response = await fetch('/api/payment', {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify({ method, amount, userId })
     });
     
     if (!response.ok) {
       throw new PaymentAPIError('Payment API request failed');
     }
     
     return response.json();
   }
   ```

### Nitpicks ⚪

1. **Method Naming**
   Location: Line 2
   
   Consider more specific name: `processPayment` → `processSinglePayment` or 
   `createPaymentTransaction` to clarify it handles one payment.

2. **Email Sending Timing**
   Location: Line 26
   
   Consider: Should email be sent before or after saving transaction? Current 
   order could send email even if save fails.

### Positive Feedback ✅

1. **Clean Return Values**
   Location: Lines 27, 29
   
   Returning consistent result objects with success/failure is good pattern. 
   Makes it easy for callers to handle both cases.

2. **Fee Calculation Separation**
   
   Having separate logic for different payment methods is correct approach. 
   Just needs to be extracted to make it more maintainable.

### Summary

**Overall Assessment**: Approve with Suggestions

**Important Suggestions**: 7 - Would significantly improve code quality
**Nitpicks**: 2
**Code Quality**: Adequate → Could be Good with changes
**Type Safety**: Needs improvement

**Recommendation**: Approve, but strongly recommend addressing type safety and 
error handling before next sprint.

**Priority Improvements**:
1. Replace `any` with proper types (breaks TypeScript benefits)
2. Add error handling (prevents production issues)
3. Extract magic numbers to constants (improves maintainability)
4. Use strict equality (===) (prevents bugs)
5. Add logging (helps debugging)

**Nice to Have**:
- Async/await for API calls
- Comprehensive validation
- Better method names

Would be happy to pair on the refactoring if you'd like!
```

## Example 5: Go Concurrency Review

### Code Being Reviewed

```go
// worker_pool.go
package worker

import "sync"

type Job struct {
    ID   int
    Data string
}

func ProcessJobs(jobs []Job) []string {
    results := make([]string, len(jobs))
    var wg sync.WaitGroup
    
    for i, job := range jobs {
        wg.Add(1)
        go func(index int, j Job) {
            results[index] = processJob(j)
            wg.Done()
        }(i, job)
    }
    
    wg.Wait()
    return results
}

func processJob(job Job) string {
    // Simulate processing
    return "processed: " + job.Data
}
```

### Review Feedback

```markdown
## Concurrency Review: Worker Pool

### Important Suggestions 🟡

1. **Unbounded Goroutine Creation**
   Location: Lines 14-20
   
   Issue: Creates one goroutine per job with no limit. For 10,000 jobs, creates 
   10,000 goroutines simultaneously, which can:
   - Exhaust system resources
   - Cause out-of-memory errors
   - Reduce performance due to context switching
   
   Recommendation: Use worker pool with bounded concurrency:
   ```go
   func ProcessJobs(jobs []Job, maxWorkers int) []string {
       results := make([]string, len(jobs))
       jobChan := make(chan struct{ index int; job Job }, len(jobs))
       var wg sync.WaitGroup
       
       // Start fixed number of workers
       for w := 0; w < maxWorkers; w++ {
           wg.Add(1)
           go func() {
               defer wg.Done()
               for item := range jobChan {
                   results[item.index] = processJob(item.job)
               }
           }()
       }
       
       // Send jobs to workers
       for i, job := range jobs {
           jobChan <- struct{ index int; job Job }{i, job}
       }
       close(jobChan)
       
       wg.Wait()
       return results
   }
   ```

2. **Race Condition on Results Slice**
   Location: Line 17
   
   Issue: Multiple goroutines write to `results` slice concurrently without 
   synchronization. While this specific code is safe (different indices), it's 
   fragile and could break with minor changes.
   
   Recommendation: Make it explicit and safe:
   ```go
   type result struct {
       index int
       value string
   }
   
   func ProcessJobs(jobs []Job, maxWorkers int) []string {
       resultChan := make(chan result, len(jobs))
       jobChan := make(chan struct{ index int; job Job }, len(jobs))
       var wg sync.WaitGroup
       
       // Workers
       for w := 0; w < maxWorkers; w++ {
           wg.Add(1)
           go func() {
               defer wg.Done()
               for item := range jobChan {
                   processed := processJob(item.job)
                   resultChan <- result{item.index, processed}
               }
           }()
       }
       
       // Close result channel when all workers done
       go func() {
           wg.Wait()
           close(resultChan)
       }()
       
       // Send jobs
       for i, job := range jobs {
           jobChan <- struct{ index int; job Job }{i, job}
       }
       close(jobChan)
       
       // Collect results
       results := make([]string, len(jobs))
       for r := range resultChan {
           results[r.index] = r.value
       }
       
       return results
   }
   ```

3. **No Error Handling**
   Location: Throughout
   
   Issue: `processJob` has no way to return errors. If processing fails, error 
   is silently lost.
   
   Recommendation: Add error handling:
   ```go
   type JobResult struct {
       Value string
       Error error
   }
   
   func ProcessJobs(jobs []Job, maxWorkers int) ([]string, error) {
       type workItem struct {
           index int
           job   Job
       }
       
       type resultItem struct {
           index int
           value string
           err   error
       }
       
       jobChan := make(chan workItem, len(jobs))
       resultChan := make(chan resultItem, len(jobs))
       var wg sync.WaitGroup
       
       // Workers
       for w := 0; w < maxWorkers; w++ {
           wg.Add(1)
           go func() {
               defer wg.Done()
               for item := range jobChan {
                   value, err := processJob(item.job)
                   resultChan <- resultItem{item.index, value, err}
               }
           }()
       }
       
       // Result collector
       go func() {
           wg.Wait()
           close(resultChan)
       }()
       
       // Send jobs
       for i, job := range jobs {
           jobChan <- workItem{i, job}
       }
       close(jobChan)
       
       // Collect results
       results := make([]string, len(jobs))
       var errors []error
       
       for r := range resultChan {
           if r.err != nil {
               errors = append(errors, fmt.Errorf("job %d: %w", r.index, r.err))
           } else {
               results[r.index] = r.value
           }
       }
       
       if len(errors) > 0 {
           return results, fmt.Errorf("failed to process %d jobs: %v", 
                                      len(errors), errors)
       }
       
       return results, nil
   }
   
   func processJob(job Job) (string, error) {
       // Can now return errors
       if job.Data == "" {
           return "", fmt.Errorf("empty job data")
       }
       return "processed: " + job.Data, nil
   }
   ```

4. **No Context Support**
   Location: Function signature
   
   Issue: No way to cancel processing or set timeouts. If a job hangs, the 
   entire process waits indefinitely.
   
   Recommendation: Add context support:
   ```go
   func ProcessJobs(ctx context.Context, jobs []Job, maxWorkers int) ([]string, error) {
       // ... setup code ...
       
       // Workers with context
       for w := 0; w < maxWorkers; w++ {
           wg.Add(1)
           go func() {
               defer wg.Done()
               for {
                   select {
                   case <-ctx.Done():
                       return
                   case item, ok := <-jobChan:
                       if !ok {
                           return
                       }
                       value, err := processJobWithContext(ctx, item.job)
                       select {
                       case resultChan <- resultItem{item.index, value, err}:
                       case <-ctx.Done():
                           return
                       }
                   }
               }
           }()
       }
       
       // ... rest of implementation ...
   }
   
   // Usage with timeout:
   ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
   defer cancel()
   results, err := ProcessJobs(ctx, jobs, 10)
   ```

5. **No Panic Recovery**
   Location: Goroutines
   
   Issue: If `processJob` panics, it crashes the goroutine and the program may 
   hang waiting for that worker to finish.
   
   Recommendation: Add panic recovery:
   ```go
   go func() {
       defer func() {
           if r := recover(); r != nil {
               err := fmt.Errorf("panic processing job: %v", r)
               resultChan <- resultItem{item.index, "", err}
           }
           wg.Done()
       }()
       
       value, err := processJob(item.job)
       resultChan <- resultItem{item.index, value, err}
   }()
   ```

### Nitpicks ⚪

1. **Missing Package Documentation**
   
   Add package comment:
   ```go
   // Package worker provides concurrent job processing with bounded parallelism.
   package worker
   ```

2. **Magic Number**
   Location: Worker count
   
   Consider default:
   ```go
   func ProcessJobsDefault(jobs []Job) ([]string, error) {
       maxWorkers := runtime.NumCPU()
       return ProcessJobs(context.Background(), jobs, maxWorkers)
   }
   ```

### Positive Feedback ✅

1. **Proper WaitGroup Usage**
   Location: Lines 12-22
   
   Good use of sync.WaitGroup to wait for all goroutines. The pattern of 
   Add(1) before starting goroutine and Done() after is correct.

2. **No Loop Variable Capture Bug**
   Location: Lines 15-19
   
   Excellent! You correctly pass loop variables as parameters to avoid the 
   common Go gotcha where goroutines capture the loop variable.
   ```go
   go func(index int, j Job) {  // ✓ Correct
   ```
   vs
   ```go
   go func() {
       results[i] = processJob(job)  // ✗ Would capture loop variables
   }()
   ```

### Summary

**Overall Assessment**: Request Changes

**Important Suggestions**: 5 - Concurrency safety and robustness
**Code Quality**: Good foundation, needs production hardening
**Concurrency**: Issues with unbounded goroutines and error handling

**Recommendation**: Address concurrency concerns before merge.

**Critical Improvements**:
1. Implement worker pool with bounded concurrency (prevents resource exhaustion)
2. Add error handling (currently errors are lost)
3. Add context support for cancellation/timeouts

**Recommended Improvements**:
4. Explicit result collection (clearer than index-based writes)
5. Panic recovery in workers (prevents silent failures)

The core pattern is solid! These changes will make it production-ready for 
handling large job volumes safely.
```

## Review Type Comparison

### Same Code, Different Review Types

```go
// sample code
func GetUser(db *sql.DB, userID string) (*User, error) {
    query := "SELECT * FROM users WHERE id = '" + userID + "'"
    var user User
    err := db.QueryRow(query).Scan(&user.ID, &user.Name, &user.Email)
    return &user, err
}
```

**Security Review:**
```
🔴 CRITICAL: SQL Injection Vulnerability
The query concatenates user input directly into SQL. Must use parameterized queries.
```

**Performance Review:**
```
✅ Query is simple and efficient (single row lookup)
🟡 Consider adding database connection pooling and query result caching
```

**Code Quality Review:**
```
🟡 Error not wrapped with context
🟡 SELECT * could be specific columns
⚪ Consider using an ORM or query builder
```

**Learning/Mentoring Review:**
```
Great start! Let me explain why this code has a security issue and how to fix it.

The current approach concatenates user input into the SQL query string. This is 
dangerous because...

Here's the safe way using parameterized queries:
[detailed explanation with examples]

This is a common mistake when learning SQL. The key principle is...
```

## Common Review Scenarios

### Scenario: Emergency Hotfix

```markdown
## Hotfix Review: Critical Production Bug

**Context**: Production is down, need fast review

### Critical Issues 🔴
[Only security/correctness that would make it worse]

### Fast Track Approval
✅ Fix addresses the immediate issue correctly
✅ No new security vulnerabilities introduced
✅ No data integrity risks

**Recommendation**: APPROVE for immediate deploy

**Follow-up Required**:
- Add tests for this scenario (tracked in JIRA-123)
- Refactor error handling (tracked in JIRA-124)
- Review logging approach (tracked in JIRA-125)

These should be addressed in next sprint, not blocking this critical fix.
```

### Scenario: Learning PR from Junior Developer

```markdown
## Code Review: First Feature Implementation

Hey @junior-dev! Great work getting this feature working. I can see you put 
thought into the structure. Let me share some feedback to help you grow:

### Critical Issues 🔴
[Only genuine bugs or security issues]

### Learning Opportunities 🎓

1. **Error Handling Pattern** (Lines 23-25)
   
   You're on the right track catching the error! In our codebase, we wrap errors 
   with context to make debugging easier:
   
   Current:
   ```go
   if err != nil {
       return err
   }
   ```
   
   Our pattern:
   ```go
   if err != nil {
       return fmt.Errorf("failed to load user %s: %w", userID, err)
   }
   ```
   
   The `%w` verb preserves the original error (for error chain inspection) while 
   adding context. This helps when reading logs later.

2. **Testing Tip** (tests/user_test.go)
   
   Your happy path test is great! Consider adding a few more cases:
   - What happens with invalid user ID?
   - What happens when database is unavailable?
   - What happens with duplicate users?
   
   These "unhappy path" tests catch bugs early and document expected behavior.

### What You Did Well ✅

- Clean variable names (very readable!)
- Proper use of interfaces for dependency injection
- Good commit messages explaining what and why

### Resources

For more on error handling: [link to team docs]
For testing patterns: [link to examples]

Feel free to ping me on Slack if you want to discuss any of this. Happy to 
pair on the changes!
```

### Scenario: Large Refactoring

```markdown
## Architecture Review: Service Layer Refactoring

**Scope**: 2,800 lines across 25 files

**Review Approach**: Given the size, I've focused on:
1. High-level architecture and design decisions
2. Critical security/correctness issues
3. API contract changes

**Not deeply reviewed**:
- Individual variable names / minor style
- Internal implementation details of private methods

### Architecture Assessment ✅

Overall design is sound:
- Clear separation of concerns (controller → service → repository)
- Consistent error handling pattern
- Good use of dependency injection
- Backward compatible API changes

### Critical Issues 🔴
[Any found]

### Design Questions ❓

1. **Service Layer Transactions** (multiple files)
   
   I notice some services span multiple repositories. How are you handling 
   transactions across them? Should we ensure all database operations in a 
   service method are in a single transaction?

2. **Caching Strategy** (service/user_service.go)
   
   I see caching added to UserService. Should this pattern be extracted to a 
   reusable decorator or middleware? Might want to discuss in tech sync.

### Recommendations

✅ **Approve overall direction**

**Before merge**:
1. Address [critical issue if any]
2. Add integration tests for the main service methods

**Follow-up work** (separate PRs):
1. Consider extracting common service patterns to base class
2. Add monitoring/metrics to service layer
3. Document service layer conventions in tech docs

Given the scope and quality, strong approve on the refactoring approach!
```

## Summary Checklist

Before submitting a review, verify:

- [ ] Provided context about review focus and any limitations
- [ ] Categorized issues by priority (Critical/Suggestion/Nitpick)
- [ ] Included specific locations (file:line)
- [ ] Explained WHY issues matter, not just WHAT is wrong
- [ ] Provided actionable fixes with code examples
- [ ] Recognized good practices and thoughtful solutions
- [ ] Tone is constructive, not demanding or dismissive
- [ ] Recommendation is clear (Approve/Request Changes/etc.)
- [ ] Next steps are explicit
- [ ] Balanced thoroughness with pragmatism given the change size
