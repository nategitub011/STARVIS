import os

class TarvisDisplayManager:
    def __init__(self):
        self.current_view = "HOME"

    def handle_context(self, user_input):
        user_input = user_input.lower()
        
        if "news" in user_input:
            self.current_view = "NEWS"
            self.display_news_feed()
        elif "skiing" in user_input or "weather" in user_input:
            self.current_view = "WEATHER"
            self.display_ski_report()
        elif "status" in user_input or "hailo" in user_input:
            self.current_view = "SYSTEM"
            self.display_system_vitals()
        else:
            self.display_default_face()

    def display_ski_report(self):
        print("[TARVIS]: Accessing weather satellites. Try not to get your hopes up.")
        # Logic to launch a browser or update the UI with weather data
        # os.system("chromium-browser --kiosk https://www.snow-forecast.com") 
        
    def display_news_feed(self):
        print("[TARVIS]: Scanning the headlines. It’s mostly chaos, as usual.")
        # Logic to display an RSS feed or news site
