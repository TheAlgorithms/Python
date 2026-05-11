"""
Canny Edge Detector - It is used to identify edges in images. 
Implementation of the Canny Edge Detection algorithm using NumPy.

https://en.wikipedia.org/wiki/Canny_edge_detector
"""

from math import pi

import cv2
import numpy as np


def grayscale(image: np.ndarray) -> np.ndarray:
    """
    To convert RGB -> grayscale using luminance weights.
    >>> image = np.array([[[255, 255, 255]]], dtype=np.uint8)
    >>> grayscale(image)
    array([[255]], dtype=uint8)
    """
    return np.dot(image[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
    #gray = 0.299R+0.587G+0.114B
    #np.uint8 = converts values to 8-bit integers(0-255)


def gaussian_kernel(kernel_size: int = 5, sigma: float = 1.4) -> np.ndarray:
    """
    To generate a Gaussian kernel.
    A typical 5*5 sized matrix with standard deviation as 1.4
    >>> gaussian_kernel(3).shape
    (3, 3)
    """
    if kernel_size % 2 == 0:
        raise ValueError("kernel's size must be odd")
        #as we need a center

    center = kernel_size // 2

    x, y = np.mgrid[-center : center + 1, -center : center + 1]
    #assigns weights, center gets largest while farther pixels get smaller values.
    kernel = (1 / (2 * pi * sigma**2)) * np.exp(
        -((x**2 + y**2) / (2 * sigma**2))
    )

    return kernel / kernel.sum()


def convolve(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Apply convolution to image.

    >>> image = np.ones((5, 5))
    >>> kernel = np.ones((3, 3))
    >>> convolve(image, kernel).shape
    (5, 5)
    """
    image_height, image_width = image.shape
    kernel_size = kernel.shape[0]
    padding = kernel_size // 2

    padded_image = np.pad(image, padding, mode="constant")
    #convolution near borders needs neighbors
    output = np.zeros_like(image, dtype=np.float64)

    for row in range(image_height):
        for column in range(image_width):
            region = padded_image[row : row + kernel_size,column : column + kernel_size]

            output[row, column] = np.sum(region * kernel)
            #multiply and add
    return output


def gaussian_blur(image: np.ndarray,kernel_size: int = 5,sigma: float = 1.4,) -> np.ndarray:
    """
    Blurring image using Gaussian filter.

    >>> image = np.ones((5, 5))
    >>> gaussian_blur(image).shape
    (5, 5)
    """
    kernel = gaussian_kernel(kernel_size, sigma)

    return convolve(image, kernel)


def sobel_gradients(image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Calculate Sobel gradients.

    >>> image = np.ones((5, 5))
    >>> magnitude, direction = sobel_gradients(image)
    >>> magnitude.shape
    (5, 5)
    """
    sobel_x = np.array(
        [
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1],
        ]
    )

    sobel_y = np.array(
        [
            [1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1],
        ]
    )

    gradient_x = convolve(image, sobel_x)
    gradient_y = convolve(image, sobel_y)

    gradient_magnitude = np.hypot(gradient_x, gradient_y)#edge strength

    gradient_magnitude = (gradient_magnitude / gradient_magnitude.max()) * 255
    #normalize values to 0-255
    gradient_direction = np.arctan2(gradient_y, gradient_x)
    #computes edge direction angle, just tan^-1(Gy/Gx)
    return gradient_magnitude, gradient_direction


def non_maximum_suppression(magnitude: np.ndarray,direction: np.ndarray,) -> np.ndarray:
    """
    Suppress non-maximum gradient values.

    >>> image = np.ones((5, 5))
    >>> direction = np.zeros((5, 5))
    >>> non_maximum_suppression(image, direction).shape
    (5, 5)
    """
    image_height, image_width = magnitude.shape

    suppressed = np.zeros((image_height, image_width), dtype=np.float64)

    angle = direction * 180.0 / np.pi
    angle[angle < 0] += 180

    for row in range(1, image_height - 1):
        for column in range(1, image_width - 1):
            neighbor_1 = 255
            neighbor_2 = 255

            current_angle = angle[row, column]

            if (0 <= current_angle < 22.5 or 157.5 <= current_angle <= 180):
                neighbor_1 = magnitude[row, column + 1]
                neighbor_2 = magnitude[row, column - 1]

            elif 22.5 <= current_angle < 67.5:
                neighbor_1 = magnitude[row + 1, column - 1]
                neighbor_2 = magnitude[row - 1, column + 1]

            elif 67.5 <= current_angle < 112.5:
                neighbor_1 = magnitude[row + 1, column]
                neighbor_2 = magnitude[row - 1, column]

            elif 112.5 <= current_angle < 157.5:
                neighbor_1 = magnitude[row - 1, column - 1]
                neighbor_2 = magnitude[row + 1, column + 1]

            if (magnitude[row, column] >= neighbor_1 and magnitude[row, column] >= neighbor_2):
                suppressed[row, column] = magnitude[row, column]

    return suppressed


def double_threshold(image: np.ndarray,low_threshold_ratio: float = 0.05,high_threshold_ratio: float = 0.15,) -> tuple[np.ndarray, int, int]:
    """
    Apply double thresholding.
    To separate strong edges from weak edges.
    >>> image = np.array([[100, 200]])
    >>> thresholded, weak, strong = double_threshold(image)
    >>> thresholded.shape
    (1, 2)
    """
    if low_threshold_ratio >= high_threshold_ratio:
        raise ValueError(
            "low_threshold_ratio must be smaller than high_threshold_ratio"
        )

    high_threshold = image.max() * high_threshold_ratio
    low_threshold = high_threshold * low_threshold_ratio

    image_height, image_width = image.shape

    result = np.zeros((image_height, image_width), dtype=np.uint8)

    weak = 75
    strong = 255

    strong_row, strong_column = np.where(image >= high_threshold)

    weak_row, weak_column = np.where(
        (image >= low_threshold) & (image < high_threshold)
    )

    result[strong_row, strong_column] = strong
    result[weak_row, weak_column] = weak

    return result, weak, strong


def hysteresis(image: np.ndarray,weak: int,strong: int = 255,) -> np.ndarray:
    """
    Track edges using hysteresis.

    >>> image = np.array([[255, 75]])
    >>> hysteresis(image, 75).shape
    (1, 2)
    """
    image_height, image_width = image.shape

    for row in range(1, image_height - 1):
        for column in range(1, image_width - 1):
            if image[row, column] == weak:
                if (
                    (image[row + 1, column - 1] == strong)
                    or (image[row + 1, column] == strong)
                    or (image[row + 1, column + 1] == strong)
                    or (image[row, column - 1] == strong)
                    or (image[row, column + 1] == strong)
                    or (image[row - 1, column - 1] == strong)
                    or (image[row - 1, column] == strong)
                    or (image[row - 1, column + 1] == strong)
                ):
                    image[row, column] = strong
                else:
                    image[row, column] = 0

    return image


class CannyEdgeDetector:
    """
    Canny Edge Detector implementation.
    """

    def __init__(self,kernel_size: int = 5,sigma: float = 1.4,low_threshold_ratio: float = 0.05,high_threshold_ratio: float = 0.15,) -> None:
        self.kernel_size = kernel_size
        self.sigma = sigma
        self.low_threshold_ratio = low_threshold_ratio
        self.high_threshold_ratio = high_threshold_ratio

    def detect(self, image_path: str) -> np.ndarray:
        """
        Detect edges in image.

        Args:
            image_path: Path to image

        Returns:
            Edge detected image
        >>> detector = CannyEdgeDetector()  # doctest: +SKIP
        >>> detector.detect("test.jpg").ndim  # doctest: +SKIP
        2
        """
        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(f"Unable to read image at {image_path}")

        gray_image = grayscale(image)

        blurred_image = gaussian_blur(
            gray_image,
            self.kernel_size,
            self.sigma,
        )

        gradient_magnitude, gradient_direction = sobel_gradients(
            blurred_image
        )

        suppressed_image = non_maximum_suppression(
            gradient_magnitude,
            gradient_direction,
        )

        thresholded_image, weak, strong = double_threshold(
            suppressed_image,
            self.low_threshold_ratio,
            self.high_threshold_ratio,
        )

        final_image = hysteresis(
            thresholded_image,
            weak,
            strong,
        )

        return final_image.astype(np.uint8)


if __name__ == "__main__":
    detector = CannyEdgeDetector()

    detected_edges = detector.detect("Screenshot 2026-05-11 065624.png")

    cv2.imwrite("canny_edges.jpg", detected_edges)