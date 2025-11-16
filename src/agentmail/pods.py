"""
Pod management module.

Provides functions to manage pods (containerized email processing units).
"""

from typing import List, Dict, Any
from .client import get_client


def list_pods(api_key: str = None) -> List[Dict[str, Any]]:
    """
    List all pods.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        List of pod objects
    """
    client = get_client(api_key)
    return client.pods.list()


def get_pod(pod_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Get a specific pod by ID.
    
    Args:
        pod_id: The ID of the pod to retrieve
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Pod object
    """
    client = get_client(api_key)
    return client.pods.get(pod_id=pod_id)


def create_pod(api_key: str = None, **kwargs) -> Dict[str, Any]:
    """
    Create a new pod.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Additional parameters for pod creation
    
    Returns:
        Created pod object
    """
    client = get_client(api_key)
    return client.pods.create(**kwargs)


def delete_pod(pod_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Delete a pod by ID.
    
    Args:
        pod_id: The ID of the pod to delete
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Deletion result
    """
    client = get_client(api_key)
    return client.pods.delete(pod_id=pod_id)

