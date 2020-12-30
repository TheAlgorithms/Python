import cv2 as cv
import numpy as np

"""Median Filter
"""

class MedianFilter:
    def __init__(self , WindowSize : tuple):

        """ WindowSize : Showing up window size
        """

        self.WindowSize = WindowSize
        self.OrgImg = None
        self.NewImg = None


    def GetMedianValue(self,arr,i,j,n):

        """ Return the median value of given a window 
        """

        A = [-1,0,1]
        temp = []
        mid = (n**2)//2 
        for r in A:
            for c in A:
                try:
                    temp.append(arr[i+r][j+c])
                except:
                    mid = mid-1
        
        temp.sort()
        return temp[mid]

    def DoMedianFiltering(self,ImgPath,n):

        """Creating a median filtered image
           Uses ShowUp method
        """

        ImgRead = cv.imread(ImgPath, cv.IMREAD_GRAYSCALE)
        img     = cv.resize(ImgRead , self.WindowSize)
        new = np.zeros(self.WindowSize , dtype="uint8")
        a,b = self.WindowSize

        for row in range(a):
            for col in range(b):
                new[row][col] = self.GetMedianValue(img,row,col,n)

        self.OrgImg = img
        self.NewImg = new

    def ShowUp(self):

        """Showing up both original image and median filtered image
        """

        cv.imshow("Original Image" , self.OrgImg)
        cv.imshow("After Median Filtering" ,self.NewImg)
        cv.waitKey(0)

    def SaveImg(self , SavePath):

        """Saving the median filtered image
        """
        cv.imwrite(SavePath , self.NewImg)

    
if __name__ == "__main__":
    obj = MedianFilter((300,300))
    obj.DoMedianFiltering("path to image",3)
    ##obj.ShowUp()
    obj.SaveImg("MedianFiltered.png")
