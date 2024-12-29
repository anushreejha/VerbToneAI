import speech_recognition as sr
from assistant.response_generation import speak

def listen_to_user(recognizer, microphone, timeout=10, pause_threshold=1.0):
    """
    This function listens to the user via the microphone and returns the recognized text.
    """
    # Adjust threshold for sensitivity (backgound noise)
    recognizer.energy_threshold = 300 
    recognizer.pause_threshold = pause_threshold

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("What can I help you with?")
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
