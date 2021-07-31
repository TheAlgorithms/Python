"""
Image data augmentation is a technique that we can be used to artificially expand the 
size of a training dataset by creating modified versions of images in the dataset.
Some Image Augementations techniques through which we can augment our image like
Resizing, Horizontal Shift, Vertical Shift, Flipping, Zooming etc.
"""

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


def fill(image, h, w):
    image = cv2.resize(image, (h, w), cv2.INTER_CUBIC)
    return image
        

def horizontal_shift(image):
    ratio = round((random.uniform(0.0, 1.0)), 1)
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return image
    #this is for choosing right shift or left shift.
    #right means - positive ratio
    #left means - negative ratio
    ratio = random.uniform(-ratio, ratio)
    h, w = image.shape[:2]
    to_shift = w*ratio
    if ratio > 0:
        image = image[:, :int(w-to_shift), :]
    if ratio < 0:
        image = image[:, int(-1*to_shift):, :]
    image = fill(image, h, w)
    return image


def vertical_shift(image):
    ratio = round((random.uniform(0.0, 1.0)), 1)
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    #this is for choosing up shift or down shift.
    #down means - positive ratio
    #up means - negative ratio
    ratio = random.uniform(-ratio, ratio)
    h, w = image.shape[:2]
    to_shift = h*ratio
    if ratio > 0:
        image = image[:int(h-to_shift), :, :]
    if ratio < 0:
        image = image[:int(-1*to_shift), :, :]
    image = fill(image, h, w)
    return image


def brightness(image):
    low = round((random.uniform(0.0, 1.0)), 1)
    high = random.uniform(1, 5)
    value = random.uniform(low, high)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = np.array(image, dtype = np.float64)
    hsv[:,:,0] = hsv[:,:,0]*value 
    hsv[:,:,0][hsv[:,:,0]>255]  = 255
    hsv[:,:,2] = hsv[:,:,2]*value 
    hsv[:,:,2][hsv[:,:,2]>255]  = 255
    hsv = np.array(hsv, dtype = np.uint8)
    image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return image


def zoom(image):
    value = round((random.uniform(0.0, 1.0)), 1)
    if value > 1 or value < 0:
        print('Value for zoom should be less than 1 and greater than 0')
        return image
    value = random.uniform(value, 1)
    h, w = image.shape[:2]
    h_taken = int(value*h)
    w_taken = int(value*w)
    h_start = random.randint(0, h-h_taken)
    w_start = random.randint(0, w-w_taken)
    image = image[h_start:h_start+h_taken, w_start:w_start+w_taken, :]
    image = fill(image, h, w)
    return image


def channel_shift(image):
    value = random.randrange(255)
    value = int(random.uniform(-value, value))
    image = image + value
    image[:,:,:][image[:,:,:]>255]  = 255
    image[:,:,:][image[:,:,:]<0]  = 0
    image = image.astype(np.uint8)
    return image


def horizontal_flip(image):
    if True:
        return cv2.flip(image, 1)
    else:
        return image
    
def vertical_flip(image):
    if True:
        return cv2.flip(image, 0)
    else:
        return image


def rotation(image):
    angle = random.randrange(360)
    angle = int(random.uniform(-angle, angle))
    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), angle, 1)
    image = cv2.warpAffine(image, M, (w, h))
    return image


if __name__=="__main__":
  path = str(input("Enter your path : "))
  image = cv2.imread(path)
  
  cv2.imshow('Original Image', image)

  Horizontal_shift_image = horizontal_shift(image)
  cv2.imshow('Horizontal Shift Image', Horizontal_shift_image)

  Vertical_shift_image = vertical_shift(image)
  cv2.imshow('Vertical Shift Image', Vertical_shift_image)

  bright_image = brightness(image)
  cv2.imshow('Bright Image', bright_image)

  zoom_image = zoom(image)
  cv2.imshow('Zoom image', zoom_image)

  channel_shift_image = channel_shift(image)
  cv2.imshow('Channel Shift Image', channel_shift_image)

  horizontal_flip_image = horizontal_flip(image)
  cv2.imshow('Horizontal Flip Image', horizontal_flip_image)

  vertical_flip_image = vertical_flip(image)
  cv2.imshow('Vertical Flip Image', vertical_flip_image)

  rotated_image= rotation(image)    
  cv2.imshow('Rotation Image', rotated_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
