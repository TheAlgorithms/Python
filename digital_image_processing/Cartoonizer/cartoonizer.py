'''
Cartoonizer is an application of Digital Image processing that converts Image to Cartoon-like Image. 
The code uses Down sampling and Up sampling using Laplacian Pyramid, Bilateral Filtering, Median Blurring, Adaptive Threshold and Bitwise And.
Checkout details and .exe application here - https://github.com/Ankuraxz/Cartoonizer
'''



from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

import os
import sys


def resize(frame):
    img = cv2.resize(frame,(800,800))
    return img

def cartoonizer(img,num_down = 2, num_bi = 5):
    #Params
    #num_down = 2 #DOWNSAMPLE STEPS
    #num_bi = 5 # BILATERAL FILTERING STEPS
    img_color = img
    for ix in range(num_down):
        img_color = cv2.pyrDown(img)# Pyramid Down : Downsampling
    # print(img_c.shape)
    
    for iy in range(num_bi):
        img_color = cv2.bilateralFilter(img_color,d=9,sigmaColor=9,sigmaSpace=7) #Filtering
    # print(img_c.shape)
    
    #UPSAMPLING
    for ix in range(num_down):
        img_color = cv2.pyrUp(img_color)# Pyramid Down : Downsampling
    # print(img_c.shape)
    
    #BLUR and Threshold
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # GRAY SCALE
    img_blur = cv2.medianBlur(img_gray,7) #MEDIAN BLUR
    img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)

    img_color = cv2.resize(img_color,(800,800))
    #RGB CONVERSION + BITWISE &
    img_edge = cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
    # print(img_c.shape)
    # print(img_edge.shape)
    img_cartoon = cv2.bitwise_and(img_color,img_edge)

    stack = np.hstack([img,img_cartoon])
    return stack


if __name__ == "__main__":
    # read original image in bgr mode
    lena = cv2.imread("../image_data/lena.jpg")
    # canny edge detection
    img = resize(lena)
    cartoon = cartoonizer(img)
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
