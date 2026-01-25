"""
The Hough transform can be used to detect lines, circles or
other parametric curves. It works by transforming
the image edge map (obtained using a Sobel Filter) to Polar coordinates
and then selecting local maxima in the Parametric space as lines based on
majority voting.

References:
    https://en.wikipedia.org/wiki/Hough_transform
    https://www.cs.cmu.edu/~16385/s17/Slides/5.3_Hough_Transform.pdf
    https://www.uio.no/studier/emner/matnat/ifi/INF4300/h09/undervisningsmateriale/hough09.pdf

Requirements (pip):
    - matplotlib
    - cv2
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

from digital_image_processing.edge_detection import canny


def generate_accumulator(edges: np.ndarray) -> np.ndarray:
    """
    - Generates an accumulator by transforming edge coordinates from Cartesian
    to polar coordinates (Hough space).

    - The accumulator array can be indexed as `accumulator[p][theta]`

    Params:
    ------
        edges (np.ndarray): The edge-detected binary image (single-channel).

    Returns:
    ------
        np.ndarray: The accumulator array with votes for line candidates.

    Example:
    ------
        >>> img = np.array([[1, 0, 0,], [1, 0, 0,], [1, 0, 0,],])
        >>> np.sum(generate_accumulator(img))
        np.float64(540.0)
    """
    n, m = edges.shape
    theta_min, theta_max = 0, 180
    p_min, p_max = 0, int(n * np.sqrt(2) + 1)
    accumulator = np.zeros((int(theta_max - theta_min), int(p_max - p_min)))
    for x in range(n):
        for y in range(m):
            if edges[x][y]:
                for theta in range(theta_min, theta_max):
                    p = int(
                        x * np.cos(np.deg2rad(theta)) + y * np.sin(np.deg2rad(theta))
                    )
                    accumulator[theta][p] += 1
    return accumulator


def hough_transform(
    img: np.ndarray, threshold: int = 30, max_num_lines: int = 5
) -> list[tuple[int, int, np.float64]]:
    """
    Performs the Hough transform to detect lines in the input image.

    Params:
    ------
        img (np.ndarray): Single-channel grayscale image.
        threshold (int): Minimum vote count in the accumulator to consider a line.
        max_num_lines (int): Maximum number of lines to return.

    Returns:
    ------
        list[tuple[int, int, int]]: List of detected lines in (theta, p, votes) format.

    Raises:
    ------
        AssertionError: If the image is not square or single-channel.

    Example:
    ------
        >>> img = np.vstack([np.zeros((30, 50)),np.ones((1, 50)),np.zeros((19, 50))])
        >>> hough_transform(img, 30, 1)
        [(0, 28, np.float64(48.0))]
    """
    assert img.shape[0] == img.shape[1], "image must have equal dimensions"
    assert len(img.shape) == 2, "image should be single-channel"

    # Obtain edge map for image
    edges = canny.canny(img)

    # Transform to Polar Coordinates
    n, _ = img.shape
    theta_min, theta_max = 0, 180
    p_min, p_max = 0, int(n * np.sqrt(2) + 1)
    accumulator = generate_accumulator(edges)

    # Select maxima in Polar space
    res = []
    for theta in range(theta_min, theta_max):
        for p in range(p_min, p_max):
            if accumulator[theta][p] > threshold:
                res.append((theta, p, accumulator[theta][p]))

    res = sorted(res, key=lambda x: x[2], reverse=True)[:max_num_lines]
    return res


def draw_hough_lines(
    img: np.ndarray,
    lines: list[tuple],
    thickness: int = 1,
    color: tuple[int, int, int] = (255, 0, 0),
) -> None:
    """
    Draws detected Hough lines on the image.

    Params:
    ------
        img (np.ndarray): The input image to draw lines on.
        lines (list[tuple[int, int, int]]):
            List of (theta, p, votes) for detected lines.
        thickness (int): Line thickness.
        color (tuple[int, int, int]): BGR color of the lines.

    Example:
    ------
        >>> draw_hough_lines(create_dummy_img(), [(50, 0),])
    """
    for line in lines:
        theta, p = line[0], line[1]
        a = np.sin(np.deg2rad(theta))
        b = np.cos(np.deg2rad(theta))
        x0, y0 = a * p, b * p
        x1, y1 = int(x0 + 100 * (-b)), int(y0 + 100 * (a))
        x2, y2 = int(x0 - 100 * (-b)), int(y0 - 100 * (a))
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)


def create_dummy_img(height: int = 50, width: int = 50) -> np.ndarray:
    """
    Test function to create dummy 3-channel image of specified width and height
    Example:
    ------
        >>> create_dummy_img(100, 120).shape
        (100, 120, 3)
    """
    img = np.zeros((height, width), dtype=np.uint8)
    cv2.line(img, (10, 10), (int(0.6 * height), int(0.8 * width)), 255, 1)  # type: ignore[call-overload]
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # type: ignore[assignment]
    return img


if __name__ == "__main__":
    import doctest

    # Run doctests
    doctest.testmod()

    img = create_dummy_img(60, 80)
    # Preprocess Image
    img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(img)
    plt.show()
    # Accumulator
    accumulator = generate_accumulator(canny.canny(gray_image))
    plt.imshow(accumulator)
    plt.show()
    # Hough Transform
    res = hough_transform(gray_image, 30, 1)
    draw_hough_lines(img, res)
    plt.imshow(img)
    plt.show()
