import webbrowser
from assistant.response_generation import speak

def google_search(query):
    """
    This function displays the Google search results for input query in browser.
    """
    speak("Searching on Google...")
    webbrowser.open(f"https://www.google.com/search?q={query}")
