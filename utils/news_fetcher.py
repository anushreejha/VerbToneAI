import requests
from bs4 import BeautifulSoup
from assistant.response_generation import speak


def get_news():
    """
    Web scrapes top news headlines from India Today's website, displays and reads them aloud
    
    Args: 
        None
    
    Returns:
        None: This function only tells the top news headlines.

    Raises:
        ValueError: If the news container element is not found on the page.
        requests.exceptions.RequestException: If there is an issue with the web request.
        Any other exception: If any error occurs during scraping or speech output process.
    """
    speak("Fetching the latest news headlines from India Today...")

    try:
        # Fetch the web page content
        response = requests.get("https://www.indiatoday.in/news.html")
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the div element containing the news headlines
        news_div = soup.find("div", class_="NewsList_newslist__1Bh2x newslist")
        if not news_div:
            raise ValueError("News container not found on the page.")
        
        # Extract all headlines from the news div
        headlines = news_div.find_all("a")
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:
                print(text)
                speak(text)

    except Exception as e:
        # Handle any errors that occur during the scraping or speaking 
        speak("Sorry, there was an error fetching the news.")
        print(f"Error: {e}")
