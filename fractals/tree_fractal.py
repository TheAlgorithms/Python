"""
Author : Rudransh Bhardwaj
Github : @rudransh61
Wikipedia to learn about fractal tree (or canopy) : https://en.wikipedia.org/wiki/Fractal_canopy
"""

import turtle  # importing the module required


turtle.speed("fastest")

# turning the turtle to upwards
turtle.lt(90)

# the acute angle between
# the base and branch of the Y
angle = 30


# function to plot a Y
def tree(sz: int, level: int)->None:
    """
    Draw a fractal tree.

    Parameters:
    - sz (int): Size of the current branch.
    - level (int): Recursion level, controls the depth of the tree.

    Returns:
    None

    Example:
    >>> tree(100, 3)  # Draw a fractal tree with size 100 and recursion depth 3
    """
    if level > 0:
        turtle.colormode(255)

        # into equal intervals for each level
        # setting the colour according to the current level
        turtle.pencolor(0, 255 // level, 0)

        # drawing the base
        turtle.fd(sz)

        turtle.rt(angle)

        # recursive call for
        # the right subtree
        tree(0.8 * sz, level - 1)

        turtle.pencolor(0, 255 // level, 0)

        turtle.lt(2 * angle)

        # recursive call for
        # the left subtree
        tree(0.8 * sz, level - 1)

        turtle.pencolor(0, 255 // level, 0)

        turtle.rt(angle)
        turtle.fd(-sz)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
