"""
@author: MatteoRaso
"""
from collections.abc import Callable
from math import pi, sqrt
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
    def is_in_circle(x: float, y: float) -> bool:
        distance_from_centre = sqrt((x**2) + (y**2))
        # Our circle has a radius of 1, so a distance
        # greater than 1 would land outside the circle.
        return distance_from_centre <= 1

    # The proportion of guesses that landed in the circle
    proportion = mean(
        int(is_in_circle(uniform(-1.0, 1.0), uniform(-1.0, 1.0)))
        for _ in range(iterations)
    )
    # The ratio of the area for circle to square is pi/4.
    pi_estimate = proportion * 4
    print(f"The estimated value of pi is {pi_estimate}")
    print(f"The numpy value of pi is {pi}")
    print(f"The total error is {abs(pi - pi_estimate)}")


def area_under_curve_estimator(
    iterations: int,
    function_to_integrate: Callable[[float], float],
    min_value: float = 0.0,
    max_value: float = 1.0,
) -> float:
    """
    An implementation of the Monte Carlo method to find area under
       a single variable non-negative real-valued continuous function,
       say f(x), where x lies within a continuous bounded interval,
       say [min_value, max_value], where min_value and max_value are
       finite numbers
    1. Let x be a uniformly distributed random variable between min_value to
       max_value
    2. Expected value of f(x) =
       (integrate f(x) from min_value to max_value)/(max_value - min_value)
    3. Finding expected value of f(x):
        a. Repeatedly draw x from uniform distribution
        b. Evaluate f(x) at each of the drawn x values
        c. Expected value = average of the function evaluations
    4. Estimated value of integral = Expected value * (max_value - min_value)
    5. Returns estimated value
    """

    return mean(
        function_to_integrate(uniform(min_value, max_value)) for _ in range(iterations)
    ) * (max_value - min_value)


def area_under_line_estimator_check(
    iterations: int, min_value: float = 0.0, max_value: float = 1.0
) -> None:
    """
    Checks estimation error for area_under_curve_estimator function
    for f(x) = x where x lies within min_value to max_value
    1. Calls "area_under_curve_estimator" function
    2. Compares with the expected value
    3. Prints estimated, expected and error value
    """

    def identity_function(x: float) -> float:
        """
        Represents identity function
        >>> [function_to_integrate(x) for x in [-2.0, -1.0, 0.0, 1.0, 2.0]]
        [-2.0, -1.0, 0.0, 1.0, 2.0]
        """
        return x

    estimated_value = area_under_curve_estimator(
        iterations, identity_function, min_value, max_value
    )
    expected_value = (max_value * max_value - min_value * min_value) / 2

    print("******************")
    print(f"Estimating area under y=x where x varies from {min_value} to {max_value}")
    print(f"Estimated value is {estimated_value}")
    print(f"Expected value is {expected_value}")
    print(f"Total error is {abs(estimated_value - expected_value)}")
    print("******************")


def pi_estimator_using_area_under_curve(iterations: int) -> None:
    """
    Area under curve y = sqrt(4 - x^2) where x lies in 0 to 2 is equal to pi
    """

    def function_to_integrate(x: float) -> float:
        """
        Represents semi-circle with radius 2
        >>> [function_to_integrate(x) for x in [-2.0, 0.0, 2.0]]
        [0.0, 2.0, 0.0]
        """
        return sqrt(4.0 - x * x)

    estimated_value = area_under_curve_estimator(
        iterations, function_to_integrate, 0.0, 2.0
    )

    print("******************")
    print("Estimating pi using area_under_curve_estimator")
    print(f"Estimated value is {estimated_value}")
    print(f"Expected value is {pi}")
    print(f"Total error is {abs(estimated_value - pi)}")
    print("******************")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
