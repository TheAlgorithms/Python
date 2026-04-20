class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class CollisionDetection:
    @staticmethod
    def circle_circle_collision(circle1, circle2):
        dx = circle1.x - circle2.x
        dy = circle1.y - circle2.y
        distance_squared = dx**2 + dy**2
        radius_sum = circle1.radius + circle2.radius
        return distance_squared <= radius_sum**2

    @staticmethod
    def rectangle_rectangle_collision(rect1, rect2):
        return not (
            rect1.x + rect1.width < rect2.x
            or rect1.x > rect2.x + rect2.width
            or rect1.y + rect1.height < rect2.y
            or rect1.y > rect2.y + rect2.height
        )

    @staticmethod
    def circle_rectangle_collision(circle, rect):
        closest_x = max(rect.x, min(circle.x, rect.x + rect.width))
        closest_y = max(rect.y, min(circle.y, rect.y + rect.height))
        dx = circle.x - closest_x
        dy = circle.y - closest_y
        return dx**2 + dy**2 <= circle.radius**2
