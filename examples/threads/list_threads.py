"""
List threads example for AgentMail.

This example demonstrates how to list all threads.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.agentmail.threads import list_threads


def main():
    """List all threads."""
    print("Listing threads...")
    try:
        resp = list_threads()
        threads = resp.threads if hasattr(resp, 'threads') else (resp if isinstance(resp, list) else [])
        
        print(f"\nFound {len(threads)} thread(s):\n")
        
        for i, thread in enumerate(threads, 1):
            thread_id = getattr(thread, 'thread_id', getattr(thread, 'id', 'N/A'))
            subject = getattr(thread, 'subject', 'N/A')
            inbox_id = getattr(thread, 'inbox_id', 'N/A')
            
            print(f"{i}. Thread ID: {thread_id}")
            print(f"   Subject: {subject}")
            print(f"   Inbox ID: {inbox_id}")
            
            # Show additional details if available
            if hasattr(thread, 'model_dump'):
                details = thread.model_dump()
                for key, value in details.items():
                    if key not in ['thread_id', 'id', 'subject', 'inbox_id']:
                        print(f"   {key}: {value}")
            print()
            
    except Exception as e:
        print(f"Error listing threads: {e}")


if __name__ == "__main__":
    main()

