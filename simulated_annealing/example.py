from typing import Callable, Dict, Sequence


def sphere(x: Sequence[float]) -> float:
    return sum(v * v for v in x)


def rastrigin(x: Sequence[float]) -> float:
    # Rastrigin function (common test function)
    A = 10
    return A * len(x) + sum((v * v - A * __import__("math").cos(2 * __import__("math").pi * v)) for v in x)


example_functions: Dict[str, Callable[[Sequence[float]], float]] = {
    "sphere": sphere,
    "rastrigin": rastrigin,
}


def cli_example():
    # CLI demo minimizing 2D sphere
    from .simulated_annealing import SimulatedAnnealing
    func = sphere
    initial = [5.0, -3.0]
    bounds = [(-10, 10), (-10, 10)]
    sa = SimulatedAnnealing(func, initial, bounds=bounds, temperature=50, cooling_rate=0.95, iterations_per_temp=200)
    best, cost, history = sa.optimize()
    print("Best:", best)
    print("Cost:", cost)


if __name__ == "__main__":
    cli_example()
