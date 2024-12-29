import speech_recognition as sr
from assistant.speech_recognition_module import listen_to_user
from assistant.intent_processing import process_query
from assistant.response_generation import speak

if __name__ == "__main__":
    r = sr.Recognizer()
    mic = sr.Microphone()
    speak("Hello! How may I assist you?")

    while True:
        try:
            user_input = listen_to_user(r, mic)
            if user_input:
                print(f"User said: {user_input}")
                process_query(user_input.lower())
        except Exception as e:
            speak(f"An error occurred: {str(e)}")
            break
