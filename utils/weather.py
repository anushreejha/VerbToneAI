import requests
from bs4 import BeautifulSoup
from assistant.response_generation import speak

def get_weather(city):
    """
    Fetches weather data for the specified city by scraping the AccuWeather website.

    Parameters:
        city (str): Name of the city to get the weather for.

    Returns:
        str: A string with the weather information (temperature, conditions, etc.).
    """
    # Search URL for the city's weather on AccuWeather
    url = f"https://www.accuweather.com/en/search-locations?query={city}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Sorry, I couldn't retrieve weather details right now."

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Search for the first result (city weather page link)
    city_url = soup.find('a', class_='search-result')  # You may need to inspect the page for correct class
    if not city_url:
        return "Sorry, I couldn't find the city you mentioned."

    # Construct the full URL for the city's weather page
    city_weather_url = "https://www.accuweather.com" + city_url['href']
    weather_response = requests.get(city_weather_url)

    if weather_response.status_code != 200:
        return "Sorry, I couldn't retrieve the detailed weather information."

    # Parse the city weather page
    weather_soup = BeautifulSoup(weather_response.text, 'html.parser')

    # Extract weather details like temperature and condition
    try:
        temperature = weather_soup.find('span', class_='temp').text.strip()
        condition = weather_soup.find('div', class_='phrase').text.strip()
        weather_info = f"The current temperature in {city} is {temperature} with {condition}."
    except AttributeError:
        weather_info = "Sorry, I couldn't retrieve the weather details."

    return weather_info

def speak_weather():
    """
    Asks the user for their city and speaks the current weather.
    """
    speak("Please enter your city.")
    city = input("Enter city: ")
    weather_info = get_weather(city)
    speak(weather_info)
