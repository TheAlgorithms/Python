import unittest
from simulated_annealing.tsp import total_distance, random_tour, euclidean_distance


class TestTSP(unittest.TestCase):
    def test_distance_symmetric(self):
        a = (0, 0)
        b = (3, 4)
        d = euclidean_distance(a, b)
        self.assertAlmostEqual(d, 5.0)

    def test_total_distance_cycle(self):
        coords = [(0, 0), (0, 1), (1, 1), (1, 0)]
        tour = [0, 1, 2, 3]
        d = total_distance(tour, coords)
        self.assertGreater(d, 0)


if __name__ == '__main__':
    unittest.main()
