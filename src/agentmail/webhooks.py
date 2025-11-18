"""
Webhook configuration module.

Provides functions to configure webhooks for real-time event notifications.

Event Types:
    - message.received: Triggered when a message is received (currently supported)
    - message.sent: Triggered when a message is sent (future support)
    - message.delivered: Triggered when a message is delivered (future support)
    - message.bounced: Triggered when a message bounces (future support)
    - message.complained: Triggered when a message receives a complaint (future support)
    - message.rejected: Triggered when a message is rejected (future support)

Note: Currently, AgentMail only supports the 'message.received' event type.
When creating a webhook, event_types is optional and defaults to ['message.received'].

Reference: https://docs.agentmail.to/api-reference/webhooks/list
Reference: https://docs.agentmail.to/overview
"""

from typing import List, Dict, Any, Optional, Literal, Union
from .client import get_client

# Event type literals matching the API specification
EventType = Literal[
    "message.received",
    "message.sent",
    "message.delivered",
    "message.bounced",
    "message.complained",
    "message.rejected"
]


def list_webhooks(
    limit: Optional[int] = None,
    page_token: Optional[str] = None,
    api_key: str = None
) -> Dict[str, Any]:
    """
    List all webhooks with optional pagination.
    
    Args:
        limit: Optional maximum number of webhooks to return
        page_token: Optional token for pagination to retrieve next page
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        ListWebhooksResponse object containing:
            - count: Number of webhooks returned
            - webhooks: List of webhook objects
            - limit: The limit applied
            - next_page_token: Token for next page (if available)
    
    Reference: https://docs.agentmail.to/api-reference/webhooks/list
    """
    client = get_client(api_key)
    return client.webhooks.list(limit=limit, page_token=page_token)


def get_webhook(webhook_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Get a specific webhook by ID.
    
    Args:
        webhook_id: The ID of the webhook to retrieve
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Webhook object containing:
            - webhook_id: Unique identifier
            - url: Webhook URL
            - event_types: List of subscribed event types
            - inbox_ids: List of associated inbox IDs
            - secret: Secret for verifying webhook signatures
            - enabled: Whether the webhook is enabled
            - created_at: Creation timestamp
            - updated_at: Last update timestamp
            - client_id: Client identifier (if provided)
    """
    client = get_client(api_key)
    return client.webhooks.get(webhook_id=webhook_id)


def create_webhook(
    url: str,
    event_types: Optional[List[Union[EventType, str]]] = None,
    inbox_ids: Optional[List[str]] = None,
    client_id: Optional[str] = None,
    api_key: str = None
) -> Dict[str, Any]:
    """
    Create a new webhook.
    
    Args:
        url: The webhook URL to receive events (required)
        event_types: Optional list of event types to subscribe to.
                    Currently, AgentMail only supports 'message.received'.
                    If not provided, defaults to ['message.received'].
                    Valid values: 'message.received', 'message.sent',
                    'message.delivered', 'message.bounced', 'message.complained',
                    'message.rejected'
        inbox_ids: Optional list of inbox IDs to filter events for specific inboxes
        client_id: Optional client identifier
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Created webhook object containing:
            - webhook_id: Unique identifier
            - url: Webhook URL
            - event_types: List of subscribed event types
            - inbox_ids: List of associated inbox IDs
            - secret: Secret for verifying webhook signatures
            - enabled: Whether the webhook is enabled
            - created_at: Creation timestamp
            - updated_at: Last update timestamp
            - client_id: Client identifier (if provided)
    
    Reference: https://docs.agentmail.to/overview
    """
    client = get_client(api_key)
    
    # Build parameters
    params = {
        "url": url
    }
    
    # Only include event_types if provided
    if event_types is not None:
        params["event_types"] = event_types
    
    if inbox_ids is not None:
        params["inbox_ids"] = inbox_ids
    
    if client_id is not None:
        params["client_id"] = client_id
    
    return client.webhooks.create(**params)


def delete_webhook(webhook_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Delete a webhook by ID.
    
    Args:
        webhook_id: The ID of the webhook to delete
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Deletion result
    """
    client = get_client(api_key)
    return client.webhooks.delete(webhook_id=webhook_id)

