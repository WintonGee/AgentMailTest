# AgentMail Test Suite

A professional, well-organized test suite for the AgentMail Python SDK, providing comprehensive coverage of all API functionality.

## Project Structure

```
AgentMailTest/
├── src/
│   └── agentmail/          # Main package
│       ├── __init__.py
│       ├── client.py       # Shared client initialization
│       ├── api_keys.py     # API keys management
│       ├── domains.py      # Domain management
│       ├── drafts.py       # Draft messages
│       ├── inboxes.py      # Inbox management
│       ├── metrics.py      # Metrics and analytics
│       ├── pods.py         # Pod management
│       ├── threads.py      # Email threads
│       └── webhooks.py     # Webhook configuration
├── examples/               # Example scripts
│   ├── __init__.py
│   └── quickstart.py      # Quickstart example
├── tests/                  # Test suite (to be implemented)
│   └── __init__.py
├── .env                    # Environment variables (gitignored)
├── .gitignore
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── update_report.md       # Detailed functionality report
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd AgentMailTest
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your API key:
   Create a `.env` file in the root directory:

```
AGENTMAIL_API_KEY=your_api_key_here
```

## Quick Start with Makefile

The easiest way to test functionality is using the Makefile:

```bash
# Show all available commands
make help

# Install dependencies
make install

# Run quickstart example
make test-quickstart

# Run all tests
make test-all
```

See `make help` for all available commands.

## Usage

### As a Package

Import and use the modules directly:

```python
from src.agentmail.inboxes import create_inbox, list_inboxes
from src.agentmail.threads import list_threads, get_thread

# Create an inbox
inbox = create_inbox()

# List all inboxes
inboxes = list_inboxes()

# List threads
threads = list_threads()
```

### Running Examples

```bash
# Run the quickstart example
python examples/quickstart.py
```

### Direct Client Access

```python
from src.agentmail.client import get_client

# Get a client instance
client = get_client()

# Use the client directly
inboxes = client.inboxes.list()
```

## Available Modules

### API Keys (`src/agentmail/api_keys.py`)

- `list_api_keys()` - List all API keys
- `create_api_key()` - Create a new API key
- `delete_api_key(api_key_id)` - Delete an API key

### Domains (`src/agentmail/domains.py`)

- `list_domains()` - List all domains
- `get_domain(domain_id)` - Get domain details
- `create_domain(domain)` - Create a new domain
- `delete_domain(domain_id)` - Delete a domain
- `verify_domain(domain_id)` - Verify domain ownership
- `get_zone_file(domain_id)` - Get DNS zone file

### Drafts (`src/agentmail/drafts.py`)

- `list_drafts()` - List all drafts
- `get_draft(draft_id)` - Get a specific draft

### Inboxes (`src/agentmail/inboxes.py`)

- `list_inboxes()` - List all inboxes
- `get_inbox(inbox_id)` - Get inbox details
- `create_inbox(domain=None)` - Create a new inbox
- `update_inbox(inbox_id, **kwargs)` - Update inbox properties
- `delete_inbox(inbox_id)` - Delete an inbox

### Metrics (`src/agentmail/metrics.py`)

- `list_metrics()` - Retrieve metrics and analytics

### Pods (`src/agentmail/pods.py`)

- `list_pods()` - List all pods
- `get_pod(pod_id)` - Get pod details
- `create_pod()` - Create a new pod
- `delete_pod(pod_id)` - Delete a pod

### Threads (`src/agentmail/threads.py`)

- `list_threads()` - List all email threads
- `get_thread(thread_id)` - Get thread with messages
- `get_attachment(thread_id, attachment_id)` - Download attachment

### Webhooks (`src/agentmail/webhooks.py`)

- `list_webhooks(limit=None, page_token=None)` - List all webhooks with pagination
- `get_webhook(webhook_id)` - Get webhook details
- `create_webhook(url, event_types=None, inbox_ids=None, client_id=None)` - Create a webhook
  - `event_types`: Optional list of event types. Currently only 'message.received' is supported. If not provided, defaults to ['message.received']
  - Valid values: 'message.received', 'message.sent', 'message.delivered', 'message.bounced', 'message.complained', 'message.rejected'
- `delete_webhook(webhook_id)` - Delete a webhook

## Architecture

### Design Principles

1. **Separation of Concerns**: Each module handles a single resource type
2. **Centralized Configuration**: Client initialization is handled in `client.py`
3. **Consistent API**: All functions follow the same pattern
4. **Type Hints**: Full type annotations for better IDE support
5. **Documentation**: Comprehensive docstrings for all functions

### Client Initialization

The `get_client()` function in `src/agentmail/client.py` provides:

- Automatic environment variable loading
- Consistent error handling
- Optional API key parameter for flexibility

## Development

### Adding New Functionality

1. Add new functions to the appropriate module in `src/agentmail/`
2. Follow the existing pattern with type hints and docstrings
3. Use `get_client()` for client initialization
4. Update this README with new functionality

### Testing

Test files should be added to the `tests/` directory. The test suite structure is ready for implementation.

## Documentation

For detailed information about all functionality, see `update_report.md`.

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
