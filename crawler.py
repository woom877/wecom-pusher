import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return feed