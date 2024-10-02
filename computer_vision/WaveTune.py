import cv2
import mediapipe as mp
import pyautogui
import math
import time
CAMERA_ID = 0
FLIP_IMAGE = True
VOLUME_CHANGE_COOLDOWN = 0.5
VOLUME_CHANGE_THRESHOLD = 50  
def main():
    cap = cv2.VideoCapture(CAMERA_ID)
    if not cap.isOpened():
        print(f"Error: Could not open camera with ID {CAMERA_ID}")
        return
    hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils
    last_volume_change_time = 0
    distance = 0  
    while True:
        success, image = cap.read()
        if not success:
            print("Failed to capture frame")
            break
        if FLIP_IMAGE:
            image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                thumb_tip = hand_landmarks.landmark[4]
                index_tip = hand_landmarks.landmark[8]
                x1, y1 = int(thumb_tip.x * image.shape[1]), int(thumb_tip.y * image.shape[0])
                x2, y2 = int(index_tip.x * image.shape[1]), int(index_tip.y * image.shape[0])
                cv2.circle(image, (x1, y1), 8, (0, 0, 255), -1)
                cv2.circle(image, (x2, y2), 8, (0, 255, 255), -1)
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                distance = math.hypot(x2 - x1, y2 - y1)
                current_time = time.time()
                if current_time - last_volume_change_time > VOLUME_CHANGE_COOLDOWN:
                    if distance > VOLUME_CHANGE_THRESHOLD:
                        pyautogui.press("volumeup")
                        print("Volume Up")
                    else: 
                        pyautogui.press("volumedown")
                        print("Volume Down")
                    last_volume_change_time = current_time
        cv2.putText(image, f"Distance: {int(distance)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("Hand Volume Control", image)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  
            print("Esc key pressed. Exiting...")
            break
        elif key == ord('q'):
            print("Q key pressed. Exiting...")
            break
    cap.release()
    cv2.destroyAllWindows()
    print("Program ended")
if __name__ == "__main__":
    main()