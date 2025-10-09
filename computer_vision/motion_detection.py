import cv2
import numpy as np

"""
Basic Motion Detection using frame differencing and background subtraction (MOG2).

Usage:
    - Set VIDEO_SOURCE to a video file path or an integer (e.g., 0) for webcam.
    - The script shows two windows: motion mask and annotated frame.
    - Press 'q' to quit.

Notes:
    - Requires OpenCV (opencv-python) and NumPy.
    - This example focuses on clarity and educational value, not production tuning.
"""


# Parameters
VIDEO_SOURCE = 0  # use integer for webcam (e.g., 0) or string path for video file
MIN_CONTOUR_AREA = 500  # pixels; filter tiny motions/noise
MORPH_KERNEL_SIZE = (5, 5)  # kernel for opening/closing
DISPLAY_SCALE = 1.0  # resize factor for display


def create_background_subtractor() -> cv2.BackgroundSubtractor:
    """
    Create and return a MOG2 background subtractor with sensible defaults.
    """
    # history=500, varThreshold=16 are common defaults; detectShadows adds robustness
    return cv2.createBackgroundSubtractorMOG2(
        history=500, varThreshold=16, detectShadows=True
    )


def preprocess_frame(frame: cv2.Mat) -> cv2.Mat:
    """
    Convert to grayscale and apply Gaussian blur to suppress noise.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred


def frame_difference(prev_gray: cv2.Mat, curr_gray: cv2.Mat) -> cv2.Mat:
    """
    Compute absolute difference between consecutive grayscale frames.
    Returns a binary motion mask after thresholding and morphology.
    """
    diff = cv2.absdiff(prev_gray, curr_gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, MORPH_KERNEL_SIZE)
    opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=1)
    return closed


def background_subtraction_mask(
    subtractor: cv2.BackgroundSubtractor, frame: cv2.Mat
) -> cv2.Mat:
    """
    Apply background subtraction to obtain a motion mask. Includes morphology.
    """
    fg_mask = subtractor.apply(frame)
    # Remove shadows if present (MOG2 shadows are typically 127)
    _, fg_mask = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, MORPH_KERNEL_SIZE)
    opened = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel, iterations=1)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=1)
    return closed


def annotate_motion(frame: cv2.Mat, motion_mask: cv2.Mat) -> cv2.Mat:
    """
    Find contours on the motion mask and draw bounding boxes on the frame.
    """
    contours, _ = cv2.findContours(
        motion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    annotated = frame.copy()
    for contour in contours:
        if cv2.contourArea(contour) < MIN_CONTOUR_AREA:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(annotated, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return annotated


def main() -> None:
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        raise RuntimeError("Unable to open video source. Set VIDEO_SOURCE correctly.")

    subtractor = create_background_subtractor()

    ret, prev_frame = cap.read()
    if not ret:
        cap.release()
        raise RuntimeError("Failed to read initial frame from source.")

    prev_gray = preprocess_frame(prev_frame)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Optionally resize for display/performance
        if DISPLAY_SCALE != 1.0:
            frame = cv2.resize(frame, None, fx=DISPLAY_SCALE, fy=DISPLAY_SCALE)

        curr_gray = preprocess_frame(frame)

        # Frame differencing motion mask
        diff_mask = frame_difference(prev_gray, curr_gray)

        # Background subtraction motion mask
        bs_mask = background_subtraction_mask(subtractor, frame)

        # Combine masks to be more robust (logical OR)
        combined_mask = cv2.bitwise_or(diff_mask, bs_mask)

        annotated = annotate_motion(frame, combined_mask)

        cv2.imshow("Motion Mask", combined_mask)
        cv2.imshow("Motion Detection", annotated)

        prev_gray = curr_gray

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    print("DONE ✅")
