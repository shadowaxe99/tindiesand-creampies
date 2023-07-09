```python
import requests
from utils import log, error_handler, format_message
from tinder_api import send_message

def send_initial_message(match_id, message):
    try:
        formatted_message = format_message(message)
        response = send_message(match_id, formatted_message)
        if response.status_code == 200:
            log(f"Message sent to match {match_id}")
        else:
            error_handler(f"Failed to send message to match {match_id}. Status code: {response.status_code}")
    except Exception as e:
        error_handler(f"Error occurred while sending message to match {match_id}: {str(e)}")

def send_messages_to_matches(matches, message):
    for match in matches:
        send_initial_message(match['id'], message)
```