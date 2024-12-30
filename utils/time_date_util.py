from datetime import datetime
from assistant.response_generation import speak


def tell_time():
    """
    Retrieves the current time from the system and reads it aloud in a 12-hour format.

    Args:
        None

    Returns:
        None: This function doesn't return anything, it only tells the time.
    """
    current_time = datetime.now().strftime("%I:%M %p")  # Format: 12-hour format (e.g., 07:45 PM)
    speak(f"The current time is {current_time}.")


def tell_day():
    """
    Retrieves the current day of the week and reads it aloud.

    Args:
        None

    Returns:
        None: This function doesn't return anything, it only tells the day.
    """
    current_day = datetime.now().strftime("%A")  # Format: Full weekday name 
    speak(f"Today is {current_day}.")


def tell_date():
    """
    Retrieves the current date in the format "Month Day, Year" and speaks it aloud.

    Args:
        None

    Returns:
        None: This function doesn't return anything, it only tells the date.
    """
    current_date = datetime.now().strftime("%B %d, %Y")  # Format: Month Day, Year
    speak(f"Today is {current_date}.")
