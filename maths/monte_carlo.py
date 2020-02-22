"""
@author: MatteoRaso
"""
from numpy import pi, sqrt
from random import uniform
from statistics import mean


def pi_estimator(iterations: int):
    """
    An implementation of the Monte Carlo method used to find pi.
    1. Draw a 2x2 square centred at (0,0).
    2. Inscribe a circle within the square.
    3. For each iteration, place a dot anywhere in the square.
       a. Record the number of dots within the circle.
    4. After all the dots are placed, divide the dots in the circle by the total.
    5. Multiply this value by 4 to get your estimate of pi.
    6. Print the estimated and numpy value of pi
    """
    # A local function to see if a dot lands in the circle.
    def in_circle(x: float, y: float) -> bool:
        distance_from_centre = sqrt((x ** 2) + (y ** 2))
        # Our circle has a radius of 1, so a distance
        # greater than 1 would land outside the circle.
        return distance_from_centre <= 1

    # The proportion of guesses that landed in the circle
    proportion = mean(
        int(in_circle(uniform(-1.0, 1.0), uniform(-1.0, 1.0))) for _ in range(iterations)
    )
    # The ratio of the area for circle to square is pi/4.
    pi_estimate = proportion * 4
    print("The estimated value of pi is ", pi_estimate)
    print("The numpy value of pi is ", pi)
    print("The total error is ", abs(pi - pi_estimate))


def area_under_line_estimator(iterations: int,
                              min_value: float=0.0,
                              max_value: float=1.0) -> float:
    """
    An implementation of the Monte Carlo method to find area under
       y = x where x lies between min_value to max_value
    1. Let x be a uniformly distributed random variable between min_value to max_value
    2. Expected value of x = (integration of x from min_value to max_value) / (max_value - min_value)
    3. Finding expected value of x:
        a. Repeatedly draw x from uniform distribution
        b. Expected value = average of those values
    4. Actual value = (max_value^2 - min_value^2) / 2
    5. Returns estimated value
    """
    return mean(uniform(min_value, max_value) for _ in range(iterations)) * (max_value - min_value)


def area_under_line_estimator_check(iterations: int,
                                    min_value: float=0.0,
                                    max_value: float=1.0) -> None:
    """
    Checks estimation error for area_under_line_estimator func
    1. Calls "area_under_line_estimator" function
    2. Compares with the expected value
    3. Prints estimated, expected and error value
    """
    
    estimated_value = area_under_line_estimator(iterations, min_value, max_value)
    expected_value = (max_value*max_value - min_value*min_value) / 2
    
    print("******************")
    print("Estimating area under y=x where x varies from ",min_value, " to ",max_value)
    print("Estimated value is ", estimated_value)
    print("Expected value is ", expected_value)
    print("Total error is ", abs(estimated_value - expected_value))
    print("******************")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
