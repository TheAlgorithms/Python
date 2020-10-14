# Importing all necessary libraries 
import cv2 
import os 
  
# Read the video from specified path
# for inputing video from camera
# cam = cv2.VideoCapture(0) 
cam = cv2.VideoCapture("C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
# for extracting frames after specified intervals
frame_interval = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret and cur_frame%frame_interval == 0: 
        # if video is still left continue creating images 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    if not ret: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows()
