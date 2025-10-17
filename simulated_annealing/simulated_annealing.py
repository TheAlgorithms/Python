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
        local_search: Optional[
            Callable[
                [
                    Sequence[float],
                    Callable[[Sequence[float]], float],
                    Callable[[Sequence[float]], Sequence[float]],
                    int,
                ],
                Tuple[Sequence[float], float],
            ]
        ] = None,
        local_search_iters: int = 10,
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
        # local_search: callable(solution, func, neighbor_fn, iters) -> (improved_solution, improved_cost)
        self.local_search = local_search
        self.local_search_iters = int(local_search_iters)
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

    def optimize(
        self,
        max_steps: Optional[int] = None,
        stop_event: Optional[object] = None,
        progress_callback: Optional[Callable[[int, float, float], None]] = None,
    ) -> Tuple[List[float], float, dict]:
        """Run optimization and return best solution, cost, and history.

        New optional args:
        - stop_event: a threading.Event-like object. If set, optimization stops early.
        - progress_callback: callable(step, best_cost, current_cost) called periodically.

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
                # Check stop event
                if (
                    stop_event is not None
                    and getattr(stop_event, "is_set", lambda: False)()
                ):
                    self.current = current
                    return best, best_cost, history

                candidate = self._neighbor(current)
                # Optionally refine candidate with local search before evaluating/accepting
                if self.local_search is not None:
                    try:
                        improved, improved_cost = self.local_search(
                            candidate,
                            self.func,
                            self._neighbor,
                            self.local_search_iters,
                        )
                        candidate = list(improved)
                        candidate_cost = float(improved_cost)
                    except Exception:
                        # Fall back to plain candidate evaluation if local search fails
                        candidate_cost = float(self.func(candidate))
                else:
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
                if (
                    progress_callback is not None
                    and steps % max(1, self.iterations_per_temp // 10) == 0
                ):
                    try:
                        progress_callback(steps, best_cost, current_cost)
                    except Exception:
                        # Don't let callback errors stop optimization
                        pass

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
    sa = SimulatedAnnealing(
        func, [0.0], bounds=[(-10, 10)], temperature=10, iterations_per_temp=50
    )
    best, cost, hist = sa.optimize()
    print("best:", best, "cost:", cost)


def simple_local_search(
    solution: Sequence[float],
    func: Callable[[Sequence[float]], float],
    neighbor_fn: Callable[[Sequence[float]], Sequence[float]],
    iterations: int = 10,
) -> Tuple[Sequence[float], float]:
    """A tiny hill-climbing local search that repeatedly accepts improving neighbors.

    Parameters
    - solution: starting solution sequence
    - func: objective function (lower is better)
    - neighbor_fn: function that given a solution returns a new neighbor solution
    - iterations: number of neighbor attempts

    Returns a tuple (best_solution, best_cost).

    >>> func = lambda x: (x[0] - 5) ** 2
    >>> start = [0.0]
    >>> def neighbor(x):
    ...     return [x[0] + 0.5]
    >>> best, cost = simple_local_search(start, func, neighbor, iterations=5)
    >>> best[0] > start[0]
    True
    >>> cost == func(best)
    True
    """
    best = list(solution)
    best_cost = float(func(best))
    for _ in range(int(iterations)):
        cand = neighbor_fn(best)
        cand_cost = float(func(cand))
        if cand_cost < best_cost:
            best = list(cand)
            best_cost = cand_cost
    return best, best_cost


def _doctest_local_search_benefit():
    """Demonstrate that providing a local_search can improve or match the solution found by SimulatedAnnealing.

    The test uses a deterministic seed so the result is reproducible in doctest.

    >>> func = lambda x: (x[0] - 5) ** 2
    >>> sa1 = SimulatedAnnealing(func, [0.0], bounds=[(-10, 10)], temperature=10, iterations_per_temp=20, seed=1)
    >>> best1, cost1, _ = sa1.optimize(max_steps=200)
    >>> # define a deterministic, greedy local search that moves toward the known minimum (5.0)
    >>> def my_local_search(sol, f, neighbour, iters):
    ...     s = list(sol)
    ...     bestc = float(f(s))
    ...     for _ in range(int(iters)):
    ...         # move halfway toward 5.0 (gradient-free, deterministic)
    ...         s[0] = s[0] + 0.5 * (5.0 - s[0])
    ...         c = float(f(s))
    ...         if c < bestc:
    ...             bestc = c
    ...         else:
    ...             break
    ...     return s, bestc
    >>> sa2 = SimulatedAnnealing(func, [0.0], bounds=[(-10, 10)], temperature=10, iterations_per_temp=20, seed=1, local_search=my_local_search, local_search_iters=5)
    >>> best2, cost2, _ = sa2.optimize(max_steps=200)
    >>> cost2 <= cost1
    True
    """
    pass


if __name__ == "__main__":
    _test_quadratic()
