import requests
import json

def push_message(url, message):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "msgtype": "text",
        "text": {
            "content": f"{message}"
        }
    }

    return requests.post(url, headers=headers, data=json.dumps(data))