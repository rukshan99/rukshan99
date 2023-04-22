import feedparser

rss_url = f"https://stackoverflow.com/feeds/user/14143312"

# Fetch the RSS feed and extract the latest answers
feed = feedparser.parse(rss_url)
latest_answers = feed.entries[:5]  # Get the 5 latest answers

# Generate the markdown content for the profile readme
content = "### Latest Stack Overflow Answers\n\n"
for answer in latest_answers:
    content += f"* [{answer.title}]({answer.link})\n"

# Write the content to the readme file
with open("README.md", "w") as f:
    f.write(content)