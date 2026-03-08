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


def erosion(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Return eroded image

    >>> erosion(np.array([[True, True, False]]), np.array([[0, 1, 0]]))
    array([[False, False, False]])
    >>> erosion(np.array([[True, False, False]]), np.array([[1, 1, 0]]))
    array([[False, False, False]])
    """
    output = np.zeros_like(image)
    image_padded = np.zeros(
        (image.shape[0] + kernel.shape[0] - 1, image.shape[1] + kernel.shape[1] - 1)
    )

    # Copy image to padded image
    image_padded[kernel.shape[0] - 2 : -1 :, kernel.shape[1] - 2 : -1 :] = image

    # Iterate over image & apply kernel
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            summation = (
                kernel * image_padded[y : y + kernel.shape[0], x : x + kernel.shape[1]]
            ).sum()
            output[y, x] = int(summation == 5)
    return output


if __name__ == "__main__":
    # read original image
    lena_path = Path(__file__).resolve().parent / "image_data" / "lena.jpg"
    lena = np.array(Image.open(lena_path))

    # kernel to be applied
    structuring_element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

    # Apply erosion operation to a binary image
    output = erosion(gray_to_binary(rgb_to_gray(lena)), structuring_element)

    # Save the output image
    pil_img = Image.fromarray(output).convert("RGB")
    pil_img.save("result_erosion.png")
