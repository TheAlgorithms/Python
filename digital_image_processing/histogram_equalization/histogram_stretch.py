"""
Created on Fri Sep 28 15:22:29 2018

@author: Binish125
"""
import copy
import os

import cv2
import numpy as np
from matplotlib import pyplot as plt


class contrastStretch:
    def __init__(self):
        self.img = ""
        self.original_image = ""
        self.last_list = []
        self.rem = 0
        self.L = 256
        self.sk = 0
        self.k = 0
        self.number_of_rows = 0
        self.number_of_cols = 0

    def stretch(self, input_image):
        self.img = cv2.imread(input_image, 0)
        self.original_image = copy.deepcopy(self.img)
        x, _, _ = plt.hist(self.img.ravel(), 256, [0, 256], label="x")
        self.k = np.sum(x)
        for i in range(len(x)):
            prk = x[i] / self.k
            self.sk += prk
            last = (self.L - 1) * self.sk
            if self.rem != 0:
                self.rem = int(last % last)
            last = int(last + 1 if self.rem >= 0.5 else last)
            self.last_list.append(last)
            self.number_of_rows = int(np.ma.count(self.img) / self.img[1].size)
            self.number_of_cols = self.img[1].size
        for i in range(self.number_of_cols):
            for j in range(self.number_of_rows):
                num = self.img[j][i]
                if num != self.last_list[num]:
                    self.img[j][i] = self.last_list[num]
        cv2.imwrite("output_data/output.jpg", self.img)

    def plotHistogram(self):
        plt.hist(self.img.ravel(), 256, [0, 256])

    def showImage(self):
        cv2.imshow("Output-Image", self.img)
        cv2.imshow("Input-Image", self.original_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    file_path = os.path.join(os.path.basename(__file__), "image_data/input.jpg")
    stretcher = contrastStretch()
    stretcher.stretch(file_path)
    stretcher.plotHistogram()
    stretcher.showImage()
