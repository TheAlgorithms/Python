"""
Haar Cascading Classifiers

Objective : Detect Object (Face)

Resources Haar Classifiers :
https://www.analyticsvidhya.com/blog/2022/04/object-detection-using-haar-cascade-opencv/#:~:text=Haar%20cascade%20is%20an%20algorithm,%2C%20buildings%2C%20fruits%2C%20etc
https://machinelearningmastery.com/using-haar-cascade-for-object-detection/
Resource for Haar classifiers: https://github.com/opencv/opencv/tree/master/data/haarcascades

Download photo from :
https://unsplash.com/

1. Open Colab and create new notebook.
2. Download a free to download photo from unsplash or use one of your own.
3. Upload the photo in the model
4.  Use haar classifier to detect face in image
"""

from google.colab.patches import (
    cv2_imshow,
)  # to assist with image processing and showing
import cv2
import numpy as np


# Defining the list of image URLs from Unsplash
foto = ["https://spash.com/[chosen photo URL]" "https://splash.com/[chosen photo URL]"]


def load_image_from_url(url):
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


for i, image_url in enumerate(foto):
    img = load_image_from_url(image_url)
    print(f"Displaying image {i+1}")
    cv2_imshow(img)
# The above code should be in one cell and display the photo you chose.

###########next cell##############

# Loading the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)  # you can use others but this one is used the most.  Resource link above.


# detecting the face and covert to grayscale
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=20, minSize=(20, 20)
    )  # Setting general parameters.  Resouces above to understand more.
    for x, y, w, h in faces:
        cv2.rectangle(
            image, (x, y), (x + w, y + h), (255, 0, 0), 2
        )  # blue colour bounding box
    return image


# Processing each loaded and resized image with Haar cascade
for i, url in enumerate(foto, start=1):
    img = load_image_from_url(url)
    img_with_faces = detect_faces(img.copy())
    print(f"Detecting Face {i}")
    cv2_imshow(img_with_faces)  # face

# this should display the image with a blue bounding box.
