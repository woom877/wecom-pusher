import json
import pusher
import processor
import crawler

# load config from file
config_path = "config.json"
with open(config_path, "r") as f:
    config = json.load(f)

url = config["webhook"]
sources = config["crawler"]["sources"]
api_key = config["openai"]["api_key"]
base_url = config["openai"]["base_url"]
model = config["openai"]["model"]
message = ""

for source in sources:
    feed = crawler.fetch_rss_feed(source)
    for entry in feed.entries:
        title = entry.title
        time = entry.published
        link = entry.link
        summary = entry.summary

        content = f"标题: {title}\n发布时间: {time}\n链接: {link}\n摘要: {summary}\n\n"
        
        message += content
# load config of OpenAI client
client = processor.load_config(
    api_key=api_key,
    base_url=base_url
)
message = processor.get_completion(client, model, message)

# push message to WeCom
response = pusher.push_message(url, message)

print(response.status_code)
print(response.text)