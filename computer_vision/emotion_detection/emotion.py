import cv2
import numpy as np
import dlib
from deepface import DeepFace
from PIL import Image
from collections import deque

# Load Dlib's face detector (more accurate than OpenCV Haar Cascade)
detector = dlib.get_frontal_face_detector()

# Load the webcam
cap = cv2.VideoCapture(0)

# Maintain a buffer of last N predictions for smoothing
emotion_queue = deque(maxlen=5)

# Load emoji images (ensure these exist in the same directory)
emoji_dict = {
    "happy": "happy_emoji.jpeg",
    "sad": "sad_emoji.webp",
    "angry": "angry_emoji.jpg",
    "surprise": "surprise_emoji.png",
    "neutral": "neutral_emoji.webp"
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for better face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using Dlib
    faces = detector(gray)

    if faces:
        # Use DeepFace to analyze the face in the frame
        try:
            analysis = DeepFace.analyze(
                frame, 
                actions=['emotion'], 
                enforce_detection=False  # ✅ FIXED: Removed 'model_name'
            )
            detected_emotion = analysis[0]['dominant_emotion']

            # Add the latest emotion to the queue
            emotion_queue.append(detected_emotion)

            # Get the most common emotion from the last few frames (smoothing)
            if len(emotion_queue) > 2:
                detected_emotion = max(set(emotion_queue), key=emotion_queue.count)

            # Load corresponding emoji
            emoji_path = emoji_dict.get(detected_emotion, "neutral_emoji.png")
            emoji = Image.open(emoji_path).resize((100, 100))

            # Convert OpenCV frame to PIL image for overlay
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            frame_pil.paste(emoji, (50, 50), emoji)

            # Convert back to OpenCV format
            frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

            # Display detected emotion text
            cv2.putText(frame, detected_emotion.capitalize(), (50, 180),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        except Exception as e:
            print("Error:", e)

    # Show the processed frame
    cv2.imshow("Live Emoji Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()