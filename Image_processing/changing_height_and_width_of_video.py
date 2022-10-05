import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Changing heights and width->
cap.set(3, 1280)  # 3 is for width and 4 is for height
cap.set(4, 720)# if provided resolution will not be available then default will be taken for a very high value provided it will shift to max resolution of camera
print(cap.get(3))  # getting width
print(cap.get(4))  # getting height

while cap.isOpened():  # checks video is opened or not
    ret, frame = cap.read()  # read will true if frame is available and it is saved in ret frame captures frame of video
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # GIVES GRAY SCALE IMAGE VIDEO
        # cv2.imshow('frame', frame)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # (& 0xFF is mask provided for 64 bit machine while using waitKey)
            break  # if q key is pressed loop will break
    else:
        break
cap.release()
cv2.destroyAllWindows()
