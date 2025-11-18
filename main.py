import requests
import json

# Read webhook URL from file
with open("webhook.txt", "r") as file:
    url = file.read().strip()

headers = {
    "Content-Type": "application/json"
}

data = {
    "msgtype": "text",
    "text": {
        "content": "test file read"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.text)