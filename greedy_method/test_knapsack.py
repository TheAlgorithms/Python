import unittest

import greedy_knapsack as kp


class TestClass(unittest.TestCase):
    """
    Test cases for knapsack
    """

    def test_sorted(self):
        """
        kp.calc_profit takes the required argument (profit, weight, max_weight)
        and returns whether the answer matches to the expected ones
        """
        profit = [10, 20, 30, 40, 50, 60]
        weight = [2, 4, 6, 8, 10, 12]
        max_weight = 100
        self.assertEqual(kp.calc_profit(profit, weight, max_weight), 210)

    def test_negative_max_weight(self):
        """
        Returns ValueError for any negative max_weight value
        :return: ValueError
        """
        # profit = [10, 20, 30, 40, 50, 60]
        # weight = [2, 4, 6, 8, 10, 12]
        # max_weight = -15
        self.assertRaisesRegex(ValueError, "max_weight must greater than zero.")

    def test_negative_profit_value(self):
        """
        Returns ValueError for any negative profit value in the list
        :return: ValueError
        """
        # profit = [10, -20, 30, 40, 50, 60]
        # weight = [2, 4, 6, 8, 10, 12]
        # max_weight = 15
        self.assertRaisesRegex(ValueError, "Weight can not be negative.")

    def test_negative_weight_value(self):
        """
        Returns ValueError for any negative weight value in the list
        :return: ValueError
        """
        # profit = [10, 20, 30, 40, 50, 60]
        # weight = [2, -4, 6, -8, 10, 12]
        # max_weight = 15
        self.assertRaisesRegex(ValueError, "Profit can not be negative.")

    def test_null_max_weight(self):
        """
        Returns ValueError for any zero max_weight value
        :return: ValueError
        """
        # profit = [10, 20, 30, 40, 50, 60]
        # weight = [2, 4, 6, 8, 10, 12]
        # max_weight = null
        self.assertRaisesRegex(ValueError, "max_weight must greater than zero.")

    def test_unequal_list_length(self):
        """
        Returns IndexError if length of lists (profit and weight) are unequal.
        :return: IndexError
        """
        # profit = [10, 20, 30, 40, 50]
        # weight = [2, 4, 6, 8, 10, 12]
        # max_weight = 100
        self.assertRaisesRegex(
            IndexError, "The length of profit and weight must be same."
        )


if __name__ == "__main__":
    unittest.main()
