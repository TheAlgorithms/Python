from random import random, randint

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
"""

P = 0.1  # The probability that a driver will slow down
SPEED_START = 1  # The speed of the cars a the start
FREQUENCY = 5  # How many cells there are between two cars at the start
MAX_SPEED = 5  # The maximum speed a car will go to
NUMBER_OF_CELLS = 1024  # How many cell are there in the highway
NUMBER_OF_UPDATE = 2048  # How many times will the position be updated
highway = []  # Where every position and speed of every car will be stored


class InputError(Exception):
    def __init__(self, value, expected_value):
        self.value = value
        self.expected_value = expected_value

    def __str__(self):
        return f"Error! It works with {self.expected_value} and not {self.value}"


def input_verification(dictionary: dict):
    for value in dictionary:
        if value != dictionary[value]:
            raise InputError(value, dictionary[value])


def construct_highway(
    NUMBER_OF_CELLS: int,
    FREQUENCY: int,
    SPEED_START: int,
    random_frequency=False,
    random_speed=False,
    MAX_SPEED=5,
) -> list:
    """
    Build the highway following the parameters given
    >>> construct_highway(10, 2, 6)
    [[6, -1, 6, -1, 6, -1, 6, -1, 6, -1]]
    >>> construct_highway(10, 10, 2)
    [[2, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    """
    input_verification(
        {
            type(NUMBER_OF_CELLS): int,
            type(FREQUENCY): int,
            type(SPEED_START): int,
            type(random_frequency): bool,
            type(random_speed): bool,
            type(MAX_SPEED): int,
        }
    )

    highway = [[-1] * NUMBER_OF_CELLS]  # Create a highway without any car
    i = 0
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


def get_distance(highway_now: list, j: int) -> int:
    """
    Get the distance between a car (at index j) and the next car
    >>> get_distance([6,-1,6,-1,6], 2)
    1
    >>> get_distance([2,-1,-1,-1,3,1,0,1,3,2], 0)
    3
    >>> get_distance([-1,-1,-1,-1,2,-1,-1,-1,3], -1)
    4
    """
    input_verification({type(highway_now): list, type(j): int})

    distance = 0
    cells = highway_now[j + 1 :]
    for cell in range(len(cells)):  # May need a better name for this
        if cells[cell] != -1:  # If the cell is not empty then
            return distance  # we have the distance we wanted
        else:
            distance += 1
    # Here if the car is near the end of the highway
    distance += get_distance(highway_now, -1)
    return distance


def update(highway_now: list, P: int, MAX_SPEED: int) -> list:
    """
    Update the speed of the cars
    >>> update([-1,-1,-1,-1,-1,2,-1,-1,-1,-1,3], 0, 5)
    [-1, -1, -1, -1, -1, 3, -1, -1, -1, -1, 4]
    >>> update([-1,-1,2,-1,-1,-1,-1,3], 0, 5)
    [-1, -1, 3, -1, -1, -1, -1, 1]
    """
    input_verification({type(highway_now): list, type(P): int, type(MAX_SPEED): int})

    NUMBER_OF_CELLS = len(highway_now)
    # Beforce calculations, the highway is empty
    next_highway = [-1] * NUMBER_OF_CELLS

    for j in range(NUMBER_OF_CELLS):
        if highway_now[j] != -1:
            # Add 1 to the current speed of the car and cap the speed
            next_highway[j] = min(highway_now[j] + 1, MAX_SPEED)
            # Number of empty cell before the next car
            dn = get_distance(highway_now, j) - 1
            # We can't have the car causing an accident
            next_highway[j] = min(next_highway[j], dn)
            if random() < P:
                # Randomly, a driver will slow down
                next_highway[j] = max(next_highway[j] - 1, 0)
    return next_highway


def simulate(highway: list, NUMBER_OF_UPDATE: int, P: int, MAX_SPEED: int) -> list:
    """
    The main fonction, it will simulate the evolution of the highway
    >>> simulate([[-1,2,-1,-1,-1,3]], 2, 0, 3)
    [[-1, 2, -1, -1, -1, 3], [-1, -1, -1, 2, -1, 0], [1, -1, -1, 0, -1, -1]]
    >>> simulate([[-1,2,-1,3]], 4, 0, 3)
    [[-1, 2, -1, 3], [-1, 0, -1, 0], [-1, 0, -1, 0], [-1, 0, -1, 0], [-1, 0, -1, 0]]
    """
    input_verification(
        {
            type(highway): list,
            type(NUMBER_OF_UPDATE): int,
            type(P): int,
            type(MAX_SPEED): int,
        }
    )

    NUMBER_OF_CELLS = len(highway[0])

    for i in range(NUMBER_OF_UPDATE):
        next_speeds_calculated = update(highway[i], P, MAX_SPEED)
        real_next_speeds = [-1] * NUMBER_OF_CELLS

        for j in range(NUMBER_OF_CELLS):
            speed = next_speeds_calculated[j]
            if speed != -1:
                # Change the position based on the speed (with % to create the loop)
                index = (j + speed) % NUMBER_OF_CELLS
                # Commit the change of position
                real_next_speeds[index] = speed
        highway.append(real_next_speeds)

    return highway


if __name__ == "__main__":
    highway = construct_highway(NUMBER_OF_CELLS, FREQUENCY, SPEED_START)
    simulate(highway, NUMBER_OF_UPDATE, P, MAX_SPEED)
