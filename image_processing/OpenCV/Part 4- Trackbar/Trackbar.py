import cv2
import numpy as np
def nothing(x):
    pass

cv2.namedWindow('trackbars')
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1.tracbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2 .window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3. default value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4 .maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)

##cap = cv2.VideoCapture(0)
##image = cv2.imread('triangles.png')
while True :
    
    image = cv2.imread('pexel.jpeg')
    ##_,frame = cap.read()
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    ##blur = cv2.GaussianBlur(hsv , (10,10),0)
    blur = cv2.medianBlur(hsv , 5)
    
    lowh=cv2.getTrackbarPos('lowh','trackbars')
    lows =cv2.getTrackbarPos('lows','trackbars') 
    lowv = cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')

    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])
    
    mask = cv2.inRange(hsv, lower_red , upper_red)

    #_,contours,_ = cv2.findContours(mask ,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    '''
    for i in contours:
        area = cv2.contourArea(i)
        if area >500:
            cv2.drawContours(frame,i,-1,(0,0,255),3)
    '''

    #cv2.drawContours(image,contours,-1,(0,0,255),3)
    cv2.imshow('frame',image)
    cv2.imshow('mask',mask)

    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break 

#cap.release()
cv2.destroyAllWindows()
            

            

            
            
        
