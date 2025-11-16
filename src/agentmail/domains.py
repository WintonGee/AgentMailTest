"""
Domain management module.

Provides functions to manage custom domains for email inboxes.
"""

from typing import List, Dict, Any, Optional
from .client import get_client


def list_domains(api_key: str = None) -> List[Dict[str, Any]]:
    """
    List all domains.
    
    Args:
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        List of domain objects
    """
    client = get_client(api_key)
    return client.domains.list()


def get_domain(domain_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Get a specific domain by ID.
    
    Args:
        domain_id: The ID of the domain to retrieve
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Domain object
    """
    client = get_client(api_key)
    return client.domains.get(domain_id=domain_id)


def create_domain(domain: str, api_key: str = None, **kwargs) -> Dict[str, Any]:
    """
    Create a new domain.
    
    Args:
        domain: The domain name to create
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Additional parameters for domain creation
    
    Returns:
        Created domain object
    """
    client = get_client(api_key)
    return client.domains.create(domain=domain, **kwargs)


def delete_domain(domain_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Delete a domain by ID.
    
    Args:
        domain_id: The ID of the domain to delete
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Deletion result
    """
    client = get_client(api_key)
    return client.domains.delete(domain_id=domain_id)


def verify_domain(domain_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Verify a domain.
    
    Args:
        domain_id: The ID of the domain to verify
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Verification result
    """
    client = get_client(api_key)
    return client.domains.verify(domain_id=domain_id)


def get_zone_file(domain_id: str, api_key: str = None) -> Dict[str, Any]:
    """
    Get the zone file for a domain.
    
    Args:
        domain_id: The ID of the domain
        api_key: Optional API key. If not provided, will load from environment.
    
    Returns:
        Zone file configuration
    """
    client = get_client(api_key)
    return client.domains.get_zone_file(domain_id=domain_id)

