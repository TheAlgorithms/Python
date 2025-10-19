"""
Color Augmentation Module for Computer Vision

This module provides various color space augmentation techniques commonly used
in computer vision and deep learning for data augmentation during model training.

Reference: https://en.wikipedia.org/wiki/Data_augmentation
"""

import numpy as np
import cv2


def brightness_adjustment(image: np.ndarray, factor: float = 1.0) -> np.ndarray:
    """
    Adjust image brightness by modifying the V channel in HSV color space.

    Args:
        image: Input image in BGR format
        factor: Brightness multiplication factor (0.0 = black, 1.0 = original, >1.0 = brighter)

    Returns:
        Brightness adjusted image in BGR format

    Raises:
        ValueError: If brightness factor is negative

    Examples:
        >>> import numpy as np
        >>> img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        >>> result = brightness_adjustment(img, factor=1.2)
        >>> result.shape
        (100, 100, 3)
        >>> result.dtype
        dtype('uint8')
    """
    if factor < 0:
        raise ValueError("Brightness factor must be non-negative")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * factor, 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)


def contrast_adjustment(image: np.ndarray, factor: float = 1.0) -> np.ndarray:
    """
    Adjust image contrast by scaling pixel values around the mean.

    Args:
        image: Input image in BGR format
        factor: Contrast factor (0.0 = gray, 1.0 = original, >1.0 = more contrast)

    Returns:
        Contrast adjusted image in BGR format

    Raises:
        ValueError: If contrast factor is negative

    Examples:
        >>> import numpy as np
        >>> img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        >>> result = contrast_adjustment(img, factor=1.5)
        >>> result.shape
        (100, 100, 3)
        >>> result.dtype
        dtype('uint8')
    """
    if factor < 0:
        raise ValueError("Contrast factor must be non-negative")

    mean = np.mean(image, axis=(0, 1), keepdims=True)
    adjusted = mean + factor * (image - mean)
    return np.clip(adjusted, 0, 255).astype(np.uint8)


def saturation_adjustment(image: np.ndarray, factor: float = 1.0) -> np.ndarray:
    """
    Adjust image saturation by modifying the S channel in HSV color space.

    Args:
        image: Input image in BGR format
        factor: Saturation factor (0.0 = grayscale, 1.0 = original, >1.0 = more saturated)

    Returns:
        Saturation adjusted image in BGR format

    Raises:
        ValueError: If saturation factor is negative

    Examples:
        >>> import numpy as np
        >>> img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        >>> result = saturation_adjustment(img, factor=1.3)
        >>> result.shape
        (100, 100, 3)
        >>> result.dtype
        dtype('uint8')
    """
    if factor < 0:
        raise ValueError("Saturation factor must be non-negative")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * factor, 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)


def hue_shift(image: np.ndarray, shift: int = 0) -> np.ndarray:
    """
    Shift the hue channel in HSV color space.

    Args:
        image: Input image in BGR format
        shift: Hue shift value in degrees (-180 to 180)

    Returns:
        Hue shifted image in BGR format

    Raises:
        ValueError: If hue shift is outside valid range

    Examples:
        >>> import numpy as np
        >>> img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        >>> result = hue_shift(img, shift=30)
        >>> result.shape
        (100, 100, 3)
        >>> result.dtype
        dtype('uint8')
    """
    if not -180 <= shift <= 180:
        raise ValueError("Hue shift must be between -180 and 180")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = hsv.astype(np.int16)
    hsv[:, :, 0] = (hsv[:, :, 0] + shift) % 180
    hsv = hsv.astype(np.uint8)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


def gamma_correction(image: np.ndarray, gamma: float = 1.0) -> np.ndarray:
    """
    Apply gamma correction to adjust image brightness non-linearly.

    Reference: https://en.wikipedia.org/wiki/Gamma_correction

    Args:
        image: Input image in BGR format
        gamma: Gamma value (< 1.0 = brighter, 1.0 = no change, > 1.0 = darker)

    Returns:
        Gamma corrected image in BGR format

    Raises:
        ValueError: If gamma is not positive

    Examples:
        >>> import numpy as np
        >>> img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        >>> result = gamma_correction(img, gamma=1.5)
        >>> result.shape
        (100, 100, 3)
        >>> result.dtype
        dtype('uint8')
    """
    if gamma <= 0:
        raise ValueError("Gamma must be positive")

    inv_gamma = 1.0 / gamma
    table = np.array(
        [((i / 255.0) ** inv_gamma) * 255 for i in range(256)]
    ).astype(np.uint8)
    return cv2.LUT(image, table)


def histogram_equalization(
    image: np.ndarray, clip_limit: float = 2.0, tile_grid_size: tuple[int, int] = (8, 8)
) -> np.ndarray:
    """
    Apply CLAHE (Contrast Limited Adaptive Histogram Equalization).

    This technique improves contrast by equalizing the histogram in localized regions.
    Reference: https://en.wikipedia.org/wiki/Adaptive_histogram_equalization

    Args:
        image: Input image in BGR format
        clip_limit: Threshold for contrast limiting
        tile_grid_size: Size of grid for histogram equalization

    Returns:
        Equalized image in BGR format

    Examples:
        >>> import numpy as np
        >>> img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        >>> result = histogram_equalization(img)
        >>> result.shape
        (100, 100, 3)
        >>> result.dtype
        dtype('uint8')
    """
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    lab[:, :, 0] = clahe.apply(lab[:, :, 0])
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)


def channel_shuffle(image: np.ndarray) -> np.ndarray:
    """
    Randomly shuffle color channels (B, G, R) for data augmentation.

    Args:
        image: Input image in BGR format

    Returns:
        Channel shuffled image

    Examples:
        >>> import numpy as np
        >>> np.random.seed(42)
        >>> img = np.random.randint(0, 255, (50, 50, 3), dtype=np.uint8)
        >>> result = channel_shuffle(img)
        >>> result.shape
        (50, 50, 3)
        >>> result.dtype
        dtype('uint8')
    """
    channels = list(cv2.split(image))
    np.random.shuffle(channels)
    return cv2.merge(channels)


def grayscale_conversion(image: np.ndarray, keep_channels: bool = True) -> np.ndarray:
    """
    Convert image to grayscale using standard luminosity formula.

    Reference: https://en.wikipedia.org/wiki/Grayscale

    Args:
        image: Input image in BGR format
        keep_channels: If True, return 3-channel grayscale, else single channel

    Returns:
        Grayscale image (3-channel if keep_channels=True, else 1-channel)

    Examples:
        >>> import numpy as np
        >>> img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        >>> result = grayscale_conversion(img, keep_channels=True)
        >>> result.shape
        (100, 100, 3)
        >>> result = grayscale_conversion(img, keep_channels=False)
        >>> result.shape
        (100, 100)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if keep_channels:
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    return gray


def temperature_tint(
    image: np.ndarray, temperature: float = 0.0, tint: float = 0.0
) -> np.ndarray:
    """
    Adjust color temperature and tint of an image.

    Temperature affects the blue-red balance, while tint affects the green-magenta balance.

    Args:
        image: Input image in BGR format
        temperature: Temperature adjustment (-1.0 to 1.0, negative = cooler, positive = warmer)
        tint: Tint adjustment (-1.0 to 1.0, negative = green, positive = magenta)

    Returns:
        Adjusted image in BGR format

    Examples:
        >>> import numpy as np
        >>> img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        >>> result = temperature_tint(img, temperature=0.5, tint=0.2)
        >>> result.shape
        (100, 100, 3)
        >>> result.dtype
        dtype('uint8')
    """
    result = image.astype(np.float32)

    # Temperature: affect blue and red channels
    if temperature > 0:  # Warmer
        result[:, :, 2] = np.clip(result[:, :, 2] * (1 + temperature * 0.3), 0, 255)
        result[:, :, 0] = np.clip(result[:, :, 0] * (1 - temperature * 0.3), 0, 255)
    else:  # Cooler
        result[:, :, 0] = np.clip(result[:, :, 0] * (1 - temperature * 0.3), 0, 255)
        result[:, :, 2] = np.clip(result[:, :, 2] * (1 + temperature * 0.3), 0, 255)

    # Tint: affect green channel
    result[:, :, 1] = np.clip(result[:, :, 1] * (1 + tint * 0.3), 0, 255)

    return result.astype(np.uint8)


if __name__ == "__main__":
    import doctest

    doctest.testmod()