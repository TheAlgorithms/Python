import cv2
import os
import numpy as np
from PIL import Image
import pickle as pkl

#print(dir (cv2.face)) //on python shell

recognizer = cv2.face.LBPHFaceRecognizer_create()

face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')
base_dir = os.path.dirname(os.path.abspath('Image/Kohli'))
image_dir = os.path.join(base_dir ,"kohli")

x_train = []
y_labels = []

label_ids = {}
current_id = 0

for root,dirs,files in os.walk(image_dir):
    for file in files:
        path = os.path.join(root,file)
        label = os.path.basename(root).replace(" " ," - ").lower()
        print(label,path)

        if not label in label_ids:
            label_ids[label] = current_id
            current_id +=1

        id_ = label_ids[label]
        print(label_ids)
        
        pil_image = Image.open(path).convert("L")  #grayScale
        image_array = np.array(pil_image ,"uint8")

        print(image_array)
        faces = face_cascade.detectMultiScale(image_array ,scaleFactor = 1.5, minNeighbors = 5)

        for x,y,w,h in faces:
            roi_image = image_array[y:y+h , x:x+w]
            x_train.append(roi_image)
            y_labels.append(id_)

with open("lable.pkl", 'wb') as f:
    pkl.dump(label_ids,f)
            
recognizer.train(x_train, np.array(y_labels))
recognizer.save("trained.yml")
