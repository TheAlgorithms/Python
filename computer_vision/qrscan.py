from pyzbar.pyzbar import decode
import cv2
import numpy as num

vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 480)

while True:

    success, read = vid.read()
    codes = decode(read)

    for code in codes:

        data = code.data.decode("utf-8")

        # create array of a polygon dimensions
        p1 = num.array([code.polygon], num.int32)

        p1 = p1.reshape((-1 , 1 , 2))

        cv2.polylines(read, [p1], True, (255, 0 , 0) , 5)

        # take rect attribute
        p2 = code.rect

        # put text over a qrcode during scanning
        font = cv2.FONT_HERSHEY_PLAIN

        cv2.putText(read, data , (p2[0], p2[1]), font , 0.9, (255, 0, 0), 2)

    cv2.imshow("SCAN", read)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
