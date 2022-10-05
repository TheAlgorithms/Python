import cv2

img = cv2.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\lena.jpg', 1)  # to read an image
# print(img)     #to print an image
cv2.imshow('image', img) #to display an image(but it will appear for very short time for longer time write wait program)
k=cv2.waitKey(5000) #image will appear for 5s(for argument 5000)   if you give zero in argument then it will not disappear you have to close the window
if k:
  cv2.destroyAllWindows() #destroys all created windows
elif k==ord('s'):
  cv2.imwrite('lena_copy.png', img) #to write an image in form of file
  cv2.destroyAllWindows()


