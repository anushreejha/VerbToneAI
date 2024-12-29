import speech_recognition as sr
from assistant.response_generation import speak

def listen_to_user(r, mic):
    with mic as source:
        speak("I'm listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
    except sr.RequestError:
        speak("I'm having trouble connecting to the speech service.")



import speech_recognition as sr
from assistant.response_generation import speak

def listen_to_user(recognizer, microphone, timeout=12, pause_threshold=2.0):
    """
    Listens to the user via the microphone and returns the recognized text.

    Parameters:
        recognizer (sr.Recognizer): Recognizer object for speech recognition.
        microphone (sr.Microphone): Microphone object for input.
        timeout (int): Maximum number of seconds to wait for speech.
        pause_threshold (float): Adjusts how quickly the recognizer considers speech to be complete.

    Returns:
        str: Recognized text from the user's speech.
    """
    # Adjust recognizer's energy threshold and pause threshold for better sensitivity
    recognizer.energy_threshold = 300  # Adjust to a level suitable for your environment
    recognizer.pause_threshold = pause_threshold

    with microphone as source:
        # Allow the recognizer to adjust to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("Listening... Please speak now.")
        try:
            # Listen for speech with the specified timeout
            audio = recognizer.listen(source, timeout=timeout)
            user_input = recognizer.recognize_google(audio)
            return user_input
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
        except sr.RequestError as e:
            speak(f"Sorry, I couldn't process your speech. Error: {e}")

    return None
