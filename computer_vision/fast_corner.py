"""
Features from accelerated segment test (FAST) Corner Detector
https://en.wikipedia.org/wiki/Features_from_accelerated_segment_test
"""

import cv2 as cv

def fast_detector(img):
    fast = cv.FastFeatureDetector_create()
    kp = fast.detect(img, None)
    img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))#drawing keypoints
    cv.imwrite('fast_true.png', img2)
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)
    detected_img = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
    return detected_img


if __name__ == "__main__":
    input_img = cv.imread("path_to_image", cv.IMREAD_GRAYSCALE)
    corner_detect = fast_detector(input_img)
    cv.imwrite("detected.png", corner_detect)
