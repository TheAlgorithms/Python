#Uploading video to colab for object detection
import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

uploaded = files.upload()

yourvideo = list(uploaded.keys())[0]
#once run, you will be promoted to select the video for object detection.

#next cell, I like to break my code up so I can check for errors
with open(yourvide, 'wb') as f:
  f.write(uploaded[yourvideo])  #this write it to a file in Colab's runtime temporary file system

#preparing video for CV2 library
video = cv2.VideoCapture(yourvideo)
if not video.isOpened():
    print("Error opening video file")
else:
  print("Video successfully loaded and ready")

            
