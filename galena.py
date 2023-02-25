import speech_recognition as sr 
import pyaudio 
import pyttsx3 
import webbrowser 
import datetime
import time
import calendar
import requests
from bs4 import BeautifulSoup
import wikipedia as wp
import pywhatkit as kt
import ecapture as ecap

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r = sr.Recognizer()
my_mic = sr.Microphone(device_index=0)
with my_mic as source:
    speak("Hello! I am Galena, your voice assistant. How may I help you?")
    r.adjust_for_ambient_noise(source) 
    audio = r.listen(source) 
try: 
        print("I heard: ")
        print(r.recognize_google(audio)) 
        task = r.recognize_google(audio)
except:
        r = sr.Recognizer()
        my_mic = sr.Microphone(device_index=0)
        with my_mic as source:
                speak("I'm sorry, I did not understand. Please can you repeat what you said?")
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source) 
        try: 
                print("I heard: ")
                print(r.recognize_google(audio)) 
                task = r.recognize_google(audio)
        except:
                speak("I'm sorry, I did not understand. Please re-run the program and try again.")

def tell_time():
    current_time = time.strftime("%I:%M %p")
    speak("The current time is")
    speak(current_time)
 
def tell_date():
    d = datetime.datetime.now()
    day = d.day
    m = d.month
    year = d.year
    month = calendar.month_name[m]
    speak("Today is")
    speak(month)
    speak(day)
    speak(year)
    
def timesofindia():
    url = "https://timesofindia.indiatimes.com/india/timestopten.cms"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")

    headlines = soup.find('div').find_all('a', {'class': 'news_title'})
    for x in headlines:
        speak(x.text.strip())
        
def wikipedia():
        query = "wiki"
        speak(wp.search(wiki), results = 15)
        
def googlesearch():
        target = look_for
        result = kt.search(target)
        speak(result)
                
while(1):
        if 'Google' in task:
                r = sr.Recognizer()
                my_mic = sr.Microphone(device_index=0)
                with my_mic as source:
                        speak("Sure. What would you like me to search on Google?")
                        r.adjust_for_ambient_noise(source) 
                        audio = r.listen(source) 
                try: 
                        print("I heard: ")
                        print(r.recognize_google(audio)) 
                        look_for = r.recognize_google(audio)
                        speak("Searching on Google. The results are:")
                        googlesearch()
                except:
                        r = sr.Recognizer()
                        my_mic = sr.Microphone(device_index=0)
                        with my_mic as source:
                                speak("I'm sorry, I did not understand. Please can you repeat what you said?")
                                r.adjust_for_ambient_noise(source) 
                                audio = r.listen(source) 
                        try: 
                                print("I heard: ")
                                print(r.recognize_google(audio)) 
                                look_for = r.recognize_google(audio)
                                speak("Searching on Google. The results are:")
                                googlesearch()
                        except:
                                speak("I'm sorry, I did not understand. Please re-run the program and try again.")
        elif 'open YouTube' in task:
                speak("Opening YouTube in your browser.")
                webbrowser.open("youtube.com")
        elif 'open Gmail' in task:
                speak("Opening Gmail in your browser.")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'time' in task:
                tell_time()
        elif 'date' in task:
                tell_date()
        elif 'news' in task:
                speak("Sure. These are the top 10 news headlines from Times of India.")
                timesofindia()
        elif 'Wikipedia' in task:
                r = sr.Recognizer()
                my_mic = sr.Microphone(device_index=0)
                with my_mic as source:
                        speak("Sure. What would you like me to search on wikipedia?")
                        r.adjust_for_ambient_noise(source) 
                        audio = r.listen(source) 
                try: 
                        print("I heard: ")
                        print(r.recognize_google(audio)) 
                        wiki = r.recognize_google(audio)
                        speak("Searching on Wikipedia. The results are:")
                        wikipedia()
                except:
                        r = sr.Recognizer()
                        my_mic = sr.Microphone(device_index=0)
                        with my_mic as source:
                                speak("I'm sorry, I did not understand. Please can you repeat what you said?")
                                r.adjust_for_ambient_noise(source) 
                                audio = r.listen(source) 
                        try: 
                                print("I heard: ")
                                print(r.recognize_google(audio)) 
                                wiki = r.recognize_google(audio)
                                speak("Searching on Wikipedia. The results are:")
                                wikipedia()
                        except:
                                speak("I'm sorry, I did not understand. Please re-run the program and try again.")
        elif 'can you' or 'do' in task:
                speak("I can tell you the time and date, search on Google and Wikipedia, open YouTube and Gmail, tell you the news from Times of India and click a photograph. If there is anything else you want me to do, please reach out to my creator. Here is the link to her GitHub profile repository.")
                print("https://github.com/anushreejha/Galena_The-Voice-Assistant.git")
        elif 'bye' or 'later' in task:
                speak("Bye! I hope you have a good day!")
                exit()
        elif 'capture' or 'photo' in task:
                speak("Sure! Capturing a photo. Smile please!")
                ecap.capture(0,"capture", "image.jpg")
                continue 
        else:
                speak("I'm sorry, I am not programmed to do that. Please try something else.")
        r = sr.Recognizer()
        my_mic = sr.Microphone(device_index=0)
        with my_mic as source:
                speak("What would you like me to do next?")
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source) 
        try: 
                print("I heard: ")
                print(r.recognize_google(audio)) 
                task = r.recognize_google(audio)
        except:
                r = sr.Recognizer()
                my_mic = sr.Microphone(device_index=0)
                with my_mic as source:
                        speak("I'm sorry, I did not understand. Please can you repeat what you would like me to do next?")
                        r.adjust_for_ambient_noise(source) 
                        audio = r.listen(source) 
                try: 
                        print("I heard: ")
                        print(r.recognize_google(audio)) 
                        task = r.recognize_google(audio)
                except:
                        speak("I'm sorry, I did not understand. Please re-run the program and try again.")