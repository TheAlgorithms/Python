from typing import Tuple
import numpy as np


# Basic implementation of the collision of two circles.
def circle_collision(fpos: Tuple[float, float, float], spos: Tuple[float, float, float]) -> bool:
    # difference by XY axes
    dx = fpos[0] - spos[0]
    dy = fpos[1] - spos[1]
    
    
    # Euclidean distance between the centers of circles
    distance = np.sqrt(pow(dx, 2) + pow(dy, 2))
    
    # minimum possible distance between circles, without collision
    min_distance = fpos[2] + fpos[2]
    
    # If actual distance smaller than minimal possible, cirlces collides
    if distance < min_distance:
        return True
    
    return False
