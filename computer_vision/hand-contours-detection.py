import cv2
img=cv2.imread('hand.jpg')
scale_percent = 220  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(resized_img, 50, 140)
contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print('Numbers of contours are : ', len(contours))
cv2.drawContours(resized_img, contours, -1, (0, 0, 255), 3)
cv2.imshow("final",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
