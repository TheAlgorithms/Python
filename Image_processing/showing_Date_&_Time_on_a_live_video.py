import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(3, 3000)
# cap.set(4, 3000)
# print(cap.get(3))
# print(cap.get(4))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX  # font name of text
        # TODO: showing width and height on live stream
        text = 'Width: ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        dateT = str(datetime.datetime.now())
        frame = cv2.putText(frame, dateT, (10, 50), font, 1, (0, 255, 255), 2,
                            cv2.LINE_AA)  # 2nd argument is text, 3rd one for coordinates, 4 th one for font,5th for font size, 6th for color, 7th for thickness, and last one for line type
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
