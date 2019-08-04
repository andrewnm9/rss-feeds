import feedparser

feed = feedparser.parse('https://feeds.a.dj.com/rss/RSSWSJD.xml')

for entry in feed.entries:
    print('Date: {0}\nTitle: {1}\nSummary: {2}\n'.format(entry.published, entry.title, entry.summary))
