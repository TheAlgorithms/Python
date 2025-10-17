from typing import Callable, Dict, Sequence


def sphere(x: Sequence[float]) -> float:
    return sum(v * v for v in x)


def rastrigin(x: Sequence[float]) -> float:
    # Rastrigin function (common test function)
    A = 10
    return A * len(x) + sum(
        (v * v - A * __import__("math").cos(2 * __import__("math").pi * v)) for v in x
    )


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
    sa = SimulatedAnnealing(
        func,
        initial,
        bounds=bounds,
        temperature=50,
        cooling_rate=0.95,
        iterations_per_temp=200,
    )
    best, cost, history = sa.optimize()
    print("Best:", best)
    print("Cost:", cost)


def tsp_example():
    # Small TSP demo
    from .simulated_annealing import SimulatedAnnealing
    from .tsp import make_tsp_cost, random_tour, vector_to_tour

    coords = [(0, 0), (1, 5), (5, 4), (6, 1), (3, -2)]
    n = len(coords)
    init_tour = random_tour(n)
    # represent tour as vector by using tour indices as values (so ranking recovers order)
    initial = [float(i) for i in init_tour]
    cost_fn = make_tsp_cost(coords)

    sa = SimulatedAnnealing(
        cost_fn, initial, temperature=100.0, cooling_rate=0.995, iterations_per_temp=500
    )
    best, cost, history = sa.optimize()
    best_tour = vector_to_tour(best)
    print("Best tour:", best_tour)
    print("Cost:", cost)


if __name__ == "__main__":
    # Run CLI examples
    print("Running continuous example...")
    cli_example()
    print("Running TSP example...")
    tsp_example()
