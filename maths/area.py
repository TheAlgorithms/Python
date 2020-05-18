""" 
finding areas of various geomitrical shapes

"""

import math


def area_rectangle(base,height):
    """ calculate the area of a rectangle
        returns the base*height
        >> area_rectangle(10,20)
        200
   """
    return base*height

def area_square(side_length):
    """ calculate the area of a square
        returns the side*side
        >>> area_square(10)
        100
    """
    return side_length*side_length

def area_triangle(length,breadth):
    """calculate the area of a triangle
        returns the 1/2*length*breadth
        >>> area_triangle(10,10)
        50
    """
    return 1/2*length*breadth

def area_parallelogram(base,height):
    """ calculate the area of a parallelogram
        returns the base*height
        >> area_parallelogram(10,20)
        200
    """
    return base*height

def area_trapezium(base1,base2,height):
    """ calculate the area of a trapezium
        returns the 1/2(base1+base2)*height
        >> area_trapezium(10,20,30)
        450
    """
    return 1/2*(base1+base2)*height

def area_circle(radius):
    """ calculate the area of a circle
        returns the math.pi*(radius*radius)
        >> area_circle(20)
        1256.6370614359173
    """
    return math.pi*(radius*radius)


def main():
    print('areas of all geometric shapes: \n')
    print('Rectangle: ' + str(area_rectangle(10,20)))
    print('Square: ' + str(area_square(10)))
    print('Triangle: ' + str(area_triangle(10,10)))
    print('Parallelogram: ' + str(area_parallelogram(10,20)))
    print('Trapezium: ' + str(area_trapezium(10,20,30)))
    print('Circle: ' + str(float(area_circle(20))))

if __name__ == "__main__":
    main()
