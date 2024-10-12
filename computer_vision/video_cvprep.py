"""
Uploading a video in CoLab and getting it ready for CV

Objective : upload a video and prepare for detection

Resources Google Colab Video Upload
    https://colab.research.google.com/drive/1VFIMF7mKJPFR0lMRlXt5VisMRTIgxjwd?usp=sharing

Download dataset from :
free videos from: https://www.pexels.com/search/videos/detection/ OR
use your own.  For this demo, I used my own using the upload function.

1. Download a video 
2. Upload that video after running upload function
3. prepare video with CV

Those new to CV are challenged with the first step, how to upload the video and process for object detection.  This code will help you do just that.

"""

import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Uploading the video
uploaded = files.upload()
your_video = list(uploaded.keys())[0]

# Save the uploaded file to Colab's runtime temporary file system
with open(your_video, 'wb') as f:
    f.write(uploaded[your_video])

# Preparing video for CV2 library
video = cv2.VideoCapture(your_video)

if not video.isOpened():
    print("Error opening video file")
else:
    print("Video successfully loaded and ready")
