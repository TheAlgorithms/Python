"""
Test script for Simulated Annealing implementations

This script tests the basic functionality of both simulated annealing
implementations without GUI to ensure they work correctly.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_basic_simulated_annealing():
    """Test the basic simulated annealing implementation."""
    print("Testing basic simulated annealing...")
    print("-" * 60)

    from searches.simulated_annealing import SearchProblem, simulated_annealing

    # Test 1: Minimize x^2 + y^2
    def test_f1(x, y):
        return x**2 + y**2

    prob = SearchProblem(x=5, y=5, step_size=1, function_to_optimize=test_f1)
    result = simulated_annealing(
        prob,
        find_max=False,
        max_x=10,
        min_x=-10,
        max_y=10,
        min_y=-10,
        visualization=False,
    )

    print(f"Test 1: Minimize f(x,y) = x^2 + y^2")
    print(f"  Starting point: (5, 5)")
    print(f"  Result: {result}")
    print(f"  Final score: {result.score():.4f}")
    print(f"  Expected minimum: ~0 at (0, 0)")

    # Verify it found a reasonable minimum
    assert result.score() < 10, f"Score too high: {result.score()}"
    print("  ✓ Test passed!\n")


def test_optimizer_with_gui_module():
    """Test the SimulatedAnnealingOptimizer class (without GUI)."""
    print("Testing SimulatedAnnealingOptimizer class...")
    print("-" * 60)

    from searches.simulated_annealing_with_gui import SimulatedAnnealingOptimizer

    # Test with Sphere function
    def sphere(x):
        return sum(xi**2 for xi in x)

    print("Test 2: Optimize Sphere function")
    print("  f(x) = sum(x_i^2)")
    print("  Starting point: [5, -5, 3]")

    optimizer = SimulatedAnnealingOptimizer(
        cost_function=sphere,
        initial_state=[5.0, -5.0, 3.0],
        bounds=[(-10, 10)] * 3,
        initial_temp=1000,
        cooling_rate=0.95,
        max_iterations=1000,
    )

    best_state, best_cost = optimizer.optimize()

    print(f"  Best solution: {[f'{x:.4f}' for x in best_state]}")
    print(f"  Best cost: {best_cost:.4f}")
    print(f"  Iterations: {optimizer.iteration}")
    print(f"  Expected minimum: ~0 at [0, 0, 0]")

    # Verify reasonable result
    assert best_cost < 1.0, f"Cost too high: {best_cost}"
    print("  ✓ Test passed!\n")

    # Test with Rastrigin function
    import math

    def rastrigin(x):
        return 10 * len(x) + sum(xi**2 - 10 * math.cos(2 * math.pi * xi) for xi in x)

    print("Test 3: Optimize Rastrigin function (multimodal)")
    print("  f(x) = 10n + sum(x_i^2 - 10*cos(2π*x_i))")
    print("  Starting point: [2, -2]")

    optimizer = SimulatedAnnealingOptimizer(
        cost_function=rastrigin,
        initial_state=[2.0, -2.0],
        bounds=[(-5.12, 5.12)] * 2,
        initial_temp=1000,
        cooling_rate=0.95,
        max_iterations=2000,
    )

    best_state, best_cost = optimizer.optimize()

    print(f"  Best solution: {[f'{x:.4f}' for x in best_state]}")
    print(f"  Best cost: {best_cost:.4f}")
    print(f"  Iterations: {optimizer.iteration}")
    print(f"  Expected minimum: 0 at [0, 0]")

    # Rastrigin is harder, so accept a less strict bound
    assert best_cost < 5.0, f"Cost too high: {best_cost}"
    print("  ✓ Test passed!\n")


def test_tsp_solver():
    """Test the TSP solver (without GUI)."""
    print("Testing TSP Simulated Annealing...")
    print("-" * 60)

    import random

    from searches.simulated_annealing_tsp import City, TSPSimulatedAnnealing

    # Create a simple set of cities
    random.seed(42)  # For reproducibility
    cities = [
        City(0, 0, "A"),
        City(1, 0, "B"),
        City(1, 1, "C"),
        City(0, 1, "D"),
    ]

    print("Test 4: Solve TSP for 4 cities (square)")
    print(f"  Cities: {len(cities)}")
    for city in cities:
        print(f"    {city}")

    solver = TSPSimulatedAnnealing(
        cities=cities, initial_temp=100, cooling_rate=0.95, max_iterations=1000
    )

    initial_distance = solver.current_route.total_distance()
    best_route = solver.solve()
    final_distance = best_route.total_distance()

    print(f"\n  Initial distance: {initial_distance:.4f}")
    print(f"  Final distance: {final_distance:.4f}")
    print(f"  Improvement: {initial_distance - final_distance:.4f}")
    print(f"  Route order: {best_route.order}")
    print(f"  Iterations: {solver.iteration}")

    # Optimal for square should be 4 (perimeter)
    print(f"  Expected optimal: 4.0")
    assert final_distance <= initial_distance, "Distance increased!"
    assert (
        abs(final_distance - 4.0) < 0.1
    ), f"Not close to optimal: {final_distance}"
    print("  ✓ Test passed!\n")

    # Test with more cities
    random.seed(42)
    cities = [
        City(random.uniform(0, 10), random.uniform(0, 10), f"City{i}")
        for i in range(10)
    ]

    print("Test 5: Solve TSP for 10 random cities")
    print(f"  Cities: {len(cities)}")

    solver = TSPSimulatedAnnealing(
        cities=cities, initial_temp=1000, cooling_rate=0.995, max_iterations=5000
    )

    initial_distance = solver.current_route.total_distance()
    best_route = solver.solve()
    final_distance = best_route.total_distance()

    print(f"\n  Initial distance: {initial_distance:.4f}")
    print(f"  Final distance: {final_distance:.4f}")
    print(f"  Improvement: {initial_distance - final_distance:.4f}")
    print(f"  Improvement %: {100 * (initial_distance - final_distance) / initial_distance:.2f}%")
    print(f"  Iterations: {solver.iteration}")

    assert final_distance < initial_distance, "No improvement found!"
    improvement_pct = 100 * (initial_distance - final_distance) / initial_distance
    assert improvement_pct > 10, f"Improvement too small: {improvement_pct:.2f}%"
    print("  ✓ Test passed!\n")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Simulated Annealing Implementation Tests")
    print("=" * 60)
    print()

    try:
        test_basic_simulated_annealing()
        test_optimizer_with_gui_module()
        test_tsp_solver()

        print("=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        print()
        print("To run the GUI applications, use:")
        print("  python searches/simulated_annealing_with_gui.py")
        print("  python searches/simulated_annealing_tsp.py")

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
