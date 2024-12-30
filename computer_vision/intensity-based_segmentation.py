# Importing necessary libraries
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from typing import List

def segment_image(image: np.ndarray, thresholds: List[int]) -> np.ndarray:
    """
    Performs image segmentation based on intensity thresholds.
    Args:
        image (np.ndarray): Input grayscale image as a 2D array.
        thresholds (List[int]): A list of intensity thresholds to define segments.
    Returns:
        np.ndarray: A labeled 2D array where each region corresponds to a threshold range.
    Example:
    >>> img = np.array([[80, 120, 180], [40, 90, 150], [20, 60, 100]])
    >>> segment_image(img, [50, 100, 150])
    array([[1, 2, 3],
           [0, 1, 2],
           [0, 0, 1]])
    """
    # Initialize an empty array to store segment labels
    segmented = np.zeros_like(image, dtype=np.int32)

    # Iterate over thresholds and label pixels in corresponding intensity ranges
    for i, threshold in enumerate(thresholds):
        segmented[image > threshold] = i + 1

    return segmented

if __name__ == "__main__":
    # Path to the image file
    image_path = "path_to_image"  # Replace with the path to your local image file

    # Load and preprocess the image
    original_image = Image.open(image_path).convert("L")  # Convert image to grayscale
    image_array = np.array(original_image)  # Convert image to a numpy array

    # Specify intensity thresholds for segmentation
    thresholds = [50, 100, 150, 200]  # Define your desired thresholds

    # Apply segmentation to the image
    segmented_image = segment_image(image_array, thresholds)

    # Visualize the results
    plt.figure(figsize=(12, 6))

    # Display the original image
    plt.subplot(1, 2, 1)
    plt.title("Original Grayscale Image")
    plt.imshow(image_array, cmap="gray")
    plt.axis("off")

    # Display the segmented image with labeled regions
    plt.subplot(1, 2, 2)
    plt.title("Segmented Image")
    plt.imshow(segmented_image, cmap="tab20")  # Use a colormap for better distinction
    plt.axis("off")

    # Show the plots
    plt.tight_layout()
    plt.show()
