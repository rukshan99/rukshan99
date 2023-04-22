import feedparser

rss_url = f"https://stackoverflow.com/feeds/user/14143312"

# Fetch the RSS feed and save it to a file
feed = feedparser.parse(rss_url)
with open("rss.xml", "w") as f:
    f.write(feed.to_xml())