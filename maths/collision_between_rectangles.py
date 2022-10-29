rect1 = {
    "x": 10,
    "y": 10,
    "height": 30,
    "width": 50
}

rect2 = {
    "x": 20,
    "y": 30,
    "height": 40,
    "width": 30
}

def checkCollision(rect1, rect2) -> bool:
    """
    Check if two rectangle are colliding/overlaping
    
    >>> checkCollision(rect1, rect2)
    True
    """
    x_bound = rect1["x"] < rect2["x"] + rect1["width"] and rect1["x"] + rect2["width"] > rect2["x"]
    y_bound = rect1["y"] < rect2["y"] + rect1["height"] and rect1["height"] + rect1["y"] > rect2["y"]
    return x_bound and y_bound

if __name__ == "__main__":
    import doctest

    doctest.testmod()
