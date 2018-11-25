# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:22:29 2018

@author: Binish125
"""
import cv2 
import matplotlib.pyplot as plt
import numpy as np

last_list=[]
rem=0
L=256
sk=0

img=cv2.imread('inputImage.jpg',0)

x,y,z=plt.hist(img.ravel(),256,[0,256],label='x')
k=np.sum(x)
for i in range(len(x)):
    prk=x[i]/k
    sk=prk+sk
    last=(L-1)*sk        
    if rem!=0:
        rem=int(last % last)
    if rem >=0.5:
        last=int(last)+1
    else:
        last=int(last)
    last_list.append(last)

number_of_rows=(int(np.ma.count(img)/img[1].size))
number_of_cols=img[1].size

for i in range(number_of_cols):
    for j in range(number_of_rows):
        num=img[j][i]
        if num != last_list[num]:
            img[j][i]=last_list[num]
    
plt.hist(img.ravel(),256,[0,256])

cv2.imwrite('ouputImage.jpg',img)