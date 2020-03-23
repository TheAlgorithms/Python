import cv2
import math
import numpy as np

cap = cv2.VideoCapture('theroad.mp4')
w=cap.get(3)
h=cap.get(4)
#print(w)

def mouse_event(event, x,y,flags, para):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (event)
        pixel = hsv[y,x]

        cv2.setTrackbarPos('lowh','trackbar',pixel[0] - 10)
        cv2.setTrackbarPos('highh','trackbar',pixel[0] + 10)
        cv2.setTrackbarPos('lows','trackbar',pixel[1] - 20)
        cv2.setTrackbarPos('highs','trackbar',pixel[1] + 20)
        cv2.setTrackbarPos('lowv','trackbar',pixel[2] - 50)
        cv2.setTrackbarPos('highv','trackbar',pixel[2] + 50)

def callback(x):
        pass

cv2.namedWindow('trackbar')
cv2.namedWindow('imag')
cv2.namedWindow('hough')
cv2.namedWindow('rad')
 
cv2.createTrackbar('lowh','trackbar',0,180,callback)
cv2.createTrackbar('highh','trackbar',0,180,callback)
cv2.createTrackbar('lows','trackbar',0,255,callback)
cv2.createTrackbar('highs','trackbar',0,255,callback)
cv2.createTrackbar('lowv','trackbar',0,255,callback)
cv2.createTrackbar('highv','trackbar',0,255,callback)


cv2.createTrackbar('minline','hough',0,80,callback)
cv2.createTrackbar('maxgap','hough',0,80,callback)

cv2.createTrackbar('rad','rad',703,1800,callback)
cv2.createTrackbar('rad2','rad',592,1800,callback)
cv2.createTrackbar('width','rad',678,1800,callback)

while 1:
    _,img=cap.read()

    rad=cv2.getTrackbarPos('rad', 'rad')
    rad2=cv2.getTrackbarPos('rad2','rad')
    width=cv2.getTrackbarPos('width', 'rad')
    cv2.circle(img,(640,640),rad, (0,0,0), width)
    cv2.ellipse(img,(640,640),(rad,rad2),0,0,360,(0,0,0),width)
    
    cv2.setMouseCallback('imag',mouse_event)
    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    edges = cv2.Canny(img,50,150,apertureSize = 3)
    cv2.imshow('edges',edges)

##    minLineLength=50
##    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=40)
##
##    
##    a,b,c = lines.shape
##    for i in range(a):
##        cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
##        #cv2.imwrite('houghlines5.jpg',gray)
    minline=cv2.getTrackbarPos('minline', 'hough')
    maxgap=cv2.getTrackbarPos('maxgap', 'hough')

    
    lines = cv2.HoughLines(edges,1, np.pi / 180, 150, None, 0, 0)
    
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(img, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    
    lowh=cv2.getTrackbarPos('lowh', 'trackbar')
    highh=cv2.getTrackbarPos('highh', 'trackbar')
    lows=cv2.getTrackbarPos('lows', 'trackbar')
    highs=cv2.getTrackbarPos('highs', 'trackbar')
    lowv=cv2.getTrackbarPos('lowv', 'trackbar')
    highv=cv2.getTrackbarPos('highv', 'trackbar')

    lowred=np.array([lowh,lows,lowv])
    highred=np.array([highh,highs,highv])

    mask= cv2.inRange (hsv,lowred,highred)
    
    kernel = np.ones((10,10),np.uint8)
    dilute = cv2.dilate(mask, kernel, iterations = 1)
    opening = cv2.morphologyEx(dilute, cv2.MORPH_CLOSE, kernel)
    
    #cv2.imshow('mask',mask)
        

    (_,contours,_)=cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i in contours:
                    area = cv2.contourArea(i)
                    if(area>2000):
                            x,y,w,h = cv2.boundingRect(i)

                            rect = cv2.minAreaRect(i)
                            box = cv2.boxPoints(rect)
                            box = np.int0(box)
                            cv2.drawContours(img,[box],0,(0,0,255),2)
                                                       
                            #img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                            cv2.putText(img,"color1 detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))


    cv2.imshow('imag',img)
    #cv2.imshow('dil',opening)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
            break                          

cap.release()
cv2.destroyAllWindows()



