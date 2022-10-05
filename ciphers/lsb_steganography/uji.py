import cv2

path = "image_assets/lsb.png"

img = cv2.imread(path,0)
cv2.imshow("uji", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img)