# import cv2
#
# cap = cv2.VideoCapture(0)  # if 0 doesn't work try -1 for other cameras try 1, 2 or 3
# while True:
#     ret, frame = cap.read()  # read will true if frame is available and it is saved in ret frame captures frame of video
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # GIVES GRAY SCALE IMAGE VIDEO
#     # cv2.imshow('frame', frame)
#     cv2.imshow('frame', gray)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # (& 0xFF is mask provided for 64 bit machine while using waitKey)
#         break  # if q key is pressed loop will break
#
# cap.release()
# cv2.destroyALLWindows()

# TODO: To check video is open or not-->

import cv2

cap = cv2.VideoCapture(0)  # if 0 doesn't work try -1 for other cameras try 1, 2 or 3
# TODO: Saving video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# check here for more fourcc codes--> fourcc.org/codecs.php
while cap.isOpened():  # checks video is opened or not
    ret, frame = cap.read()  # read will true if frame is available and it is saved in ret frame captures frame of video
    if ret:
        # TODO: To check height and width properties (there are many properties check opencv documentation)
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # every property has number associated with it you can also use that
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # GIVES GRAY SCALE IMAGE VIDEO
    # cv2.imshow('frame', frame)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # (& 0xFF is mask provided for 64 bit machine while using waitKey)
        break  # if q key is pressed loop will break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
