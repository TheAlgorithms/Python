
import numpy as np

import cv2

cap = cv2.VideoCapture(1)
template = cv2.CascadeClassifier("./archive/haarcascade_frontalface_default.xml")


skip = 0
face_data = []
dataset_path = './data/'
offset = 10

file_name = input("Enter the name of the person : ")

for _ in range(120):
    ret,frame = cap.read()
            
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates = template.detectMultiScale(grayscaled_img)
        
    print(face_coordinates)
    for face in face_coordinates:
        print(face)
        x, y, w, h =  face 

        cv2.rectangle(frame,(x, y),(x + w,y +h),(255,0,0),2)
    
    #extract main face
    face_section = frame[ y-offset: y+h+offset, x-offset:x+ w+ offset]
    face_section = cv2.resize(face_section,(100, 100))
    
    skip += 1
    
    if(skip % 10 == 0):
        face_data.append(face_section)
        print(len(face_data))
        
    
    cv2.imshow("Cropped", face_section) 
    cv2.imshow("VIDEO FRAME", frame)
        
    keypressed = cv2.waitKey(1) & 0xFF
        
face_data = np.array(face_data)
print(face_data.shape)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)


np.save(dataset_path + file_name + '.npy',face_data)
print("data successfully saved at " + dataset_path+file_name+'.npy')
