import webbrowser
from assistant.response_generation import speak


def google_search(query):
    """
    Opens a Google search for the specified query in the web browser.

    Args:
        query (str): The search query to be sent to Google.

    Returns:
        None: This function only opens the search results in the browser.
    """
    speak("Searching on Google...")
    
    webbrowser.open(f"https://www.google.com/search?q={query}")
