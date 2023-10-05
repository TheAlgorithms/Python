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
    def __init__(self, image_path: str):
        self.image_path = image_path

    def preprocess_image(self) -> np.ndarray:
        """
        Preprocesses the input image by converting it to grayscale.

        Returns:
            np.ndarray: The grayscale image as a NumPy array.
        """
        image = cv2.imread(self.image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def detect_contours(self, gray_image: np.ndarray, lower_threshold: int = 50, upper_threshold: int = 150) -> np.ndarray:
        """
        Detects contours in the grayscale image using the Canny edge detector.

        Args:
            gray_image (np.ndarray): The grayscale input image.
            lower_threshold (int): The lower threshold for Canny edge detection (default: 50).
            upper_threshold (int): The upper threshold for Canny edge detection (default: 150).

        Returns:
            np.ndarray: The binary image with detected edges.
        """
        edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)
        return edges

    def draw_contours(self, image: np.ndarray, edges: np.ndarray) -> np.ndarray:
        """
        Draws contours on the original color image.

        Args:
            image (np.ndarray): The original color image.
            edges (np.ndarray): The binary image with detected edges.

        Returns:
            np.ndarray: The color image with drawn contours.
        """
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        contour_image = image.copy()
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Green color for contours
        
        return contour_image

    def save_image_with_contours(self, output_path: str, contour_image: np.ndarray) -> None:
        """
        Saves the image with drawn contours to the specified output path.

        Args:
            output_path (str): The path to save the output image.
            contour_image (np.ndarray): The color image with drawn contours.
        """
        cv2.imwrite(output_path, contour_image)

if __name__ == "__main__":
    detector = ContourDetector('path_to_image.jpg')
    gray_image = detector.preprocess_image()
    edges = detector.detect_contours(gray_image, lower_threshold=50, upper_threshold=150)
    image = cv2.imread(detector.image_path)
    contour_image = detector.draw_contours(image, edges)
    detector.save_image_with_contours('output_image_with_contours.jpg', contour_image)

    print("Contours detected and saved.")
