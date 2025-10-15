import unittest
from simulated_annealing.simulated_annealing import SimulatedAnnealing


def sphere(x):
    return sum(v * v for v in x)


class TestSimulatedAnnealing(unittest.TestCase):
    def test_minimize_sphere_1d(self):
        sa = SimulatedAnnealing(sphere, [5.0], bounds=[(-10, 10)], temperature=10, cooling_rate=0.9, iterations_per_temp=50)
        best, cost, hist = sa.optimize()
        # Best should be near 0 with tiny cost
        self.assertLess(cost, 1e-2)

    def test_stop_event(self):
        import threading
        stop = threading.Event()
        sa = SimulatedAnnealing(sphere, [5.0], bounds=[(-10, 10)], temperature=10, cooling_rate=0.9, iterations_per_temp=1000)
        # request stop immediately
        stop.set()
        best, cost, hist = sa.optimize(stop_event=stop)
        # Should return without error
        self.assertIsNotNone(best)


if __name__ == '__main__':
    unittest.main()
