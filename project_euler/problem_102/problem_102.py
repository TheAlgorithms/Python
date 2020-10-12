def solution() -> int:
    """
    Return the number of triangles from triangles.txt that
    include the origin.
    >>> solution()
    228
    """
    import math

    f = open("triangles.txt")
    list_of_lines = f.readlines()

    def Area(a1: int, a2: int, b1: int, b2: int, c1: int, c2: int) -> int:
        a = math.sqrt((b1 - c1) ** 2 + (b2 - c2) ** 2)
        b = math.sqrt((a1 - c1) ** 2 + (a2 - c2) ** 2)
        c = math.sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2)
        s = (a + b + c) / 2
        # print(a,b,c,s)
        A = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return A

    count = 0
    for line in list_of_lines:
        a1, a2, b1, b2, c1, c2 = [int(x) for x in line.split(",")]
        A = Area(a1, a2, b1, b2, c1, c2)
        A1 = Area(0, 0, b1, b2, c1, c2)
        A2 = Area(a1, a2, 0, 0, c1, c2)
        A3 = Area(a1, a2, b1, b2, 0, 0)
        # print(A1+A2+A3-A)
        if math.isclose(A, A1 + A2 + A3):
            count += 1

    return count


if __name__ == "__main__":
    print(solution())
