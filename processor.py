from openai import OpenAI

def load_config(api_key, base_url):
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    return client

def get_completion(client, model, message):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个网络安全专家，精通信息安全领域的最新动态。请根据用户提供的内容，生成简洁明了的摘要，突出关键信息和重要细节，确保信息正确。"},
            {"role": "user", "content": f"这是我收集到的最新网络安全资讯，请帮我整理和筛选这其中最有用最重要的安全相关的咨询，按照威胁等级排序，并且去重,选出其中最重要的两个紧急+两个高危+一个中危，最后按照整齐一致的格式输出，并在每条消息后面附上相应的链接，格式按照“总结+文章标题+文章发表时间+文章链接”，只要最近的一天之内的，一定要确保文章的标题和发布时间跟我给你的完全一样，时间格式采用北京时间：\n\n{message}"}
        ]
    )
    return completion.choices[0].message.content