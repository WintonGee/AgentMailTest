"""
List inboxes example for AgentMail.

This example demonstrates how to list all inboxes.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.agentmail.inboxes import list_inboxes


def main():
    """List all inboxes."""
    print("Listing inboxes...")
    try:
        resp = list_inboxes()
        inboxes = resp.inboxes if hasattr(resp, 'inboxes') else (resp if isinstance(resp, list) else [])
        
        print(f"\nFound {len(inboxes)} inbox(es):\n")
        
        for i, inbox in enumerate(inboxes, 1):
            inbox_id = getattr(inbox, 'inbox_id', getattr(inbox, 'id', 'N/A'))
            email = getattr(inbox, 'email', 'N/A')
            print(f"{i}. Inbox ID: {inbox_id}")
            print(f"   Email: {email}")
            
            # Show additional details if available
            if hasattr(inbox, 'model_dump'):
                details = inbox.model_dump()
                for key, value in details.items():
                    if key not in ['inbox_id', 'id', 'email']:
                        print(f"   {key}: {value}")
            print()
            
    except Exception as e:
        print(f"Error listing inboxes: {e}")


if __name__ == "__main__":
    main()

