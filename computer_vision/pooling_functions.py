# Source : https://computersciencewiki.org/index.php/Max-pooling_/_Pooling
# Importing the libraries
import numpy as np
from PIL import Image


# Maxpooling Function
def maxpooling(arr:list, size:int, stride:int) -> list:
    """
    This function is used to perform maxpooling on the input array of 2D matrix(image)

    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of maxpooled matrix
    """
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    # compute the shape of the output matrix
    maxpool_shape = (arr.shape[0] - size) // stride + 1
    # initialize the output matrix with zeros of shape maxpool_shape
    updated_arr = np.zeros((maxpool_shape, maxpool_shape))

    while i < arr.shape[0]:
        if i + size > arr.shape[0]:
            # if the end of the matrix is reached, break
            break
        while j < arr.shape[1]:
            # if the end of the matrix is reached, break
            if j + size > arr.shape[1]:
                break
            # compute the maximum of the pooling matrix
            updated_arr[i][j] = np.max(arr[i:i + size, j:j + size])
            # shift the pooling matrix by stride of column pixels
            j += stride

        # shift the pooling matrix by stride of row pixels
        i += stride
        # reset the column index to 0
        j = 0

    return updated_arr


# Averagepooling Function
def avgpooling(arr:list, size:int, stride:int) -> list:
    """
    This function is used to perform avgpooling on the input array of 2D matrix(image)
    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of avgpooled matrix
    """
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    # compute the shape of the output matrix
    avgpool_shape = (arr.shape[0] - size) // stride + 1
    # initialize the output matrix with zeros of shape avgpool_shape
    updated_arr = np.zeros((avgpool_shape, avgpool_shape))

    while i < arr.shape[0]:
        # if the end of the matrix is reached, break
        if i + size > arr.shape[0]:
            break
        while j < arr.shape[1]:
            # if the end of the matrix is reached, break
            if j + size > arr.shape[1]:
                break
            # compute the average of the pooling matrix
            updated_arr[i][j] = int(np.average(arr[i:i + size, j:j + size]))
            # shift the pooling matrix by stride of column pixels
            j += stride

        # shift the pooling matrix by stride of row pixels
        i += stride
        # reset the column index to 0
        j = 0

    return updated_arr


# Main Function
if __name__ == "__main__":
    # Loading the image
    image = Image.open("path_to_image")

    # Converting the image to numpy array and maxpooling, displaying the result
    # Ensure that the image is a square matrix

    # Parameters
    size = 3
    stride = 2
    Image.fromarray(maxpooling(np.array(image), size, stride)).show()

    # Converting the image to numpy array and averagepooling, displaying the result
    # Ensure that the image is a square matrix

    # Parameters
    size = 3
    stride = 2
    Image.fromarray(avgpooling(np.array(image), size, stride)).show()
