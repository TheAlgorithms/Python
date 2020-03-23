import cv2
import numpy as np
import matplotlib.pyplot as plt
def nothing(x):   # callback function which is executed everytime trackbar value changes.
    
    pass

cap = cv2.VideoCapture(0)
##trackbars
cv2.namedWindow('trackbars')
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1.tracbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2 .window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3. default value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4 .maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)




lowh,lows,lowv=180,24,56
highh,highs,highv=130,34,78


while True :
    #take each frame
    _, image = cap.read()

    image = cv2.imread('puppy.jpeg',1)
    lowh=cv2.getTrackbarPos('lowh','trackbars')
    lows =cv2.getTrackbarPos('lows','trackbars') 
    lowv = cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')
    
     # Convert BGR to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

      # define range of red color in HSV
    
    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])

     # Threshold the HSV image to get only red colors

    mask = cv2.inRange(hsv, lower_red , upper_red)

    
    # Bitwise-AND mask and original image

    res = cv2.bitwise_and(image ,image , mask = mask)
    kernel = np.array((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)

    output = [hsv ,mask  , res , smoothed]
    titles = ['hsv' , 'mask' , 'res' , filter]

    for i in range(4):
        plt.subplot(2, 3, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()
    k = cv2.waitKey(0) & 0xFF    #basically just pressing ESC button then cond will true then it will be break 
    if k == 27:                    #cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds.here it will wait for any key to be pressed then 100ms it will destroy 
        break

cap.release()             # When everything done, release the capture          
cv2.destroyAllWindows()   #use to destroy all  windows which u were created
                          #cv2.destroyWindow() where you pass the exact window name as the argument.

    

    
 #  cv2.namedWindow('Window_name', cv2.WINDOW_NORMAL) : use to resize the window which u are created
 #  cv2.imwrite()   : to save an image.
