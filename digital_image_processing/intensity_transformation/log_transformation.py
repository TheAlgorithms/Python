# Log Intensity Transformation Functions

import cv2
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 255)
c = 255/(np.log(1+255))
L = 255 - x
y = c*np.log(1+x)
y_inv = np.exp(x)**(1/c)-1

plt.plot(x, x)
plt.plot(x, L)
plt.plot(x, y)
plt.plot(x, y_inv)
plt.xlim([0, 255])
plt.ylim([0, 255])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
# ------------------------------------------------------------------
# Open the image.
img = cv2.imread(
    'digital_image_processing/image_data/lena.jpg')


def negatives_linear(img: jpg) -> negative_linear_function:
    return 255-img


cv2.imshow('negatives_linear ', negatives_linear(img))
# ------------------------------------------------------------------


def log_transform(img: jpg)-> log_transformation_function:
    c = 255/(np.log(1 + np.max(img)))
    log_transformed = c * np.log(1 + img)
    log_transformed = np.array(log_transformed, dtype=np.uint8)
    return log_transformed, c


log_transformed,  c = log_transform(img)
cv2.imshow('log_transformed '+str(c), log_transformed)
# ------------------------------------------------------------------


def inverse_log_transformation(inv_log: jpg)-> inverse_transformation_function:
    c = 255/(np.log(1 + np.max(inv_log)))
    inverse_log_trans = np.exp(inv_log**1/c)-1
    inverse_log_trans = np.array(inverse_log_trans, dtype=np.uint8)
    return inverse_log_trans, c


inverse_log_transformation,  c = inverse_log_transformation(log_transformed)
cv2.imshow('Inverse_log '+str(c), inverse_log_transformation)
cv2.imshow('Original ', img)


# ------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
