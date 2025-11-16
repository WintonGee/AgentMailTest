"""
Email thread management module.

Provides functions to access and manage email threads and conversations.
"""

from typing import List, Dict, Any
from .client import get_client


def list_threads(api_key: str = None, **kwargs) -> List[Dict[str, Any]]:
    """
    List all threads.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Additional parameters for filtering threads
    
    Returns:
        List of thread objects
    """
    client = get_client(api_key)
    return client.threads.list(**kwargs)


def get_thread(thread_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Get a specific thread by ID.
    
    Args:
        thread_id: The ID of the thread to retrieve
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Thread object with all messages
    """
    client = get_client(api_key)
    return client.threads.get(thread_id=thread_id)


def get_attachment(thread_id: str, attachment_id: str, api_key: str = None) -> bytes:
    """
    Get an attachment from a thread.
    
    Args:
        thread_id: The ID of the thread
        attachment_id: The ID of the attachment
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Attachment file data
    """
    client = get_client(api_key)
    return client.threads.get_attachment(thread_id=thread_id, attachment_id=attachment_id)

