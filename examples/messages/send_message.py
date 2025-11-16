"""
Send message example for AgentMail.

This example demonstrates how to send a new email message.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.agentmail.inboxes import create_inbox, list_inboxes
from src.agentmail.messages import send_message


def main():
    """Send a new message."""
    print("Sending message...")
    try:
        # First, ensure we have at least 2 inboxes
        print("Getting inboxes...")
        resp = list_inboxes()
        if hasattr(resp, 'inboxes'):
            inboxes = resp.inboxes
        elif isinstance(resp, list):
            inboxes = resp
        else:
            inboxes = []
        
        # Calculate how many inboxes we need to create (max 2 total)
        inboxes_needed = max(0, 2 - len(inboxes))
        
        # Store newly created inboxes
        newly_created = []
        
        if inboxes_needed > 0:
            print(f"Found {len(inboxes)} inbox(es). Creating {inboxes_needed} more inbox(es)...")
            for i in range(inboxes_needed):
                try:
                    new_inbox = create_inbox()
                    newly_created.append(new_inbox)
                    new_inbox_id = getattr(new_inbox, 'inbox_id', getattr(new_inbox, 'id', None))
                    new_inbox_email = getattr(new_inbox, 'email', None) or new_inbox_id
                    print(f"Created inbox {i+1}: {new_inbox_email} (ID: {new_inbox_id})")
                except Exception as e:
                    error_msg = str(e)
                    if 'LimitExceededError' in error_msg or 'limit' in error_msg.lower():
                        print(f"Warning: Could not create inbox {i+1}: Inbox limit reached")
                    else:
                        print(f"Warning: Could not create inbox {i+1}: {e}")
        
        # Combine existing and newly created inboxes
        # Use newly created ones first, then existing ones
        all_inboxes = newly_created + inboxes
        
        if len(all_inboxes) < 2:
            print(f"Error: Need at least 2 inboxes, but only have {len(all_inboxes)}")
            return
        
        # Get first and second inbox
        first_inbox = all_inboxes[0]
        second_inbox = all_inboxes[1]
        
        first_inbox_id = getattr(first_inbox, 'inbox_id', getattr(first_inbox, 'id', None))
        second_inbox_id = getattr(second_inbox, 'inbox_id', getattr(second_inbox, 'id', None))
        
        # Use inbox_id as email if email attribute is not available
        first_inbox_email = getattr(first_inbox, 'email', None) or first_inbox_id
        second_inbox_email = getattr(second_inbox, 'email', None) or second_inbox_id
        
        if not first_inbox_id:
            print("Error: Could not determine first inbox ID")
            return
        
        if not second_inbox_id:
            print("Error: Could not determine second inbox ID")
            return
        
        print(f"\nUsing first inbox to send: {first_inbox_email} (ID: {first_inbox_id})")
        print(f"Sending to second inbox: {second_inbox_email} (ID: {second_inbox_id})")
        
        # Verify inbox_ids are valid (should be email addresses)
        if not first_inbox_id or '@' not in str(first_inbox_id):
            print(f"Error: Invalid first inbox ID format: {first_inbox_id}")
            return
        
        if not second_inbox_email or '@' not in str(second_inbox_email):
            print(f"Error: Invalid second inbox email format: {second_inbox_email}")
            return
        
        # Send a test message from first inbox to second inbox
        print("\nSending test message...")
        try:
            message = send_message(
                inbox_id=first_inbox_id,
                to=second_inbox_email,
                subject="Test Message from AgentMail",
                text="This is a test message sent using the AgentMail Python SDK.",
                html="<p>This is a test message sent using the AgentMail Python SDK.</p>"
            )
        except Exception as send_error:
            error_str = str(send_error)
            if 'NotFoundError' in error_str or 'not found' in error_str.lower():
                print(f"Error: Inbox '{first_inbox_id}' not found. This might be a timing issue or the inbox may not be accessible.")
                print("Trying to verify inbox exists...")
                # Try to get the inbox to verify it exists
                try:
                    from src.agentmail.inboxes import get_inbox
                    get_inbox(first_inbox_id)  # Verify inbox exists
                    print("Inbox verified. Retrying send...")
                    message = send_message(
                        inbox_id=first_inbox_id,
                        to=second_inbox_email,
                        subject="Test Message from AgentMail",
                        text="This is a test message sent using the AgentMail Python SDK.",
                        html="<p>This is a test message sent using the AgentMail Python SDK.</p>"
                    )
                except Exception as verify_error:
                    print(f"Could not verify inbox: {verify_error}")
                    raise send_error
            else:
                raise
        
        message_id = getattr(message, 'message_id', getattr(message, 'id', 'N/A'))
        
        print("\n✓ Message sent successfully!")
        print(f"Message ID: {message_id}")
        
        # Show additional details if available
        if hasattr(message, 'model_dump'):
            details = message.model_dump()
            print("\nAdditional details:")
            for key, value in details.items():
                if key not in ['message_id', 'id']:
                    print(f"  {key}: {value}")
            
    except Exception as e:
        print(f"Error sending message: {e}")


if __name__ == "__main__":
    main()

