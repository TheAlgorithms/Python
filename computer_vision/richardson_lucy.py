"""
https://en.wikipedia.org/wiki/Motion_blur
https://en.wikipedia.org/wiki/Image_noise
https://en.wikipedia.org/wiki/Richardson-Lucy_deconvolution
"""
import imageio.v2 as imageio
import numpy as np
from numpy.fft import fft2, ifft2, ifftshift


def root_mean_square_error(original: np.ndarray, reference: np.ndarray) -> float:
    """Simple implementation of Root Mean Squared Error
    for two N dimensional numpy arrays.

    Examples:
        >>> root_mean_square_error(np.array([1, 2, 3]), np.array([1, 2, 3]))
        0.0
        >>> root_mean_square_error(np.array([1, 2, 3]), np.array([2, 2, 2]))
        0.816496580927726
        >>> root_mean_square_error(np.array([1, 2, 3]), np.array([6, 4, 2]))
        3.1622776601683795
    """
    return np.sqrt(((original - reference) ** 2).mean())


def pad_to_size(image: np.ndarray, reference: np.ndarray):
    """Pad an image to have final shape equal to reference image."""
    p, q = (size for size in reference.shape)
    difference = (
        (p - image.shape[0]) // 2,
        (q - image.shape[1]) // 2 + (q - image.shape[1]) % 2,
    )

    return np.pad(image, difference, mode="constant")


def normalize_image(
    image: np.ndarray, cap: float = 255.0, data_type: np.dtype = np.uint8
) -> np.ndarray:
    """
    Normalizes image in Numpy 2D array format, between ranges 0-cap,
    as to fit uint8 type.

    Args:
        image: 2D numpy array representing image as matrix, with values in any range
        cap: Maximum cap amount for normalization
        data_type: numpy data type to set output variable to
    Returns:
        return 2D numpy array of type uint8, corresponding to limited range matrix

    Examples:
        >>> normalize_image(np.array([[1, 2, 3], [4, 5, 10]]),
        ...                 cap=1.0, data_type=np.float64)
        array([[0.        , 0.11111111, 0.22222222],
               [0.33333333, 0.44444444, 1.        ]])
        >>> normalize_image(np.array([[4, 4, 3], [1, 7, 2]]))
        array([[127, 127,  85],
               [  0, 255,  42]], dtype=uint8)
    """
    normalized = (image - np.min(image)) / (np.max(image) - np.min(image)) * cap
    return normalized.astype(data_type)


def gaussian_noise(size: tuple, mean=0, std=0.05):
    """Creates normal distribution array with given size to use as noise.

    Args:
        size: Size of the desired output image
        mean: Mean to use within the Gaussian Function
        std: Standard deviation to use within the Gaussian Function

    Returns:
        Matrix with given size, containing generated gaussian values.

    Example:
        >>> np.random.seed(0)
        >>> gaussian_noise((5, 5))
        array([[ 22.49166741,   5.10200441,  12.4789093 ,  28.57138829,
                 23.81136437],
               [-12.46029297,  12.11362732,  -1.92980441,  -1.31604036,
                  5.2351309 ],
               [  1.83655553,  18.54198721,   9.703231  ,   1.55135646,
                  5.65925622],
               [  4.25434767,  19.04950818,  -2.61576786,   3.9916132 ,
                -10.88972068],
               [-32.55062015,   8.33363709,  11.02156154,  -9.46260401,
                 28.93937146]])
    """
    noise = np.multiply(np.random.normal(mean, std, size), 255)
    return noise


def gaussian_filter(k: int = 5, sigma: float = 1.0) -> np.ndarray:
    """Generates a matrix with weights corresponding to centered gaussian distribution.

    Args:
        k: Lateral size of the kernel.
        sigma: Standard deviation to be used when generating distribution

    Returns:
        np.ndarray: [k x k] sized kernel to be used as filter

    Examples:
        >>> gaussian_filter()
        array([[0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902],
               [0.01330621, 0.0596343 , 0.09832033, 0.0596343 , 0.01330621],
               [0.02193823, 0.09832033, 0.16210282, 0.09832033, 0.02193823],
               [0.01330621, 0.0596343 , 0.09832033, 0.0596343 , 0.01330621],
               [0.00296902, 0.01330621, 0.02193823, 0.01330621, 0.00296902]])
    """
    arx = np.arange((-k // 2) + 1.0, (k // 2) + 1.0)
    x, y = np.meshgrid(arx, arx)
    filt = np.exp(-(1 / 2) * (np.square(x) + np.square(y)) / np.square(sigma))
    return filt / np.sum(filt)


def convolve(matrix: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Convolves a given kernel around a matrix through the frequency domain, using Fourier transformations.

    Args:
        matrix: Numpy array containing values to be convolved
        kernel: Kernel (with all dimensions smaller than those of the matrix) with weights to apply to each pixel.

    Returns:
        np.ndarray: Final equally shaped matrix with convoluted pixels.

    Examples:
        >>> matrix = np.array([[-1.45436567,  0.04575852],
        ...                    [-0.18718385,  1.53277921]])
        >>> kernel = np.array([[1, 0], [0, 1]])
        >>> convolve(matrix, kernel)
        array([[ 0.07841354, -0.14142533],
               [-0.14142533,  0.07841354]])
    """
    if kernel.shape[0] > matrix.shape[1] or kernel.shape[1] > matrix.shape[1]:
        return matrix
    kernel = pad_to_size(kernel, matrix)

    kernel_f = fft2(kernel)
    matrix_f = fft2(matrix)

    return ifftshift(ifft2(np.multiply(matrix_f, kernel_f))).real


def get_motion_psf(shape: tuple, angle: float, num_pixel_dist: int = 20) -> np.ndarray:
    """Generate an array with given shape corresponding to Point Spread Function for the desired angle.

    Args:
        shape: The shape of the image.
        angle: The angle of the motion blur. Should be in degrees. [0, 360)
        num_pixel_dist: The distance of the motion blur. [0, infinity)
            Remember that the distance is measured in pixels. Greater will be more blurry

    Returns:
        np.ndarray: The point-spread array associated with the motion blur.

    Examples:
        >>> shape = (3, 3)
        >>> angle = 15
        >>> get_motion_psf(shape, angle, num_pixel_dist=3)
        array([[0.        , 0.33333333, 0.        ],
               [0.        , 0.33333333, 0.        ],
               [0.33333333, 0.        , 0.        ]])
    """
    psf = np.zeros(shape)
    center = np.array([shape[0] - 1, shape[1] - 1]) // 2
    radians = angle / 180 * np.pi
    phase = np.array([np.cos(radians), np.sin(radians)])
    for i in range(num_pixel_dist):
        offset_x = int(center[0] - np.round_(i * phase[0]))
        offset_y = int(center[1] - np.round_(i * phase[1]))
        psf[offset_x, offset_y] = 1
    psf /= psf.sum()

    return psf


def richardson_lucy(
    degraded: np.ndarray, function_kernel: np.ndarray, steps: int
) -> np.ndarray:
    """Richardson-Lucy method to restore an image affected by known motion blur function, as well as arbitrary steps
    to perform during iterative image restoration.

    Args:
        degraded: Observed image, considered to be degraded - to be restored
        function_kernel: Supposed function used to blur original image
        steps: Iterative steps to take for restoring image

    Returns:
        np.ndarray: Restored image after method application


    Examples:
        >>> np.random.seed(0)
        >>> shape = (3, 3)
        >>> degraded = gaussian_noise(shape)
        >>> kernel = np.identity(2)
        >>> richardson_lucy(degraded, kernel, steps=4)
        array([[1.16272775e+02, 0.00000000e+00, 7.58091075e+01],
               [2.40582123e+01, 2.09006034e+01, 0.00000000e+00],
               [0.00000000e+00, 1.52620152e-02, 1.31734948e+00]])
    """
    estimated_img = np.full(shape=degraded.shape, fill_value=1, dtype="float64")

    for i in range(steps):
        dividend = convolve(estimated_img, function_kernel)
        quotient = np.divide(degraded, dividend, where=dividend != 0)

        estimated_img = np.multiply(
            estimated_img, convolve(quotient, np.flip(function_kernel))
        )

        estimated_img = np.clip(estimated_img, 0, 255)

    return estimated_img


def main():
    input_file = str(input()).rstrip()
    degraded= imageio.imread(input_file)

    angle = int(input())
    steps = int(input())

    # The Richardson-Lucy iterative method is used to restore an image
    # degraded by motion blur and noise.
    restored = richardson_lucy(degraded, get_motion_psf(degraded.shape, angle), steps)

    print(root_mean_square_error(degraded, restored))


if __name__ == "__main__":
    main()
