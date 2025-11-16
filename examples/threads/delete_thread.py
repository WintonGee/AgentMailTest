"""
Delete thread example for AgentMail.

This example demonstrates how to delete a thread.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.agentmail.threads import list_threads, delete_thread


def main():
    """Delete the first thread found."""
    print("Listing threads...")
    try:
        resp = list_threads()
        threads = resp.threads if hasattr(resp, 'threads') else (resp if isinstance(resp, list) else [])
        
        if not threads or len(threads) == 0:
            print("No threads found. Nothing to delete.")
            return
        
        # Get the first thread
        first_thread = threads[0]
        thread_id = getattr(first_thread, 'thread_id', getattr(first_thread, 'id', None))
        inbox_id = getattr(first_thread, 'inbox_id', None)
        subject = getattr(first_thread, 'subject', thread_id)
        
        if not thread_id:
            print("Error: Could not determine thread ID")
            return
        
        if not inbox_id:
            print("Error: Could not determine inbox ID from thread")
            return
        
        print(f"\nDeleting thread: {subject} (ID: {thread_id})...")
        result = delete_thread(thread_id=thread_id, inbox_id=inbox_id)
        print(f"✓ Thread deleted successfully!")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

