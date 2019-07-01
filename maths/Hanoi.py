"""Tower of Hanoi."""

# @author willx75
# Tower of Hanoi recursion game algorithm is a game, it consists of three rods
# and a number of disks of different sizes, which can slide onto any rod

import logging

log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


def Tower_Of_Hanoi(n, source, dest, by, movement):
    """Tower of Hanoi - Move plates to different rods."""
    if n == 0:
        return n
    elif n == 1:
        movement += 1
        # no print statement
        # (you could make it an optional flag for printing logs)
        logging.debug('Move the plate from', source, 'to', dest)
        return movement
    else:

        movement = movement + Tower_Of_Hanoi(n - 1, source, by, dest, 0)
        logging.debug('Move the plate from', source, 'to', dest)

        movement = movement + 1 + Tower_Of_Hanoi(n - 1, by, dest, source, 0)
        return movement
