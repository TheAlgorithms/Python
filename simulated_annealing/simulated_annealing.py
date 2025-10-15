import math
import random
from typing import Callable, Sequence, Tuple, List, Optional


class SimulatedAnnealing:
    """Generic Simulated Annealing optimizer for continuous domains.

    Usage:
        sa = SimulatedAnnealing(func, initial_solution, bounds=..., **params)
        best, best_cost, history = sa.optimize()
    """

    def __init__(
        self,
        func: Callable[[Sequence[float]], float],
        initial_solution: Sequence[float],
        bounds: Optional[Sequence[Tuple[float, float]]] = None,
        temperature: float = 100.0,
        cooling_rate: float = 0.99,
        min_temperature: float = 1e-3,
        iterations_per_temp: int = 100,
        neighbor_scale: float = 0.1,
        seed: Optional[int] = None,
    ):
        self.func = func
        self.current = list(initial_solution)
        self.dim = len(initial_solution)
        self.bounds = bounds
        self.temperature = float(temperature)
        self.initial_temperature = float(temperature)
        self.cooling_rate = float(cooling_rate)
        self.min_temperature = float(min_temperature)
        self.iterations_per_temp = int(iterations_per_temp)
        self.neighbor_scale = float(neighbor_scale)
        if seed is not None:
            random.seed(seed)

    def _clip(self, x: float, i: int) -> float:
        if not self.bounds:
            return x
        lo, hi = self.bounds[i]
        return max(lo, min(hi, x))

    def _neighbor(self, solution: Sequence[float]) -> List[float]:
        # Gaussian perturbation scaled by neighbor_scale and variable range
        new = []
        for i, v in enumerate(solution):
            scale = self.neighbor_scale
            if self.bounds:
                lo, hi = self.bounds[i]
                rng = (hi - lo) if hi > lo else 1.0
                scale = self.neighbor_scale * rng
            candidate = v + random.gauss(0, scale)
            candidate = self._clip(candidate, i)
            new.append(candidate)
        return new

    def _accept(self, delta: float, temp: float) -> bool:
        if delta < 0:
            return True
        try:
            prob = math.exp(-delta / temp)
        except OverflowError:
            prob = 0.0
        return random.random() < prob

    def optimize(self, max_steps: Optional[int] = None) -> Tuple[List[float], float, dict]:
        """Run optimization and return best solution, cost, and history.

        history dict contains: temps, best_costs, current_costs
        """
        temp = self.temperature
        current = list(self.current)
        current_cost = float(self.func(current))
        best = list(current)
        best_cost = current_cost

        history = {"temps": [], "best_costs": [], "current_costs": []}

        steps = 0
        while temp > self.min_temperature:
            for _ in range(self.iterations_per_temp):
                candidate = self._neighbor(current)
                candidate_cost = float(self.func(candidate))
                delta = candidate_cost - current_cost
                if self._accept(delta, temp):
                    current = candidate
                    current_cost = candidate_cost
                    if current_cost < best_cost:
                        best = list(current)
                        best_cost = current_cost

                history["temps"].append(temp)
                history["best_costs"].append(best_cost)
                history["current_costs"].append(current_cost)

                steps += 1
                if max_steps is not None and steps >= max_steps:
                    self.current = current
                    return best, best_cost, history

            # Cool down
            temp *= self.cooling_rate

        self.current = current
        return best, best_cost, history


def _test_quadratic():
    # Simple test: minimize f(x) = (x-3)^2
    func = lambda x: (x[0] - 3) ** 2
    sa = SimulatedAnnealing(func, [0.0], bounds=[(-10, 10)], temperature=10, iterations_per_temp=50)
    best, cost, hist = sa.optimize()
    print("best:", best, "cost:", cost)


if __name__ == "__main__":
    _test_quadratic()
