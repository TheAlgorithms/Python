"""
@author: MatteoRaso
"""

def piEstimator(iterations: int):
    """An implementation of the Monte Carlo method used to find pi.
    1. Draw a 2x2 square centred at (0,0).
    2. Inscribe a circle within the square.
    3. For each iteration, place a dot anywhere in the square.
    3.1 Record the number of dots within the circle.
    4. After all the dots are placed, divide the dots in the circle by the total.
    5. Multiply this value by 4 to get your estimate of pi.
    6. Print the estimated and numpy value of pi
    """
    import numpy as np
    circle_dots = 0
    
    #A local function to see if a dot lands in the circle.
    def circle(x: float, y: float): 
        distance_from_centre = np.sqrt((x ** 2) + (y ** 2))
         #Our circle has a radius of 1, so a distance greater than 1 would land outside the circle.
        if distance_from_centre > 1:
            return False
        else:
            return True
            
    for i in range(0, iterations):
        #Random float from -1.0 to 1.0.
        x = np.random.uniform(-1.0, 1.0) 
        y = np.random.uniform(-1.0, 1.0)
        if circle(x,y) == True:
            circle_dots += 1
            
    #The proportion of guesses that landed within the circle
    proportion = circle_dots / iterations
    #The ratio of the area for circle to square is pi/4.
    pi = proportion * 4 
    print("The estimated value of pi is ", pi)
    print("The numpy value of pi is ", np.pi)
    print("The total error is ", abs(np.pi - pi))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
