import cv2 as cv
face_cascade = cv.CascadeClassifier('..\libs\haarcascade_frontalface_default.xml')
face_cascade_eye = cv.CascadeClassifier('..\libs\haarcascade_eye.xml')
#face_glass = cv.CascadeClassifier('..\libs\haarcascade_eye_tree_eyeglasses.xml')

cap = cv.VideoCapture(0)
while(cap.isOpened()):

    falg ,img = cap.read() #start reading the camera output i mean frames
    # cap.read() returning a bool value and a frame onject type value

    gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY) # converting to grayscale image to perform smoother
    faces = face_cascade.detectMultiScale(img , 1.1, 7) #we use detectMultiscale library function to detect the predefined structures of a face
    eyes = face_cascade_eye.detectMultiScale(img , 1.1 , 7)
    # using for loops we are trying to read each and every frame and map
    for(x , y ,w ,h ) in faces:
         cv.rectangle(img , (x , y) , (x+w , y+h) , (0 , 255 , 0) , 1)

    for(a , b , c , d) in eyes:
         cv.rectangle(img, (a , b), (a+c, b+d), (255, 0, 0), 1)

    cv.imshow('img' , img )
    c = cv.waitKey(1)
    if c == ord('q'):
        break

cv.release()
cv.destroyAllWindows()


