import speech_recognition as sr
from transformers import pipeline
import webbrowser
import datetime
from gtts import gTTS
import os
import subprocess
import platform

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")  # Adjust this command (based on your OS) for playing the audio

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

def bye():
    speak("Goodbye! Have a nice day!")
    exit(0)

nlp = pipeline("sentiment-analysis")

def process_query(query):
    if "open" in query:
        app_name = query.split("open", 1)[1].strip()
        open_app(app_name)
        speak("App opened")
    elif "time" in query:
        tell_time()
    elif "day" in query:
        tell_day()
    elif "search" in query:
        search_query = query.split("search", 1)[1].strip()  
        google_search(search_query)
    elif "bye" or "end" in query:
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
