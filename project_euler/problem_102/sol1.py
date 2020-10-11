class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def isZero(self):
        return self.x == 0 and self.y == 0

    def minus(self, p):
        return Point(p.x - self.x, p.y - self.y)

    def __str__(self):
        return f"( {self.x}, {self.y})"


def side(p1, p2):
    return (abs(p2.x - p1.x) ** 2.0 + abs(p2.y - p1.y) ** 2.0) ** 0.5


def crossproduct(p1, p2):
    return p1.x * p2.y - p1.y * p2.x


def area(p1, p2, p3):
    a = side(p1, p2)
    b = side(p2, p3)
    c = side(p3, p1)

    cp = crossproduct(p1.minus(p2), p1.minus(p3))

    if cp == 0:
        return 0

    s = (a + b + c) / 2.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def contains(p1, p2, p3):
    p0 = Point(0.0, 0.0)

    bigArea = area(p1, p2, p3)
    smallerAreas = [
        area(p1, p2, p0),
        area(p2, p3, p0),
        area(p3, p1, p0),
    ]

    return round(bigArea, 5) == round(sum(smallerAreas), 5)


def triangleContainsOrigin(triangle):
    p1, p2, p3 = triangle
    return contains(p1, p2, p3)


def triangles_from_file(fileName):
    def build_triangle(fromStr):
        splitted = fromStr.split(",")
        asInt = [float(i) for i in splitted]
        triangle = []
        for i in range(0, 6, 2):
            newPoint = Point(asInt[i], asInt[i + 1])
            triangle.append(newPoint)
        return triangle

    data = open(fileName, "r").read()
    tests = data.split("\n")
    triangles = [build_triangle(i) for i in tests if not i == ""]

    return triangles


def run():
    triangles = triangles_from_file("triangles_euler102.txt")

    count = [True for i in triangles if triangleContainsOrigin(i)]


run()
