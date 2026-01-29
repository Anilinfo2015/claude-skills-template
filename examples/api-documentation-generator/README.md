# API Documentation Generator

Comprehensive API documentation generation from code, comments, and specifications.

## Overview

This skill helps you create professional, developer-friendly API documentation from source code, inline comments, specifications, and existing endpoints. It produces comprehensive documentation following industry standards for REST, GraphQL, WebSocket, and gRPC APIs.

## Key Features

- **Multiple API Types**: REST, GraphQL, WebSocket, gRPC
- **Auto-Generation**: Extract documentation from code and comments
- **OpenAPI Support**: Generate OpenAPI/Swagger 3.0 specifications
- **Code Examples**: Multi-language examples (curl, JavaScript, Python, Java)
- **Interactive Elements**: Try-it-out features and API explorers
- **Best Practices**: Following industry documentation standards
- **Complete Coverage**: Endpoints, authentication, errors, rate limiting, webhooks

## When to Use

Perfect for:
- Documenting REST APIs with endpoints and responses
- Creating GraphQL schema documentation
- Generating OpenAPI/Swagger specifications
- Documenting WebSocket events and messages
- Creating API reference guides
- Onboarding developers to your API
- Updating docs after code changes
- Documenting authentication flows

## What You'll Get

### Complete API Documentation

**1. Overview & Getting Started**
- API purpose and capabilities
- Base URLs and versioning
- Quick start guide
- Authentication setup

**2. Authentication**
- OAuth 2.0, API keys, JWT
- Token acquisition and refresh
- Scopes and permissions
- Security best practices

**3. API Reference**
- All endpoints documented
- Request/response formats
- Parameters and schemas
- HTTP status codes
- Error responses

**4. Data Models**
- Schema definitions
- Field descriptions
- Validation rules
- Examples

**5. Additional Features**
- Pagination and filtering
- Rate limiting
- Webhooks
- WebSocket events
- Error handling

**6. Code Examples**
- Multiple programming languages
- Copy-paste ready
- Realistic use cases
- Authentication included

### OpenAPI Specification

Machine-readable API specs:
```yaml
openapi: 3.0.0
info:
  title: Your API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      responses:
        '200':
          description: Success
```

### Developer Experience

- Clear, scannable format
- Logical organization
- Searchable content
- Interactive examples
- Consistent terminology
- Up-to-date information

## Quick Examples

### REST Endpoint Documentation

**From code:**
```javascript
// GET /api/v1/users/:id
async function getUser(req, res) {
  const user = await User.findById(req.params.id);
  if (!user) return res.status(404).json({ error: 'Not found' });
  res.json(user);
}
```

**Generates:**
````markdown
## Get User

Retrieve a single user by ID.

### Request
```
GET /api/v1/users/{id}
```

### Path Parameters
| Parameter | Type   | Description |
|-----------|--------|-------------|
| id        | string | User ID     |

### Response (200 OK)
```json
{
  "id": "usr_123",
  "email": "user@example.com",
  "name": "John Doe"
}
```

### Error (404 Not Found)
```json
{
  "error": "not_found",
  "message": "User not found"
}
```
````

### GraphQL Documentation

**From schema:**
```graphql
type Query {
  user(id: ID!): User
  users(page: Int, limit: Int): [User!]!
}
```

**Generates:**
```markdown
## Queries

### user(id: ID!): User
Get a single user by ID.

**Example:**
```graphql
query {
  user(id: "usr_123") {
    id
    email
    name
  }
}
```
```

### Authentication Documentation

**Generates complete flows:**
- OAuth 2.0 authorization code flow
- Client credentials flow
- Token refresh process
- API key usage
- Code examples in multiple languages

## Documentation Patterns

### REST APIs
✓ Resource-oriented URLs  
✓ HTTP methods (GET, POST, PUT, DELETE)  
✓ Status codes  
✓ JSON request/response  
✓ Pagination patterns

### GraphQL APIs
✓ Schema definitions  
✓ Query examples  
✓ Mutation examples  
✓ Type descriptions  
✓ Variables and arguments

### WebSocket APIs
✓ Connection process  
✓ Event types  
✓ Message formats  
✓ Heartbeat mechanism  
✓ Error handling

### gRPC APIs
✓ Protocol buffers  
✓ Service definitions  
✓ Message types  
✓ Streaming methods  
✓ Error codes

## What's Included

### Core Documentation

- **Endpoints**: All routes, methods, parameters
- **Authentication**: Complete auth flows and examples
- **Data Models**: Schema definitions with examples
- **Errors**: Error codes, formats, and solutions
- **Rate Limiting**: Limits, headers, and handling
- **Pagination**: Offset and cursor-based patterns
- **Filtering**: Query parameters and operators
- **Webhooks**: Setup, events, and verification

### Code Examples

Multiple languages for each endpoint:
- **curl**: Command-line examples
- **JavaScript**: fetch/axios examples
- **Python**: requests library examples
- **Java**: HTTP client examples
- **Go**: net/http examples

### Machine-Readable Specs

- **OpenAPI 3.0**: Complete API specification
- **GraphQL Schema**: SDL format
- **Postman Collection**: Import into Postman
- **AsyncAPI**: For WebSocket/event-driven APIs

## Best Practices Applied

### Documentation Quality
✓ Accurate and tested examples  
✓ Complete endpoint coverage  
✓ Consistent terminology  
✓ Clear error documentation  
✓ Security considerations

### Organization
✓ Logical grouping by resource  
✓ Progressive complexity  
✓ Clear navigation  
✓ Searchable content  
✓ Cross-references

### Developer Experience
✓ Quick start guide  
✓ Copy-paste ready examples  
✓ Multiple programming languages  
✓ Interactive try-it-out features  
✓ Comprehensive error handling

## Example Use Cases

### New API Launch
Generate complete documentation from scratch for a new API, including all endpoints, authentication, and examples.

### API Updates
Update documentation after adding new endpoints or changing existing ones while maintaining consistency.

### Legacy API Documentation
Document an existing undocumented API by analyzing code and testing endpoints.

### API Migration
Create migration guides when moving from v1 to v2, documenting breaking changes and new features.

### Developer Onboarding
Provide comprehensive documentation that helps new developers integrate quickly.

## Documentation Structure

```
API Documentation
├── Introduction
│   ├── Overview
│   ├── Base URLs
│   └── Quick Start
├── Authentication
│   ├── Methods
│   ├── Obtaining Credentials
│   └── Examples
├── Core Concepts
│   ├── Data Models
│   ├── Pagination
│   ├── Filtering
│   └── Error Handling
├── API Reference
│   ├── Users
│   ├── Products
│   ├── Orders
│   └── ...
├── Webhooks (if applicable)
├── Rate Limiting
├── Versioning
└── Changelog
```

## Output Formats

- **Markdown**: Easy to maintain and version control
- **HTML**: Web-ready documentation
- **OpenAPI/Swagger**: Machine-readable specification
- **Postman**: Import and test immediately
- **PDF**: Printable documentation

## Getting Started

1. **Provide Source Code**: Share API code with endpoints and models
2. **Specify API Type**: REST, GraphQL, WebSocket, or gRPC
3. **Include Comments**: Inline documentation helps but isn't required
4. **Review Generated Docs**: Check accuracy and completeness
5. **Customize**: Adjust examples and descriptions as needed
6. **Publish**: Deploy to your documentation platform

## Tips for Best Results

✓ **Include code comments** - Better input = better output  
✓ **Provide API specs** - OpenAPI, GraphQL schema files help  
✓ **Test endpoints** - Verify examples actually work  
✓ **Specify audience** - Internal vs external developers  
✓ **Note conventions** - Special patterns or requirements  
✓ **Include examples** - Show real-world usage patterns

## Quality Guarantees

- ✓ Accurate endpoint documentation
- ✓ Working code examples
- ✓ Complete error coverage
- ✓ Consistent formatting
- ✓ Security best practices
- ✓ Industry-standard patterns

## Limitations

- Cannot document business logic not evident in code
- Generated examples may need customization
- Complex authentication flows may need manual review
- Requires access to source code or specifications
- Interactive features depend on documentation platform

## Related Skills

- **Code Documentation Generator**: For inline code comments
- **OpenAPI Validator**: Validate API specifications
- **Migration Guide Creator**: Document breaking changes
- **Technical Writing Assistant**: Polish documentation prose

## Tools & Standards

**Supported Standards:**
- OpenAPI/Swagger 3.0
- GraphQL Schema Definition Language
- AsyncAPI for async/event-driven APIs
- OAuth 2.0 / OpenID Connect
- JSON Schema

**Compatible Platforms:**
- Swagger UI / Redoc
- Stoplight
- Postman
- Docusaurus
- GitBook
- ReadMe.io

## Examples & Resources

See [SKILL.md](SKILL.md) for:
- Detailed instructions
- Step-by-step process
- Best practices
- Error handling
- Security considerations

See [examples.md](examples.md) for:
- REST API examples
- GraphQL examples
- WebSocket examples
- Webhook documentation
- Error handling patterns
- Rate limiting docs
- Complete code samples

## Success Metrics

Good API documentation should:
- ✓ Reduce developer onboarding time by 50%+
- ✓ Decrease support questions about API usage
- ✓ Enable developers to integrate without contacting support
- ✓ Provide working examples for all common use cases
- ✓ Stay synchronized with actual API behavior

## Support

Need help?
- Check [SKILL.md](SKILL.md) for detailed instructions
- Review [examples.md](examples.md) for patterns
- Ensure code has comments and type information
- Provide OpenAPI specs if available
- Test generated documentation with actual developers

## License

MIT

---

**Ready to document your API?** Start with your source code and let this skill generate comprehensive, developer-friendly documentation that follows industry best practices and helps developers integrate quickly.
