"""
    Flood fill algorithm implementation in Python
    Wikipedia: https://en.wikipedia.org/wiki/Flood_fill
    Author: Akshay Dubey (https://github.com/itsAkshayDubey)
"""

from array import *

def get_pixel(image, x_co_ordinate, y_co_ordinate):
    """
    This method will return pixel value at the given co-ordinates in the input image matrix
    Parammeters:
        image: 2d image matrix
        x-co-cordinate: x co-ordinate of the image of which pixel value is to be obtained
        y-co-cordinate: y co-ordinate of the image of which pixel value is to be obtained
    Returns:
        int pixel value
    """
    return image[x_co_ordinate][y_co_ordinate]

def put_pixel(image, x_co_ordinate, y_co_ordinate, color):
    """
    This method will put input color at the given co-ordinates in the input image matrix
    Parammeters:
        image: 2d image matrix
        x-co-cordinate: x co-ordinate of the image of which pixel value is to be changed to new color
        y-co-cordinate: y co-ordinate of the image of which pixel value is to be changed to new color
        color: new color to be filled in the givem co-ordinates
    """
    image[x_co_ordinate][y_co_ordinate] = color

def print_image_array(image):
    """
    This method will print the input image matrix
    Parammeters:
        image: 2d image matrix
    """
    for r in image:
        for c in r:
            print(c,end = "  ")
        print()

def flood_fill(image, x_co_ordinate, y_co_ordinate, new_color, old_color):
    """
    This method will put input color starting from at the given co-ordinates in the input image matrix
    Parammeters:
        image: 2d image matrix
        x-co-cordinate: x co-ordinate of the image of which pixel value is to be changed to new color
        y-co-cordinate: y co-ordinate of the image of which pixel value is to be changed to new color
        new_color: new color to be filled in the givem co-ordinates
        old_color: exisitng color present at the given co-ordinates
    """
    if(x_co_ordinate >= 0 and y_co_ordinate >= 0 and get_pixel(image, x_co_ordinate, y_co_ordinate) == old_color):
        put_pixel(image, x_co_ordinate, y_co_ordinate, new_color)
        flood_fill(image, x_co_ordinate + 1, y_co_ordinate, new_color, old_color)
        flood_fill(image, x_co_ordinate - 1, y_co_ordinate, new_color, old_color)
        flood_fill(image, x_co_ordinate, y_co_ordinate + 1, new_color, old_color)
        flood_fill(image, x_co_ordinate, y_co_ordinate - 1, new_color, old_color)
        flood_fill(image, x_co_ordinate + 1, y_co_ordinate - 1, new_color, old_color)
        flood_fill(image, x_co_ordinate - 1, y_co_ordinate + 1, new_color, old_color)
        flood_fill(image, x_co_ordinate + 1, y_co_ordinate + 1, new_color, old_color)
        flood_fill(image, x_co_ordinate - 1, y_co_ordinate - 1, new_color, old_color)


if __name__ == "__main__":
    """
    Output:
    1  1  1  1
    1  7  7  2
    1  7  7  2
    2  2  2  2
    """
    image = [[1,1,1,1], [1,9,9,2], [1,9,9,2], [2,2,2,2]]
    print("Before")
    print_image_array(image)
    print("After")
    flood_fill(image,1,1,7,9)
    print_image_array(image)
