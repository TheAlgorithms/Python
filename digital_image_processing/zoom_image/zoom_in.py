
#importing libraries
from PIL import Image
import numpy
import matplotlib.pyplot as plt

image = Image.open("image_data/lena.jpg")
print("Image format, size, mode: ")
print(image.format)
print(image.size)
print(image.mode)

#converting image into numpy array
np_img = numpy.array(image)

print(np_img)
print(np_img.shape)

#converting image to gray image
gray_data = np_img[:,:,0]
print("Gray image shape: {}".format(gray_data.shape))

w, h = gray_data.shape
print('Width : {}\tHeight :{}'.format(w, h))

#declaring scaling factor
scale_x = 2
scale_y = 2
print(gray_data)
plt.imshow(gray_data,cmap="gray")
plt.show()

gray_new = numpy.zeros((w*scale_x, h*scale_y))
print(gray_new.shape)

for i in range(0, (w*scale_x)):
    for j in range(0, (h*scale_y)):
        gray_new[i, j] = gray_data[int(i/2), int(j/2)]
        
print("Shape of modified image: {}".format(gray_new.shape))
plt.imshow(gray_new,cmap="gray")
plt.show()