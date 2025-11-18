import requests
import json
import pusher

# read webhook URL from file
with open("webhook.txt", "r") as file:
    url = file.read().strip()

# read the every line of rss.txt
with open("rss.txt", "r") as file:
    rss = file.readlines()

# message to send
message = "test file read"

response = pusher.push_message(url, message)

print(response.status_code)
print(response.text)