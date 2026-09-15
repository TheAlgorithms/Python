def is_colliding(rect1, rect2):
    """
    Checks if rect1 and rect2 collide.
    rect1, rect2: tuples (x, y, width, height)
    Returns: True if colliding, else False
    """
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    horizontal = (x1 + w1 >= x2) and (x2 + w2 >= x1)
    vertical = (y1 + h1 >= y2) and (y2 + h2 >= y1)
    return horizontal and vertical
