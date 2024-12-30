import speech_recognition as sr
from assistant.response_generation import speak


def listen_to_user(recognizer, microphone, timeout=10, pause_threshold=1.0):
    """
    Listens for user speech via the microphone and returns the recognized text.

    This function captures audio input from the user and uses Google's speech recognition API
    to transcribe the speech into text. If an error occurs during listening or recognition, 
    an appropriate response message is spoken.

    Args:
        recognizer (sr.Recognizer): The speech recognizer object to process the audio.
        microphone (sr.Microphone): The microphone object to capture the user's speech.
        timeout (int, optional): The time to wait for speech before raising an exception. Default is 10 seconds.
        pause_threshold (float, optional): The amount of silence (in seconds) to wait before considering the speech finished. Default is 1 second.

    Returns:
        str: The recognized text from the user's speech, or None if no input was recognized.
    """
    # Adjust threshold for sensitivity (background noise)
    recognizer.energy_threshold = 300
    recognizer.pause_threshold = pause_threshold

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("What can I help you with?")

        try:
            # Listen to the user's input and process the audio
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
