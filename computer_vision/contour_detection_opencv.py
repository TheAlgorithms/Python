"""
Contour Detection Using OpenCV

This script reads an image, performs contour detection using OpenCV,
and saves the result with detected contours.

Author: Anuj Mishra
Date: 05-10-2023
"""

import cv2
import numpy as np

class ContourDetector:
    def __init__(self, image_path):
        # Initialize the ContourDetector with the path to an image.
        self.image_path = image_path
        self.image = cv2.imread(image_path)

    def preprocess_image(self):
        # Preprocess the input image by converting it to grayscale and applying Gaussian blur.
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.blurred = cv2.GaussianBlur(self.gray, (5, 5), 0)

    def detect_contours(self):
        # Detect contours in the preprocessed image using the Canny edge detection algorithm.
        self.edges = cv2.Canny(self.blurred, 50, 150)
        self.contours, _ = cv2.findContours(self.edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    def draw_contours(self):
        # Draw the detected contours on a copy of the original image.
        image_with_contours = self.image.copy()
        cv2.drawContours(image_with_contours, self.contours, -1, (0, 255, 0), 2)
        return image_with_contours

    def save_image_with_contours(self, output_path):
        # Save the image with detected contours to the specified output path.
        image_with_contours = self.draw_contours()
        cv2.imwrite(output_path, image_with_contours)

if __name__ == "__main__":
    image_path = 'path_to_image.jpg'
    output_path = 'output_image_with_contours.jpg'

    detector = ContourDetector(image_path)
    detector.preprocess_image()
    detector.detect_contours()
    detector.save_image_with_contours(output_path)

    print(f"Contours detected and saved to {output_path}")
