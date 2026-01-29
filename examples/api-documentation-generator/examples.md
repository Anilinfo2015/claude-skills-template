# API Documentation Generator - Extended Examples

Additional examples demonstrating API documentation patterns for different scenarios.

## Example 5: WebSocket API Documentation

**Source Code:**
```javascript
// websocket/events.js
const events = {
  'user:login': { auth: true },
  'message:new': { auth: true },
  'chat:typing': { auth: true },
  'notification:receive': { auth: true }
};
```

**Generated Documentation:**

````markdown
## WebSocket API

Real-time communication via WebSocket connection.

### Connection

```javascript
const ws = new WebSocket('wss://api.example.com/v1/ws?token=your_token');

ws.onopen = () => {
  console.log('Connected');
};

ws.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log('Received:', message);
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

ws.onclose = () => {
  console.log('Disconnected');
};
```

### Authentication

Include your access token in the connection URL:
```
wss://api.example.com/v1/ws?token=your_access_token
```

Or send authentication message after connection:
```json
{
  "type": "auth",
  "token": "your_access_token"
}
```

### Message Format

All messages follow this structure:

```json
{
  "type": "event_name",
  "id": "unique_message_id",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    // Event-specific data
  }
}
```

### Events

#### Client → Server Events

##### user:login

Sent when user logs in via WebSocket.

**Payload:**
```json
{
  "type": "user:login",
  "id": "msg_123",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "userId": "usr_456"
  }
}
```

**Response:**
```json
{
  "type": "user:login:ack",
  "id": "msg_123",
  "timestamp": "2024-01-15T10:30:01Z",
  "data": {
    "success": true,
    "sessionId": "sess_789"
  }
}
```

##### chat:typing

Sent when user is typing.

**Payload:**
```json
{
  "type": "chat:typing",
  "id": "msg_124",
  "timestamp": "2024-01-15T10:31:00Z",
  "data": {
    "roomId": "room_abc",
    "userId": "usr_456",
    "isTyping": true
  }
}
```

**No Response:** This is a fire-and-forget event.

#### Server → Client Events

##### message:new

Received when a new message is posted.

**Payload:**
```json
{
  "type": "message:new",
  "id": "msg_125",
  "timestamp": "2024-01-15T10:32:00Z",
  "data": {
    "messageId": "msg_xyz",
    "roomId": "room_abc",
    "userId": "usr_789",
    "username": "John Doe",
    "text": "Hello everyone!",
    "createdAt": "2024-01-15T10:32:00Z"
  }
}
```

##### notification:receive

Received when there's a new notification.

**Payload:**
```json
{
  "type": "notification:receive",
  "id": "msg_126",
  "timestamp": "2024-01-15T10:33:00Z",
  "data": {
    "notificationId": "notif_123",
    "type": "mention",
    "title": "You were mentioned",
    "message": "John mentioned you in #general",
    "link": "/chat/general",
    "read": false
  }
}
```

### Error Events

When an error occurs, server sends:

```json
{
  "type": "error",
  "id": "original_message_id",
  "timestamp": "2024-01-15T10:34:00Z",
  "data": {
    "code": "invalid_room",
    "message": "Room not found or access denied",
    "details": {
      "roomId": "room_xyz"
    }
  }
}
```

### Heartbeat

Server sends periodic heartbeat to keep connection alive:

```json
{
  "type": "ping",
  "timestamp": "2024-01-15T10:35:00Z"
}
```

Client should respond with:

```json
{
  "type": "pong",
  "timestamp": "2024-01-15T10:35:00Z"
}
```

If no pong received within 30 seconds, server closes connection.

### Connection Limits

- Maximum 3 concurrent connections per user
- Idle connections (no activity for 5 minutes) automatically closed
- Reconnection with exponential backoff recommended

### Example Client Implementation

```javascript
class ChatWebSocket {
  constructor(token) {
    this.token = token;
    this.ws = null;
    this.reconnectDelay = 1000;
    this.maxReconnectDelay = 30000;
  }

  connect() {
    this.ws = new WebSocket(`wss://api.example.com/v1/ws?token=${this.token}`);
    
    this.ws.onopen = () => {
      console.log('Connected');
      this.reconnectDelay = 1000; // Reset delay on successful connection
    };
    
    this.ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      this.handleMessage(message);
    };
    
    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
    
    this.ws.onclose = () => {
      console.log('Disconnected, reconnecting...');
      this.reconnect();
    };
  }

  handleMessage(message) {
    switch (message.type) {
      case 'ping':
        this.send({ type: 'pong', timestamp: new Date().toISOString() });
        break;
      case 'message:new':
        this.onNewMessage(message.data);
        break;
      case 'notification:receive':
        this.onNotification(message.data);
        break;
      case 'error':
        this.onError(message.data);
        break;
    }
  }

  send(message) {
    if (this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify({
        ...message,
        id: this.generateId(),
        timestamp: new Date().toISOString()
      }));
    }
  }

  reconnect() {
    setTimeout(() => {
      this.reconnectDelay = Math.min(
        this.reconnectDelay * 2,
        this.maxReconnectDelay
      );
      this.connect();
    }, this.reconnectDelay);
  }

  generateId() {
    return `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  // Event handlers (override these)
  onNewMessage(data) {}
  onNotification(data) {}
  onError(data) {}
}

// Usage
const chat = new ChatWebSocket('your_token');
chat.onNewMessage = (data) => {
  console.log('New message:', data);
};
chat.connect();
```
````

## Example 6: Pagination and Filtering Documentation

**Generated Documentation:**

````markdown
## Pagination

All list endpoints support pagination using cursor-based or offset-based pagination.

### Offset-Based Pagination

Use `page` and `limit` parameters:

```http
GET /api/v1/users?page=2&limit=20
```

**Parameters:**
- `page`: Page number (starts at 1)
- `limit`: Results per page (default: 20, max: 100)

**Response:**
```json
{
  "data": [
    { "id": "usr_21", "name": "User 21" },
    { "id": "usr_22", "name": "User 22" }
  ],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNextPage": true,
    "hasPreviousPage": true
  }
}
```

**Navigation:**
- First page: `?page=1&limit=20`
- Next page: `?page=3&limit=20`
- Previous page: `?page=1&limit=20`
- Last page: `?page=8&limit=20`

### Cursor-Based Pagination

Use `cursor` and `limit` parameters for consistent results:

```http
GET /api/v1/posts?cursor=eyJpZCI6MTAwfQ&limit=20
```

**Parameters:**
- `cursor`: Opaque cursor string (omit for first page)
- `limit`: Results per page (default: 20, max: 100)

**Response:**
```json
{
  "data": [
    { "id": "post_101", "title": "Post 101" },
    { "id": "post_102", "title": "Post 102" }
  ],
  "pagination": {
    "limit": 20,
    "nextCursor": "eyJpZCI6MTIwfQ",
    "previousCursor": "eyJpZCI6MTAwfQ",
    "hasMore": true
  }
}
```

**Advantages:**
- Consistent results even when data changes
- Better performance for large datasets
- No skipped or duplicate items

## Filtering

Filter results using query parameters.

### Single Field Filter

```http
GET /api/v1/users?role=admin
GET /api/v1/products?category=electronics
```

### Multiple Filters (AND)

```http
GET /api/v1/users?role=admin&status=active
```

Returns users where `role = admin AND status = active`

### Range Filters

```http
GET /api/v1/products?minPrice=50&maxPrice=100
GET /api/v1/posts?createdAfter=2024-01-01&createdBefore=2024-12-31
```

**Supported Range Operators:**
- `min{Field}` and `max{Field}`: Numeric ranges
- `{field}After` and `{field}Before`: Date ranges

### Array Filters (OR)

```http
GET /api/v1/users?role=admin,editor,moderator
```

Returns users where `role IN (admin, editor, moderator)`

### Text Search

```http
GET /api/v1/products?search=wireless+keyboard
```

Searches across multiple fields (name, description, tags).

### Advanced Filters

Use filter parameter with JSON-encoded query:

```http
GET /api/v1/users?filter={"age":{"gte":18,"lte":65},"city":"New York"}
```

**Filter Operators:**
- `eq`: Equals
- `ne`: Not equals
- `gt`: Greater than
- `gte`: Greater than or equal
- `lt`: Less than
- `lte`: Less than or equal
- `in`: In array
- `nin`: Not in array
- `contains`: String contains
- `startsWith`: String starts with
- `endsWith`: String ends with

## Sorting

Sort results using `sort` parameter:

```http
GET /api/v1/users?sort=name
GET /api/v1/products?sort=-price
```

**Syntax:**
- Field name: Ascending order
- `-` prefix: Descending order

**Multiple Fields:**
```http
GET /api/v1/users?sort=role,-createdAt
```

Sorts by role (ascending), then by createdAt (descending).

**Available Sort Fields:**
- Most fields can be sorted
- Check individual endpoint documentation for exceptions

## Field Selection

Request specific fields using `fields` parameter:

```http
GET /api/v1/users?fields=id,name,email
```

**Response:**
```json
{
  "data": [
    { "id": "usr_1", "name": "John Doe", "email": "john@example.com" },
    { "id": "usr_2", "name": "Jane Smith", "email": "jane@example.com" }
  ]
}
```

**Benefits:**
- Reduced payload size
- Faster response times
- Lower bandwidth usage

## Combining Parameters

Combine pagination, filtering, sorting, and field selection:

```http
GET /api/v1/products?
  category=electronics&
  minPrice=50&
  maxPrice=200&
  sort=-rating,price&
  page=2&
  limit=20&
  fields=id,name,price,rating
```

**Example Response:**
```json
{
  "data": [
    { "id": "prod_21", "name": "Wireless Mouse", "price": 79.99, "rating": 4.8 },
    { "id": "prod_22", "name": "USB Cable", "price": 59.99, "rating": 4.8 }
  ],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 87,
    "totalPages": 5
  }
}
```
````

## Example 7: Error Response Documentation

**Generated Documentation:**

````markdown
## Error Handling

The API uses standard HTTP status codes and consistent error response format.

### Error Response Format

All errors return this structure:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Request validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format",
        "value": "invalid-email"
      }
    ],
    "requestId": "req_abc123",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

**Fields:**
- `code`: Machine-readable error code
- `message`: Human-readable error description
- `details`: Array of specific error details (optional)
- `requestId`: Unique request identifier for debugging
- `timestamp`: When the error occurred

### HTTP Status Codes

#### 2xx Success

| Code | Name    | Description                                      |
|------|---------|--------------------------------------------------|
| 200  | OK      | Request succeeded                                |
| 201  | Created | Resource created successfully                    |
| 204  | No Content | Request succeeded, no response body           |

#### 4xx Client Errors

| Code | Name            | Description                               | Common Causes                          |
|------|-----------------|-------------------------------------------|----------------------------------------|
| 400  | Bad Request     | Invalid request syntax or parameters      | Malformed JSON, invalid parameters     |
| 401  | Unauthorized    | Authentication required or failed         | Missing/invalid token                  |
| 403  | Forbidden       | Authenticated but insufficient permissions| Accessing unauthorized resource        |
| 404  | Not Found       | Resource does not exist                   | Invalid ID, deleted resource           |
| 409  | Conflict        | Request conflicts with current state      | Duplicate resource, concurrent update  |
| 422  | Unprocessable   | Validation failed                         | Invalid data format, business rule     |
| 429  | Too Many Requests| Rate limit exceeded                      | Too many API calls                     |

#### 5xx Server Errors

| Code | Name                  | Description                          | Action                                  |
|------|-----------------------|--------------------------------------|-----------------------------------------|
| 500  | Internal Server Error | Unexpected server error              | Retry, contact support if persists      |
| 502  | Bad Gateway           | Upstream service error               | Retry with exponential backoff          |
| 503  | Service Unavailable   | Server temporarily unavailable       | Check status page, retry later          |
| 504  | Gateway Timeout       | Upstream service timeout             | Retry with longer timeout               |

### Error Codes

Detailed error codes for programmatic handling:

#### Authentication Errors

**invalid_token**
```json
{
  "error": {
    "code": "invalid_token",
    "message": "The access token is invalid or has expired"
  }
}
```
**HTTP Status:** 401
**Solution:** Obtain a new access token

**missing_authentication**
```json
{
  "error": {
    "code": "missing_authentication",
    "message": "Authentication required for this endpoint"
  }
}
```
**HTTP Status:** 401
**Solution:** Include Authorization header

#### Validation Errors

**validation_error**
```json
{
  "error": {
    "code": "validation_error",
    "message": "Request validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format",
        "value": "not-an-email"
      },
      {
        "field": "age",
        "message": "Must be at least 18",
        "value": 16
      }
    ]
  }
}
```
**HTTP Status:** 422
**Solution:** Fix the invalid fields and resubmit

**missing_required_field**
```json
{
  "error": {
    "code": "missing_required_field",
    "message": "Required field is missing",
    "details": [
      {
        "field": "email",
        "message": "This field is required"
      }
    ]
  }
}
```
**HTTP Status:** 400
**Solution:** Include all required fields

#### Resource Errors

**resource_not_found**
```json
{
  "error": {
    "code": "resource_not_found",
    "message": "The requested resource was not found",
    "details": {
      "resourceType": "User",
      "resourceId": "usr_123"
    }
  }
}
```
**HTTP Status:** 404
**Solution:** Verify the resource ID

**resource_already_exists**
```json
{
  "error": {
    "code": "resource_already_exists",
    "message": "A resource with this identifier already exists",
    "details": {
      "resourceType": "User",
      "field": "email",
      "value": "user@example.com"
    }
  }
}
```
**HTTP Status:** 409
**Solution:** Use a different identifier or update the existing resource

#### Rate Limiting Errors

**rate_limit_exceeded**
```json
{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "Rate limit exceeded. Please try again later.",
    "details": {
      "limit": 1000,
      "remaining": 0,
      "resetAt": "2024-01-15T11:00:00Z"
    }
  }
}
```
**HTTP Status:** 429
**Response Headers:**
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1705316400
Retry-After: 3600
```
**Solution:** Wait until reset time or reduce request frequency

### Error Handling Best Practices

#### Retry Logic

Implement exponential backoff for retries:

```javascript
async function apiRequestWithRetry(url, options, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await fetch(url, options);
      
      // Success
      if (response.ok) {
        return await response.json();
      }
      
      // Don't retry client errors (except 429)
      if (response.status >= 400 && response.status < 500 && response.status !== 429) {
        throw new Error(`Client error: ${response.status}`);
      }
      
      // Handle rate limiting
      if (response.status === 429) {
        const retryAfter = response.headers.get('Retry-After') || Math.pow(2, attempt);
        await sleep(retryAfter * 1000);
        continue;
      }
      
      // Retry server errors with exponential backoff
      if (response.status >= 500) {
        const delay = Math.pow(2, attempt) * 1000; // 1s, 2s, 4s
        await sleep(delay);
        continue;
      }
      
    } catch (error) {
      if (attempt === maxRetries - 1) throw error;
      await sleep(Math.pow(2, attempt) * 1000);
    }
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

#### Error Display

```javascript
function handleApiError(error) {
  // Network error
  if (!error.response) {
    return 'Network error. Please check your connection.';
  }
  
  const { code, message, details } = error.response.error;
  
  // Specific error handling
  switch (code) {
    case 'invalid_token':
      // Redirect to login
      redirectToLogin();
      return 'Session expired. Please log in again.';
    
    case 'validation_error':
      // Show field-specific errors
      return details.map(d => `${d.field}: ${d.message}`).join('\n');
    
    case 'rate_limit_exceeded':
      const resetTime = new Date(details.resetAt);
      return `Rate limit exceeded. Try again at ${resetTime.toLocaleTimeString()}`;
    
    case 'resource_not_found':
      return `${details.resourceType} not found`;
    
    default:
      return message || 'An error occurred. Please try again.';
  }
}
```

#### Logging Errors

Always log the `requestId` for debugging:

```javascript
try {
  const data = await apiCall();
} catch (error) {
  console.error('API Error:', {
    requestId: error.response?.error?.requestId,
    code: error.response?.error?.code,
    message: error.response?.error?.message,
    timestamp: new Date().toISOString()
  });
  
  // Send to error tracking service
  trackError({
    type: 'api_error',
    requestId: error.response?.error?.requestId,
    endpoint: url,
    statusCode: error.response?.status
  });
}
```

### Getting Help

If you encounter persistent errors:

1. Check the [Status Page](https://status.example.com)
2. Search [Known Issues](https://docs.example.com/known-issues)
3. Include the `requestId` when contacting support
4. Provide request details (endpoint, method, parameters)
5. Include error response and timestamp

**Support Contact:**
- Email: api-support@example.com
- Response time: 24 hours for standard, 2 hours for premium
````

## Example 8: Webhook Documentation

**Generated Documentation:**

````markdown
## Webhooks

Receive real-time notifications when events occur in your account.

### Overview

Webhooks allow you to receive HTTP POST requests to your server when specific events happen. Instead of polling the API, your application is notified immediately.

### Setup

1. Register a webhook endpoint in your dashboard
2. Choose which events to subscribe to
3. Provide a URL that can receive POST requests
4. Optionally, configure a signing secret for verification

### Webhook Endpoint Requirements

Your endpoint must:
- ✓ Accept POST requests
- ✓ Use HTTPS (HTTP not allowed)
- ✓ Respond within 5 seconds
- ✓ Return 2xx status code for successful receipt
- ✓ Be publicly accessible (no localhost)

**Recommended:**
- Verify webhook signatures
- Process asynchronously (respond quickly, process later)
- Implement idempotency (same event may be sent twice)

### Webhook Payload Format

All webhooks send this structure:

```json
{
  "id": "evt_1234567890",
  "type": "user.created",
  "created": "2024-01-15T10:30:00Z",
  "data": {
    // Event-specific data
  },
  "previousData": {
    // For update events, previous values
  }
}
```

**Headers:**
```
Content-Type: application/json
X-Webhook-Signature: sha256=abc123...
X-Webhook-Id: evt_1234567890
X-Webhook-Timestamp: 1705316400
User-Agent: ExampleWebhook/1.0
```

### Signature Verification

Verify webhook authenticity using the signature:

**1. Get your signing secret** from the dashboard

**2. Compute expected signature:**
```
signature_payload = timestamp + "." + json_body
expected_signature = HMAC-SHA256(signature_payload, signing_secret)
```

**3. Compare signatures** (constant-time comparison)

**Example (Node.js):**
```javascript
const crypto = require('crypto');

function verifyWebhookSignature(payload, signature, secret) {
  const timestamp = payload.created;
  const signaturePayload = `${timestamp}.${JSON.stringify(payload)}`;
  
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(signaturePayload)
    .digest('hex');
  
  // Constant-time comparison
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(`sha256=${expectedSignature}`)
  );
}

// Usage
app.post('/webhooks', (req, res) => {
  const signature = req.headers['x-webhook-signature'];
  const payload = req.body;
  
  if (!verifyWebhookSignature(payload, signature, process.env.WEBHOOK_SECRET)) {
    return res.status(401).send('Invalid signature');
  }
  
  // Process webhook
  processWebhook(payload);
  
  // Respond quickly
  res.status(200).send('OK');
});
```

**Example (Python):**
```python
import hmac
import hashlib

def verify_webhook_signature(payload, signature, secret):
    timestamp = payload['created']
    signature_payload = f"{timestamp}.{json.dumps(payload)}"
    
    expected_signature = hmac.new(
        secret.encode(),
        signature_payload.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(
        signature,
        f"sha256={expected_signature}"
    )
```

### Event Types

#### User Events

**user.created**
```json
{
  "id": "evt_123",
  "type": "user.created",
  "created": "2024-01-15T10:30:00Z",
  "data": {
    "id": "usr_456",
    "email": "user@example.com",
    "name": "John Doe",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

**user.updated**
```json
{
  "id": "evt_124",
  "type": "user.updated",
  "created": "2024-01-15T10:31:00Z",
  "data": {
    "id": "usr_456",
    "email": "user@example.com",
    "name": "John Doe Updated"
  },
  "previousData": {
    "name": "John Doe"
  }
}
```

**user.deleted**
```json
{
  "id": "evt_125",
  "type": "user.deleted",
  "created": "2024-01-15T10:32:00Z",
  "data": {
    "id": "usr_456"
  }
}
```

#### Payment Events

**payment.succeeded**
```json
{
  "id": "evt_126",
  "type": "payment.succeeded",
  "created": "2024-01-15T10:33:00Z",
  "data": {
    "id": "pay_789",
    "amount": 99.99,
    "currency": "USD",
    "customerId": "cus_123",
    "status": "succeeded"
  }
}
```

**payment.failed**
```json
{
  "id": "evt_127",
  "type": "payment.failed",
  "created": "2024-01-15T10:34:00Z",
  "data": {
    "id": "pay_790",
    "amount": 99.99,
    "currency": "USD",
    "customerId": "cus_123",
    "status": "failed",
    "failureReason": "insufficient_funds"
  }
}
```

### Retry Logic

If your endpoint doesn't respond with 2xx:

1. **Immediate retry**: After 1 second
2. **Second retry**: After 5 seconds
3. **Third retry**: After 30 seconds
4. **Fourth retry**: After 2 minutes
5. **Fifth retry**: After 10 minutes
6. **Sixth retry**: After 1 hour
7. **Seventh retry**: After 6 hours
8. **Final retry**: After 24 hours

After 8 failed attempts, the webhook is marked as failed and retries stop.

**Retry Headers:**
```
X-Webhook-Attempt: 3
X-Webhook-Max-Attempts: 8
```

### Handling Duplicate Events

The same event may be sent multiple times. Implement idempotency:

```javascript
const processedEvents = new Set();

function processWebhook(payload) {
  // Check if already processed
  if (processedEvents.has(payload.id)) {
    console.log('Event already processed:', payload.id);
    return;
  }
  
  // Process event
  handleEvent(payload);
  
  // Mark as processed
  processedEvents.add(payload.id);
  
  // Cleanup old entries periodically
  if (processedEvents.size > 10000) {
    const oldestEntries = Array.from(processedEvents).slice(0, 5000);
    oldestEntries.forEach(id => processedEvents.delete(id));
  }
}
```

### Testing Webhooks

#### Test Events

Send test events from the dashboard or via API:

```bash
curl -X POST https://api.example.com/v1/webhooks/test \
  -H "Authorization: Bearer your_token" \
  -H "Content-Type: application/json" \
  -d '{
    "endpoint": "https://your-app.com/webhooks",
    "eventType": "user.created"
  }'
```

#### Local Testing

Use tools to expose localhost:

**ngrok:**
```bash
ngrok http 3000
# Use the HTTPS URL as your webhook endpoint
```

**localtunnel:**
```bash
npx localtunnel --port 3000
```

#### Webhook Inspector

View webhook delivery history in dashboard:
- Request payload
- Response status and body
- Timestamps
- Retry attempts

### Example Implementation

**Full Express.js endpoint:**

```javascript
const express = require('express');
const crypto = require('crypto');
const app = express();

app.use(express.json());

// Store processed event IDs (use Redis in production)
const processedEvents = new Set();

// Webhook handler
app.post('/webhooks', async (req, res) => {
  try {
    const signature = req.headers['x-webhook-signature'];
    const payload = req.body;
    
    // Verify signature
    if (!verifyWebhookSignature(payload, signature, process.env.WEBHOOK_SECRET)) {
      console.error('Invalid webhook signature');
      return res.status(401).json({ error: 'Invalid signature' });
    }
    
    // Check for duplicate
    if (processedEvents.has(payload.id)) {
      console.log('Duplicate event:', payload.id);
      return res.status(200).json({ received: true, duplicate: true });
    }
    
    // Respond immediately
    res.status(200).json({ received: true });
    
    // Process asynchronously
    processWebhookAsync(payload);
    
  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

async function processWebhookAsync(payload) {
  try {
    // Mark as processed
    processedEvents.add(payload.id);
    
    // Handle event
    switch (payload.type) {
      case 'user.created':
        await handleUserCreated(payload.data);
        break;
      case 'payment.succeeded':
        await handlePaymentSucceeded(payload.data);
        break;
      default:
        console.log('Unhandled event type:', payload.type);
    }
  } catch (error) {
    console.error('Failed to process webhook:', error);
    // Log to error tracking service
  }
}

function verifyWebhookSignature(payload, signature, secret) {
  const timestamp = payload.created;
  const signaturePayload = `${timestamp}.${JSON.stringify(payload)}`;
  
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(signaturePayload)
    .digest('hex');
  
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(`sha256=${expectedSignature}`)
  );
}

app.listen(3000, () => {
  console.log('Webhook server running on port 3000');
});
```

### Security Best Practices

🔒 **Always verify signatures** - Don't trust incoming requests

🔒 **Use HTTPS only** - Protect data in transit

🔒 **Validate payload structure** - Check for expected fields

🔒 **Rate limit your endpoint** - Prevent abuse

🔒 **Keep secrets secure** - Store in environment variables

🔒 **Implement timeouts** - Don't let processing block indefinitely

🔒 **Log webhook deliveries** - Audit trail for debugging

### Troubleshooting

**Webhooks not received:**
- Check endpoint URL is correct and publicly accessible
- Verify endpoint returns 2xx status code
- Check firewall rules allow our IPs
- View delivery logs in dashboard

**Invalid signature errors:**
- Verify signing secret is correct
- Check you're using raw request body (not parsed)
- Ensure timestamp is from payload, not current time

**Timeout errors:**
- Respond immediately (within 5 seconds)
- Process events asynchronously
- Avoid long database queries in webhook handler

**Duplicate events:**
- Implement idempotency using event IDs
- Store processed event IDs
- Return 200 for duplicates

### Rate Limits

- Maximum 100 webhooks per endpoint per minute
- Maximum 10 endpoints per account
- Maximum 1000 events queued per endpoint

### Webhook Management API

**List webhooks:**
```bash
GET /v1/webhooks
```

**Create webhook:**
```bash
POST /v1/webhooks
{
  "url": "https://your-app.com/webhooks",
  "events": ["user.created", "payment.succeeded"],
  "description": "Production webhook"
}
```

**Update webhook:**
```bash
PATCH /v1/webhooks/{id}
{
  "events": ["user.*", "payment.*"]
}
```

**Delete webhook:**
```bash
DELETE /v1/webhooks/{id}
```
````

## Example 9: Rate Limiting Documentation

**Generated Documentation:**

````markdown
## Rate Limiting

API requests are rate limited to ensure fair usage and system stability.

### Rate Limits

Different limits apply based on your plan:

| Plan       | Requests/Hour | Requests/Minute | Burst |
|------------|---------------|-----------------|-------|
| Free       | 1,000         | 100             | 10    |
| Basic      | 10,000        | 500             | 50    |
| Pro        | 100,000       | 2,000           | 100   |
| Enterprise | Unlimited     | Custom          | Custom|

### Rate Limit Headers

Every API response includes rate limit information:

```http
HTTP/1.1 200 OK
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 997
X-RateLimit-Reset: 1705320000
X-RateLimit-Retry-After: 3600
```

**Headers:**
- `X-RateLimit-Limit`: Total requests allowed in window
- `X-RateLimit-Remaining`: Requests remaining in current window
- `X-RateLimit-Reset`: Unix timestamp when limit resets
- `X-RateLimit-Retry-After`: Seconds until limit resets (when limit exceeded)

### Rate Limit Exceeded

When you exceed the limit, you receive a 429 response:

```http
HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1705320000
Retry-After: 3600

{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "Rate limit exceeded. Please try again in 3600 seconds.",
    "retryAfter": 3600,
    "resetAt": "2024-01-15T11:00:00Z"
  }
}
```

### Handling Rate Limits

**Check remaining requests:**

```javascript
async function makeApiRequest(url) {
  const response = await fetch(url, {
    headers: { 'Authorization': 'Bearer token' }
  });
  
  const remaining = response.headers.get('X-RateLimit-Remaining');
  const reset = response.headers.get('X-RateLimit-Reset');
  
  console.log(`${remaining} requests remaining`);
  console.log(`Limit resets at ${new Date(reset * 1000)}`);
  
  if (response.status === 429) {
    const retryAfter = response.headers.get('Retry-After');
    console.log(`Rate limited. Retry after ${retryAfter} seconds`);
    await sleep(retryAfter * 1000);
    return makeApiRequest(url); // Retry
  }
  
  return response.json();
}
```

**Implement exponential backoff:**

```javascript
async function apiRequestWithBackoff(url, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await fetch(url);
      
      if (response.status !== 429) {
        return await response.json();
      }
      
      const retryAfter = response.headers.get('Retry-After');
      const delay = retryAfter ? retryAfter * 1000 : Math.pow(2, i) * 1000;
      
      console.log(`Rate limited. Waiting ${delay}ms before retry ${i + 1}`);
      await sleep(delay);
      
    } catch (error) {
      if (i === maxRetries - 1) throw error;
    }
  }
}
```

### Best Practices

**1. Cache responses** when possible
```javascript
const cache = new Map();

async function getCachedUser(userId) {
  if (cache.has(userId)) {
    return cache.get(userId);
  }
  
  const user = await apiRequest(`/users/${userId}`);
  cache.set(userId, user);
  setTimeout(() => cache.delete(userId), 5 * 60 * 1000); // 5 min TTL
  
  return user;
}
```

**2. Batch requests** when supported
```javascript
// Instead of multiple requests
const user1 = await fetch('/users/1');
const user2 = await fetch('/users/2');
const user3 = await fetch('/users/3');

// Use batch endpoint
const users = await fetch('/users/batch?ids=1,2,3');
```

**3. Use webhooks** instead of polling
```javascript
// ❌ Polling (wastes rate limit)
setInterval(async () => {
  const newOrders = await fetch('/orders?status=new');
}, 30000);

// ✅ Webhooks (no rate limit impact)
app.post('/webhooks/orders', (req, res) => {
  const order = req.body.data;
  processNewOrder(order);
});
```

**4. Monitor usage**
```javascript
let requestCount = 0;
let resetTime = Date.now() + 3600000;

async function trackRateLimit(response) {
  const remaining = parseInt(response.headers.get('X-RateLimit-Remaining'));
  const reset = parseInt(response.headers.get('X-RateLimit-Reset')) * 1000;
  
  requestCount++;
  resetTime = reset;
  
  // Alert if approaching limit
  if (remaining < 100) {
    console.warn(`WARNING: Only ${remaining} requests remaining`);
    notifyAdmin(`Low rate limit: ${remaining} remaining`);
  }
}
```

### Per-Endpoint Limits

Some endpoints have stricter limits:

| Endpoint               | Limit/Min | Reason                    |
|------------------------|-----------|---------------------------|
| POST /users            | 10        | Prevent spam accounts     |
| POST /auth/token       | 5         | Prevent brute force       |
| POST /passwords/reset  | 3         | Security                  |
| DELETE /users/{id}     | 20        | Data protection           |

### IP-Based Limits

Unauthenticated requests are limited by IP address:
- 100 requests per hour per IP
- Use authentication for higher limits

### Increasing Limits

Need higher limits?
1. Upgrade your plan
2. Contact sales for custom Enterprise limits
3. Optimize requests to stay within limits
4. Use caching and webhooks

### Status Page

Check current rate limit status:
```bash
GET /v1/rate-limit/status

Response:
{
  "limit": 1000,
  "remaining": 842,
  "reset": "2024-01-15T11:00:00Z",
  "percentUsed": 15.8
}
```
````

## Documentation Patterns by API Type

### REST APIs
**Focus on:**
- HTTP methods and status codes
- Resource-oriented URLs
- Request/response formats
- CRUD operations
- Pagination and filtering

**Example Structure:**
```
/users
  GET    - List users
  POST   - Create user
/users/{id}
  GET    - Get user
  PUT    - Update user
  DELETE - Delete user
```

### GraphQL APIs
**Focus on:**
- Schema definitions
- Query and mutation examples
- Type descriptions
- Arguments and variables
- Error handling in GraphQL format

**Example Structure:**
```
Types
  User
  Post
  Comment
Queries
  user(id)
  posts(filter)
Mutations
  createUser(input)
  updatePost(id, input)
```

### gRPC APIs
**Focus on:**
- Protocol buffer definitions
- Service methods
- Message types
- Streaming capabilities
- Error codes

**Example Structure:**
```
service UserService {
  rpc GetUser(GetUserRequest) returns (User)
  rpc ListUsers(ListUsersRequest) returns (stream User)
}
```

### WebSocket APIs
**Focus on:**
- Connection process
- Event types (client→server, server→client)
- Message formats
- Heartbeat mechanism
- Reconnection strategy

**Example Structure:**
```
Events
  Client → Server
    user:login
    chat:message
  Server → Client
    message:new
    notification:receive
```

## Quality Checklist

Before publishing API documentation:

- [ ] **Accuracy**: All endpoints tested and verified
- [ ] **Completeness**: All public endpoints documented
- [ ] **Examples**: Working code samples in multiple languages
- [ ] **Errors**: All error codes and responses documented
- [ ] **Authentication**: Clear auth instructions and examples
- [ ] **Models**: All data schemas documented
- [ ] **Pagination**: Pagination patterns explained
- [ ] **Rate Limits**: Limits and handling strategies documented
- [ ] **Versioning**: Version information and migration guides
- [ ] **Changelog**: Recent changes documented
- [ ] **Search**: Documentation is searchable
- [ ] **Navigation**: Easy to find specific information
- [ ] **Interactive**: Try-it-out features when possible
- [ ] **OpenAPI**: Machine-readable spec generated
- [ ] **Support**: Contact information provided

## Advanced Documentation Features

### Interactive API Explorer

Embed interactive elements:
```html
<api-explorer
  endpoint="GET /users"
  auth-required="true"
  try-it-out="true"
/>
```

### Code Generation

Provide generated client code:
```javascript
// Auto-generated from OpenAPI spec
const client = new APIClient({ token: 'your_token' });
const users = await client.users.list({ page: 1, limit: 20 });
```

### SDK Documentation

Link to SDKs with examples:
- JavaScript/TypeScript SDK
- Python SDK
- Ruby SDK
- Go SDK
- Java SDK

### Postman Collection

Export API as Postman collection:
```json
{
  "info": { "name": "Example API" },
  "item": [...]
}
```

### OpenAPI Extensions

Use custom extensions:
```yaml
paths:
  /users:
    get:
      x-code-samples:
        - lang: JavaScript
          source: |
            const users = await fetch('/users');
```
