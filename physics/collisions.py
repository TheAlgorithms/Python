# Basic implementation of the collision of two circles.
def circle_collision(fpos: tuple[float, float, float], spos: tuple[float, float, float]) -> bool:
    # difference by XY axes
    dx = fpos[0] - spos[0]
    dy = fpos[1] - spos[1]
    
    
    # Euclidean distance between the centers of circles
    distance = pow((pow(dx, 2) + pow(dy, 2)), 0.5)
    
    # minimum possible distance between circles, without collision
    min_distance = fpos[2] + fpos[2]
    collide = distance < min_distance
    
    # If actual distance smaller than minimal possible, cirlces collides
    return collide

if __name__ == "__main__":
    from doctest import testmod

    testmod()
