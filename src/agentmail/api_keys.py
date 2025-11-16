"""
API Keys management module.

Provides functions to manage API keys for authentication and access control.
"""

from typing import List, Dict, Any
from .client import get_client


def list_api_keys(api_key: str = None) -> List[Dict[str, Any]]:
    """
    List all API keys.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        List of API key objects
    """
    client = get_client(api_key)
    return client.api_keys.list()


def create_api_key(api_key: str = None, **kwargs) -> Dict[str, Any]:
    """
    Create a new API key.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Additional parameters for API key creation
    
    Returns:
        Created API key object
    """
    client = get_client(api_key)
    return client.api_keys.create(**kwargs)


def delete_api_key(api_key_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Delete an API key by ID.
    
    Args:
        api_key_id: The ID of the API key to delete
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Deletion result
    """
    client = get_client(api_key)
    return client.api_keys.delete(api_key_id=api_key_id)

