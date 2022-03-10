# Source : https://computersciencewiki.org/index.php/Max-pooling_/_Pooling
# Importing the libraries
import numpy as np
from PIL import Image


# Maxpooling Function
def maxpooling(arr: np.ndarray, size: int, stride: int) -> np.ndarray:
    """
    This function is used to perform maxpooling on the input array of 2D matrix(image)
    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of maxpooled matrix
    Sample Input Output:
    >>> maxpooling([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 6.,  8.],
           [14., 16.]])
    >>> maxpooling([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[241., 180.],
           [241., 157.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0

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
            updated_arr[mat_i][mat_j] = np.max(arr[i : i + size, j : j + size])
            # shift the pooling matrix by stride of column pixels
            j += stride
            mat_j += 1

        # shift the pooling matrix by stride of row pixels
        i += stride
        mat_i += 1

        # reset the column index to 0
        j = 0
        mat_j = 0

    return updated_arr


# Averagepooling Function
def avgpooling(arr: np.ndarray, size: int, stride: int) -> np.ndarray:
    """
    This function is used to perform avgpooling on the input array of 2D matrix(image)
    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of avgpooled matrix
    Sample Input Output:
    >>> avgpooling([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 3.,  5.],
           [11., 13.]])
    >>> avgpooling([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[161., 102.],
           [114.,  69.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0

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
            updated_arr[mat_i][mat_j] = int(np.average(arr[i : i + size, j : j + size]))
            # shift the pooling matrix by stride of column pixels
            j += stride
            mat_j += 1

        # shift the pooling matrix by stride of row pixels
        i += stride
        mat_i += 1
        # reset the column index to 0
        j = 0
        mat_j = 0

    return updated_arr


# Main Function
if __name__ == "__main__":
    from doctest import testmod

    testmod(name="avgpooling", verbose=True)

    # Loading the image
    image = Image.open("path_to_image")

    # Converting the image to numpy array and maxpooling, displaying the result
    # Ensure that the image is a square matrix

    Image.fromarray(maxpooling(np.array(image), size=3, stride=2)).show()

    # Converting the image to numpy array and averagepooling, displaying the result
    # Ensure that the image is a square matrix

    Image.fromarray(avgpooling(np.array(image), size=3, stride=2)).show()
