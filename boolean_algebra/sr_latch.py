"""
SR latch (this is a cross-coupled NOR implementation;
for a cross-coupled NAND, just complement the inputs before applying them):
is a simple memory element that stores 1 bit of information
State table:
   | Input 1(set pin) | Input 2(reset pin) | q  (not q) |
   |       0          |         0          | no change  |
   |       0          |         1          | 0     1    |
   |       1          |         0          | 1     0    |
   |       1          |         1          | undefined  |
Note: get_current_state() return value of [q,!q]
"""


class SrLatch:
    """
    Example:
    >>> sr_latch = SrLatch(True)
    >>> sr_latch.get_current_state()
    [True, False]
    >>> sr_latch.set_current_state(False,True)
    >>> sr_latch.get_current_state()
    [False, True]
    >>> sr_latch.set_current_state(False,False)
    >>> sr_latch.get_current_state()
    [False, True]
    >>> sr_latch.set_current_state(True,True)
    Traceback (most recent call last):
       ...
    ValueError: undefined state.
    """

    def __init__(self, initial_state: bool) -> None:
        self.__initial_state = initial_state

    def get_current_state(self) -> list:
        return [self.__initial_state, not self.__initial_state]

    def set_current_state(self, set_pin: bool, reset_pin: bool) -> None:
        if set_pin and reset_pin:
            raise ValueError("undefined state.")
        elif not set_pin and reset_pin:
            self.__initial_state = False
        elif set_pin and not reset_pin:
            self.__initial_state = True


if __name__ == "__main__":
    from doctest import testmod

    testmod()
