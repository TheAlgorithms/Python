from PIL import Image
import numpy as np

"""
Otsu thresholding algorithm for image processing
https://en.wikipedia.org/wiki/Otsu%27s_method
"""


def otsu_threshold(image: Image) -> Image:
    """
    image: is a grayscale PIL image object
    """
    # Convert the image to numpy array
    pixel_array = np.array(image)

    # Compute histogram
    hist, bins = np.histogram(pixel_array, bins=256, range=(0, 256))

    # Compute cumulative sum of the histogram
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # Compute between class variance
    total_pixels = pixel_array.size
    current_max, threshold = 0, 0
    sum_total, sum_foreground, weight_background, weight_foreground = 0, 0, 0, 0

    for i in range(256):
        sum_total += i * hist[i]

    for i in range(256):
        weight_background += hist[i]
        if weight_background == 0:
            continue
        weight_foreground = total_pixels - weight_background
        if weight_foreground == 0:
            break
        sum_foreground += i * hist[i]

        mean_background = sum_foreground / weight_background
        mean_foreground = (sum_total - sum_foreground) / weight_foreground

        between_class_variance = (
            weight_background
            * weight_foreground
            * (mean_background - mean_foreground) ** 2
        )

        if between_class_variance > current_max:
            current_max = between_class_variance
            threshold = i

    # Apply threshold to the image
    binary_image = pixel_array > threshold
    binary_image = binary_image.astype(np.uint8) * 255

    # Convert numpy array back to PIL image
    return Image.fromarray(binary_image)


if __name__ == "__main__":
    image = otsu_threshold(Image.open("path_to_image").convert("L"))
    image.save("output_image_path")
