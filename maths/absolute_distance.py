import math

def calculate_absolute_distance(coord1, coord2):
    """
    Calculate the absolute Euclidean distance between two 3D coordinates.
    
    Args:
        coord1 (list): The first 3D coordinate [x, y, z].
        coord2 (list): The second 3D coordinate [x, y, z].
        
    Returns:
        float: The absolute distance between the two coordinates.
    """
    abs_diff_x = abs(coord2[0] - coord1[0])
    abs_diff_y = abs(coord2[1] - coord1[1])
    abs_diff_z = abs(coord2[2] - coord1[2])
    total_absolute_distance = abs_diff_x + abs_diff_y + abs_diff_z
    return total_absolute_distance

def calculate_travel_time(distance, linear_speed=3.5, angular_speed=120):
    """
    Calculate the time it takes to travel a given distance with specified speeds.

    Args:
        distance (float): The distance to travel.
        linear_speed (float): Linear speed in units per second (default: 3.5).
        angular_speed (float): Angular speed in degrees per second (default: 120).

    Returns:
        float: The time in seconds to travel the given distance.
    """
    initial_velocity = 0  # Agent starts from rest
    acceleration = 8  # Units per second squared

    # Convert angular speed to radians per second
    angular_speed_radians = math.radians(angular_speed)

    # Calculate linear acceleration due to angular speed
    linear_acceleration = angular_speed_radians * linear_speed

    # Calculate final linear velocity
    final_linear_velocity = math.sqrt(initial_velocity ** 2 + 2 * acceleration * distance)

    # Calculate time using the final velocity
    time = (final_linear_velocity - initial_velocity) / linear_acceleration

    return time

if __name__ == "__main__":
    coordinates = {
        'A': [-9.3, 1.25, -4.94],
        # ... (other coordinates)
        'N': [9.3, 1.25, 9.55]
    }

    # Calculate and print the time between each pair of nodes
    for node1 in coordinates:
        for node2 in coordinates:
            if node1 != node2:
                distance = calculate_absolute_distance(coordinates[node1], coordinates[node2])
                time = calculate_travel_time(distance)
                print(f"Time to move from {node1} to {node2}: {time:.2f} seconds")
