# @Author: @joydipb01
# @File: pruning_operation.py
# @Time: 2025-10-03 19:45

from pathlib import Path

import numpy as np
from PIL import Image


def rgb_to_gray(rgb: np.ndarray) -> np.ndarray:
    """
    Return gray image from rgb image

    >>> rgb_to_gray(np.array([[[127, 255, 0]]]))
    array([[187.6453]])
    >>> rgb_to_gray(np.array([[[0, 0, 0]]]))
    array([[0.]])
    >>> rgb_to_gray(np.array([[[2, 4, 1]]]))
    array([[3.0598]])
    >>> rgb_to_gray(np.array([[[26, 255, 14], [5, 147, 20], [1, 200, 0]]]))
    array([[159.0524,  90.0635, 117.6989]])
    """
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    return 0.2989 * r + 0.5870 * g + 0.1140 * b


def gray_to_binary(gray: np.ndarray) -> np.ndarray:
    """
    Return binary image from gray image

    >>> gray_to_binary(np.array([[127, 255, 0]]))
    array([[False,  True, False]])
    >>> gray_to_binary(np.array([[0]]))
    array([[False]])
    >>> gray_to_binary(np.array([[26.2409, 4.9315, 1.4729]]))
    array([[False, False, False]])
    >>> gray_to_binary(np.array([[26, 255, 14], [5, 147, 20], [1, 200, 0]]))
    array([[False,  True, False],
           [False,  True, False],
           [False,  True, False]])
    """
    return (gray > 127) & (gray <= 255)


def neighbours(image: np.ndarray, x_coord: int, y_coord: int) -> list:
    """
    Return 8-neighbours of point (x_coord, y_coord), in clockwise order

    >>> neighbours(
    ...     np.array(
    ...         [
    ...             [True, True, False],
    ...             [True, False, False],
    ...             [False, True, False]
    ...         ]
    ...     ), 1, 1
    ... )
    [np.True_, np.False_, np.False_, np.False_, np.True_, np.False_, np.True_, np.True_]
    >>> neighbours(
    ...     np.array(
    ...         [
    ...             [True, True, False, True],
    ...             [True, False, False, True],
    ...             [False, True, False, True]
    ...         ]
    ...     ), 1, 2
    ... )
    [np.False_, np.True_, np.True_, np.True_, np.False_, np.True_, np.False_, np.True_]
    """
    img = image

    neighborhood = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ]

    neighbour_points = []

    for dx, dy in neighborhood:
        if 0 <= x_coord + dx < img.shape[0] and 0 <= y_coord + dy < img.shape[1]:
            neighbour_points.append(img[x_coord + dx][y_coord + dy])
        else:
            neighbour_points.append(False)

    return neighbour_points


def is_endpoint(image: np.ndarray, x_coord: int, y_coord: int) -> bool:
    """
    Check if a pixel is an endpoint based on its 8-neighbors.

    An endpoint is defined as a pixel that has exactly one neighboring pixel
    that is part of the foreground (True).

    >>> is_endpoint(
    ...     np.array(
    ...         [
    ...             [True, True, False],
    ...             [True, False, False],
    ...             [False, True, False]
    ...         ]
    ...     ), 1, 1
    ... )
    False
    >>> is_endpoint(
    ...     np.array(
    ...         [
    ...             [True, True, False, True],
    ...             [True, False, False, True],
    ...             [False, True, False, True]
    ...         ]
    ...     ), 2, 3
    ... )
    True
    """
    img = image
    return int(sum(neighbours(img, x_coord, y_coord))) == 1


def prune_skeletonized_image(
    image: np.ndarray, spur_branch_length: int = 50
) -> np.ndarray:
    """
    Return pruned image by removing spurious branches of specified length
    Source: https://www.scribd.com/doc/15792184/042805-04

    >>> arr = np.array([
    ...     [False, True, False],
    ...     [False, True, False],
    ...     [False, True, True]
    ... ])
    >>> prune_skeletonized_image(arr, spur_branch_length=1)
    array([[False,  True, False],
           [False,  True, False],
           [False,  True,  True]])
    >>> arr2 = np.array([
    ...     [False, False, False, False],
    ...     [False, True, True, False],
    ...     [False, False, False, False]
    ... ])
    >>> prune_skeletonized_image(arr2, spur_branch_length=1)
    array([[False, False, False, False],
           [False, False, False, False],
           [False, False, False, False]])
    >>> arr3 = np.array([
    ...     [False, True, False],
    ...     [False, True, False],
    ...     [False, True, False]
    ... ])
    >>> prune_skeletonized_image(arr3, spur_branch_length=2)
    array([[False,  True, False],
           [False,  True, False],
           [False,  True, False]])
    """
    img = image.copy()
    rows, cols = img.shape

    for _ in range(spur_branch_length):
        endpoints = []

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if img[i][j] and is_endpoint(img, i, j):
                    endpoints.append((i, j))
        for x, y in endpoints:
            img[x][y] = False
    return img


if __name__ == "__main__":
    # Read original (skeletonized) image
    skeleton_lena_path = (
        Path(__file__).resolve().parent.parent / "image_data" / "skeleton_lena.png"
    )
    skeleton_lena = np.array(Image.open(skeleton_lena_path))

    # Apply pruning operation to a skeletonized image
    output = prune_skeletonized_image(gray_to_binary(rgb_to_gray(skeleton_lena)))

    # Save the output image
    pil_img = Image.fromarray(output).convert("RGB")
    pil_img.save("result_pruned.png")
