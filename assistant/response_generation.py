from gtts import gTTS
import os

def speak(audio):
    """
    This function converts the text to speech, saves it as an MP3 file, and plays it using the system's default audio player.
    """
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")
