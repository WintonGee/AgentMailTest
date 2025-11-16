"""
Create inbox example for AgentMail.

This example demonstrates how to create a new inbox.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.agentmail.inboxes import create_inbox


def main():
    """Create a new inbox."""
    print("Creating inbox...")
    try:
        inbox = create_inbox()
        
        inbox_id = getattr(inbox, 'inbox_id', getattr(inbox, 'id', 'N/A'))
        email = getattr(inbox, 'email', 'N/A')
        
        print(f"\n✓ Inbox created successfully!")
        print(f"Inbox ID: {inbox_id}")
        print(f"Email: {email}")
        
        # Show additional details if available
        if hasattr(inbox, 'model_dump'):
            details = inbox.model_dump()
            print("\nAdditional details:")
            for key, value in details.items():
                if key not in ['inbox_id', 'id', 'email']:
                    print(f"  {key}: {value}")
            
    except Exception as e:
        print(f"Error creating inbox: {e}")


if __name__ == "__main__":
    main()

