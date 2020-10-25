import cv2

# Read image from which paragraphs needs to be extracted
im = cv2.imread("img_name.jpg")
img = im.copy() 
  
# Preprocessing the image starts 
  
# Convert the image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Performing OTSU threshold 
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
  
# Specify structure shape and kernel size.  
# Kernel size increases or decreases the area  
# of the rectangle to be detected. 
#(18,18) is an approx length for paras
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 
  
# Appplying dilation on the threshold image 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
  
# Finding contours 
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                 cv2.CHAIN_APPROX_NONE) 
  
# Creating a copy of image 
im2 = img.copy() 
  
# Looping through the identified contours 
i=0
for cnt in contours: 
    x, y, w, h = cv2.boundingRect(cnt) 
    if h<30 or w<30:
        continue
    print(x,y,w,h)  
    # Drawing a rectangle on copied image 
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
    crops = im2[y:y+h, x:x+w]
    name = "res_"+str(i)+".jpeg"
    cv2.imwrite(name, crops)
    i+=1
cv2.imwrite('final.jpg', im2)
