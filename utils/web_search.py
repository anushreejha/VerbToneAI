import webbrowser
from assistant.response_generation import speak

def google_search(query):
    speak("Searching on Google...")
    webbrowser.open(f"https://www.google.com/search?q={query}")
