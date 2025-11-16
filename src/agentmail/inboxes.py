"""
Inbox management module.

Provides functions to create and manage email inboxes.
"""

from typing import List, Dict, Any, Optional
from .client import get_client


def list_inboxes(api_key: str = None) -> List[Dict[str, Any]]:
    """
    List all inboxes.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        List of inbox objects
    """
    client = get_client(api_key)
    return client.inboxes.list()


def get_inbox(inbox_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Get a specific inbox by ID.
    
    Args:
        inbox_id: The ID of the inbox to retrieve
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Inbox object
    """
    client = get_client(api_key)
    return client.inboxes.get(inbox_id=inbox_id)


def create_inbox(domain: Optional[str] = None, api_key: str = None, **kwargs) -> Dict[str, Any]:
    """
    Create a new inbox.
    
    Args:
        domain: Optional domain name for the inbox
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Additional parameters for inbox creation
    
    Returns:
        Created inbox object
    """
    client = get_client(api_key)
    if domain:
        return client.inboxes.create(domain=domain, **kwargs)
    return client.inboxes.create(**kwargs)


def update_inbox(inbox_id: str, api_key: str = None, **kwargs) -> Dict[str, Any]:
    """
    Update an inbox by ID.
    
    Args:
        inbox_id: The ID of the inbox to update
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Fields to update
    
    Returns:
        Updated inbox object
    """
    client = get_client(api_key)
    return client.inboxes.update(inbox_id=inbox_id, **kwargs)


def delete_inbox(inbox_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Delete an inbox by ID.
    
    Args:
        inbox_id: The ID of the inbox to delete
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Deletion result
    """
    client = get_client(api_key)
    return client.inboxes.delete(inbox_id=inbox_id)

