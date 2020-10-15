def distance_formula(x1, y1, x2, y2):
    """
    Calculate the distance between the two coordinates (x1,y1) and (x2,y2).
    >>> distance_formula(0, 0, 2, 2)
    2.8284271247461903
    >>> distance_formula(1, 0, 5, 2)
    4.47213595499958
    >>> distance_formula(0, 0, 5, 0)
    5.0
    """
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** (1 / 2)


if __name__ == "__main__":
    print(distance_formula(0, 0, 2, 2))
