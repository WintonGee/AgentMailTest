"""
Message management module.

Provides functions to send and reply to email messages.
"""

from typing import List, Dict, Any, Optional, Union
from .client import get_client


def send_message(
    inbox_id: str,
    to: Union[str, List[str]],
    subject: str,
    text: Optional[str] = None,
    html: Optional[str] = None,
    labels: Optional[List[str]] = None,
    api_key: str = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Send a new email message.
    
    Args:
        inbox_id: The ID of the inbox to send from
        to: Recipient email address(es) - can be a string or list of strings
        subject: Email subject line
        text: Optional plain text body of the email
        html: Optional HTML body of the email
        labels: Optional list of label strings to apply to the message
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Additional parameters for message sending
    
    Returns:
        Sent message object
    """
    client = get_client(api_key)
    
    # Ensure 'to' is a list
    if isinstance(to, str):
        to = [to]
    
    # Build request body parameters (inbox_id is a path parameter, not in body)
    request_body = {
        "to": to,
        "subject": subject
    }
    
    if text is not None:
        request_body["text"] = text
    
    if html is not None:
        request_body["html"] = html
    
    if labels is not None:
        request_body["labels"] = labels
    
    request_body.update(kwargs)
    
    # Pass inbox_id as path parameter and request_body as body
    return client.inboxes.messages.send(inbox_id=inbox_id, **request_body)


def reply_message(
    inbox_id: str,
    message_id: str,
    text: Optional[str] = None,
    html: Optional[str] = None,
    api_key: str = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Reply to an existing email message.
    
    Args:
        inbox_id: The ID of the inbox to reply from
        message_id: The ID of the message to reply to
        text: Optional plain text body of the reply
        html: Optional HTML body of the reply
        api_key: Optional API key. If not provided, will load from environment.
        **kwargs: Additional parameters for the reply
    
    Returns:
        Reply message object
    """
    client = get_client(api_key)
    
    params = {
        "inbox_id": inbox_id,
        "message_id": message_id
    }
    
    if text is not None:
        params["text"] = text
    
    if html is not None:
        params["html"] = html
    
    params.update(kwargs)
    
    return client.inboxes.messages.reply(**params)

