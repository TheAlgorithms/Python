"""
Basic of this concept..
The area of a rectangle is defined as the product  of its two adjacent sides.
For more information 
https://en.wikipedia.org/wiki/Rectangle

"""


def area(length, breadth):
    """
    Find the area of recatngle.
    >>> area(5,6)
    30
    >>> area(2,10)
    20
    >>> area(30,50)
    1500
    This functio will return integer value
    """
    return length * breadth 


if __name__ == "__main__":
    print(area(10, 20))  # --> 10,20(and two integer values)
