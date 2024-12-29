import requests
from bs4 import BeautifulSoup
from assistant.response_generation import speak

def timesofindia():
    speak("Fetching the latest news headlines...")
    url = "https://timesofindia.indiatimes.com/home/headlines"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all('a', {'class': 'w_img'})

        count = 0
        for headline in headlines:
            speak(headline.text.strip())
            count += 1
            if count == 5:  # Fetch only top 5 headlines
                break
    else:
        speak("Sorry, I couldn't fetch the news at the moment.")
