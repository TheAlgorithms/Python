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
#building in if else statement
if not video.isOpened():
    print("Error opening video file")
else:
    print("Video successfully loaded and ready")
