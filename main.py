import requests
import json
import pusher

# Read webhook URL from file
with open("webhook.txt", "r") as file:
    url = file.read().strip()

# message to send
message = "test file read"

response = pusher.push_message(url, message)

print(response.status_code)
print(response.text)