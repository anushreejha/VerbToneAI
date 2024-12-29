import json
from assistant.response_generation import speak
from utils.web_search import google_search
from utils.weather import speak_weather
from utils.news_fetcher import timesofindia
from utils.time_date_util import tell_time, tell_day
from assistant.email_module import authenticate_and_send_email

# Load intents from the JSON file
with open("intents.json", "r") as f:
    INTENTS = json.load(f)

def process_query(query):
    query = query.lower()

    # Greetings and exit commands
    if any(word in query for word in INTENTS["greetings"]):
        speak("Hello! How may I help you today?")
        return
    elif any(word in query for word in INTENTS["exit"]):
        speak("Goodbye! Have a great day.")
        exit()

    # Specific commands
    if any(word in query for word in INTENTS["search"]):
        search_query = query.split("search", 1)[1].strip()
        google_search(search_query)
    elif any(word in query for word in INTENTS["weather"]):
        speak_weather()
    elif any(word in query for word in INTENTS["news"]):
        timesofindia()
    elif any(word in query for word in INTENTS["email"]):
        authenticate_and_send_email()
    elif any(word in query for word in INTENTS["time"]):
        tell_time()
    elif any(word in query for word in INTENTS["day"]):
        tell_day()
    else:
        speak("Sorry, I didn't understand that request.")
