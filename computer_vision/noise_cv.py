import cv2

image = cv2.imread('9qBsB.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
se=cv2.getStructuringElement(cv2.MORPH_RECT , (8,8))
bg=cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
out_gray=cv2.divide(image, bg, scale=255)
out_binary=cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU )[1] 

cv2.imshow('binary', out_binary)  
cv2.imwrite('binary.png',out_binary)

cv2.imshow('gray', out_gray)  
cv2.imwrite('gray.png',out_gray)
