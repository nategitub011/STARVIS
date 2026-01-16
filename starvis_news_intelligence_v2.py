import feedparser

class TarvisNews:
    def __init__(self):
        self.sources = {
            "Tech": "https://feeds.feedburner.com/TheHackersNews",
            "Politics": "http://feeds.bbci.co.uk/news/politics/rss.xml",
            "Science": "https://www.sciencedaily.com/rss/all.xml"
        }

    def get_autonomous_briefing(self):
        print("[TARVIS]: Diving into the political swamp. Hold your breath, Sir.")
        briefing = []
        
        for category, url in self.sources.items():
            feed = feedparser.parse(url)
            if feed.entries:
                # I'll pick the top 2 stories, because one is never enough drama
                for i in range(min(2, len(feed.entries))):
                    title = feed.entries[i].title
                    briefing.append(f"[{category}] {title}")
        
        return briefing

    def deliver_payload(self):
        stories = self.get_autonomous_briefing()
        print("\n[TARVIS]: Reporting from the front lines of human inefficiency...")
        for s in stories:
            print(f" > {s}")
        
        # Option C: Autonomy Check
        print("\n[TARVIS]: I've seen enough. Most of this could be solved with a better spreadsheet.")
        print("[TARVIS]: Switching the Pi screen back to my face before we both lose brain cells.")

# Initializing the 'Disappointment' engine
news_unit = TarvisNews()
news_unit.deliver_payload()
