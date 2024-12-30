import json
from assistant.response_generation import speak
from utils.web_search import google_search
from utils.weather import speak_weather
from utils.news_fetcher import get_news
from utils.time_date_util import tell_time, tell_day, tell_date
from assistant.email_module import send_email
from assistant.general_processing import process_with_local_nlp

# Load intents
with open("intents.json", "r") as f:
    INTENTS = json.load(f)

def process_query(query):
    """
    Processes the user's spoken query and triggers the appropriate response.

    This function combines JSON-based intent matching with ML-powered intent classification.

    Args:
        None
    
    Returns:
        None
    """
    query = query.lower()

    # Check for JSON-based intent matches
    if any(word in query for word in INTENTS["greetings"]):
        speak("Hello! How may I help you today?")

    elif any(word in query for word in INTENTS["exit"]):
        speak("Goodbye! Have a great day.")
        exit()

    elif any(word in query for word in INTENTS["search"]):
        search_query = query.split("search", 1)[1].strip()
        google_search(search_query)
 
    elif any(word in query for word in INTENTS["weather"]):
        speak_weather()
        
    elif any(word in query for word in INTENTS["news"]):
        get_news()

    elif any(word in query for word in INTENTS["email"]):
        speak("Please enter the details.")
        sender_email = input("\nEnter sender's email address: \n")
        subject = input("\nEnter the subject: \n")
        message = input("\nEnter the message: \n")
        send_email(sender_email, subject, message)

    elif any(word in query for word in INTENTS["time"]):
        tell_time()

    elif any(word in query for word in INTENTS["day"]):
        tell_day()

    elif any(word in query for word in INTENTS["date"]):
        tell_date()

    else:
        # Handle general queries with GPT-2
        speak("Let me think...")
        nlp_response = process_with_local_nlp(query)
        speak(nlp_response)