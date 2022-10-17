import time

import cv2
import mediapipe as mp


class FaceMeshDetector:
    def __init__(
        self, staticmode=False, maxFaces=2, mindetectioncon=0.5, minTrackCon=0.5
    ):

        self.staticmode = staticmode
        self.maxFaces = maxFaces
        self.mindetectioncon = mindetectioncon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            self.staticmode, self.maxFaces, self.mindetectioncon, self.minTrackCon
        )
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self, img, draw=True):
        self.imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgrgb)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img,
                        faceLms,
                        self.mpFaceMesh.FACE_CONNECTIONS,
                        self.drawSpec,
                        self.drawSpec,
                    )
            face = []
            for id, lm in enumerate(faceLms.landmark):
                # print(lm)
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                # cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN,
                # 0.7, (0, 255, 0), 1)

            # print(id,x,y)
            face.append([x, y])
            faces.append(face)
        return img, faces


def main():
    cap = cv2.VideoCapture(0)
    ptime = 0
    detector = FaceMeshDetector(maxFaces=2)
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces) != 0:
            print(faces[0])

        cTime = time.time()
        fps = 1 / (cTime - ptime)
        ptime = cTime
        cv2.putText(
            img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3
        )
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
