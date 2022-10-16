"""
Basic of this concept..
The area of a rectangle is defined as the product  of its two adjacent sides.
For more information
https://en.wikipedia.org/wiki/Rectangle

"""


def area(length, breadth)-> int:
    """
    Find the area of recatngle.
    >>> area(5,6)
    30
    >>> area(2,10)
    20
    >>> area(30,50)
    1500
    """
    return length * breadth


if __name__ == "__main__":
   import doctest

   doctest.testmod(name ='area', verbose = True)

