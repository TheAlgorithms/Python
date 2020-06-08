import unittest
import knapsack_problem as kp

class TestClass(unittest.TestCase):

    def test_sorted(self):
        gain = kp.calc_Profit([10,20,30,40,50,60], [2, 4, 6, 8, 10, 12],100)
        # self.assertTrue(result)
        self.assertEqual(gain,75)


if __name__ == "__main__":
    unittest.main()