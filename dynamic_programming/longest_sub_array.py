"""
Author  : Yvonne

This is a pure Python implementation of Dynamic Programming solution to the
    longest_sub_array problem.

The problem is  :
Given an array, to find the longest and continuous sub array and get the max sum of the
    sub array in the given array.
"""


class SubArray:
    def __init__(self, arr):
        # we need a list not a string, so do something to change the type
        self.array = arr.split(",")

    def solve_sub_array(self):
        rear = [int(self.array[0])] * len(self.array)
        sum_value = [int(self.array[0])] * len(self.array)
        for i in range(1, len(self.array)):
            sum_value[i] = max(
                int(self.array[i]) + sum_value[i - 1], int(self.array[i])
            )
            rear[i] = max(sum_value[i], rear[i - 1])
        return rear[len(self.array) - 1]


if __name__ == "__main__":
    whole_array = input("please input some numbers:")
    array = SubArray(whole_array)
    re = array.solve_sub_array()
    print(("the results is:", re))
