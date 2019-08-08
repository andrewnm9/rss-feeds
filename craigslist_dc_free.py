import feedparser

feed = feedparser.parse('https://washingtondc.craigslist.org/d/free-stuff/search/zip?format=rss')

for entry in feed.entries:
    print('Date: {0}\nTitle: {1}\nSummary: {2}\n'.format(entry.published, entry.title, entry.summary))
