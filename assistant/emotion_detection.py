from fer import FER
import cv2
from assistant.response_generation import speak

def detect_emotion():
    """
    Captures a single frame from the video feed, detects the emotion of the first detected face, 
    and returns the most prominent emotion. The video feed is automatically closed after capturing.
    
    Args:
        None

    Returns:
        str: The detected emotion as a string, or None if no face or emotion is detected.
    """
    # Initialize webcam
    video_capture = cv2.VideoCapture(0)
    emotion_detector = FER(mtcnn=True)
    detected_emotion = None

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame from webcam.")
            break

        # Detect emotions
        emotions = emotion_detector.detect_emotions(frame)
        if emotions:
            # Get the first detected face's emotions
            primary_emotion = max(emotions[0]["emotions"], key=emotions[0]["emotions"].get)
            detected_emotion = primary_emotion
            print(f"Detected emotion: {primary_emotion}")
            break  # Stop processing after the first detection

        # Display video feed with a basic overlay
        cv2.imshow("Emotion Detection - Press Q to exit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

    return detected_emotion



