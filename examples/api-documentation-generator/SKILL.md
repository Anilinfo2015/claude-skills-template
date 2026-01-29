---
name: api-documentation-generator
version: 1.0.0
description: Generate comprehensive API documentation from code, comments, and specifications
author: Claude Skills Template
tags: [documentation, api, rest, graphql, openapi, developer-tools]
category: documentation
license: MIT
created: 2024-01-01
updated: 2024-01-01
maturity: stable
complexity: medium
estimated_time: "10-30 minutes"
requirements:
  - Source code with APIs
  - API specifications (optional)
  - Understanding of API patterns
---

# API Documentation Generator

## Overview

Generate comprehensive, developer-friendly API documentation from source code, inline comments, specifications, and existing endpoints. Produces documentation that follows industry standards and best practices for REST APIs, GraphQL APIs, WebSocket APIs, and gRPC services.

## Purpose

Good API documentation is critical for developer experience but often neglected or outdated. This skill transforms code and specifications into clear, consistent, and complete documentation that developers can rely on.

## When to Use

Use this skill when you need to:
- Document REST APIs with endpoints, parameters, and responses
- Create GraphQL schema documentation with queries and mutations
- Generate OpenAPI/Swagger specifications
- Document WebSocket events and messages
- Create gRPC service documentation
- Update existing API docs after code changes
- Onboard developers to your API
- Create API reference guides
- Document authentication and authorization flows

## Instructions

### Step 1: Analyze the API Structure

Examine the codebase to identify:

**API Type:**
- REST API (HTTP methods, routes)
- GraphQL API (schema, queries, mutations)
- WebSocket API (events, messages)
- gRPC service (proto definitions)

**Key Components:**
- Endpoints/routes
- Request/response formats
- Authentication mechanisms
- Error handling patterns
- Rate limiting
- Versioning approach

**Documentation Sources:**
- Route definitions
- Controller/handler code
- Model/schema definitions
- Inline comments and docstrings
- OpenAPI/Swagger annotations
- Tests (for usage examples)
- Existing documentation

### Step 2: Extract Endpoint Information

For each endpoint or operation, collect:

**Basic Information:**
- HTTP method (GET, POST, PUT, DELETE, PATCH)
- URL path with parameters
- Brief description of purpose
- Tags/categories for organization

**Request Details:**
- Path parameters (`:id`, `{userId}`)
- Query parameters (`?page=1&limit=10`)
- Request headers (Content-Type, Authorization)
- Request body schema with examples
- Required vs optional fields

**Response Details:**
- Success response codes (200, 201, 204)
- Success response body schema with examples
- Error response codes (400, 401, 404, 500)
- Error response formats
- Response headers

**Additional Context:**
- Authentication requirements
- Authorization/permissions needed
- Rate limiting rules
- Deprecation status
- Since version introduced
- Related endpoints

### Step 3: Document Data Models

For each data model or schema:

**Structure:**
- Field name and type
- Description of purpose
- Validation rules (min/max, pattern, enum)
- Required vs optional
- Default values
- Examples
- Relationships to other models

**Format:**
```
User
  id: integer (required)
    Unique identifier for the user
    Example: 12345
  
  email: string (required)
    User's email address
    Format: email
    Example: "user@example.com"
  
  name: string (optional)
    User's display name
    Max length: 100
    Example: "Jane Doe"
  
  created_at: string (required)
    ISO 8601 timestamp of account creation
    Format: date-time
    Example: "2024-01-15T10:30:00Z"
```

### Step 4: Document Authentication

Describe authentication mechanisms:

**Authentication Type:**
- API Key (header, query parameter)
- Bearer Token (JWT, OAuth)
- Basic Auth
- OAuth 2.0 (flows: authorization code, client credentials, etc.)
- Custom authentication

**For Each Method:**
- How to obtain credentials
- How to include in requests
- Token expiration and refresh
- Scopes and permissions
- Example authentication flow

**Example:**
```
Authentication: Bearer Token

1. Obtain token via POST /auth/token with credentials
2. Include in requests: Authorization: Bearer {token}
3. Token expires after 1 hour
4. Refresh using POST /auth/refresh with refresh_token
```

### Step 5: Create Usage Examples

For each endpoint, provide:

**Request Examples:**
- Multiple programming languages (curl, JavaScript, Python, Java)
- Include authentication
- Show actual parameter values
- Use realistic data

**Response Examples:**
- Success responses with complete data
- Error responses with error details
- Edge cases (empty results, pagination)

**Example Structure:**
```
Request:
  curl -X POST https://api.example.com/v1/users \
    -H "Authorization: Bearer abc123" \
    -H "Content-Type: application/json" \
    -d '{"email": "user@example.com", "name": "Jane"}'

Response (201 Created):
  {
    "id": 12345,
    "email": "user@example.com",
    "name": "Jane",
    "created_at": "2024-01-15T10:30:00Z"
  }

Error Response (400 Bad Request):
  {
    "error": "validation_error",
    "message": "Invalid email format",
    "field": "email"
  }
```

### Step 6: Structure the Documentation

Organize into clear sections:

**1. Introduction**
- API overview and purpose
- Base URL(s)
- API version
- Quick start guide

**2. Authentication**
- Methods and flows
- Getting credentials
- Including auth in requests

**3. Core Concepts**
- Key terminology
- Data models
- Common patterns
- Pagination
- Filtering and sorting
- Error handling

**4. API Reference**
Grouped by resource or functionality:
- User Management
  - List Users: GET /users
  - Create User: POST /users
  - Get User: GET /users/{id}
  - Update User: PUT /users/{id}
  - Delete User: DELETE /users/{id}

**5. Webhooks** (if applicable)
- Webhook events
- Payload formats
- Signature verification
- Retry logic

**6. Rate Limiting**
- Limits per endpoint
- Rate limit headers
- Handling rate limit errors

**7. Versioning**
- Current version
- Supported versions
- Deprecation policy
- Migration guides

**8. Error Reference**
- Error code list
- Error response format
- Common errors and solutions

**9. SDKs and Tools**
- Available client libraries
- Testing tools (Postman collections)
- Code generators

**10. Changelog**
- Recent changes
- Breaking changes
- New features

### Step 7: Format for Readability

Apply formatting best practices:

**Headings:**
- Use clear hierarchy (H1 > H2 > H3)
- Make scannable (developers skim)
- Include HTTP methods in endpoint titles

**Code Blocks:**
- Syntax highlighting
- Copy-paste ready
- Include language identifier

**Tables:**
- For parameters, fields, error codes
- Consistent column structure
- Use markdown tables or HTML

**Callouts:**
- ⚠️ Warnings for breaking changes
- 💡 Tips for best practices
- 🔒 Security considerations
- 🚧 Deprecated features

**Navigation:**
- Table of contents
- Section links
- Breadcrumbs for multi-page docs

### Step 8: Add Interactive Elements

Where possible, enhance with:

**Try It Out:**
- Interactive API explorer
- Pre-filled examples
- Execute requests from docs

**Response Viewer:**
- Collapsible sections
- Syntax highlighted responses
- Copy to clipboard buttons

**Search:**
- Full-text search capability
- Endpoint quick search
- Model/type search

### Step 9: Generate Machine-Readable Specs

Create structured specifications:

**OpenAPI/Swagger 3.0:**
```yaml
openapi: 3.0.0
info:
  title: Example API
  version: 1.0.0
  description: API for managing users
servers:
  - url: https://api.example.com/v1
paths:
  /users:
    get:
      summary: List users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
      properties:
        id:
          type: integer
        email:
          type: string
          format: email
```

**GraphQL Schema:**
```graphql
"""
A user in the system
"""
type User {
  "Unique identifier"
  id: ID!
  
  "User's email address"
  email: String!
  
  "User's display name"
  name: String
  
  "Account creation timestamp"
  createdAt: DateTime!
}

type Query {
  "Get user by ID"
  user(id: ID!): User
  
  "List all users with pagination"
  users(page: Int, limit: Int): [User!]!
}
```

### Step 10: Validate Completeness

Check documentation covers:

- ✓ All public endpoints documented
- ✓ All required parameters listed
- ✓ Response schemas accurate
- ✓ Examples work correctly
- ✓ Error cases documented
- ✓ Authentication clearly explained
- ✓ Code examples in multiple languages
- ✓ Versioning information included
- ✓ Contact/support information
- ✓ Terms of service/usage limits

**Test Documentation:**
- Try examples as written
- Verify response formats match reality
- Check links work
- Validate machine-readable specs
- Review with actual developers

## Examples

### Example 1: REST API Endpoint Documentation

**Source Code:**
```javascript
// controllers/userController.js
/**
 * Get user by ID
 * @route GET /api/v1/users/:id
 * @param {string} id - User ID
 * @returns {User} User object
 * @throws {404} User not found
 */
async function getUser(req, res) {
  const user = await User.findById(req.params.id);
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }
  res.json(user);
}
```

**Generated Documentation:**

````markdown
## Get User

Retrieve a single user by their unique identifier.

### Request

```
GET /api/v1/users/{id}
```

### Path Parameters

| Parameter | Type   | Required | Description           |
|-----------|--------|----------|-----------------------|
| id        | string | Yes      | Unique user identifier |

### Headers

```
Authorization: Bearer {token}
Content-Type: application/json
```

### Response

#### Success (200 OK)

```json
{
  "id": "usr_123456",
  "email": "john.doe@example.com",
  "name": "John Doe",
  "role": "admin",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-20T14:22:00Z"
}
```

#### Error Responses

**404 Not Found** - User does not exist
```json
{
  "error": "not_found",
  "message": "User not found"
}
```

**401 Unauthorized** - Invalid or missing token
```json
{
  "error": "unauthorized",
  "message": "Invalid authentication token"
}
```

### Examples

#### cURL
```bash
curl -X GET "https://api.example.com/v1/users/usr_123456" \
  -H "Authorization: Bearer your_token_here" \
  -H "Content-Type: application/json"
```

#### JavaScript (fetch)
```javascript
const response = await fetch('https://api.example.com/v1/users/usr_123456', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer your_token_here',
    'Content-Type': 'application/json'
  }
});
const user = await response.json();
console.log(user);
```

#### Python (requests)
```python
import requests

response = requests.get(
    'https://api.example.com/v1/users/usr_123456',
    headers={
        'Authorization': 'Bearer your_token_here',
        'Content-Type': 'application/json'
    }
)
user = response.json()
print(user)
```

### Rate Limiting

This endpoint is rate limited to 1000 requests per hour per API key.

### Related Endpoints

- [List Users](#list-users) - Get multiple users
- [Update User](#update-user) - Modify user data
- [Delete User](#delete-user) - Remove a user
````

### Example 2: GraphQL API Documentation

**Source Schema:**
```graphql
type Query {
  product(id: ID!): Product
  products(filter: ProductFilter, page: Int, limit: Int): ProductConnection!
}

type Mutation {
  createProduct(input: CreateProductInput!): Product!
  updateProduct(id: ID!, input: UpdateProductInput!): Product!
  deleteProduct(id: ID!): Boolean!
}

input CreateProductInput {
  name: String!
  description: String
  price: Float!
  categoryId: ID!
}

type Product {
  id: ID!
  name: String!
  description: String
  price: Float!
  category: Category!
  createdAt: DateTime!
}
```

**Generated Documentation:**

````markdown
## Products API

Manage products in the catalog.

### Queries

#### Get Product

Retrieve a single product by ID.

```graphql
query GetProduct($id: ID!) {
  product(id: $id) {
    id
    name
    description
    price
    category {
      id
      name
    }
    createdAt
  }
}
```

**Variables:**
```json
{
  "id": "prod_123"
}
```

**Response:**
```json
{
  "data": {
    "product": {
      "id": "prod_123",
      "name": "Wireless Keyboard",
      "description": "Ergonomic wireless keyboard with backlight",
      "price": 79.99,
      "category": {
        "id": "cat_456",
        "name": "Electronics"
      },
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }
}
```

#### List Products

Retrieve multiple products with filtering and pagination.

```graphql
query ListProducts($filter: ProductFilter, $page: Int, $limit: Int) {
  products(filter: $filter, page: $page, limit: $limit) {
    edges {
      node {
        id
        name
        price
      }
    }
    pageInfo {
      hasNextPage
      totalCount
    }
  }
}
```

**Variables:**
```json
{
  "filter": {
    "categoryId": "cat_456",
    "minPrice": 50,
    "maxPrice": 100
  },
  "page": 1,
  "limit": 10
}
```

### Mutations

#### Create Product

Add a new product to the catalog.

```graphql
mutation CreateProduct($input: CreateProductInput!) {
  createProduct(input: $input) {
    id
    name
    price
    category {
      id
      name
    }
  }
}
```

**Variables:**
```json
{
  "input": {
    "name": "Wireless Mouse",
    "description": "Ergonomic wireless mouse",
    "price": 49.99,
    "categoryId": "cat_456"
  }
}
```

**Response:**
```json
{
  "data": {
    "createProduct": {
      "id": "prod_789",
      "name": "Wireless Mouse",
      "price": 49.99,
      "category": {
        "id": "cat_456",
        "name": "Electronics"
      }
    }
  }
}
```

**Error Response:**
```json
{
  "errors": [
    {
      "message": "Category not found",
      "path": ["createProduct"],
      "extensions": {
        "code": "NOT_FOUND",
        "field": "categoryId"
      }
    }
  ]
}
```

### Types

#### Product

Represents a product in the catalog.

| Field       | Type     | Required | Description                    |
|-------------|----------|----------|--------------------------------|
| id          | ID       | Yes      | Unique product identifier      |
| name        | String   | Yes      | Product name                   |
| description | String   | No       | Detailed product description   |
| price       | Float    | Yes      | Product price in USD           |
| category    | Category | Yes      | Product category               |
| createdAt   | DateTime | Yes      | Product creation timestamp     |

#### CreateProductInput

Input for creating a new product.

| Field       | Type   | Required | Description                           |
|-------------|--------|----------|---------------------------------------|
| name        | String | Yes      | Product name (max 200 characters)     |
| description | String | No       | Product description (max 1000 chars)  |
| price       | Float  | Yes      | Product price (must be positive)      |
| categoryId  | ID     | Yes      | Category ID (must exist)              |

### Authentication

All queries and mutations require authentication via bearer token:

```
Authorization: Bearer your_token_here
```

### Rate Limiting

- Queries: 100 requests per minute
- Mutations: 20 requests per minute

Rate limit headers included in responses:
- `X-RateLimit-Limit`: Total requests allowed
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Unix timestamp when limit resets

### Error Codes

| Code              | Description                        |
|-------------------|------------------------------------|
| UNAUTHENTICATED   | Missing or invalid authentication  |
| FORBIDDEN         | Insufficient permissions           |
| NOT_FOUND         | Resource does not exist            |
| VALIDATION_ERROR  | Input validation failed            |
| INTERNAL_ERROR    | Server error                       |
````

### Example 3: OpenAPI Specification

**From Code:**
```python
from flask import Flask, request
from flask_restful import Resource

class UserList(Resource):
    """User management endpoints"""
    
    def get(self):
        """
        List all users
        ---
        parameters:
          - name: page
            in: query
            type: integer
            default: 1
          - name: limit
            in: query
            type: integer
            default: 20
        responses:
          200:
            description: List of users
        """
        pass
    
    def post(self):
        """
        Create new user
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              required: [email, password]
              properties:
                email:
                  type: string
                  format: email
                password:
                  type: string
                  minLength: 8
        """
        pass
```

**Generated OpenAPI 3.0 Specification:**

```yaml
openapi: 3.0.0
info:
  title: User Management API
  version: 1.0.0
  description: API for managing user accounts
  contact:
    email: api@example.com
  license:
    name: MIT

servers:
  - url: https://api.example.com/v1
    description: Production server
  - url: https://staging.api.example.com/v1
    description: Staging server

security:
  - bearerAuth: []

paths:
  /users:
    get:
      summary: List users
      description: Retrieve a paginated list of all users
      operationId: listUsers
      tags:
        - Users
      parameters:
        - name: page
          in: query
          description: Page number for pagination
          required: false
          schema:
            type: integer
            minimum: 1
            default: 1
        - name: limit
          in: query
          description: Number of results per page
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
                  pagination:
                    $ref: '#/components/schemas/Pagination'
              example:
                data:
                  - id: usr_123
                    email: john@example.com
                    name: John Doe
                    created_at: "2024-01-15T10:30:00Z"
                pagination:
                  page: 1
                  limit: 20
                  total: 150
        '401':
          $ref: '#/components/responses/Unauthorized'
        '429':
          $ref: '#/components/responses/RateLimitExceeded'
    
    post:
      summary: Create user
      description: Create a new user account
      operationId: createUser
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
            example:
              email: newuser@example.com
              password: SecurePass123!
              name: New User
      responses:
        '201':
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
              example:
                id: usr_456
                email: newuser@example.com
                name: New User
                created_at: "2024-01-20T15:45:00Z"
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '409':
          description: User already exists
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                error: conflict
                message: User with this email already exists

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: JWT token obtained from /auth/token endpoint
  
  schemas:
    User:
      type: object
      required:
        - id
        - email
        - created_at
      properties:
        id:
          type: string
          description: Unique user identifier
          example: usr_123
        email:
          type: string
          format: email
          description: User's email address
          example: user@example.com
        name:
          type: string
          description: User's display name
          maxLength: 100
          example: John Doe
        created_at:
          type: string
          format: date-time
          description: Account creation timestamp
          example: "2024-01-15T10:30:00Z"
    
    CreateUserRequest:
      type: object
      required:
        - email
        - password
      properties:
        email:
          type: string
          format: email
          description: User's email address
        password:
          type: string
          minLength: 8
          description: User's password (min 8 characters)
        name:
          type: string
          maxLength: 100
          description: User's display name
    
    Pagination:
      type: object
      properties:
        page:
          type: integer
          description: Current page number
        limit:
          type: integer
          description: Results per page
        total:
          type: integer
          description: Total number of results
    
    Error:
      type: object
      required:
        - error
        - message
      properties:
        error:
          type: string
          description: Error code
        message:
          type: string
          description: Human-readable error message
        field:
          type: string
          description: Field that caused the error (for validation errors)
  
  responses:
    Unauthorized:
      description: Authentication required or invalid token
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: unauthorized
            message: Invalid or missing authentication token
    
    BadRequest:
      description: Invalid request parameters
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: validation_error
            message: Invalid email format
            field: email
    
    RateLimitExceeded:
      description: Rate limit exceeded
      headers:
        X-RateLimit-Limit:
          schema:
            type: integer
          description: Request limit per hour
        X-RateLimit-Remaining:
          schema:
            type: integer
          description: Requests remaining
        X-RateLimit-Reset:
          schema:
            type: integer
          description: Unix timestamp when limit resets
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: rate_limit_exceeded
            message: Too many requests. Please try again later.
```

### Example 4: Authentication Flow Documentation

**Generated Documentation:**

````markdown
## Authentication

The API uses OAuth 2.0 for authentication. All API requests must include a valid access token.

### Getting Started

1. Register your application to obtain client credentials
2. Obtain an access token using one of the supported flows
3. Include the token in API requests

### OAuth 2.0 Flows

#### Client Credentials Flow

For server-to-server API access without user interaction.

**Request:**
```http
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id=your_client_id
&client_secret=your_client_secret
&scope=read write
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "read write"
}
```

**Example (cURL):**
```bash
curl -X POST https://api.example.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=your_client_id" \
  -d "client_secret=your_client_secret" \
  -d "scope=read write"
```

#### Authorization Code Flow

For user-authorized access (web applications).

**Step 1: Get Authorization Code**

Redirect user to:
```
GET /oauth/authorize?
  response_type=code
  &client_id=your_client_id
  &redirect_uri=https://your-app.com/callback
  &scope=read write
  &state=random_state_string
```

User approves, and you receive code:
```
https://your-app.com/callback?
  code=AUTH_CODE
  &state=random_state_string
```

**Step 2: Exchange Code for Token**

```http
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&code=AUTH_CODE
&redirect_uri=https://your-app.com/callback
&client_id=your_client_id
&client_secret=your_client_secret
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "refresh_token_here",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "read write"
}
```

### Using Access Tokens

Include the access token in the `Authorization` header:

```http
GET /api/v1/users
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Examples:**

```bash
# cURL
curl -H "Authorization: Bearer your_token" \
  https://api.example.com/v1/users
```

```javascript
// JavaScript
const response = await fetch('https://api.example.com/v1/users', {
  headers: {
    'Authorization': 'Bearer your_token'
  }
});
```

```python
# Python
import requests

headers = {'Authorization': 'Bearer your_token'}
response = requests.get('https://api.example.com/v1/users', headers=headers)
```

### Refreshing Tokens

Access tokens expire after 1 hour. Use the refresh token to obtain a new one:

```http
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&refresh_token=your_refresh_token
&client_id=your_client_id
&client_secret=your_client_secret
```

**Response:**
```json
{
  "access_token": "new_access_token",
  "refresh_token": "new_refresh_token",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### Scopes

Available OAuth scopes:

| Scope          | Description                                  |
|----------------|----------------------------------------------|
| `read`         | Read access to resources                     |
| `write`        | Create and update resources                  |
| `delete`       | Delete resources                             |
| `admin`        | Full administrative access                   |
| `user:email`   | Access to user email addresses               |
| `user:profile` | Access to user profile information           |

### Security Best Practices

⚠️ **Important Security Guidelines:**

1. **Never expose client secrets** in client-side code or public repositories
2. **Always use HTTPS** for all OAuth flows and API requests
3. **Validate state parameter** in authorization code flow to prevent CSRF
4. **Store tokens securely** - use secure, httpOnly cookies or secure storage
5. **Refresh tokens before expiry** to avoid service interruptions
6. **Revoke tokens** when no longer needed
7. **Use minimal scopes** - request only what you need

### Error Responses

**Invalid Token:**
```json
{
  "error": "invalid_token",
  "error_description": "The access token expired"
}
```
**HTTP Status:** 401 Unauthorized

**Insufficient Scope:**
```json
{
  "error": "insufficient_scope",
  "error_description": "The request requires higher privileges than provided by the access token",
  "scope": "admin"
}
```
**HTTP Status:** 403 Forbidden

### Token Introspection

Validate and get information about a token:

```http
POST /oauth/introspect
Authorization: Basic base64(client_id:client_secret)
Content-Type: application/x-www-form-urlencoded

token=access_token_to_introspect
```

**Response:**
```json
{
  "active": true,
  "scope": "read write",
  "client_id": "your_client_id",
  "exp": 1706356800,
  "iat": 1706353200,
  "sub": "user_123"
}
```

### Revoking Tokens

Revoke an access or refresh token:

```http
POST /oauth/revoke
Authorization: Basic base64(client_id:client_secret)
Content-Type: application/x-www-form-urlencoded

token=token_to_revoke
&token_type_hint=access_token
```

**Response:** 200 OK (no body)
````

## Best Practices

### Documentation Quality

1. **Be Accurate**: Test all examples - nothing frustrates developers more than broken examples
2. **Be Complete**: Document all endpoints, parameters, and error cases
3. **Be Consistent**: Use same terminology, format, and structure throughout
4. **Be Clear**: Write for developers unfamiliar with your system
5. **Be Current**: Update docs with every API change

### Organization

1. **Group Related Endpoints**: Organize by resource or feature (Users, Products, Orders)
2. **Progressive Disclosure**: Start simple, add complexity gradually
3. **Highlight Common Tasks**: Show most-used endpoints first
4. **Cross-Reference**: Link related endpoints and concepts
5. **Version Clearly**: Document which version introduced each feature

### Examples

1. **Use Realistic Data**: Show real-world examples, not "foo" and "bar"
2. **Show Success and Failure**: Document both happy path and error cases
3. **Multiple Languages**: Provide examples in common languages (curl, JS, Python)
4. **Copy-Paste Ready**: Make examples work as-is with minimal changes
5. **Explain Non-Obvious**: Comment complex examples

### Maintenance

1. **Generate from Code**: Use tools to auto-generate docs from code
2. **Test Documentation**: Run automated tests against examples
3. **Version Documentation**: Keep docs for all supported API versions
4. **Track Changes**: Maintain changelog of API modifications
5. **Deprecate Gracefully**: Clearly mark deprecated features with migration path

## Common Mistakes to Avoid

❌ **Incomplete examples** - Missing auth headers, required fields
❌ **Outdated information** - Docs don't match current API behavior
❌ **Inconsistent terminology** - Calling same thing different names
❌ **Missing error documentation** - Only documenting success cases
❌ **No migration guides** - Breaking changes without upgrade path
❌ **Assuming knowledge** - Not explaining authentication or setup
❌ **Poor organization** - Random order, no logical grouping
❌ **No search functionality** - Hard to find specific information
❌ **Example-less descriptions** - All theory, no practical usage
❌ **Ignoring edge cases** - Not documenting pagination, empty results

## Error Handling

### Missing Information

**Issue:** Code lacks comments or documentation
**Solution:** 
- Infer purpose from code structure and naming
- Test endpoints to discover behavior
- Mark sections as "undocumented" for review
- Ask developers for clarification

### Inconsistent Patterns

**Issue:** Different endpoints use different conventions
**Solution:**
- Document actual behavior (don't force consistency)
- Note inconsistencies with callouts
- Suggest standardization in future versions

### Complex Authentication

**Issue:** Multiple auth methods or complex flows
**Solution:**
- Create separate section for each method
- Provide flowcharts for complex processes
- Include complete examples for each flow
- Link to OAuth RFCs or specifications

### Deprecated Features

**Issue:** Old endpoints still in use but deprecated
**Solution:**
- Clearly mark as deprecated with warning
- Provide migration instructions
- Document removal timeline
- Link to replacement endpoints

## Security Considerations

### Sensitive Information

- 🔒 Never include real API keys or tokens in documentation
- 🔒 Use placeholder values (`your_token_here`, `your_client_secret`)
- 🔒 Document which credentials to keep secret
- 🔒 Warn against including secrets in client-side code

### Security Features

- Document rate limiting to prevent abuse
- Explain authentication requirements clearly
- Detail authorization/permission model
- Document input validation rules
- Explain CORS and cross-origin policies
- Describe encryption requirements (HTTPS)

### Vulnerability Disclosure

- Provide security contact information
- Document security reporting process
- Explain responsible disclosure timeline

## Performance Tips

### Documentation Size

- Use progressive loading for large docs
- Collapse code examples by default
- Implement pagination for long endpoint lists
- Lazy-load images and diagrams

### Generation Speed

- Cache generated documentation
- Generate incrementally (only changed parts)
- Use parallel processing for large codebases
- Pre-compute expensive operations (schema validation)

### Search Performance

- Index documentation for full-text search
- Use client-side search for small docs
- Implement server-side search for large docs
- Cache search results

## Limitations

- Cannot document undocumented code perfectly - manual review needed
- Generated examples may need customization for real-world use
- Complex business logic may require manual explanation
- Automatic generation tools may miss nuances
- Interactive features require specific documentation platforms
- GraphQL introspection may not capture all descriptions
- Internal/private APIs need different documentation approach

## Related Skills

- **Code Documentation Generator**: For inline code comments
- **OpenAPI Validator**: For validating API specifications
- **API Client Generator**: For creating SDK docs alongside API docs
- **Migration Guide Creator**: For documenting breaking changes

## Tools and Technologies

### Documentation Generators

- **Swagger/OpenAPI**: Industry standard REST API documentation
- **GraphQL**: Built-in schema documentation
- **Postman**: API documentation and testing platform
- **Redoc**: Beautiful OpenAPI documentation
- **Stoplight**: API design and documentation platform
- **Slate**: Static API documentation generator
- **Docusaurus**: Documentation website generator

### Code Annotation Frameworks

- **JSDoc**: JavaScript documentation
- **JavaDoc**: Java documentation
- **Sphinx**: Python documentation
- **YARD**: Ruby documentation
- **GoDoc**: Go documentation

## Version History

- **1.0.0** (2024-01-01): Initial release

## Additional Resources

- [OpenAPI Specification](https://swagger.io/specification/)
- [GraphQL Schema Documentation](https://graphql.org/learn/schema/)
- [OAuth 2.0 RFC](https://tools.ietf.org/html/rfc6749)
- [REST API Design Best Practices](https://restfulapi.net/)
- [API Documentation Best Practices](https://swagger.io/blog/api-documentation/)

## Notes

- Good API documentation is as important as the API itself
- Invest in tooling to keep documentation synchronized with code
- Treat documentation as a product, not an afterthought
- Get feedback from actual API consumers
- Consider hiring technical writers for large APIs
- Use documentation-driven development: write docs first, implement second
