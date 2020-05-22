"""
Implementation Burke's algorithm (dithering)
"""
from cv2 import destroyAllWindows, imread, imshow, waitKey
import numpy as np


class Burkes:
    """
    Burke's algorithm is using for converting grayscale image to black and white version
    Source: Source: https://en.wikipedia.org/wiki/Dither

    Note:
        * Best results are given with threshold= ~1/2 * max greyscale value.
        * This implementation get RGB image and converts it to greyscale in runtime.
    """

    def __init__(self, input_img, threshold: int):
        self.min_threshold = 0
        # max greyscale value for #FFFFFF
        self.max_threshold = int(self.get_greyscale(255, 255, 255))

        if not self.min_threshold < threshold < self.max_threshold:
            raise ValueError(f"Factor value should be from 0 to {self.max_threshold}")

        self.input_img = input_img
        self.threshold = threshold
        self.width, self.height = self.input_img.shape[1], self.input_img.shape[0]

        # error table size (+4 columns and +1 row) greater than input image because of
        # lack of if statements
        self.error_table = [
            [0 for _ in range(self.height + 4)] for __ in range(self.width + 1)
        ]
        self.output_img = np.ones((self.width, self.height, 3), np.uint8) * 255

    @classmethod
    def get_greyscale(cls, blue: int, green: int, red: int) -> float:
        """
        >>> Burkes.get_greyscale(3, 4, 5)
        3.753
        """
        return 0.114 * blue + 0.587 * green + 0.2126 * red

    def process(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                greyscale = int(self.get_greyscale(*self.input_img[y][x]))
                if self.threshold > greyscale + self.error_table[y][x]:
                    self.output_img[y][x] = (0, 0, 0)
                    current_error = greyscale + self.error_table[x][y]
                else:
                    self.output_img[y][x] = (255, 255, 255)
                    current_error = greyscale + self.error_table[x][y] - 255
                """
                Burkes error propagation (`*` is current pixel):

                                 *          8/32        4/32
                2/32    4/32    8/32    4/32    2/32
                """
                self.error_table[y][x + 1] += int(8 / 32 * current_error)
                self.error_table[y][x + 2] += int(4 / 32 * current_error)
                self.error_table[y + 1][x] += int(8 / 32 * current_error)
                self.error_table[y + 1][x + 1] += int(4 / 32 * current_error)
                self.error_table[y + 1][x + 2] += int(2 / 32 * current_error)
                self.error_table[y + 1][x - 1] += int(4 / 32 * current_error)
                self.error_table[y + 1][x - 2] += int(2 / 32 * current_error)


if __name__ == "__main__":
    # create Burke's instances with original images in greyscale
    burkes_instances = [
        Burkes(imread("image_data/lena.jpg", 1), threshold)
        for threshold in (1, 126, 130, 140)
    ]

    for burkes in burkes_instances:
        burkes.process()

    for burkes in burkes_instances:
        imshow(
            f"Original image with dithering threshold: {burkes.threshold}",
            burkes.output_img,
        )

    waitKey(0)
    destroyAllWindows()
