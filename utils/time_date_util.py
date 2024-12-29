from datetime import datetime
from assistant.response_generation import speak

def tell_time():
    """
    This function tells the current time.
    """
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")

def tell_day():
    """
    This function tells the current date.
    """
    current_day = datetime.now().strftime("%A")
    speak(f"Today is {current_day}.")
