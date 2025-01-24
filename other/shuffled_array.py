# To create a shuffled array. Generate a pseudo random number
# Swap that number with any other element in the list run this swapping len(Array)
# times to get desired shuffled array

# To Understand more of random number generation
# follow https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator

import doctest
import time


class Solution:

    # """
    # >>> Solution().__init__(array=[1,2,3])
    # Traceback (most recent call last):
    #            ....
    # TypeError: __init__() missing 1 required positional argument: 'array'
    # """

    def __init__(self, array: list) -> None:
        self.arr = array
        self.seed = int(str(time.time())[-1:-5:-1])

    # generating a 4 digit number randomly
    # by taking the last four numbers of the system generated time
    # pseudo random number generator
    def prng(self, num: int) -> int:
        """
        >>> Solution([56]).prng(1)
        0
        """
        if num == 1:
            return 0
        self.seed *= self.seed
        any = str(self.seed)
        if any != "0":
            self.seed = int(any[-1:-5:-1])
        else:
            any = any[:] + str(len(self.arr) // 2)
        if int(any[-1]) < num:
            return int(any[-1])
        return self.prng(num)

    def reset(self) -> list:
        # it will return the original given array
        """
        >>> Solution([-7, 0, 4, -56.7]).reset()
        [-7, 0, 4, -56.7]
        """
        return self.arr

    def shuffle(self) -> list:
        # generated a pseudo number for each traversal
        # and swapped the traversing value with that number
        """
        >>> Solution([2]).shuffle()
        [2]
        """
        temp = self.arr.copy()
        for i in range(len(self.arr)):
            a = self.prng(len(self.arr))
            temp[a], temp[i] = temp[i], temp[a]
        return temp

if __name__ == '__main__':
    solclass = Solution([18, 2, 3, 4, 5, 7, 8, 10, 21])
    shuffled_arr = solclass.shuffle()
    print(shuffled_arr)

    doctest.testmod()
