import cv2

path = "image_assets/lsb.png"

img = cv2.imread(path,0)

print(img)

cv2.imwrite("original_image.png", img)
