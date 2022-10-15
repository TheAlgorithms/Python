import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()        #use RGB image so we have to convert it
mpDraw = mp.solutions.drawing_utils

previousTime = 0
currentTime = 0




while True:
    success , img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    #converting here from BRG to RGB
    result = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for i in result.multi_hand_landmarks:
            for id , lm in enumerate(i.landmark):
                height , width , channel = img.shape
                cx , cy = int(lm.x * width) , int(lm.y * height)
                print(id,cx,cy)
                if id == 4 or id == 8:
                    cv2.circle(img , (cx,cy), 8 , (255,0,0) , cv2.FILLED)
            mpDraw.draw_landmarks(img , i , mpHands.HAND_CONNECTIONS)

    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255), 3)


    cv2.imshow("Image" , img)
    cv2.waitKey(1)
