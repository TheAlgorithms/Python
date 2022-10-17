import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
ptime = 0

mpfacedetection = mp.solutions.face_detection
mpdraw = mp.solutions.drawing_utils
facedetection = mpfacedetection.FaceDetection(0.75)

while True:
    success, img = cap.read()

    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = facedetection.process(imgrgb)
    print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpdraw.draw_detection(img, detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            bboxc = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = (
                int(bboxc.xmin * iw),
                int(bboxc.ymin * ih),
                int(bboxc.width * iw),
                int(bboxc.height * ih),
            )
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(
                img,
                f"{int(detection.score[0] * 100)}%",
                (bbox[0], bbox[1] - 20),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (255, 0, 255),
                2,
            )

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(
        img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2
    )
    cv2.imshow("Image", img)
    cv2.waitKey(1)
