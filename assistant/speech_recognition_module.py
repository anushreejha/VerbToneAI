import speech_recognition as sr
import re
from assistant.response_generation import speak

def listen_for_wake_word():
    """
    Listens for a set of predefined wake words in the user's speech input and activates the assistant when detected.
    It processes the user's query immediately if a wake word is detected.

    Returns:
        str: The user's query if a wake word is detected, None otherwise.
    """
    wake_words = ["hi", "hello", "hey", "verbtone", "hey verbtone", "verbtone ai", "listen", "ai", "assistant"]

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for a wake word...")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio).lower()
            print(f"User said: {user_input}")

            # Check if any wake word matches
            if any(re.search(rf"\b{re.escape(word)}\b", user_input) for word in wake_words):
                print("Wake word detected! Activating assistant.")
                speak("I'm listening. What can I help you with?")
                return user_input  # Return user's query for processing request

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("Speech recognition service unavailable.")
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period.")

    return None

def listen_to_user(recognizer, microphone, timeout=10, pause_threshold=1.0):
    """
    Listens for user speech via the microphone and returns the recognized text.

    Args:
        recognizer (sr.Recognizer): The speech recognizer object to process the audio.
        microphone (sr.Microphone): The microphone object to capture the user's speech.
        timeout (int, optional): The time to wait for speech before raising an exception. Default is 10 seconds.
        pause_threshold (float, optional): The amount of silence (in seconds) to wait before considering the speech finished. Default is 1 second.

    Returns:
        str: The recognized text from the user's speech, or None if no input was recognized.
    """
    recognizer.energy_threshold = 300
    recognizer.pause_threshold = pause_threshold

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            user_input = recognizer.recognize_google(audio)
            return user_input
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please give me a moment before you can repeat that.")
        except sr.RequestError as e:
            speak(f"Sorry, I couldn't process your speech. Error: {e}")

    return None
