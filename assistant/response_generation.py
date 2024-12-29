from gtts import gTTS
import os

def speak(audio):
    """
    This function converts the provided text (audio) to speech, saves it as an MP3 file and plays the audio using the default system player.
    """
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")
