import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
ptime = 0

mpDraw = mp.solutions.drawing_utils
mpfacemesh = mp.solutions.face_mesh
faceMesh = mpfacemesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)

while True:
    success, img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgrgb)
    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(
                img, facelms, mpfacemesh.FACEMESH_TESSELATION, drawSpec, drawSpec
            )
            # mpDraw.draw_landmarks(img, facelms, mpfacemesh.FACEMESH_CONTOURS ,drawSpec,drawSpec)
        for id, lm in enumerate(facelms.landmark):
            # print(lm)
            ih, iw, ic = img.shape
            x, y = int(lm.x * iw), int(lm.y * ih)
            print(id, x, y)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(
        img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3
    )
    cv2.imshow("Image", img)
    cv2.waitKey(1)
