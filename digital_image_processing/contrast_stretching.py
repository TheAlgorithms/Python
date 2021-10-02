"""
    Implemented an algorithm using opencv to apply constrast stretching on an image
"""
from cv2 import destroyAllWindows, imread, imshow, waitKey
import numpy as np

def contrast_stretching(img,a,v,b,w):
    # getting number of pixels in the image
    pixel_h, pixel_v = img.shape[0],img.shape[1]

    #making an empty numpy array which will store the constrast stretched image
    img_contrast = np.zeros((pixel_h,pixel_v), dtype = int) 
    
    #total number of gray levels in the image
    L=256
    #threshold values
    a=150
    b=250


    # applying the constrast stretching logic on each pixel of the image
    for i in range(pixel_h):
        for j in range(pixel_v):
            if 0 <= img[i,j] < a: 
                img_contrast[i,j]= int(v/a)*img[i,j]
            elif a <= img[i,j] < b: 
                img_contrast[i,j]= int(w-v/b-a)*(img[i,j]-a) + v
            else:
                img_contrast[i,j] = int(255-w/255-b)*(img[i,j]-b) + w

    return img_contrast


if __name__ == "__main__":
    
    # Taking pair of coordinates as input to apply contrast stretching
    a, v = map(int, input("Enter the pair a, v: ").split())
    b, w = map(int, input("Enter the pair b, w: ").split())

    # read original image
    img = imread("digital_image_processing/image_data/lena.jpg", 0)

    # apply constrast stretching on the image
    contrast_stretched_img = contrast_stretching(img,a,v,b,w)

    # show result image
    imshow("negative of original image", img)
    waitKey(0)
    destroyAllWindows()
   