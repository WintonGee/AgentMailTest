"""
Send bulk messages for AgentMail API limit testing.

This script sends multiple emails without labels.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agentmail.inboxes import create_inbox, list_inboxes
from src.agentmail.messages import send_message

# Configuration
NUM_EMAILS = 1000  # Number of emails to send
RECIPIENT = "winton@intern.amail.dev"


def main():
    """Send bulk emails."""
    print(f"Sending {NUM_EMAILS} emails to {RECIPIENT}...")
    
    try:
        # Get or create an inbox to send from
        print("Getting inboxes...")
        resp = list_inboxes()
        if hasattr(resp, 'inboxes'):
            inboxes = resp.inboxes
        elif isinstance(resp, list):
            inboxes = resp
        else:
            inboxes = []
        
        # Use first inbox or create one if none exist
        if not inboxes:
            print("No inboxes found. Creating one...")
            inbox = create_inbox()
            inboxes = [inbox]
        
        sender_inbox = inboxes[0]
        sender_inbox_id = getattr(sender_inbox, 'inbox_id', getattr(sender_inbox, 'id', None))
        sender_inbox_email = getattr(sender_inbox, 'email', None) or sender_inbox_id
        
        if not sender_inbox_id:
            print("Error: Could not determine sender inbox ID")
            return
        
        if '@' not in str(sender_inbox_id):
            print(f"Error: Invalid sender inbox ID format: {sender_inbox_id}")
            return
        
        print(f"Using sender inbox: {sender_inbox_email} (ID: {sender_inbox_id})\n")
        
        successful = 0
        failed = 0
        
        # Send emails
        for i in range(NUM_EMAILS):
            try:
                print(f"Sending email {i+1}/{NUM_EMAILS}...")
                
                send_message(
                    inbox_id=sender_inbox_id,
                    to=RECIPIENT,
                    subject=f"Bulk Test Email #{i+1}",
                    text=f"This is bulk test email number {i+1}",
                    html=f"<p>This is bulk test email number <strong>{i+1}</strong></p>"
                )
                successful += 1
                print(f"✓ Sent email {i+1}/{NUM_EMAILS}")
            except Exception as e:
                failed += 1
                print(f"Error sending email {i+1}: {e}")
        
        # Print summary
        print("\n✓ Completed!")
        print(f"  Successful: {successful}")
        print(f"  Failed: {failed}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

