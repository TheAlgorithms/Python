# simple face detectin algorithm to detect the presence of at least a face in an image provided.
''' 
    :input => image path
    :output => boolean corresponding to the detection of a face or not
    TRUE if face(s) detected. else FALSE
'''
import cv2
def detect_face(image):
    gray = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    faces = cascade.detectMultiScale(gray, 1.03, 3)
    return len(faces) > 0

if __name__ == "__main__":
    print(detect_face('im1.jpg'))
