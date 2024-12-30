from gtts import gTTS
import os


def speak(audio):
    """
    Converts the input text to speech and plays it using the system's default audio player.

    This function uses the gTTS library to convert the provided text into an MP3 file, 
    then plays the file using the system's default audio player.

    Args:
        audio (str): The text to be converted into speech.

    Returns:
        None
    """
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")

    # Play the generated speech output (audio file) using the system's default audio player
    os.system("afplay output.mp3")

    # Platform-specific audio play commands:
    # 'afplay' is for macOS.
    # On Windows, use: os.system("start output.mp3")
    # On Linux, use: os.system("mpg321 output.mp3") or "aplay" (depending on the system)
