import cv2
import numpy as np

"""
Dense Optical Flow using Lucas Kanade Method
https://en.wikipedia.org/wiki/Lucas%E2%80%93Kanade_method
"""

cap = cv2.VideoCapture(0)

# Lucas Kanade Parameters
lk_params = dict(
    winSize=(30, 30),
    maxLevel=4,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
)


class LucasKanade:
    @staticmethod
    def execute():
        # get first frame of video
        _, frame1 = cap.read()
        
        if _:
            # convert frame to grayscale
            frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            x = cv2.goodFeaturesToTrack(frame1_gray, 200, 0.01, 10, None, None, 7)
    
            lin = np.zeros_like(frame1)
            i = 0
            while True:
                i = i + 1
                _, frame2 = cap.read()
                if not _:
                    break
                frame2 = cv2.medianBlur(frame2, 5)
                frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
                y, st, error = cv2.calcOpticalFlowPyrLK(
                    frame1_gray, frame2_gray, x, None, **lk_params
                )
    
                for j, (new, old) in enumerate(zip(y, x)):
                    a, b = new.ravel()
                    c, d = old.ravel()
                    frame2 = cv2.circle(frame2, (a, b), 5, (0, 0, 255), -1)
                    frame2 = cv2.circle(frame2, (c, d), 5, (255, 0, 0), -1)
                    lin = cv2.line(lin, (a, b), (c, d), (0, 255, 0), 2)
    
                if i == 2:
                    # Draw line for every 2 frames
                    lin = np.zeros_like(frame1)
                    i = 0
                img = cv2.add(frame2, lin)
                img = cv2.flip(img, 1)
    
                if img is not None:
                    cv2.imshow("Video", img)
                    key = cv2.waitKey(1)
                    if key & 0xFF == ord("q"):
                        break
    
                # update the new values
                frame1_gray = np.copy(frame2_gray)
                x = cv2.goodFeaturesToTrack(frame1_gray, 200, 0.01, 10, None, None, 10)


run = LucasKanade()
run.execute()

cap.release()
cv2.destroyAllWindows()
