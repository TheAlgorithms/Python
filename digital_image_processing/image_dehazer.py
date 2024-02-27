import numpy as np
import cv2

"""
Implemented an image de-hazer using OpenCV and Dark Channel
"""


def dehaze_image(
    image: np.ndarray, omega: float = 0.78, t0: float = 0.01
) -> np.ndarray:
    """
    Dehaze an input image using the dark channel prior method.
    Args:
        image: Input a hazy image as a NumPy array.
        omega: Weighting factor for transmission map calculation. Default: 0.78.
        t0: Threshold for minimum transmission value. Default: 0.01.
    Returns:
        Dehazed image as a NumPy array.
    Example:
    >>> input_image = cv2.imread('image_data/haze.jpg')
    """

    dark_channel = cv2.ximgproc.createFastGlobalSmootherFilter(image, 10, 0.05)
    dark_channel = dark_channel.filter(image)

    # Step 2: Estimate the atmospheric light of the image
    atmospheric_light = np.percentile(image, 90, axis=(0, 1))

    # Step 3: Calculate the transmission map
    transmission = 1 - omega * dark_channel / atmospheric_light
    transmission[transmission < t0] = t0

    # Step 4: Dehaze the image
    dehazed_channels = []
    for i in range(3):
        dehazed_channel = (
            (image[:, :, i].astype(np.float32) - atmospheric_light[i])
            / transmission[:, :, 0]
        ) + atmospheric_light[i]
        dehazed_channels.append(dehazed_channel)

    dehazed_image = np.stack(dehazed_channels, axis=-1)
    dehazed_image = np.clip(dehazed_image, 0, 255).astype(np.uint8)

    return dehazed_image


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # Load the input hazy image from a file
    input_image = cv2.imread("image_path")

    # Apply the de-hazing function to the input image
    dehazed_result = dehaze_image(input_image)

    # Create a side-by-side comparison of the input and de-hazed images
    result = np.hstack((input_image, dehazed_result))

    # Display the images using OpenCV
    cv2.imshow("Image", result)

    # Wait for a key press and then close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
