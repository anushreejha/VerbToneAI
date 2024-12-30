import requests
import os
from dotenv import load_dotenv
from assistant.response_generation import speak


def get_weather(city):
    """
    Fetches the current weather information for a specified city from the WeatherAPI.

    This function retrieves weather data (temperature, condition, humidity, and
    feels-like temperature) for the specified city. It handles exceptions if there is an error 
    during the API request or data parsing.

    Args:
        city (str): The name of the city for which the weather data is to be fetched.

    Returns:
        weather_info (str): A string containing the current weather information for the city.

    Raises:
        Exception: If an error occurs during the API request or data retrieval.
    """
    load_dotenv()
    
    # Retrieve the weather API key from the environment variable
    key = os.getenv("WEATHER_API_KEY")
    
    # WeatherAPI endpoint for current weather, replace with '/forecast.json' for predictions
    url = 'http://api.weatherapi.com/v1/current.json'
    
    query = {
        "key": key,  
        "q": city
    }

    try:
        response = requests.get(url, params=query)
        response.raise_for_status()  
        
        data = response.json()
        
        # Extract weather details from the response
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        feelslike_c = data['current']['feelslike_c']
        
        weather_info = (f"The current temperature in {city} is {temp_c}°C. "
                        f"The weather condition is '{condition}'. "
                        f"Humidity is {humidity}%. "
                        f"It feels like {feelslike_c}°C.")

        return weather_info

    except Exception as e:
        speak("An error occurred. Please try again later.")
        print(f"Error occurred: {e}")
        return None


def speak_weather():
    """
    Prompts the user to enter a city name and then fetches and speaks the current weather.

    This function asks the user for their city, retrieves the weather information for that city 
    using the `get_weather()` function, and then speaks the weather information aloud.

    Args:
        None

    Returns:
        None
    """
    speak("Please enter your city.")
    city = input("Enter city: ")
    weather_info = get_weather(city)
    
    if weather_info:
        speak(weather_info)
    else:
        speak("Sorry, I could not fetch the weather information.")
