from draw import Rect, plot

class quadTree():

    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def contains(self, point):
        x = self.boundary.center[0]
        y = self.boundary.center[1]
        w = self.boundary.width
        h = self.boundary.height
        return True if(x-w <= point[0] and x+w >= point[0]) and (y-h <= point[1] and y+h >= point[1]) else False

    def divide(self):
        x = self.boundary.center[0]
        y = self.boundary.center[1]
        w = self.boundary.width/2
        h = self.boundary.height/2
        c = self.capacity

        self.northEast = quadTree(Rect([x+w, y+h], h, w), c)
        self.northWest = quadTree(Rect([x-w, y+h], h, w), c)
        self.southEast = quadTree(Rect([x+w, y-h], h, w), c)
        self.southWest = quadTree(Rect([x-w, y-h], h, w), c)

    def insert(self, point):
        if self.contains(point):
            if len(self.points) < 4:
                self.points.append(point)
                return
            if(self.divided):
                self.northEast.insert(point)
                self.northWest.insert(point)
                self.southEast.insert(point)
                self.southWest.insert(point)
            else:
                self.divide()
                self.divided = True
                self.insert(point)
                return

    def draw(self):
        for i in self.points:
            plot(i)
        if(self.divided):
            self.boundary.drawDivision()
            self.northEast.draw()
            self.northWest.draw()
            self.southEast.draw()
            self.southWest.draw()

    def insertDraw(self, point):
        if self.contains(point):
            if len(self.points) < 4:
                self.points.append(point)
                return
            if(self.divided):
                self.northEast.insertDraw(point)
                self.northWest.insertDraw(point)
                self.southEast.insertDraw(point)
                self.southWest.insertDraw(point)
            else:
                self.divide()
                self.divided = True
                self.boundary.drawDivision()
                self.insert(point)
                return

    def __str__(self):
        return "".join(str(self.points))