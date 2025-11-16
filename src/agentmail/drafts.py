"""
Draft messages module.

Provides functions to access and manage draft email messages.
"""

from typing import List, Dict, Any
from .client import get_client


def list_drafts(api_key: str = None) -> List[Dict[str, Any]]:
    """
    List all drafts.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        List of draft objects
    """
    client = get_client(api_key)
    return client.drafts.list()


def get_draft(draft_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Get a specific draft by ID.
    
    Args:
        draft_id: The ID of the draft to retrieve
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Draft object
    """
    client = get_client(api_key)
    return client.drafts.get(draft_id=draft_id)

