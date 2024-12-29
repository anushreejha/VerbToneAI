from datetime import datetime
from assistant.response_generation import speak

def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")

def tell_day():
    current_day = datetime.now().strftime("%A")
    speak(f"Today is {current_day}.")
