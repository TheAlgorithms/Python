"""
    The Horn-Schunck method estimates the optical flow for every single pixel of
    a sequence of images.
    It works by assuming brightness constancy between two consecutive frames
    and smoothness in the optical flow.

    Useful resources:
    Wikipedia: https://en.wikipedia.org/wiki/Horn%E2%80%93Schunck_method
    Paper: http://image.diku.dk/imagecanon/material/HornSchunckOptical_Flow.pdf
"""

from typing import SupportsIndex

import numpy as np
from scipy.ndimage import convolve


def warp(
    image: np.ndarray, horizontal_flow: np.ndarray, vertical_flow: np.ndarray
) -> np.ndarray:
    """
    Warps the pixels of an image into a new image using the horizontal and vertical
    flows.
    Pixels that are warped from an invalid location are set to 0.

    Parameters:
        image: Grayscale image
        horizontal_flow: Horizontal flow
        vertical_flow: Vertical flow

    Returns: Warped image

    >>> warp(np.array([[0, 1, 2], [0, 3, 0], [2, 2, 2]]), \
    np.array([[0, 1, -1], [-1, 0, 0], [1, 1, 1]]), \
    np.array([[0, 0, 0], [0, 1, 0], [0, 0, 1]]))
    array([[0, 0, 0],
           [3, 1, 0],
           [0, 2, 3]])
    """
    flow = np.stack((horizontal_flow, vertical_flow), 2)

    # Create a grid of all pixel coordinates and subtract the flow to get the
    # target pixels coordinates
    grid = np.stack(
        np.meshgrid(np.arange(0, image.shape[1]), np.arange(0, image.shape[0])), 2
    )
    grid = np.round(grid - flow).astype(np.int32)

    # Find the locations outside of the original image
    invalid = (grid < 0) | (grid >= np.array([image.shape[1], image.shape[0]]))
    grid[invalid] = 0

    warped = image[grid[:, :, 1], grid[:, :, 0]]

    # Set pixels at invalid locations to 0
    warped[invalid[:, :, 0] | invalid[:, :, 1]] = 0

    return warped


def horn_schunck(
    image0: np.ndarray,
    image1: np.ndarray,
    num_iter: SupportsIndex,
    alpha: float | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    This function performs the Horn-Schunck algorithm and returns the estimated
    optical flow. It is assumed that the input images are grayscale and
    normalized to be in [0, 1].

    Parameters:
        image0: First image of the sequence
        image1: Second image of the sequence
        alpha: Regularization constant
        num_iter: Number of iterations performed

    Returns: estimated horizontal & vertical flow

    >>> np.round(horn_schunck(np.array([[0, 0, 2], [0, 0, 2]]), \
    np.array([[0, 2, 0], [0, 2, 0]]), alpha=0.1, num_iter=110)).\
    astype(np.int32)
    array([[[ 0, -1, -1],
            [ 0, -1, -1]],
    <BLANKLINE>
           [[ 0,  0,  0],
            [ 0,  0,  0]]], dtype=int32)
    """
    if alpha is None:
        alpha = 0.1

    # Initialize flow
    horizontal_flow = np.zeros_like(image0)
    vertical_flow = np.zeros_like(image0)

    # Prepare kernels for the calculation of the derivatives and the average velocity
    kernel_x = np.array([[-1, 1], [-1, 1]]) * 0.25
    kernel_y = np.array([[-1, -1], [1, 1]]) * 0.25
    kernel_t = np.array([[1, 1], [1, 1]]) * 0.25
    kernel_laplacian = np.array(
        [[1 / 12, 1 / 6, 1 / 12], [1 / 6, 0, 1 / 6], [1 / 12, 1 / 6, 1 / 12]]
    )

    # Iteratively refine the flow
    for _ in range(num_iter):
        warped_image = warp(image0, horizontal_flow, vertical_flow)
        derivative_x = convolve(warped_image, kernel_x) + convolve(image1, kernel_x)
        derivative_y = convolve(warped_image, kernel_y) + convolve(image1, kernel_y)
        derivative_t = convolve(warped_image, kernel_t) + convolve(image1, -kernel_t)

        avg_horizontal_velocity = convolve(horizontal_flow, kernel_laplacian)
        avg_vertical_velocity = convolve(vertical_flow, kernel_laplacian)

        # This updates the flow as proposed in the paper (Step 12)
        update = (
            derivative_x * avg_horizontal_velocity
            + derivative_y * avg_vertical_velocity
            + derivative_t
        )
        update = update / (alpha**2 + derivative_x**2 + derivative_y**2)

        horizontal_flow = avg_horizontal_velocity - derivative_x * update
        vertical_flow = avg_vertical_velocity - derivative_y * update

    return horizontal_flow, vertical_flow


if __name__ == "__main__":
    import doctest

    doctest.testmod()
