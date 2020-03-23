import cv2
import numpy as np

def nothing(x):
    
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('smoothed', cv2.WINDOW_NORMAL)
cv2.namedWindow('blur', cv2.WINDOW_NORMAL)
cv2.namedWindow('bilateral', cv2.WINDOW_NORMAL)
cv2.namedWindow('median', cv2.WINDOW_NORMAL)




cv2.namedWindow('trackbars')
cv2.createTrackbar('lowh','trackbars',0,180,nothing)
cv2.createTrackbar('highh','trackbars',0,180,nothing)
cv2.createTrackbar('lows','trackbars',0,255,nothing)
cv2.createTrackbar('highs','trackbars',0,255,nothing)
cv2.createTrackbar('lowv','trackbars',0,255,nothing)
cv2.createTrackbar('highv','trackbars',0,255,nothing)



lowh,lows,lowv=180,24,56
highh,highs,highv=130,34,78


while True :
 
    _, frame = cap.read()
    
    

    lowh=cv2.getTrackbarPos('lowh','trackbars')
    lows =cv2.getTrackbarPos('lows','trackbars') 
    lowv = cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')
    
     # Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

      # define range of red color in HSV
    
    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])

     # Threshold the HSV image to get only red colors
    
    mask = cv2.inRange(hsv, lower_red , upper_red)

    
    # Bitwise-AND mask and original image

    res = cv2.bitwise_and(frame,frame , mask = mask)
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    blur = cv2.GaussianBlur(res,(15,15),0)
    bilateral = cv2.bilateralFilter(res,15,100,100)
    median = cv2.medianBlur(res,15)

    

    

    cv2.imshow('shark',hsv)
    cv2.imshow('res',res)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur',blur)
    cv2.imshow(' bilateral', bilateral)
    cv2.imshow('median',median)


    
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    

    
