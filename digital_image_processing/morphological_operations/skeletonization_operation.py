# @Author: @joydipb01
# @File: skeletonization_operation.py
# @Time: 2025-10-03 13:45 IST

import numpy as np
from PIL import Image
from pathlib import Path


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


def neighbours(image: np.ndarray, x: int, y: int) -> list:
    """
    Return 8-neighbours of point (x, y), in clockwise order

    >>> neighbours(1, 1, np.array([[True, True, False], [True, False, False], [False, True, False]]))
    [np.True_, np.False_, np.False_, np.False_, np.True_, np.False_, np.True_, np.True_]
    >>> neighbours(1, 2, np.array([[True, True, False, True], [True, False, False, True], [False, True, False, True]]))
    [np.False_, np.True_, np.True_, np.True_, np.False_, np.True_, np.False_, np.True_]
    """
    img = image
    return [
        img[x-1][y], img[x-1][y+1], img[x][y+1], img[x+1][y+1],
        img[x+1][y], img[x+1][y-1], img[x][y-1], img[x-1][y-1]
    ]


def transitions(neighbors: list) -> int:
    """
    Count 0->1 transitions in the neighborhood
    
    >>> transitions([np.False_, np.True_, np.True_, np.False_, np.True_, np.False_, np.False_, np.False_])
    2
    >>> transitions([np.True_, np.True_, np.True_, np.True_, np.True_, np.True_, np.True_, np.True_])
    0
    >>> transitions([np.False_, np.False_, np.False_, np.False_, np.False_, np.False_, np.False_, np.False_])
    0
    >>> transitions([np.False_, np.True_, np.False_, np.True_, np.False_, np.True_, np.False_, np.True_])
    4
    >>> transitions([np.True_, np.False_, np.True_, np.False_, np.True_, np.False_, np.True_, np.False_])
    4
    """
    n = neighbors + [neighbors[0]]
    return int(sum((n1 == 0 and n2 == 1) for n1, n2 in zip(n, n[1:])))


def skeletonize_image(image: np.ndarray) -> np.ndarray:
    """
    Apply Zhang-Suen thinning to binary image for skeletonization.
    Source: https://rstudio-pubs-static.s3.amazonaws.com/302782_e337cfbc5ad24922bae96ca5977f4da8.html
    
    >>> skeletonize_image(np.array([[np.False_, np.True_, np.False_],
    ...                 [np.True_, np.True_, np.True_],
    ...                 [np.False_, np.True_, np.False_]]))
    array([[False,  True, False],
           [ True,  True,  True],
           [False,  True, False]])
    >>> skeletonize_image(np.array([[np.False_, np.False_, np.False_],
    ...                  [np.False_, np.True_, np.False_],
    ...                  [np.False_, np.False_, np.False_]]))
    array([[False, False, False],
           [False,  True, False],
           [False, False, False]])
    """
    img = image.copy()
    changing1 = changing2 = True

    while changing1 or changing2:

        # Step 1: Points to be removed in the first sub-iteration
        changing1 = []
        rows, cols = img.shape
        for x in range(1, rows - 1):
            for y in range(1, cols - 1):
                P = img[x][y]
                if P != 1:
                    continue
                neighbours_list = neighbours(img, x, y)
                total_transitions = transitions(neighbours_list)
                N = sum(neighbours_list)
                if (2 <= N <= 6 and
                    total_transitions == 1 and
                    neighbours_list[0] * neighbours_list[2] * neighbours_list[4] == 0 and
                    neighbours_list[2] * neighbours_list[4] * neighbours_list[6] == 0):
                    changing1.append((x, y))
        for x, y in changing1:
            img[x][y] = 0

        # Step 2: Points to be removed in the second sub-iteration
        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, cols - 1):
                P = img[x][y]
                if P != 1:
                    continue
                neighbours_list = neighbours(img, x, y)
                total_transitions = transitions(neighbours_list)
                N = sum(neighbours_list)
                if (2 <= N <= 6 and
                    total_transitions == 1 and
                    neighbours_list[0] * neighbours_list[2] * neighbours_list[6] == 0 and
                    neighbours_list[0] * neighbours_list[4] * neighbours_list[6] == 0):
                    changing2.append((x, y))
        for x, y in changing2:
            img[x][y] = 0

    return img


if __name__ == "__main__":
    # Read original image
    lena_path = Path(__file__).resolve().parent.parent / "image_data" / "lena.jpg"
    lena = np.array(Image.open(lena_path))

    # Apply skeletonization operation to a binary image
    output = skeletonize_image(gray_to_binary(rgb_to_gray(lena)))

    # Save the output image
    pil_img = Image.fromarray(output).convert("RGB")
    pil_img.save("result_skeleton.png")