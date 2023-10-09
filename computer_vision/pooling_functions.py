import numpy as np
from PIL import Image


class PoolingLayer:
    def __init__(self, size: int, stride: int, pooling_type: str = "max"):
        """
        Pooling layer can be initialized with the following parameters:
        Args:
            size: size of pooling matrix
            stride: the number of pixels shifts over the input matrix
            pooling_type: type of pooling to be performed, can be either "max" or "avg"
        """
        self.size = size
        self.stride = stride
        self.pooling_type = pooling_type

    def forward(self, arr: np.ndarray) -> np.ndarray:
        """
        This function performs pooling on the input array of 2D matrix(image)

        Args:
            arr: numpy array

        Returns:
            numpy array of pooled matrix
        """
        arr = np.array(arr)
        if arr.shape[0] != arr.shape[1]:
            raise ValueError("The input array is not a square matrix")
        i = 0
        j = 0
        mat_i = 0
        mat_j = 0

        # compute the shape of the output matrix
        pool_shape = (arr.shape[0] - self.size) // self.stride + 1

        # initialize the output matrix with zeros of shape pool_shape
        updated_arr = np.zeros((pool_shape, pool_shape))

        while i < arr.shape[0]:
            # if the end of the matrix is reached, break
            if i + self.size > arr.shape[0]:
                break
            while j < arr.shape[1]:
                # if the end of the matrix is reached, break
                if j + self.size > arr.shape[1]:
                    break
                # compute the maximum/average of the pooling matrix
                if self.pooling_type == "max":
                    updated_arr[mat_i][mat_j] = np.max(arr[i : i + self.size, j : j + self.size])
                elif self.pooling_type == "avg":
                    updated_arr[mat_i][mat_j] = int(np.average(arr[i : i + self.size, j : j + self.size]))
                else:
                    raise ValueError("Invalid pooling type")

                # shift the pooling matrix by stride of column pixels
                j += self.stride
                mat_j += 1

            # shift the pooling matrix by stride of row pixels
            i += self.stride
            mat_i += 1
            # reset the column index to 0
            j = 0
            mat_j = 0

        return updated_arr


# Main Function
if __name__ == "__main__":
    from doctest import testmod

    testmod(name="PoolingLayer", verbose=True)

    # Loading the image
    image = Image.open("path_to_image")

    # Converting the image to numpy array and maxpooling, displaying the result
    # Ensure that the image is a square matrix

    maxpooling_layer = PoolingLayer(size=3, stride=2, pooling_type="max")
    maxpooled_image = maxpooling_layer.forward(np.array(image))
    Image.fromarray(maxpooled_image).show()

    # Converting the image to numpy array and averagepooling, displaying the result
    # Ensure that the image is a square matrix

    avgpooling_layer = PoolingLayer(size=3, stride=2, pooling_type="avg")
    avgpooled_image = avgpooling_layer.forward(np.array(image))
    Image.fromarray(avgpooled_image).show()

