"""
    The Horn-Schunck method estimates the optical flow for every single pixel of
    a sequence of images.
    It works by assuming brightness constancy between two consecutive frames
    and smoothness in the optical flow.

    Useful resources:
    Wikipedia: https://en.wikipedia.org/wiki/Horn%E2%80%93Schunck_method
    Paper: http://image.diku.dk/imagecanon/material/HornSchunckOptical_Flow.pdf
"""

from typing import Optional

import numpy as np
from scipy.ndimage.filters import convolve
from typing_extensions import SupportsIndex


def warp(image: np.ndarray, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Warps the pixels of an image into a new image using the horizontal and vertical
    flows.
    Pixels that are warped from an invalid location are set to 0.

    Parameters:
        image: Grayscale image
        u: Horizontal flow
        v: Vertical flow

    Returns: Warped image
    """
    flow = np.stack((u, v), 2)

    # Create a grid of all pixel coordinates and subtract the offsets
    grid = np.stack(
        np.meshgrid(np.arange(0, image.shape[1]), np.arange(0, image.shape[0])), 2
    )
    grid = np.round(grid - flow).astype(np.int)

    # Find the locations outside of the original image
    invalid = (grid < 0) | (grid >= np.array([image.shape[1], image.shape[0]]))
    grid[invalid] = 0

    warped = image[grid[:, :, 1], grid[:, :, 0]]

    # Set pixels at invalid locations to 0
    warped[invalid[:, :, 0] | invalid[:, :, 1]] = 0

    return warped


def calc_derivatives(
    im0: np.ndarray, im1: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Calculates the vertical and horizontal image derivatives as well as the
    time derivatives used in the Horn-Schunck algorithm

    Parameters:
        im0: First image
        im1: Warped second image

    Returns:
        dX: Horizontal image derivative
        dY: Vertical image derivative
        dT: Time derivative
    """
    # Prepare kernels for the calculation of the derivatives
    kernel_x = np.array([[-1, 1], [-1, 1]]) * 0.25
    kernel_y = np.array([[-1, -1], [1, 1]]) * 0.25
    kernel_t = np.array([[1, 1], [1, 1]]) * 0.25

    # Calculate the derivatives
    dX = convolve(im0, kernel_x) + convolve(im1, kernel_x)
    dY = convolve(im0, kernel_y) + convolve(im1, kernel_y)
    dT = convolve(im0, kernel_t) + convolve(im1, -kernel_t)

    return dX, dY, dT


def horn_schunck(
    im0: np.ndarray,
    im1: np.ndarray,
    num_iter: SupportsIndex,
    alpha: Optional[float] = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    This function performs the Horn-Schunck algorithm and returns the estimated
    optical flow. It is assumed that the input images are grayscale and
    normalized to be in [0, 1].

    Parameters:
        im0: First image
        im1: Second image
        alpha: Regularization constant
        num_iter: Number of iterations performed

    Returns:
        u: Horizontal flow
        v: Vertical flow
    """
    if alpha is None:
        alpha = 0.1

    # Initialize flow
    u = np.zeros_like(im0)
    v = np.zeros_like(im0)

    laplacian_kernel = np.array(
        [[1 / 12, 1 / 6, 1 / 12], [1 / 6, 0, 1 / 6], [1 / 12, 1 / 6, 1 / 12]]
    )

    # Iteratively refine the flow
    for _ in range(num_iter):
        dx, dy, dt = calc_derivatives(warp(im0, u, v), im1)

        avg_u = convolve(u, laplacian_kernel)
        avg_v = convolve(v, laplacian_kernel)

        # This updates the flow as proposed in the paper (Step 12)
        d = (dx * avg_u + dy * avg_v + dt) / (alpha ** 2 + dx ** 2 + dy ** 2)

        u = avg_u - dx * d
        v = avg_v - dy * d

    return u, v
