"""
Metrics and analytics module.

Provides functions to access usage and performance metrics.
"""

from typing import List, Dict, Any
from .client import get_client


def list_metrics(api_key: str = None, **kwargs) -> List[Dict[str, Any]]:
    """
    List metrics.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Additional parameters for filtering metrics
    
    Returns:
        List of metric objects
    """
    client = get_client(api_key)
    return client.metrics.list(**kwargs)

