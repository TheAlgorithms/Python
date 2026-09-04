"""Multiple image resizing techniques"""

import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey


class NearestNeighbour:
    """
    Simplest and fastest version of image resizing.
    Source: https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation
    """

    def __init__(self, img, dst_width: int, dst_height: int):
        if dst_width < 0 or dst_height < 0:
            raise ValueError("Destination width/height should be > 0")

        self.img = img
        self.src_w = img.shape[1]
        self.src_h = img.shape[0]
        self.dst_w = dst_width
        self.dst_h = dst_height

        self.ratio_x = self.src_w / self.dst_w
        self.ratio_y = self.src_h / self.dst_h

        self.output = self.output_img = (
            np.ones((self.dst_h, self.dst_w, 3), np.uint8) * 255
        )

    def process(self):
        for i in range(self.dst_h):
            for j in range(self.dst_w):
                self.output[i][j] = self.img[self.get_y(i)][self.get_x(j)]

    def get_x(self, x: int) -> int:
        """
        Get parent X coordinate for destination X
        :param x: Destination X coordinate
        :return: Parent X coordinate based on `x ratio`
        >>> nn = NearestNeighbour(imread("digital_image_processing/image_data/lena.jpg",
        ...                              1), 100, 100)
        >>> nn.ratio_x = 0.5
        >>> nn.get_x(4)
        2
        """
        return int(self.ratio_x * x)

    def get_y(self, y: int) -> int:
        """
        Get parent Y coordinate for destination Y
        :param y: Destination X coordinate
        :return: Parent X coordinate based on `y ratio`
        >>> nn = NearestNeighbour(imread("digital_image_processing/image_data/lena.jpg",
        ...                              1), 100, 100)
        >>> nn.ratio_y = 0.5
        >>> nn.get_y(4)
        2
        """
        return int(self.ratio_y * y)


class BilinearInterpolation:
    """
    Bilinear interpolation for image resizing.
    Source: https://en.wikipedia.org/wiki/Bilinear_interpolation
    """

    def __init__(self, img, dst_width: int, dst_height: int):
        if dst_width < 0 or dst_height < 0:
            raise ValueError("Destination width/height should be > 0")

        self.img = img
        self.src_w = img.shape[1]
        self.src_h = img.shape[0]
        self.dst_w = dst_width
        self.dst_h = dst_height

        self.ratio_x = self.src_w / self.dst_w
        self.ratio_y = self.src_h / self.dst_h

        self.output = np.ones((self.dst_h, self.dst_w, 3), np.uint8) * 255

    def process(self):
        for i in range(self.dst_h):
            for j in range(self.dst_w):
                x = self.ratio_x * j
                y = self.ratio_y * i

                x1, y1 = int(x), int(y)
                x2, y2 = min(x1 + 1, self.src_w - 1), min(y1 + 1, self.src_h - 1)

                a = x - x1
                b = y - y1

                top = (1 - a) * self.img[y1][x1] + a * self.img[y1][x2]
                bottom = (1 - a) * self.img[y2][x1] + a * self.img[y2][x2]
                self.output[i][j] = (1 - b) * top + b * bottom


class BicubicInterpolation:
    """
    Bicubic interpolation for image resizing.
    Source: https://en.wikipedia.org/wiki/Bicubic_interpolation
    """

    def __init__(self, img, dst_width: int, dst_height: int):
        if dst_width < 0 or dst_height < 0:
            raise ValueError("Destination width/height should be > 0")

        self.img = img
        self.src_w = img.shape[1]
        self.src_h = img.shape[0]
        self.dst_w = dst_width
        self.dst_h = dst_height

        self.ratio_x = self.src_w / self.dst_w
        self.ratio_y = self.src_h / self.dst_h

        self.output = np.ones((self.dst_h, self.dst_w, 3), np.uint8) * 255

    def cubic(self, x):
        abs_x = abs(x)
        if abs_x <= 1:
            return 1.5 * abs_x**3 - 2.5 * abs_x**2 + 1
        elif abs_x < 2:
            return -0.5 * abs_x**3 + 2.5 * abs_x**2 - 4 * abs_x + 2
        else:
            return 0

    def interpolate(self, x, y, channel):
        x1 = int(x)
        y1 = int(y)
        total = 0.0
        for m in range(-1, 3):
            for n in range(-1, 3):
                xm = min(max(x1 + m, 0), self.src_w - 1)
                yn = min(max(y1 + n, 0), self.src_h - 1)
                weight = self.cubic(m - (x - x1)) * self.cubic(n - (y - y1))
                total += self.img[yn, xm, channel] * weight
        return np.clip(total, 0, 255)

    def process(self):
        for i in range(self.dst_h):
            for j in range(self.dst_w):
                x = self.ratio_x * j
                y = self.ratio_y * i
                for c in range(3):  # For each color channel (R, G, B)
                    self.output[i, j, c] = self.interpolate(x, y, c)


if __name__ == "__main__":
    dst_w, dst_h = 800, 600
    im = imread("image_data/lena.jpg", 1)

    # Nearest Neighbour
    nn = NearestNeighbour(im, dst_w, dst_h)
    nn.process()
    imshow(f"Nearest Neighbor: {dst_w}x{dst_h}", nn.output)
    waitKey(0)

    # Bilinear Interpolation
    bi = BilinearInterpolation(im, dst_w, dst_h)
    bi.process()
    imshow(f"Bilinear Interpolation: {dst_w}x{dst_h}", bi.output)
    waitKey(0)

    # Bicubic Interpolation
    bc = BicubicInterpolation(im, dst_w, dst_h)
    bc.process()
    imshow(f"Bicubic Interpolation: {dst_w}x{dst_h}", bc.output)
    waitKey(0)

    destroyAllWindows()
