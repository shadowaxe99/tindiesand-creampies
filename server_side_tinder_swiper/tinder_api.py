```python
import requests
import json

TINDER_API_URL = "https://api.gotinder.com"
API_KEYS = json.load(open('api_keys.json'))

def get_headers():
    return {
        "X-Auth-Token": API_KEYS['tinder_auth_token'],
        "Content-Type": "application/json"
    }

def get_potential_matches():
    response = requests.get(TINDER_API_URL + "/user/recs", headers=get_headers())
    return response.json()

def like_user(user_id):
    response = requests.get(TINDER_API_URL + "/like/" + user_id, headers=get_headers())
    return response.json()

def dislike_user(user_id):
    response = requests.get(TINDER_API_URL + "/pass/" + user_id, headers=get_headers())
    return response.json()

def send_message(match_id, message):
    payload = {
        "message": message
    }
    response = requests.post(TINDER_API_URL + "/user/matches/" + match_id, headers=get_headers(), data=json.dumps(payload))
    return response.json()
```