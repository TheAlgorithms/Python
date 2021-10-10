import numpy as np
from PIL import Image


def rgb2gray(rgb):
    """
    Return gray image from rgb image
    """
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def gray2binary(gray):
    """
    Return binary image from gray image
    """
    return (127 < gray) & (gray <= 255)


def dilation(image, kernel):
    """
    Return dilated image
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
            if summation > 0:
                output[y, x] = 1
            else:
                output[y, x] = 0
    return output


# kernel to be applied
structuring_element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])


if __name__ == "__main__":
    # read original image
    image = np.array(Image.open(r"..\image_data\lena.jpg"))
    # convert it into binary image
    binary = gray2binary(rgb2gray(image))
    # Apply dilation operation
    output = dilation(binary, structuring_element)
    # Save the output image
    pil_img = Image.fromarray(output).convert("RGB")
    pil_img.save("result_dilation.png")
