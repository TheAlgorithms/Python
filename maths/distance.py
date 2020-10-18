"""
Finding distance between a pair of coordinates (x1, y1) and (x2, y2)
"""


def getDistance(x1, y1, x2, y2):
    """
    Using the standard distance Formula
    **2 is to perform square operation
    **5 is to perform square root operation
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


if __name__ == "__main__":
    print(f"The distance between the points is {getDistance(2,4,7,16)} units")
