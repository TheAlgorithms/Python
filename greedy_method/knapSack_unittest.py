import unittest
import knapsack_problem as kp


class TestClass(unittest.TestCase):
    """
    Test cases for knapsack_problem
    """

    def test_sorted(self):
        """
        kp.calc_Profit takes the required argument (profit, weight, max_weight)
        and returns whether the answer matches to the expected ones
        """
        gain = kp.calc_Profit([10, 20, 30, 40, 50, 60], [2, 4, 6, 8, 10, 12], 100)
        # self.assertTrue(result)
        self.assertEqual(gain, 75)


if __name__ == "__main__":
    unittest.main()
