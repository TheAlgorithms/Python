import cv2
import numpy as np


def nothing(x):
    pass
cv2.namedWindow('trackbars')
cv2.createTrackbar('quality','trackbars',1,100,nothing)
cv2.createTrackbar('maxCorners','trackbars',0,500,nothing)

cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    print(gray)
        
    quality = cv2.getTrackbarPos('quality','trackbars')
    maxCorners = cv2.getTrackbarPos('maxCorners','trackbars')

    if quality > 0:
        quality = quality/100
    else :
        quality=0.01

    #convert that pixel in the form of float
    harris = cv2.cornerHarris(gray,2,3,0.04)

    #cv.CornerHarris(image, harris_dst, blockSize, aperture_size =3, k=0.04)
    #kernel = np.ones((5,5),np.uint8)
    
    #dilation = cv2.dilate(harris,kernel,iterations = 1)
    dilation = cv2.dilate(harris,None)
    
    threshold = cv2.threshold(dilation,0.01*dilation.max(),255,0)
    dst = np.uint8(threshold)

    #find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
    
    if corners is not None:
        corners = np.int0(corners)

    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(frame,(x,y),5,(0,0,255),-1)

        
    cv2.imshow("frame",img)

    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break 

cap.release()
cv2.destroyAllWindows()
