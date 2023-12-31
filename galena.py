import speech_recognition as sr
from transformers import pipeline
import webbrowser
import datetime
from gtts import gTTS
import os
import subprocess
import platform
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")  

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
os.environ['CREDS_FILE'] = '/Users/anushreejha/Desktop/Programming/pythonProj/galena/creds.json'

def create_message(sender, to, subject, message_text):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg)
    return {'raw': message.as_string()}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except Exception as e:
        print('An error occurred: %s' % e)
        return None
    
def authenticate_and_send_email():
    creds = None
    token_path = 'token.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds_file = os.environ.get('CREDS_FILE')
            if creds_file is None:
                raise ValueError("CREDS_FILE environment variable not set")
            else:
                flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
                creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    sender_email = input("Please enter your email address: ")
    receiver_email = input("Please enter the receiver's email address: ")
    subject = input("Please enter the email subject: ")
    body = input("Please enter the email body: ")
    message = create_message(sender_email, receiver_email, subject, body)
    send_message(service, 'me', message)

def open_app(app_name):
    system = platform.system().lower()
    if system == "windows":
        subprocess.Popen(f'explorer shell:appsFolder\\{app_name}')
    elif system == "darwin":
        subprocess.Popen(["/usr/bin/open", "-n", f"/Applications/{app_name}.app"])
    elif system == "linux":
        subprocess.Popen([f"/usr/bin/{app_name}"])
    else:
        speak("Sorry, I cannot open apps on your operating system.")

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_day():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    speak(f"Today is {day}")

def google_search(query):
    speak("Searching on Google")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def timesofindia():
    try:
        url = "https://timesofindia.indiatimes.com/india/timestopten.cms"
        page_request = requests.get(url)
        data = page_request.content
        soup = BeautifulSoup(data, "html.parser")
        headlines = soup.find('div').find_all('a', {'class': 'news_title'})
        for x in headlines:
            speak(x.text.strip())
    except Exception as e:
        speak("Apologies, I'm encountering issues fetching the news at the moment. Please try again later.")

def get_weather(city):
    url = f"https://www.accuweather.com/en/search-locations?query={city}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        location_link = soup.find("a", class_="search-results-item")["href"]
        location_url = f"https://www.accuweather.com{location_link}"
        
        location_response = requests.get(location_url)
        if location_response.status_code == 200:
            location_soup = BeautifulSoup(location_response.content, "html.parser")
            temperature = location_soup.find("div", class_="display-temp").get_text()
            condition = location_soup.find("div", class_="phrase").get_text()
            
            weather_info = f"The weather in {city} is {condition} with a temperature of {temperature}."
            return weather_info
        else:
            return "Unable to fetch weather information for the specified city."
    else:
        return "City not found. Please try another city."

def speak_weather():
    speak("Please enter your city")
    city_input = input("Enter city: ")
    weather_info = get_weather(city_input)
    if weather_info:
        print(weather_info)
        tts = gTTS(text=weather_info, lang='en')
        tts.save("output.mp3")
        os.system("afplay output.mp3")  
    else:
        print("Weather information not available.")

def bye():
    speak("Goodbye! Have a nice day!")
    exit(0)

nlp = pipeline("sentiment-analysis")

def process_query(query):
    if "open" in query:
        app_name = query.split("open", 1)[1].strip()
        open_app(app_name)
        speak("App opened")
    elif "email" or "mail" in query:
        authenticate_and_send_email()
        speak("Email sent successfully!")
    elif "time" in query:
        tell_time()
    elif "day" in query:
        tell_day()
    elif "search" in query:
        search_query = query.split("search", 1)[1].strip()  
        google_search(search_query)
    elif "news" or "top10" in query:
        speak("Sure. Here are the top10 headlines from Times of India")
        timesofindia()
    elif "weather" or "temperature" in query:
        speak("Sure")
        speak_weather()
    elif "bye" or "exit" in query:
        bye()
    else:
        speak("Sorry, I cannot handle that request.")

r = sr.Recognizer()
mic = sr.Microphone()

def ask_anything_else():
    with mic as source:
        speak("Is there anything else I can help you with?")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio)
        return user_input.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        speak("Sorry, there was an error processing your request.")

speak("Hello! How may I help you?")

while True:
    attempts = 0
    while attempts < 2:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio)
            print(f"\nRecognized: {user_input}")  
            process_query(user_input.lower())
            response = ask_anything_else()
            if "bye" in response or "no" in response:
                speak("Goodbye!")
                break
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said. Can you repeat?")
        except sr.RequestError:
            speak("Sorry, there was an error processing your request.")
        attempts += 1

    if attempts == 2:
        response = ask_anything_else()
        if "bye" in response or "no" in response:
            bye()
            break
