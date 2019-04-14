# @author willx75
# Tower of Hanoi recursion game algorithm is a game, it consists of three rods and a number of disks of different sizes, which can slide onto any rod

import logging

log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


def Tower_Of_Hanoi(n, source, dest, by, mouvement):
    if n == 0:
        return n
    elif n == 1:
        mouvement += 1
        # no print statement (you could make it an optional flag for printing logs)
        logging.debug('Move the plate from', source, 'to', dest)
        return mouvement
    else:

        mouvement = mouvement + Tower_Of_Hanoi(n-1, source, by, dest, 0)
        logging.debug('Move the plate from', source, 'to', dest)

        mouvement = mouvement + 1 + Tower_Of_Hanoi(n-1, by, dest, source, 0)
        return mouvement
