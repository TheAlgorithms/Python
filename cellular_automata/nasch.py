from random import randint, random

"""
This algorithm simulate the evolution of a highway with only one road
The highway is divided in cells, each cell can have at most one car in it
The highway make a loop. That means that when a car comes to one end, they will
 come out of the other
A car is represented by it's speed (from 0 to 5)

Some information about speed:
    -1 means that the cell on the highway is empty
    0 to 5 are the speed of the cars with 0 being the lowest and 5 the highest

More information here: https://en.wikipedia.org/wiki/Nagel%E2%80%93Schreckenberg_model

Examples for doctest:
>>>highway = construct_highway(6, 3, 0)
>>>simulate(highway, 2, 0, 2)
[[0, -1, -1, 0, -1, -1], [-1, 1, -1, -1, 1, -1], [-1, -1, 1, -1, -1, 1]]
>>>highway = construct_highway(5, 2, -2)
>>>simulate(highway, 3, 0, 2)
[[0, -1, 0, -1, 0], [0, -1, 0, -1, -1], [0, -1, -1, 1, -1], [-1, 1, -1, 0, -1]]
"""

PROBABILITY = 0.1  # The probability that a driver will slow down
SPEED_START = 1  # The speed of the cars a the start
FREQUENCY = 5  # How many cells there are between two cars at the start
MAX_SPEED = 5  # The maximum speed a car will go to
NUMBER_OF_CELLS = 1024  # How many cell are there in the highway
NUMBER_OF_UPDATE = 2048  # How many times will the position be updated
highway = []  # Where every position and speed of every car will be stored


def construct_highway(
    NUMBER_OF_CELLS: int,
    FREQUENCY: int,
    SPEED_START: int,
    random_frequency: bool = False,
    random_speed: bool = False,
    MAX_SPEED: int = 5,
) -> list:
    """
    Build the highway following the parameters given
    >>> construct_highway(10, 2, 6)
    [[6, -1, 6, -1, 6, -1, 6, -1, 6, -1]]
    >>> construct_highway(10, 10, 2)
    [[2, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    """

    highway = [[-1] * NUMBER_OF_CELLS]  # Create a highway without any car
    i = 0
    if SPEED_START < 0:
        SPEED_START = 0
    while i < NUMBER_OF_CELLS:
        if random_speed:
            highway[0][i] = randint(0, MAX_SPEED)
        else:
            highway[0][i] = SPEED_START  # Place the cars
        if random_frequency:
            i += randint(1, MAX_SPEED * 2)  # Arbitrary number, may need tuning
        else:
            i += FREQUENCY
    return highway


def get_distance(highway_now: list, car_index: int) -> int:
    """
    Get the distance between a car (at index car_index) and the next car
    >>> get_distance([6,-1,6,-1,6], 2)
    1
    >>> get_distance([2,-1,-1,-1,3,1,0,1,3,2], 0)
    3
    >>> get_distance([-1,-1,-1,-1,2,-1,-1,-1,3], -1)
    4
    """

    distance = 0
    cells = highway_now[car_index + 1 :]
    for cell in range(len(cells)):  # May need a better name for this
        if cells[cell] != -1:  # If the cell is not empty then
            return distance  # we have the distance we wanted
        else:
            distance += 1
    # Here if the car is near the end of the highway
    distance += get_distance(highway_now, -1)
    return distance


def update(highway_now: list, PROBABILITY: float, MAX_SPEED: int) -> list:
    """
    Update the speed of the cars
    >>> update([-1,-1,-1,-1,-1,2,-1,-1,-1,-1,3], 0.0, 5)
    [-1, -1, -1, -1, -1, 3, -1, -1, -1, -1, 4]
    >>> update([-1,-1,2,-1,-1,-1,-1,3], 0.0, 5)
    [-1, -1, 3, -1, -1, -1, -1, 1]
    """

    NUMBER_OF_CELLS = len(highway_now)
    # Beforce calculations, the highway is empty
    next_highway = [-1] * NUMBER_OF_CELLS

    for car_index in range(NUMBER_OF_CELLS):
        if highway_now[car_index] != -1:
            # Add 1 to the current speed of the car and cap the speed
            next_highway[car_index] = min(highway_now[car_index] + 1, MAX_SPEED)
            # Number of empty cell before the next car
            dn = get_distance(highway_now, car_index) - 1
            # We can't have the car causing an accident
            next_highway[car_index] = min(next_highway[car_index], dn)
            if random() < PROBABILITY:
                # Randomly, a driver will slow down
                next_highway[car_index] = max(next_highway[car_index] - 1, 0)
    return next_highway


def simulate(
    highway: list, NUMBER_OF_UPDATE: int, PROBABILITY: float, MAX_SPEED: int
) -> list:
    """
    The main function, it will simulate the evolution of the highway
    >>> simulate([[-1,2,-1,-1,-1,3]], 2, 0.0, 3)
    [[-1, 2, -1, -1, -1, 3], [-1, -1, -1, 2, -1, 0], [1, -1, -1, 0, -1, -1]]
    >>> simulate([[-1,2,-1,3]], 4, 0.0, 3)
    [[-1, 2, -1, 3], [-1, 0, -1, 0], [-1, 0, -1, 0], [-1, 0, -1, 0], [-1, 0, -1, 0]]
    """

    NUMBER_OF_CELLS = len(highway[0])

    for i in range(NUMBER_OF_UPDATE):
        next_speeds_calculated = update(highway[i], PROBABILITY, MAX_SPEED)
        real_next_speeds = [-1] * NUMBER_OF_CELLS

        for car_index in range(NUMBER_OF_CELLS):
            speed = next_speeds_calculated[car_index]
            if speed != -1:
                # Change the position based on the speed (with % to create the loop)
                index = (car_index + speed) % NUMBER_OF_CELLS
                # Commit the change of position
                real_next_speeds[index] = speed
        highway.append(real_next_speeds)

    return highway


if __name__ == "__main__":
    import doctest

    doctest.testmod()
