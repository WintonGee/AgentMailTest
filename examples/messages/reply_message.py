"""
Reply message example for AgentMail.

This example demonstrates how to reply to an existing email message.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from src
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.agentmail.inboxes import list_inboxes
from src.agentmail.threads import list_threads, get_thread
from src.agentmail.messages import reply_message


def main():
    """Reply to an existing message."""
    print("Replying to message...")
    try:
        # Get inboxes
        print("Getting inboxes...")
        resp = list_inboxes()
        inboxes = resp.inboxes if hasattr(resp, 'inboxes') else (resp if isinstance(resp, list) else [])
        
        if not inboxes or len(inboxes) == 0:
            print("No inboxes found. Please create an inbox first.")
            return
        
        inbox = inboxes[0]
        inbox_id = getattr(inbox, 'inbox_id', getattr(inbox, 'id', None))
        inbox_email = getattr(inbox, 'email', 'N/A')
        
        if not inbox_id:
            print("Error: Could not determine inbox ID")
            return
        
        print(f"Using inbox: {inbox_email} (ID: {inbox_id})")
        
        # Get threads
        print("\nGetting threads...")
        threads_resp = list_threads()
        threads = threads_resp.threads if hasattr(threads_resp, 'threads') else (threads_resp if isinstance(threads_resp, list) else [])
        
        if not threads or len(threads) == 0:
            print("No threads found. Please send or receive a message first.")
            return
        
        # Get the first thread
        thread = threads[0]
        thread_id = getattr(thread, 'thread_id', getattr(thread, 'id', None))
        
        if not thread_id:
            print("Error: Could not determine thread ID")
            return
        
        print(f"Using thread: {thread_id}")
        
        # Get full thread details to find the last message
        print("\nGetting thread details...")
        thread_details = get_thread(thread_id)
        
        # Extract messages from thread
        messages = getattr(thread_details, 'messages', [])
        if isinstance(thread_details, dict):
            messages = thread_details.get('messages', [])
        
        if not messages or len(messages) == 0:
            print("No messages found in thread.")
            return
        
        # Get the last message ID
        last_message = messages[-1]
        message_id = getattr(last_message, 'message_id', getattr(last_message, 'id', None))
        
        if isinstance(last_message, dict):
            message_id = last_message.get('message_id') or last_message.get('id')
        
        if not message_id:
            print("Error: Could not determine message ID")
            return
        
        print(f"Replying to message: {message_id}")
        
        # Send reply
        print("\nSending reply...")
        reply = reply_message(
            inbox_id=inbox_id,
            message_id=message_id,
            text="This is a reply sent using the AgentMail Python SDK.",
            html="<p>This is a reply sent using the AgentMail Python SDK.</p>"
        )
        
        reply_id = getattr(reply, 'message_id', getattr(reply, 'id', 'N/A'))
        
        print(f"\n✓ Reply sent successfully!")
        print(f"Reply Message ID: {reply_id}")
        
        # Show additional details if available
        if hasattr(reply, 'model_dump'):
            details = reply.model_dump()
            print("\nAdditional details:")
            for key, value in details.items():
                if key not in ['message_id', 'id']:
                    print(f"  {key}: {value}")
            
    except Exception as e:
        print(f"Error replying to message: {e}")


if __name__ == "__main__":
    main()

