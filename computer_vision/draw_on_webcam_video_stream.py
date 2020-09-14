import cv2


# Variables
drawing = False
pt1 = (0, 0)
pt2 = (0, 0)
press = False


def draw_rectangle(event, x, y, flags, params):

    global pt1, pt2, drawing, press

    # when mouse left button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # assign top left point of rectangle
        pt1 = (x, y)
        drawing = False
        # mouse button pressed flag
        press = True

    # when mouse pointer is moving
    elif event == cv2.EVENT_MOUSEMOVE:
        drawing = True
        if drawing & press:
            # assign bottom right corner of rectangle
            pt2 = (x, y)

    # when mouse button is released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = True
        # resetting pressed mouse button
        press = False


# Capture Video
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# Create a named window for connections
cv2.namedWindow(winname="frame")

# Bind draw_rectangle function to mouse cliks
cv2.setMouseCallback("frame", draw_rectangle)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # draw when drawing flag is on
    if drawing:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 5)

    # Display the resulting frame
    cv2.imshow("frame", frame)

    # close window when Q is pressed
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
