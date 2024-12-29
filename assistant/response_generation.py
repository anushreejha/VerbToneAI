from gtts import gTTS
import os

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")
