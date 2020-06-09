import unittest
import knapsack_problem as kp


class TestClass(unittest.TestCase):
    """
    Test cases for knapsack_problem
    """

    def test_sorted(self):
        """
        kp.calc_profit takes the required argument (profit, weight, max_weight)
        and returns whether the answer matches to the expected ones
        """
        profit = [10, 20, 30, 40, 50, 60]
        weight = [2, 4, 6, 8, 10, 12]
        max_Weight = 100
        self.assertEqual(kp.calc_profit(profit, weight, max_Weight), 210)

    def test_negative_maxWeight(self):
        """
        Returns ValueError for any negative max_weight value
        :return: ValueError
        """
        # profit = [10, 20, 30, 40, 50, 60]
        # weight = [2, 4, 6, 8, 10, 12]
        # max_Weight = -15
        self.assertRaisesRegex(
            ValueError,
            "<< Gotcha! Max_Weight is a positive quantity greater than zero! >>",
        )

    def test_negative_profit_Value(self):
        """
        Returns ValueError for any negative profit value in the list
        :return: ValueError
        """
        # profit = [10, -20, 30, 40, 50, 60]
        # weight = [2, 4, 6, 8, 10, 12]
        # max_Weight = 15
        self.assertRaisesRegex(
            ValueError,
            "<< Oops! Could not accept a negative value for weight. Try Again.. >>",
        )

    def test_negative_weight_Value(self):
        """
        Returns ValueError for any negative weight value in the list
        :return: ValueError
        """
        # profit = [10, 20, 30, 40, 50, 60]
        # weight = [2, -4, 6, -8, 10, 12]
        # max_Weight = 15
        self.assertRaisesRegex(
            ValueError, "<< Ono! Profit means positive value. Better luck next time! >>"
        )

    def test_zero_maxWeight(self):
        """
        Returns ValueError for any zero max_weight value
        :return: ValueError
        """
        # profit = [10, 20, 30, 40, 50, 60]
        # weight = [2, 4, 6, 8, 10, 12]
        # max_Weight = 0
        self.assertRaisesRegex(
            ValueError,
            "<< Gotcha! Max_Weight is a positive quantity greater than zero! >>",
        )

    def test_unequal_list_length(self):
        """
        Returns IndexError if length of lists (profit and weight) are unequal.
        :return: IndexError
        """
        # profit = [10, 20, 30, 40, 50]
        # weight = [2, 4, 6, 8, 10, 12]
        # max_Weight = 100
        self.assertRaisesRegex(
            IndexError, "<< The length of both the arrays must be same! Try again.. >>"
        )


if __name__ == "__main__":
    unittest.main()
