"""
Client configuration and initialization module.

Provides a centralized way to initialize and configure the AgentMail client.
"""

import os
from typing import Optional
from dotenv import load_dotenv
from agentmail import AgentMail


def get_client(api_key: Optional[str] = None) -> AgentMail:
    """
    Initialize and return an AgentMail client instance.
    
    Args:
        api_key: Optional API key. If not provided, will attempt to load
                 from environment variable AGENTMAIL_API_KEY or .env file.
    
    Returns:
        AgentMail: Initialized client instance
    
    Raises:
        ValueError: If no API key is provided and none is found in environment
    """
    if api_key is None:
        load_dotenv()
        api_key = os.getenv("AGENTMAIL_API_KEY")
    
    if not api_key:
        raise ValueError(
            "API key is required. Provide it as an argument or set "
            "AGENTMAIL_API_KEY environment variable."
        )
    
    return AgentMail(api_key=api_key)

