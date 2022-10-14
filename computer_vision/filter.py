import cv2
import numpy as np


class Filter:
    def __int__(self, image: str) -> None:

        self.image = image

    def image_read(self) -> np.array:
        """
        Read the image
        :return: The image as numpy array
        """
        return cv2.imread(self.image, 0)

    def get_identity_kernel(self) -> np.array:
        """
        Apply identity kernel
        :return: array with the value of the middle element
        is 1 and all the other elements are 0
        """
        return np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    def get_blur_kernel(self) -> np.array:
        """
        Kernel for box blur filter
        :return:  unity matrix which is divided by 9
        """
        return np.array(
            [
                [0.1111111, 0.1111111, 0.1111111],
                [0.1111111, 0.1111111, 0.1111111],
                [0.1111111, 0.1111111, 0.1111111],
            ]
        )

    def get_sharp_kernel(self) -> np.array:
        """
        Apply kernel for sharpening
        :return: sharpening filter array
        """
        return np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    def get_emboss_kernel(self) -> np.array:
        """
        Apply kernel for embossing
        :return: embossing filter array
        """
        return np.array([[-1, 0, 0], [0, 0, 0], [0, 0, 1]])

    def image_shape(self) -> tuple[int, int]:
        """
        Get the Image Shape
        :return: The number of rows and columns of the Image
        """
        image = cv2.imread(self.image, 0)
        rows, columns = image.shape
        return rows, columns

    def get_new_image(self) -> np.array:
        """
        Convolve mask over the image
        :return: New Image as numpy array
        """
        rows, columns = self.image_shape()
        return np.zeros([rows, columns])

    def average_mask(self) -> np.array:
        """
        Averaging filter Mask
        :return: mask with 3×3 dim
        """
        return (np.ones([3, 3], dtype=int)) / 9

    def get_ready(self) -> tuple[int, int, np.array, np.array]:
        """
        Read the image, Get the Image Shape, Convolve mask over the image
        :return: row, columns , image and new image
        """
        image = self.image_read()
        rows, columns = self.image_shape()
        new_image = self.get_new_image()

        return rows, columns, image, new_image

    def set_up_filter(self, kernel) -> np.array:
        """
        kernel is used for specifying the kernel operation
        :param kernel: choose the kernel we want to apply
        :return: the image after applying the filter with the chosen kernel
        """
        image = self.image_read()
        kernel = kernel
        filter_image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
        return filter_image

    def average(self) -> np.array:
        """
        :return: image after applying the Average filter
        """
        rows, columns, image, new_image = self.get_ready()
        mask = self.average_mask()
        for i in range(1, rows - 1):
            for j in range(1, columns - 1):
                temp = (
                    image[i - 1, j - 1] * mask[0, 0]
                    + image[i - 1, j] * mask[0, 1]
                    + image[i - 1, j + 1] * mask[0, 2]
                    + image[i, j - 1] * mask[1, 0]
                    + image[i, j] * mask[1, 1]
                    + image[i, j + 1] * mask[1, 2]
                    + image[i + 1, j - 1] * mask[2, 0]
                    + image[i + 1, j] * mask[2, 1]
                    + image[i + 1, j + 1] * mask[2, 2]
                )

                new_image[i, j] = temp
        return new_image.astype(np.uint8)

    def median(self) -> np.array:
        """
        Traverse the image find the median of the pixels and
        replace the center pixel by median filter
        :return:  image after applying the median filter
        """
        rows, columns, image, new_image = self.get_ready()
        for i in range(1, rows - 1):
            for j in range(1, columns - 1):
                temp = [
                    image[i - 1, j - 1],
                    image[i - 1, j],
                    image[i - 1, j + 1],
                    image[i, j - 1],
                    image[i, j],
                    image[i, j + 1],
                    image[i + 1, j - 1],
                    image[i + 1, j],
                    image[i + 1, j + 1],
                ]

                temp = sorted(temp)
                new_image[i, j] = temp[4]
        return new_image.astype(np.uint8)

    def filter_2d(self) -> np.array:
        """
        Use Identity Kernel with 2D filter
        :return: Filtered image with  Identity Kernel
        """
        kernel = self.get_identity_kernel()
        return self.set_up_filter(kernel)

    def blur_filter(self) -> np.array:
        """
        Use Kernel Blur with 2D filter
        :return: Blur Filtered image with Blur Kernel
        """
        kernel = self.get_blur_kernel()
        return self.set_up_filter(kernel)

    def gaussian_blur(self) -> np.array:
        """
        Applying Gaussian Blur Filter using Gaussian Blur method
        :return: Gaussian Blur filtered image
        """
        image = self.image_read()
        gaussian_blur_filter_image = cv2.GaussianBlur(
            src=image, ksize=(3, 3), sigmaX=0, sigmaY=0
        )
        return gaussian_blur_filter_image

    def median_blur(self) -> np.array:
        """
        Applying median Blur Filter using median Blur method
        :return: Median Blur filtered image
        """
        image = self.image_read()
        median_blur_filtered_image = cv2.medianBlur(src=image, ksize=9)
        return median_blur_filtered_image

    def sharp_filter(self) -> np.array:
        """
        Use Sharp kernel with 2D filter
        :return: Sharpened image with sharp Kernel
        """
        kernel = self.get_sharp_kernel()
        return self.set_up_filter(kernel)

    def emboss_filter(self) -> np.array:
        """
        Use Emboss kernel with 2D filter
        :return: Embossed image with emboss Kernel
        """
        kernel = self.get_emboss_kernel()
        return self.set_up_filter(kernel)


# Main Function
if __name__ == "__main__":
    filter_object = Filter()
    filter_object.image = "path/image-name.png"
    cv2.imwrite("average.tif", filter_object.average())
    cv2.imwrite("median.tif", filter_object.median())
    cv2.imwrite("filter_2d.tif", filter_object.filter_2d())
    cv2.imwrite("blur_filter.tif", filter_object.blur_filter())
    cv2.imwrite("gaussian_blur.tif", filter_object.gaussian_blur())
    cv2.imwrite("median_blur.tif", filter_object.median_blur())
    cv2.imwrite("sharp_filter.tif", filter_object.sharp_filter())
    cv2.imwrite("emboss_filter.tif", filter_object.emboss_filter())
