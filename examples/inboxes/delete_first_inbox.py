"""
Delete first inbox example for AgentMail.

This example demonstrates how to delete the first inbox found.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.agentmail.inboxes import list_inboxes, delete_inbox


def main():
    """Delete the first inbox found."""
    print("Listing inboxes...")
    try:
        resp = list_inboxes()
        inboxes = resp.inboxes if hasattr(resp, 'inboxes') else (resp if isinstance(resp, list) else [])
        
        if not inboxes or len(inboxes) == 0:
            print("No inboxes found. Nothing to delete.")
            return
        
        # Get the first inbox
        first_inbox = inboxes[0]
        inbox_id = getattr(first_inbox, 'inbox_id', getattr(first_inbox, 'id', None))
        email = getattr(first_inbox, 'email', inbox_id)
        
        if not inbox_id:
            print("Error: Could not determine inbox ID")
            return
        
        print(f"\nDeleting inbox: {email} (ID: {inbox_id})...")
        result = delete_inbox(inbox_id)
        print(f"✓ Inbox deleted successfully!")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

