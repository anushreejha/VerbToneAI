import requests
from bs4 import BeautifulSoup
from assistant.response_generation import speak

def get_news():
    """
    This function web scrapes top news headlines from India Today's website, displays and gives speech output of the results.
    """
    speak("Fetching the latest news headlines from India Today...")
    try:
        response = requests.get("https://www.indiatoday.in/news.html")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        news_div = soup.find("div", class_="NewsList_newslist__1Bh2x newslist")
        if not news_div:
            raise ValueError("News container not found on the page.")
        
        headlines = news_div.find_all("a")
        for headline in headlines:
            text = headline.get_text(strip=True)  
            if text: 
                print(text)  
                speak(text)
    except Exception as e:
        speak("Sorry, there was an error fetching the news.")
        print(f"Error: {e}")
