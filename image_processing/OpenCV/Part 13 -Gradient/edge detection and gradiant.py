import cv2
import numpy as np
def nothing(x):   # callback function which is executed everytime trackbar value changes.
    
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('trackbars')
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1.tracbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2 .window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3. default value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4 .maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)
while True:
    _, frame = cap.read()
    lowh=cv2.getTrackbarPos('lowh','trackbars')
    lows =cv2.getTrackbarPos('lows','trackbars') 
    lowv = cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])
    mask = cv2.inRange(hsv, lower_red , upper_red)
    # higher type of datatype is cv2.CV_64F and simple type of data type is np.uint8 etc
    # we cant use simple data type bcoz  when you convert data to np.uint8,
    #all negative slopes are made zero. In simple words, you miss that edge.hence we are using higher type of data type
    laplacian = cv2.Laplacian(mask,cv2.CV_64F)
    sobelx = cv2.Sobel(hsv,cv2.CV_64F,1,0,ksize= -1)

    sobely = cv2.Sobel(hsv,cv2.CV_64F,0,1,ksize= -1)
    #First argument is our input image. Second and third arguments are our minVal and maxVal respectively
    edge = cv2.Canny(mask,120,150)
    ##cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edge',edge)
    cv2.imshow('mask',mask)
    

    k = cv2.waitKey(4) & 0xFF
    if k == 27:
        break
    

cv2.destroyAllWindows()
cap.release()
                       
# plzz refers this
'''
We use the functions: cv.Sobel (src, dst, ddepth, dx, dy, ksize = 3, scale = 1, delta = 0, borderType = cv.BORDER_DEFAULT)

Parameters
src	input image.
dst	output image of the same size and the same number of channels as src.
ddepth	output image depth(see cv.combinations); in the case of 8-bit input images it will result in truncated derivatives.
dx	order of the derivative x.
dy	order of the derivative y.
ksize	size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
scale	optional scale factor for the computed derivative values.
delta	optional delta value that is added to the results prior to storing them in dst.
borderType	pixel extrapolation method(see cv.BorderTypes)
'''
