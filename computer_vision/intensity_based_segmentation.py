# Source: "https://www.ijcse.com/docs/IJCSE11-02-03-117.pdf"

# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def segment_image(image: np.ndarray, thresholds: list[int]) -> np.ndarray:
    """
    Performs image segmentation based on intensity thresholds.

    Args:
        image: Input grayscale image as a 2D array.
        thresholds: Intensity thresholds to define segments.

    Returns:
        A labeled 2D array where each region corresponds to a threshold range.

    Example:
        >>> img = np.array([[80, 120, 180], [40, 90, 150], [20, 60, 100]])
        >>> segment_image(img, [50, 100, 150])
        array([[1, 2, 3],
               [0, 1, 2],
               [0, 1, 1]], dtype=int32)
    """
    # Initialize segmented array with zeros
    segmented = np.zeros_like(image, dtype=np.int32)

    # Assign labels based on thresholds
    for i, threshold in enumerate(thresholds):
        segmented[image > threshold] = i + 1

    return segmented


if __name__ == "__main__":
    # Load the image
    image_path = "path_to_image"  # Replace with your image path
    original_image = Image.open(image_path).convert("L")
    image_array = np.array(original_image)

    # Define thresholds
    thresholds = [50, 100, 150, 200]

    # Perform segmentation
    segmented_image = segment_image(image_array, thresholds)

    # Display the results
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image_array, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Segmented Image")
    plt.imshow(segmented_image, cmap="tab20")
    plt.axis("off")

    plt.show()
