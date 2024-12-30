from gtts import gTTS
import os
import pyttsx3

def speak(audio, offline=False):
    """
    Converts the input text to speech and plays it using the system's default audio player.

    This function supports both online and offline modes for text-to-speech conversion.
    In online mode, it uses the gTTS library, and in offline mode, it uses pyttsx3.

    Args:
        audio (str): The text to be converted into speech.
        offline (bool): Whether to use offline text-to-speech (default: False).

    Returns:
        None
    """
    if offline:
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()
    else:
        tts = gTTS(text=audio, lang='en')
        tts.save("output.mp3")

        # Play the generated speech output (audio file) using the system's default audio player
        os.system("afplay output.mp3")  # macOS
        # On Windows, use: os.system("start output.mp3")
        # On Linux, use: os.system("mpg321 output.mp3") or "aplay" (depending on the system)
