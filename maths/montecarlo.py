"""
@author: MatteoRaso
"""
from numpy import pi, sqrt
from random import uniform
from statistics import mean


def pi_estimator(iterations: int):
    """An implementation of the Monte Carlo method used to find pi.
    1. Draw a 2x2 square centred at (0,0).
    2. Inscribe a circle within the square.
    3. For each iteration, place a dot anywhere in the square.
    3.1 Record the number of dots within the circle.
    4. After all the dots are placed, divide the dots in the circle by the total.
    5. Multiply this value by 4 to get your estimate of pi.
    6. Print the estimated and numpy value of pi
    """

    circle_dots = 0

    # A local function to see if a dot lands in the circle.
    def circle(x: float, y: float):
        distance_from_centre = sqrt((x ** 2) + (y ** 2))
        # Our circle has a radius of 1, so a distance greater than 1 would land outside the circle.
        return distance_from_centre <= 1

    circle_dots = sum(
        int(circle(uniform(-1.0, 1.0), uniform(-1.0, 1.0))) for i in range(iterations)
    )

    # The proportion of guesses that landed within the circle
    proportion = circle_dots / iterations
    # The ratio of the area for circle to square is pi/4.
    pi_estimate = proportion * 4
    print("The estimated value of pi is ", pi_estimate)
    print("The numpy value of pi is ", pi)
    print("The total error is ", abs(pi - pi_estimate))


def area_under_line_estimator(iterations: int) -> float:
    """An implementation of the Monte Carlo method to find area under
       y = x where x lies between 0 to 1
    1. Let x be a uniformly distributed random variable between 0 and 1
    2. expected value of x = integration of x from 0 to 1
    3. Finding expected value of x:
        a. Repeatedly draw x from uniform distribution
        b. expected value = average of those values
    4. Actual value = 1/2
    5. Returns estimated value
    """
    
    return mean(uniform(0,1) for i in range(iterations))


def area_under_line_estimator_check(iterations: int):
    """ Checks estimation error for area_under_line_estimator func
    1. Calls "area_under_line_estimator" function
    2. Compares with the expected value
    3. Prints estimated, expected and error value
    """

    estimate = area_under_line_estimator(iterations)
    
    print("******************")
    print("Estimating area under y=x where x varies from 0 to 1")
    print("Expected value is ", 0.5)
    print("Estimated value is ", estimate)
    print("Total error is ", abs(estimate - 0.5))
    print("******************")
    
    return


if __name__ == "__main__":
    import doctest

    doctest.testmod()
