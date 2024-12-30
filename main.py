import speech_recognition as sr
from assistant.speech_recognition_module import listen_to_user
from assistant.intent_processing import process_query
from assistant.response_generation import speak


if __name__ == "__main__":
    """
    Main entry point of the program. Continuously listens for user input and processes queries.

    The program initializes the speech recognition system and enters a loop where it listens 
    for user commands, processes the commands, and provides responses via speech synthesis. 
    The loop continues indefinitely until an error occurs or the user exits.
    """
    r = sr.Recognizer()
    mic = sr.Microphone()

    # Welcome message
    speak("Hello! Welcome to VerbTone AI.")

    while True:
        try:
            # Listen for user input
            user_input = listen_to_user(r, mic)

            if user_input:
                print(f"\nUser said: {user_input}")
                # Process query based on user input
                process_query(user_input.lower())

        except Exception as e:
            # If any error occurs, speak the error message
            speak(f"An error occurred: {str(e)}")
            break
