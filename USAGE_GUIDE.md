# AgentMail Test Suite - Usage Guide

## What Can You Do With This?

This test suite gives you complete access to all AgentMail functionality. Here's what you can accomplish:

---

## 🚀 Quick Start

### 1. **Create Temporary Email Addresses**

Perfect for testing, signups, or one-time use cases:

```python
from src.agentmail.inboxes import create_inbox

# Create a disposable email address
inbox = create_inbox()
print(f"Your email: {inbox['email']}")
# Output: Your email: abc123@agentmail.to
```

**Use Cases:**

- Testing email flows in your application
- Signing up for services without using your real email
- Creating temporary accounts for testing
- Email automation testing

---

## 📧 Email Management

### 2. **Receive and Read Emails**

```python
from src.agentmail.inboxes import create_inbox
from src.agentmail.threads import list_threads, get_thread

# Create inbox
inbox = create_inbox()
email_address = inbox['email']

# Later, check for emails
threads = list_threads()
for thread in threads['threads']:
    if thread['inbox_id'] == inbox['inbox_id']:
        # Get full email details
        full_thread = get_thread(thread['thread_id'])
        print(f"Subject: {full_thread['subject']}")
        print(f"From: {full_thread['from']['email']}")
        print(f"Body: {full_thread['body']}")
```

**Use Cases:**

- Email verification testing
- Reading confirmation emails
- Testing email templates
- Automated email processing

### 3. **Download Attachments**

```python
from src.agentmail.threads import get_attachment

# Download an attachment from an email
attachment_data = get_attachment(
    thread_id="thread_123",
    attachment_id="att_456"
)

# Save to file
with open("attachment.pdf", "wb") as f:
    f.write(attachment_data)
```

---

## 🔔 Real-Time Notifications with Webhooks

### 4. **Set Up Webhooks for Instant Notifications**

```python
from src.agentmail.webhooks import create_webhook

# Create a webhook that triggers on new emails
# event_types is optional - defaults to ['message.received']
webhook = create_webhook(
    url="https://your-server.com/webhook",
    inbox_ids=["inbox_123"]  # Optional: specific inboxes only
)

print(f"Webhook ID: {webhook['webhook_id']}")
print(f"Secret: {webhook['secret']}")  # Save this for verification!
```

**Event Types Available:**

- `message.received` - New email arrived (currently supported)
- `message.sent` - Email was sent (future support)
- `message.delivered` - Email was delivered (future support)
- `message.bounced` - Email bounced (future support)
- `message.complained` - Spam complaint (future support)
- `message.rejected` - Email was rejected (future support)

**Note:** Currently, AgentMail only supports the `message.received` event type. The `event_types` parameter is optional and defaults to `['message.received']` if not provided.

**Use Cases:**

- Real-time email notifications
- Triggering workflows when emails arrive
- Building email automation systems
- Monitoring email delivery status

---

## 🌐 Custom Domain Management

### 5. **Use Your Own Domain**

```python
from src.agentmail.domains import create_domain, verify_domain, get_zone_file

# Add your custom domain
domain = create_domain(domain="example.com")

# Get DNS records to configure
zone_file = get_zone_file(domain_id=domain['domain_id'])
print("DNS records to add:", zone_file)

# Verify domain is configured correctly
verification = verify_domain(domain_id=domain['domain_id'])
print(f"Domain verified: {verification['verified']}")

# Now create inboxes with your domain
from src.agentmail.inboxes import create_inbox
inbox = create_inbox(domain="example.com")
# inbox['email'] will be something like "user@example.com"
```

**Use Cases:**

- Professional email addresses for your app
- Branded email addresses
- Production email systems

---

## 📊 Analytics & Monitoring

### 6. **Track Usage and Metrics**

```python
from src.agentmail.metrics import list_metrics

# Get usage statistics
metrics = list_metrics()
print(f"Total emails: {metrics['total_emails']}")
print(f"API calls: {metrics['api_calls']}")
```

**Use Cases:**

- Monitoring API usage
- Tracking email volume
- Billing and cost analysis
- Performance monitoring

---

## 🔐 API Key Management

### 7. **Manage Multiple API Keys**

```python
from src.agentmail.api_keys import list_api_keys, create_api_key, delete_api_key

# List all your API keys
keys = list_api_keys()

# Create a new key for a specific application
new_key = create_api_key()
print(f"New API key: {new_key['api_key']}")

# Rotate keys for security
delete_api_key(api_key_id="old_key_id")
```

**Use Cases:**

- Key rotation for security
- Separate keys per application
- Revoking compromised keys

---

## 🐳 Pod Management (Advanced)

### 8. **Scale Email Processing**

```python
from src.agentmail.pods import create_pod, list_pods

# Create additional processing pods
pod = create_pod()
print(f"Pod created: {pod['pod_id']}")

# List all pods
pods = list_pods()
print(f"Active pods: {len(pods)}")
```

**Use Cases:**

- Scaling email processing capacity
- Isolated processing environments
- Load distribution

---

## 💡 Practical Examples

### Example 1: Email Verification Testing

```python
from src.agentmail.inboxes import create_inbox
from src.agentmail.threads import list_threads, get_thread
import time

# Create test inbox
inbox = create_inbox()
test_email = inbox['email']
print(f"Use this email for signup: {test_email}")

# Wait for verification email
print("Waiting for verification email...")
for _ in range(30):  # Check for 30 seconds
    threads = list_threads()
    for thread in threads['threads']:
        if 'verification' in thread.get('subject', '').lower():
            email = get_thread(thread['thread_id'])
            # Extract verification link from email body
            print("Verification email received!")
            break
    time.sleep(1)
```

### Example 2: Automated Email Monitoring

```python
from src.agentmail.inboxes import create_inbox
from src.agentmail.threads import list_threads
import time

inbox = create_inbox()

def check_for_emails():
    threads = list_threads()
    return [t for t in threads['threads']
            if t['inbox_id'] == inbox['inbox_id']]

# Monitor inbox every 10 seconds
while True:
    emails = check_for_emails()
    if emails:
        print(f"New emails: {len(emails)}")
    time.sleep(10)
```

### Example 3: Webhook Integration

```python
from src.agentmail.inboxes import create_inbox
from src.agentmail.webhooks import create_webhook

# Create inbox
inbox = create_inbox()

# Set up webhook to notify your server
# event_types is optional - defaults to ['message.received']
webhook = create_webhook(
    url="https://api.yourapp.com/agentmail/webhook",
    inbox_ids=[inbox['inbox_id']]
)

# Your server will now receive POST requests when emails arrive
# The webhook payload will include email details
```

---

## 🎯 Common Use Cases

1. **Testing & Development**

   - Test email flows without using real emails
   - Verify email templates and formatting
   - Test email delivery and processing

2. **Automation**

   - Automated email verification
   - Email-triggered workflows
   - Email parsing and data extraction

3. **Privacy**

   - Disposable email addresses
   - Temporary accounts
   - Privacy-focused signups

4. **Integration**

   - Connect email to your applications
   - Real-time email notifications
   - Email-based triggers

5. **Monitoring**
   - Track email delivery
   - Monitor bounce rates
   - Analyze email performance

---

## 📝 Running the Examples

```bash
# Basic quickstart
python examples/quickstart.py

# Complete functionality demo
python examples/complete_example.py

# Email monitoring
python examples/email_monitor.py

# Webhook setup example
python examples/webhook_server_example.py
```

---

## 🔗 Next Steps

1. **Set up your API key** in `.env` file
2. **Run the quickstart** to create your first inbox
3. **Try the examples** to see different use cases
4. **Build your own** email automation workflows
5. **Set up webhooks** for real-time notifications

---

## 📚 Additional Resources

- [AgentMail API Documentation](https://docs.agentmail.to)
- [Webhook Documentation](https://docs.agentmail.to/api-reference/webhooks)
- See `update_report.md` for detailed API reference

---

## ⚠️ Important Notes

- **Webhook URLs** must be publicly accessible
- **Save webhook secrets** - you'll need them for verification
- **API keys** should be kept secure (use `.env` file)
- **Rate limits** may apply - check AgentMail documentation

---

Happy testing! 🚀
