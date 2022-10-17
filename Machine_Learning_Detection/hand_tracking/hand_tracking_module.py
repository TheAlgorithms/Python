import time

import cv2
import mediapipe as mp


class handdetector:
    def __init__(self, mode=False, maxhands=2, detectioncon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.detectioncon = detectioncon
        self.trackCon = trackCon
        self.mphands = mp.solutions.hands
        # self.hands = self.mphands.Hands(self.mode, self.maxhands,
        #                                 self.detectioncon, self.trackCon)
        self.hands = self.mphands.Hands()
        self.mpdraw = mp.solutions.drawing_utils

    def findhands(self, img, draw=True):
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(
                        img, handlms, self.mphands.HAND_CONNECTIONS
                    )
        return img

    def findposition(self, img, handno=0, draw=True):
        imlist = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(myhand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                imlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return imlist


def main():
    ptime = 0
    ctime = 0
    cap = cv2.VideoCapture()
    detector = handdetector()
    while True:
        success, img = cap.read()
        img = detector.findhands(img)
        imlist = detector.findposition(img)
        if len(imlist) != 0:
            print(imlist[4])
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(
            img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
        )
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
