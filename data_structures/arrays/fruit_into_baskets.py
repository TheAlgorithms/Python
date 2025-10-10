from collections import defaultdict


class FruitIntoBaskets:
    """
    Problem:
    Given an array of integers representing types of fruit, pick a contiguous
    subarray containing at most two different types of fruit. Return the maximum
    number of fruits you can collect.

    Example:
    >>> solver = FruitIntoBaskets()
    >>> solver.total_fruit([1, 2, 1, 2, 3])
    4
    """

    def total_fruit(self, fruits: list[int]) -> int:
        count = defaultdict(int)
        left = 0
        max_fruit = 0

        for right, fruit in enumerate(fruits):
            count[fruit] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_fruit = max(max_fruit, right - left + 1)

        return max_fruit


if __name__ == "__main__":
    solver = FruitIntoBaskets()
    print("Maximum Fruits Collected:", solver.total_fruit([1, 2, 1, 2, 3]))

