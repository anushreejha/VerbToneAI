import speech_recognition as sr
from assistant.speech_recognition_module import listen_for_wake_word, listen_to_user
from assistant.intent_processing import process_query
from assistant.response_generation import speak
from assistant.emotion_detection import detect_emotion
import time

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Welcome the user and detect emotion once
    speak("Hello! Welcome to VerbTone AI.")
    emotion = detect_emotion()
    if emotion == "happy":
        speak("You look happy! Let's get started.")
    elif emotion == "angry":
        speak("I sense some frustration. I'm here to help.")
    elif emotion == "sad":
        speak("You seem a bit down. Let me know how I can assist.")
    else:
        speak("I'm ready to help when you need me.")

    # Wait for the wakeword
    print("\nListening for wakeword..")
    while True:
        if listen_for_wake_word():
            speak("How can I assist you?")
            break

    # Enter query processing loop
    while True:
        try:
            user_input = listen_to_user(recognizer, microphone)
            if user_input:
                print(f"User said: {user_input}")
                process_query(user_input.lower())

                # Ask for the next query or wait for inactivity
                speak("What else can I help you with?")
                start_time = time.time()

                while True:
                    user_input = listen_to_user(recognizer, microphone, timeout=15)
                    if user_input:
                        print(f"User said: {user_input}")
                        process_query(user_input.lower())
                        speak("Anything else?")
                        start_time = time.time()  # Reset inactivity timer
                    elif time.time() - start_time > 30:  # Check inactivity
                        speak("It seems you've been inactive. Say a wake word to activate me again.")
                        if listen_for_wake_word():
                            speak("How can I assist you?")
                            start_time = time.time()
                        else:
                            break
        except Exception as e:
            speak(f"An error occurred: {str(e)}")
            break

if __name__ == "__main__":
    main()
