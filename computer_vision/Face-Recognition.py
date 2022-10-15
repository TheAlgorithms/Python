import face_recognition
import cv2
import numpy

shahzaib = face_recognition.load_image_file('shahzaib.jpeg')
shahzaib_encode = face_recognition.face_encodings(shahzaib)[0]

farooq = face_recognition.load_image_file('farooq.jpeg')
farooq_encode = face_recognition.face_encodings(farooq)[0]

raheel = face_recognition.load_image_file('Raheel.jpeg')
raheel_encode = face_recognition.face_encodings(raheel)[0]

talha = face_recognition.load_image_file('talha1.png')
talha_encode = face_recognition.face_encodings(talha)[0]


encodings = [shahzaib_encode, farooq_encode, raheel_encode, talha_encode]
names = ['Shahzaib', 'Farooq', 'Raheel', 'Talha']

pics = ['party.jpeg', 'darya.jpeg', 'talha.jpeg ', 'group.jpeg']
for i in pics:


    find_in_pic = cv2.imread(i)
    locations = face_recognition.face_locations(find_in_pic)
    find_in_pic_encode = face_recognition.face_encodings(find_in_pic, locations)

    for (top, right, bottom, left) , face_encode in zip(locations , find_in_pic_encode):
        match = face_recognition.compare_faces(encodings , face_encode)

        name = "Unknown"

        

        face_dist = face_recognition.face_distance(encodings, face_encode)
        best_match = numpy.argmin(face_dist)
        if match[best_match]:
            name = names[best_match]

        find_in_pic = cv2.rectangle(find_in_pic, (left, top) ,(right,bottom), (0,0,255), 2)
        #find_in_pic = cv2.line(find_in_pic, (bottom, left),(bottom, right) ,(255,255,255), 2)
        #find_in_pic = cv2.rectangle(find_in_pic, (left-20, top-15) , (right,bottom), (255,0,0), cv2.FILLED)
        font = cv2.FONT_ITALIC
        find_in_pic = cv2.putText(find_in_pic, name, (left, bottom+20), font, 0.65, (0,0,255) , 2)



    cv2.imshow('window', find_in_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
