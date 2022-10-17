import time

import cv2
import mediapipe as mp


class FaceMeshDetector:
    def __init__(
        self, staticmode=False, maxfaces=2, mindetectioncon=0.5, mintrackcon=0.5
    ):

        self.staticmode = staticmode
        self.maxfaces = maxfaces
        self.mindetectioncon = mindetectioncon
        self.mintrackcon = mintrackcon

        self.mpdraw = mp.solutions.drawing_utils
        self.mpfacemesh = mp.solutions.face_mesh
        self.facemesh = self.mpfacemesh.FaceMesh(
            self.staticmode, self.maxfaces, self.mindetectioncon, self.mintrackcon
        )
        self.drawspec = self.mpdraw.DrawingSpec(thickness=1, circle_radius=2)

    def findfacemesh(self, img, draw=True):
        self.imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.facemesh.process(self.imgrgb)
        faces = []
        if self.results.multi_face_landmarks:
            for facelms in self.results.multi_face_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(
                        img,
                        facelms,
                        self.mpfacemesh.FACE_CONNECTIONS,
                        self.drawspec,
                        self.drawspec,
                    )
            face = []
            for id_, lm in enumerate(facelms.landmark):
                # print(lm)
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                # cv2.putText(img, str(id_), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 1)

            print(id_, x, y)
            face.append([x, y])
            faces.append(face)
        return img, faces


def main():
    cap = cv2.VideoCapture(0)
    ptime = 0
    detector = FaceMeshDetector(maxfaces=2)
    while True:
        success, img = cap.read()
        img, faces = detector.findfacemesh(img)
        if len(faces) != 0:
            print(faces[0])

        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(
            img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3
        )
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
