{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import time\n",
    "import numpy as np\n",
    "\n",
    "## Preparation for writing the ouput video\n",
    "fourcc = cv2.VideoWriter_fourcc(*'XVID')\n",
    "out = cv2.VideoWriter('output.avi',fourcc,20.0, (640,480))\n",
    "\n",
    "##reading from the webcam \n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "## Allow the system to sleep for 3 seconds before the webcam starts\n",
    "time.sleep(3)\n",
    "count = 0\n",
    "background = 0\n",
    "\n",
    "## Capture the background in range of 60\n",
    "for i in range(60):\n",
    "    ret,background = cap.read()\n",
    "background = np.flip(background,axis=1)\n",
    "\n",
    "\n",
    "## Read every frame from the webcam, until the camera is open\n",
    "while(cap.isOpened()):\n",
    "    ret, img = cap.read()\n",
    "    if not ret:\n",
    "        break\n",
    "    count+=1\n",
    "    img = np.flip(img,axis=1)\n",
    "    \n",
    "    ## Convert the color space from BGR to HSV\n",
    "    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)\n",
    "\n",
    "    ## Generat masks to detect red color\n",
    "    lower_red = np.array([0,120,50])\n",
    "    upper_red = np.array([10,255,255])\n",
    "    mask1 = cv2.inRange(hsv,lower_red,upper_red)\n",
    "\n",
    "    lower_red = np.array([170,120,70])\n",
    "    upper_red = np.array([180,255,255])\n",
    "    mask2 = cv2.inRange(hsv,lower_red,upper_red)\n",
    "\n",
    "    mask1 = mask1+mask2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
