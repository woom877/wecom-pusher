import json
import pusher
import processor

# load config from file
config_path = "config.json"
with open(config_path, "r") as f:
    config = json.load(f)

url = config["webhook"]
sources = config["crawler"]["sources"]

# load config of OpenAI client
completion = processor.load_config(
    api_key=config["openai"]["api_key"],
    base_url=config["openai"]["base_url"],
    model=config["openai"]["model"]
)

message = processor.get_completion(completion)

# push message to WeCom
response = pusher.push_message(url, message)

print(response.status_code)
print(response.text)