# Author: Anuj Mishra
# GitHub Profile: https://github.com/Anuj-gr8/
# Email: anujmishra282003@gmail.com

import math

def degrees_to_radians(degrees: float) -> float:
    """
    Convert degrees to radians.

    Args:
        degrees (float): Angle in degrees.

    Returns:
        float: Angle in radians.
    """
    return degrees * (math.pi / 180.0)

def calculate_horizontal_range(initial_velocity: float,
                               launch_angle_degrees: float,
                               gravity: float) -> float:
    """
    Calculate the horizontal range of a rocket in projectile motion.

    Args:
        initial_velocity (float): The initial velocity of the rocket
        (in meters per second).
        launch_angle_degrees (float): The launch angle in degrees (angle of projection
        with respect to the horizontal).
        gravity (float): The acceleration due to gravity (in meters per second squared).

    Returns:
        float: The horizontal range of the rocket's motion (in meters).
    """

    # Convert the launch angle from degrees to radians
    launch_angle_radians = degrees_to_radians(launch_angle_degrees)
    
    # Calculate the horizontal range using the formula: R = (u^2 * sin(2 * θ)) / g
    horizontal_range = (initial_velocity ** 2 * math.sin(2 * launch_angle_radians))
    horizontal_range = horizontal_range / gravity
    return horizontal_range

if __name__ == "__main__":
    # Example usage:
    initial_velocity = float(input())  # m/s
    launch_angle = float(input())    # degrees
    gravity = float(input())         # m/s²

    # Calculate the horizontal range using the function
    range_of_rocket = calculate_horizontal_range(initial_velocity,launch_angle,gravity)

    # Print the result with appropriate formatting
    print(f"The horizontal range of the rocket is {range_of_rocket:.2f} meters.")
