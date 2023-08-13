"""
Wa-Tor algorithm (1984)

@ https://en.wikipedia.org/wiki/Wa-Tor
@ https://beltoforion.de/en/wator/
@ https://beltoforion.de/en/wator/images/wator_medium.webm

This solution aims to completely remove any systematic approach
to the Wa-Tor planet, and utilise fully random methods.

The constants are a working set that allows the Wa-Tor planet
to result in one of the three possible results.
"""

from collections.abc import Callable
from random import randint, shuffle
from time import sleep
from typing import Literal

WIDTH = 50  # Width of the Wa-Tor planet
HEIGHT = 50  # Height of the Wa-Tor planet

PREY_INITIAL_COUNT = 30  # The initial number of prey entities
PREY_REPRODUCTION_TIME = 5  # The chronons before reproducing

PREDATOR_INITIAL_COUNT = 50  # The initial number of predator entities
# The initial energy value of predator entities
PREDATOR_INITIAL_ENERGY_VALUE = 15
# The energy value provided when consuming prey
PREDATOR_FOOD_VALUE = 5
PREDATOR_REPRODUCTION_TIME = 20  # The chronons before reproducing

MAX_ENTITIES = 500  # The max number of organisms on the board
# The number of entities to delete from the unbalanced side
DELETE_UNBALANCED_ENTITIES = 50


class Entity:
    """
    Represents an entity (either prey or predator).

    >>> e = Entity(True, coords=(0, 0))
    >>> e.prey
    True
    >>> e.coords
    (0, 0)
    >>> e.alive
    True
    """

    def __init__(self, prey: bool, coords: tuple[int, int]) -> None:
        self.prey = prey
        # The (row, col) pos of the entity
        self.coords = coords

        self.remaining_reproduction_time = (
            PREY_REPRODUCTION_TIME if prey else PREDATOR_REPRODUCTION_TIME
        )
        self.energy_value = None if prey is True else PREDATOR_INITIAL_ENERGY_VALUE
        self.alive = True

    def reset_reproduction_time(self) -> None:
        """
        >>> e = Entity(True, coords=(0, 0))
        >>> e.reset_reproduction_time()
        >>> e.remaining_reproduction_time == PREY_REPRODUCTION_TIME
        True
        >>> e = Entity(False, coords=(0, 0))
        >>> e.reset_reproduction_time()
        >>> e.remaining_reproduction_time == PREDATOR_REPRODUCTION_TIME
        True
        """
        self.remaining_reproduction_time = (
            PREY_REPRODUCTION_TIME if self.prey is True else PREDATOR_REPRODUCTION_TIME
        )

    def __repr__(self) -> str:
        """
        >>> Entity(prey=True, coords=(1, 1))
        Entity(prey=True, coords=(1, 1), remaining_reproduction_time=5)
        >>> Entity(prey=False, coords=(2, 1))  # doctest: +NORMALIZE_WHITESPACE
        Entity(prey=False, coords=(2, 1),
        remaining_reproduction_time=20, energy_value=15)
        """
        repr_ = (
            f"Entity(prey={self.prey}, coords={self.coords}, "
            f"remaining_reproduction_time={self.remaining_reproduction_time}"
        )
        if self.energy_value is not None:
            repr_ += f", energy_value={self.energy_value}"
        return f"{repr_})"


class WaTor:
    """
    Represents the main Wa-Tor algorithm.

    :attr time_passed: A function that is called every time
        time passes (a chronon) in order to visually display
        the new Wa-Tor planet. The time_passed function can block
        using time.sleep to slow the algorithm progression.

    >>> wt = WaTor(10, 15)
    >>> wt.width
    10
    >>> wt.height
    15
    >>> len(wt.planet)
    15
    >>> len(wt.planet[0])
    10
    >>> len(wt.get_entities()) == PREDATOR_INITIAL_COUNT + PREY_INITIAL_COUNT
    True
    """

    time_passed: Callable[["WaTor", int], None] | None

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.time_passed = None

        self.planet: list[list[Entity | None]] = [[None] * width for _ in range(height)]

        # Populate planet with predators and prey randomly
        for _ in range(PREY_INITIAL_COUNT):
            self.add_entity(prey=True)
        for _ in range(PREDATOR_INITIAL_COUNT):
            self.add_entity(prey=False)
        self.set_planet(self.planet)

    def set_planet(self, planet: list[list[Entity | None]]) -> None:
        """
        Ease of access for testing

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> planet = [
        ... [None, None, None],
        ... [None, Entity(True, coords=(1, 1)), None]
        ... ]
        >>> wt.set_planet(planet)
        >>> wt.planet == planet
        True
        >>> wt.width
        3
        >>> wt.height
        2
        """
        self.planet = planet
        self.width = len(planet[0])
        self.height = len(planet)

    def add_entity(self, prey: bool) -> None:
        """
        Adds an entity, making sure the entity does
        not override another entity

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> wt.set_planet([[None, None], [None, None]])
        >>> wt.add_entity(True)
        >>> len(wt.get_entities())
        1
        >>> wt.add_entity(False)
        >>> len(wt.get_entities())
        2
        """
        while True:
            row, col = randint(0, self.height - 1), randint(0, self.width - 1)
            if self.planet[row][col] is None:
                self.planet[row][col] = Entity(prey=prey, coords=(row, col))
                return

    def get_entities(self) -> list[Entity]:
        """
        Returns a list of all the entities within the planet.

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> len(wt.get_entities()) == PREDATOR_INITIAL_COUNT + PREY_INITIAL_COUNT
        True
        """
        return [entity for column in self.planet for entity in column if entity]

    def balance_predators_and_prey(self) -> None:
        """
        Balances predators and preys so that prey
        can not dominate the predators, blocking up
        space for them to reproduce.

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> for i in range(2000):
        ...     row, col = i // HEIGHT, i % WIDTH
        ...     wt.planet[row][col] = Entity(True, coords=(row, col))
        >>> entities = len(wt.get_entities())
        >>> wt.balance_predators_and_prey()
        >>> len(wt.get_entities()) == entities
        False
        """
        entities = self.get_entities()
        shuffle(entities)

        if len(entities) >= MAX_ENTITIES - MAX_ENTITIES / 10:
            prey = [entity for entity in entities if entity.prey]
            predators = [entity for entity in entities if not entity.prey]

            prey_count, predator_count = len(prey), len(predators)

            entities_to_purge = (
                prey[:DELETE_UNBALANCED_ENTITIES]
                if prey_count > predator_count
                else predators[:DELETE_UNBALANCED_ENTITIES]
            )
            for entity in entities_to_purge:
                self.planet[entity.coords[0]][entity.coords[1]] = None

    def get_surrounding_prey(self, entity: Entity) -> list[Entity]:
        """
        Returns all the prey entities around (N, S, E, W) a predator entity.

        Subtly different to the try_to_move_to_unoccupied square.

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> wt.set_planet([
        ... [None, Entity(True, (0, 1)), None],
        ... [None, Entity(False, (1, 1)), None],
        ... [None, Entity(True, (2, 1)), None]])
        >>> wt.get_surrounding_prey(
        ... Entity(False, (1, 1)))  # doctest: +NORMALIZE_WHITESPACE
        [Entity(prey=True, coords=(0, 1), remaining_reproduction_time=5),
        Entity(prey=True, coords=(2, 1), remaining_reproduction_time=5)]
        >>> wt.set_planet([[Entity(False, (0, 0))]])
        >>> wt.get_surrounding_prey(Entity(False, (0, 0)))
        []
        >>> wt.set_planet([
        ... [Entity(True, (0, 0)), Entity(False, (1, 0)), Entity(False, (2, 0))],
        ... [None, Entity(False, (1, 1)), Entity(True, (2, 1))],
        ... [None, None, None]])
        >>> wt.get_surrounding_prey(Entity(False, (1, 0)))
        [Entity(prey=True, coords=(0, 0), remaining_reproduction_time=5)]
        """
        row, col = entity.coords
        adjacent: list[tuple[int, int]] = [
            (row - 1, col),  # North
            (row + 1, col),  # South
            (row, col - 1),  # West
            (row, col + 1),  # East
        ]

        return [
            ent
            for r, c in adjacent
            if 0 <= r < self.height
            and 0 <= c < self.width
            and (ent := self.planet[r][c]) is not None
            and ent.prey
        ]

    def move_and_reproduce(
        self, entity: Entity, direction_orders: list[Literal["N", "E", "S", "W"]]
    ) -> None:
        """
        Attempts to move to an unoccupied neighbouring square
        in either of the four directions (North, South, East, West).
        If the move was successful and the remaining_reproduction time is
        equal to 0, then a new prey or predator can also be created
        in the previous square.

        :param direction_orders: Ordered list (like priority queue) depicting
                            order to attempt to move. Removes any systematic
                            approach of checking neighbouring squares.

        >>> planet = [
        ... [None, None, None],
        ... [None, Entity(True, coords=(1, 1)), None],
        ... [None, None, None]
        ... ]
        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> wt.set_planet(planet)
        >>> wt.move_and_reproduce(Entity(True, coords=(1, 1)), direction_orders=["N"])
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        [[None, Entity(prey=True, coords=(0, 1), remaining_reproduction_time=4), None],
        [None, None, None],
        [None, None, None]]
        >>> wt.planet[0][0] = Entity(True, coords=(0, 0))
        >>> wt.move_and_reproduce(Entity(True, coords=(0, 1)),
        ... direction_orders=["N", "W", "E", "S"])
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        [[Entity(prey=True, coords=(0, 0), remaining_reproduction_time=5), None,
        Entity(prey=True, coords=(0, 2), remaining_reproduction_time=4)],
        [None, None, None],
        [None, None, None]]
        >>> wt.planet[0][1] = wt.planet[0][2]
        >>> wt.planet[0][2] = None
        >>> wt.move_and_reproduce(Entity(True, coords=(0, 1)),
        ... direction_orders=["N", "W", "S", "E"])
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        [[Entity(prey=True, coords=(0, 0), remaining_reproduction_time=5), None, None],
        [None, Entity(prey=True, coords=(1, 1), remaining_reproduction_time=4), None],
        [None, None, None]]

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> reproducable_entity = Entity(False, coords=(0, 1))
        >>> reproducable_entity.remaining_reproduction_time = 0
        >>> wt.planet = [[None, reproducable_entity]]
        >>> wt.move_and_reproduce(reproducable_entity,
        ... direction_orders=["N", "W", "S", "E"])
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        [[Entity(prey=False, coords=(0, 0),
        remaining_reproduction_time=20, energy_value=15),
        Entity(prey=False, coords=(0, 1), remaining_reproduction_time=20,
        energy_value=15)]]
        """
        row, col = coords = entity.coords

        adjacent_squares: dict[Literal["N", "E", "S", "W"], tuple[int, int]] = {
            "N": (row - 1, col),  # North
            "S": (row + 1, col),  # South
            "W": (row, col - 1),  # West
            "E": (row, col + 1),  # East
        }
        # Weight adjacent locations
        adjacent: list[tuple[int, int]] = []
        for order in direction_orders:
            adjacent.append(adjacent_squares[order])

        for r, c in adjacent:
            if (
                0 <= r < self.height
                and 0 <= c < self.width
                and self.planet[r][c] is None
            ):
                # Move entity to empty adjacent square
                self.planet[r][c] = entity
                self.planet[row][col] = None
                entity.coords = (r, c)
                break

        # (2.) See if it possible to reproduce in previous square
        if coords != entity.coords and entity.remaining_reproduction_time <= 0:
            # Check if the entities on the planet is less than the max limit
            if len(self.get_entities()) < MAX_ENTITIES:
                # Reproduce in previous square
                self.planet[row][col] = Entity(prey=entity.prey, coords=coords)
                entity.reset_reproduction_time()
        else:
            entity.remaining_reproduction_time -= 1

    def perform_prey_actions(
        self, entity: Entity, direction_orders: list[Literal["N", "E", "S", "W"]]
    ) -> None:
        """
        Performs the actions for a prey entity

        For prey the rules are:
          1. At each chronon, a prey moves randomly to one of the adjacent unoccupied
            squares. If there are no free squares, no movement takes place.
          2. Once a prey has survived a certain number of chronons it may reproduce.
            This is done as it moves to a neighbouring square,
            leaving behind a new prey in its old position.
            Its reproduction time is also reset to zero.

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> reproducable_entity = Entity(True, coords=(0, 1))
        >>> reproducable_entity.remaining_reproduction_time = 0
        >>> wt.planet = [[None, reproducable_entity]]
        >>> wt.perform_prey_actions(reproducable_entity,
        ... direction_orders=["N", "W", "S", "E"])
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        [[Entity(prey=True, coords=(0, 0), remaining_reproduction_time=5),
        Entity(prey=True, coords=(0, 1), remaining_reproduction_time=5)]]
        """
        self.move_and_reproduce(entity, direction_orders)

    def perform_predator_actions(
        self,
        entity: Entity,
        occupied_by_prey_coords: tuple[int, int] | None,
        direction_orders: list[Literal["N", "E", "S", "W"]],
    ) -> None:
        """
        Performs the actions for a predator entity

        :param occupied_by_prey_coords: Move to this location if there is prey there

        For predators the rules are:
          1. At each chronon, a predator moves randomly to an adjacent square occupied
            by a prey. If there is none, the predator moves to a random adjacent
            unoccupied square. If there are no free squares, no movement takes place.
          2. At each chronon, each predator is deprived of a unit of energy.
          3. Upon reaching zero energy, a predator dies.
          4. If a predator moves to a square occupied by a prey,
            it eats the prey and earns a certain amount of energy.
          5. Once a predator has survived a certain number of chronons
          it may reproduce in exactly the same way as the prey.

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> wt.set_planet([[Entity(True, coords=(0, 0)), Entity(False, coords=(0, 1))]])
        >>> wt.perform_predator_actions(Entity(False, coords=(0, 1)), (0, 0), [])
        >>> wt.planet  # doctest: +NORMALIZE_WHITESPACE
        [[Entity(prey=False, coords=(0, 0),
        remaining_reproduction_time=20, energy_value=19), None]]
        """
        assert entity.energy_value is not None  # [type checking]

        # (3.) If the entity has 0 energy, it will die
        if entity.energy_value == 0:
            self.planet[entity.coords[0]][entity.coords[1]] = None
            return

        # (1.) Move to entity if possible
        if occupied_by_prey_coords is not None:
            # Kill the prey
            prey = self.planet[occupied_by_prey_coords[0]][occupied_by_prey_coords[1]]
            assert prey is not None
            prey.alive = False

            # Move onto prey
            self.planet[occupied_by_prey_coords[0]][occupied_by_prey_coords[1]] = entity
            self.planet[entity.coords[0]][entity.coords[1]] = None

            entity.coords = occupied_by_prey_coords
            # (4.) Eats the prey and earns energy
            entity.energy_value += PREDATOR_FOOD_VALUE
        else:
            # (5.) If it has survived the certain number of chronons it will also
            # reproduce in this function
            self.move_and_reproduce(entity, direction_orders)

        # (2.) Each chronon, the predator is deprived of a unit of energy
        entity.energy_value -= 1

    def run(self, *, iteration_count: int) -> None:
        """
        Emulate time passing by looping iteration_count times

        >>> wt = WaTor(WIDTH, HEIGHT)
        >>> wt.run(iteration_count=PREDATOR_INITIAL_ENERGY_VALUE - 1)
        >>> len(list(filter(lambda entity: entity.prey is False,
        ... wt.get_entities()))) >= PREDATOR_INITIAL_COUNT
        True
        """
        for iter_num in range(iteration_count):
            # Generate list of all entities in order to randomly
            # pop an entity at a time to simulate true randomness
            # This removes the systematic approach of iterating
            # through each entity width by height
            all_entities = self.get_entities()

            for __ in range(len(all_entities)):
                entity = all_entities.pop(randint(0, len(all_entities) - 1))
                if entity.alive is False:
                    continue

                directions: list[Literal["N", "E", "S", "W"]] = ["N", "E", "S", "W"]
                shuffle(directions)  # Randomly shuffle directions

                if entity.prey:
                    self.perform_prey_actions(entity, directions)
                else:
                    # Create list of surrounding prey
                    surrounding_prey = self.get_surrounding_prey(entity)
                    surrounding_prey_coords = None

                    if surrounding_prey:
                        # Again, randomly shuffle directions
                        shuffle(surrounding_prey)
                        surrounding_prey_coords = surrounding_prey[0].coords

                    self.perform_predator_actions(
                        entity, surrounding_prey_coords, directions
                    )

            # Balance out the predators and prey
            self.balance_predators_and_prey()

            if self.time_passed is not None:
                # Call time_passed function for Wa-Tor planet
                # visualisation in a terminal or a graph.
                self.time_passed(self, iter_num)


def visualise(wt: WaTor, iter_number: int, *, colour: bool = True) -> None:
    """
    Visually displays the Wa-Tor planet using
    an ascii code in terminal to clear and re-print
    the Wa-Tor planet at intervals.

    Uses ascii colour codes to colourfully display
    the predators and prey.

    (0x60f197) Prey = #
    (0xfffff) Predator = x

    >>> wt = WaTor(30, 30)
    >>> wt.set_planet([
    ... [Entity(True, coords=(0, 0)), Entity(False, coords=(0, 1)), None],
    ... [Entity(False, coords=(1, 0)), None, Entity(False, coords=(1, 2))],
    ... [None, Entity(True, coords=(2, 1)), None]
    ... ])
    >>> visualise(wt, 0, colour=False)  # doctest: +NORMALIZE_WHITESPACE
    #  x  .
    x  .  x
    .  #  .
    <BLANKLINE>
    Iteration: 0 | Prey count: 2 | Predator count: 3 |
    """
    if colour:
        __import__("os").system("")
        print("\x1b[0;0H\x1b[2J\x1b[?25l")

    reprint = "\x1b[0;0H" if colour else ""
    ansi_colour_end = "\x1b[0m " if colour else " "

    planet = wt.planet
    output = ""

    # Iterate over every entity in the planet
    for row in planet:
        for entity in row:
            if entity is None:
                output += " . "
            else:
                if colour is True:
                    output += (
                        "\x1b[38;2;96;241;151m"
                        if entity.prey
                        else "\x1b[38;2;255;255;15m"
                    )
                output += f" {'#' if entity.prey else 'x'}{ansi_colour_end}"

        output += "\n"

    entities = wt.get_entities()
    prey_count = sum(entity.prey for entity in entities)

    print(
        f"{output}\n Iteration: {iter_number} | Prey count: {prey_count} | "
        f"Predator count: {len(entities) - prey_count} | {reprint}"
    )
    # Block the thread to be able to visualise seeing the algorithm
    sleep(0.05)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    wt = WaTor(WIDTH, HEIGHT)
    wt.time_passed = visualise
    wt.run(iteration_count=100_000)
