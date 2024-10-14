import cv2
import mediapipe as mp
import time

def resize_image(img, max_width=1000, max_height=800):
    """Resizes the image while maintaining aspect ratio."""
    height, width, _ = img.shape
    scale = min(max_width / width, max_height / height)
    return cv2.resize(img, None, fx=scale, fy=scale)

def draw_face_detections(img, detections):
    """Draws bounding boxes around detected faces."""
    if detections:
        for detection in detections:
            # Extract bounding box information
            bbox = detection.location_data.relative_bounding_box
            ih, iw, _ = img.shape
            box = (
                int(bbox.xmin * iw), int(bbox.ymin * ih),
                int(bbox.width * iw), int(bbox.height * ih)
            )
            # Draw the bounding box
            cv2.rectangle(img, box, (17, 219, 13), 2)

def main(video_path):
    # Initialize video capture
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file")
        return

    # Mediapipe Face Detection setup
    mp_face_detection = mp.solutions.face_detection
    mp_draw = mp.solutions.drawing_utils
    face_detection = mp_face_detection.FaceDetection(0.75)

    prev_time = 0  # Previous time for FPS calculation

    while True:
        success, img = cap.read()
        if not success:
            print("Error: Can't read the video frame.")
            break

        # Resize image for better performance
        img = resize_image(img)

        # Convert image to RGB for face detection
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = face_detection.process(img_rgb)

        # Draw face detections
        draw_face_detections(img, result.detections)

        # FPS calculation
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        # Display FPS on the video
        cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

        # Show the output image
        cv2.imshow("Face Detection", img)

        # Break the loop on 'q' key press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Release video capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'path/to/your/video.mp4'  # Update with the actual video path
    main(video_path)
