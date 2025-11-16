"""
Create, list, and delete inbox pipeline example for AgentMail.

This example demonstrates the full pipeline: create an inbox, list all inboxes, then delete the first inbox.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import the main functions from other example files
from examples.inboxes.create_inbox import main as create_inbox_main
from examples.inboxes.list_inboxes import main as list_inboxes_main
from examples.inboxes.delete_first_inbox import main as delete_first_inbox_main


def main():
    """Create, list, and delete inbox pipeline."""
    print("=" * 60)
    print("Full Pipeline: Create -> List -> Delete")
    print("=" * 60)
    
    # Step 1: Create an inbox
    print("\n1. Creating inbox...")
    try:
        create_inbox_main()
    except Exception as e:
        print(f"   ✗ Error creating inbox: {e}")
        return
    
    # Step 2: List all inboxes
    print("\n2. Listing all inboxes...")
    try:
        list_inboxes_main()
    except Exception as e:
        print(f"   ✗ Error listing inboxes: {e}")
        return
    
    # Step 3: Delete the first inbox
    print("\n3. Deleting first inbox...")
    try:
        delete_first_inbox_main()
    except Exception as e:
        print(f"   ✗ Error deleting inbox: {e}")
        return
    
    print("\n" + "=" * 60)
    print("Pipeline completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

