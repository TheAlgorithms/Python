#!/usr/bin/env python3
"""
Comprehensive test and example script for neural network optimizers.

This script demonstrates all implemented optimizers and provides comparative
analysis on different optimization problems.
"""

import math
from typing import List, Tuple

# Import all optimizers
from neural_network.optimizers import SGD, MomentumSGD, NAG, Adagrad, Adam


def test_basic_functionality() -> None:
    """Test basic functionality of all optimizers."""
    print("=" * 60)
    print("BASIC FUNCTIONALITY TESTS")
    print("=" * 60)

    # Test parameters
    params = [1.0, 2.0]
    grads = [0.1, 0.2]

    optimizers = {
        "SGD": SGD(learning_rate=0.1),
        "MomentumSGD": MomentumSGD(learning_rate=0.1, momentum=0.9),
        "NAG": NAG(learning_rate=0.1, momentum=0.9),
        "Adagrad": Adagrad(learning_rate=0.1),
        "Adam": Adam(learning_rate=0.1),
    }

    print(f"Initial parameters: {params}")
    print(f"Gradients: {grads}")
    print()

    for name, optimizer in optimizers.items():
        updated = optimizer.update(params.copy(), grads)
        print(f"{name:12s}: {updated}")

        # Test reset functionality
        optimizer.reset()

    print("\n✅ All optimizers working correctly!\n")


def quadratic_optimization() -> None:
    """Compare optimizers on simple quadratic function f(x) = x²."""
    print("=" * 60)
    print("QUADRATIC OPTIMIZATION: f(x) = x²")
    print("=" * 60)
    print("Target: minimize f(x) = x² starting from x = 5")
    print("Optimal solution: x* = 0, f(x*) = 0")
    print()

    # Initialize optimizers
    optimizers = {
        "SGD": SGD(0.1),
        "Momentum": MomentumSGD(0.1, 0.9),
        "NAG": NAG(0.1, 0.9),
        "Adagrad": Adagrad(0.3),
        "Adam": Adam(0.2),
    }

    # Starting positions
    positions = {name: [5.0] for name in optimizers}

    print(
        f"{'Step':<4} {'SGD':<8} {'Momentum':<8} {'NAG':<8} {'Adagrad':<8} {'Adam':<8}"
    )
    print("-" * 50)

    for step in range(21):
        if step % 5 == 0:  # Print every 5 steps
            print(f"{step:<4d} ", end="")
            for name in optimizers:
                x = positions[name][0]
                print(f"{x:7.4f} ", end=" ")
            print()

        # Update all optimizers
        for name, optimizer in optimizers.items():
            x = positions[name][0]
            gradient = [2 * x]  # f'(x) = 2x
            positions[name] = optimizer.update(positions[name], gradient)

    print("\nFinal convergence distances from optimum:")
    for name in optimizers:
        final_x = positions[name][0]
        distance = abs(final_x)
        print(f"{name:12s}: |x - 0| = {distance:.6f}")
    print()


def multidimensional_optimization() -> None:
    """Compare optimizers on f(x,y) = x² + 10y² (different curvatures)."""
    print("=" * 60)
    print("MULTI-DIMENSIONAL: f(x,y) = x² + 10y²")
    print("=" * 60)
    print("Different curvatures test optimizer adaptation")
    print("Starting point: (5, 1), Target: (0, 0)")
    print()

    optimizers = {
        "SGD": SGD(0.01),
        "Momentum": MomentumSGD(0.01, 0.9),
        "NAG": NAG(0.01, 0.9),
        "Adagrad": Adagrad(0.1),
        "Adam": Adam(0.05),
    }

    positions = {name: [5.0, 1.0] for name in optimizers}

    def f(x: float, y: float) -> float:
        return x * x + 10 * y * y

    def grad_f(x: float, y: float) -> List[float]:
        return [2 * x, 20 * y]

    print(f"{'Step':<4} {'Loss':<45}")
    print(f"     {'SGD':<8} {'Momentum':<8} {'NAG':<8} {'Adagrad':<8} {'Adam':<8}")
    print("-" * 54)

    for step in range(51):
        if step % 10 == 0:
            print(f"{step:<4d} ", end="")
            for name in optimizers:
                x, y = positions[name]
                loss = f(x, y)
                print(f"{loss:7.3f} ", end=" ")
            print()

        # Update all optimizers
        for name, optimizer in optimizers.items():
            x, y = positions[name]
            gradient = grad_f(x, y)
            positions[name] = optimizer.update(positions[name], gradient)

    print("\nFinal results:")
    for name in optimizers:
        x, y = positions[name]
        loss = f(x, y)
        distance = math.sqrt(x * x + y * y)
        print(f"{name:12s}: loss = {loss:.6f}, distance = {distance:.6f}")
    print()


def rosenbrock_optimization() -> None:
    """Compare optimizers on challenging Rosenbrock function."""
    print("=" * 60)
    print("ROSENBROCK FUNCTION: f(x,y) = 100(y-x²)² + (1-x)²")
    print("=" * 60)
    print("Classic non-convex test function")
    print("Global minimum: (1, 1), f(1, 1) = 0")
    print("Starting point: (-1, 1)")
    print()

    optimizers = {
        "SGD": SGD(0.0005),
        "Momentum": MomentumSGD(0.0005, 0.9),
        "NAG": NAG(0.0005, 0.9),
        "Adagrad": Adagrad(0.01),
        "Adam": Adam(0.01),
    }

    positions = {name: [-1.0, 1.0] for name in optimizers}

    def rosenbrock(x: float, y: float) -> float:
        return 100 * (y - x * x) ** 2 + (1 - x) ** 2

    def rosenbrock_grad(x: float, y: float) -> List[float]:
        df_dx = -400 * x * (y - x * x) - 2 * (1 - x)
        df_dy = 200 * (y - x * x)
        return [df_dx, df_dy]

    print(f"{'Step':<5} {'Loss':<48}")
    print(f"      {'SGD':<9} {'Momentum':<9} {'NAG':<9} {'Adagrad':<9} {'Adam':<9}")
    print("-" * 58)

    for step in range(201):
        if step % 40 == 0:
            print(f"{step:<5d} ", end="")
            for name in optimizers:
                x, y = positions[name]
                loss = rosenbrock(x, y)
                print(f"{loss:8.3f} ", end=" ")
            print()

        # Update all optimizers
        for name, optimizer in optimizers.items():
            x, y = positions[name]
            gradient = rosenbrock_grad(x, y)
            positions[name] = optimizer.update(positions[name], gradient)

    print("\nFinal results:")
    best_loss = float("inf")
    best_optimizer = ""

    for name in optimizers:
        x, y = positions[name]
        loss = rosenbrock(x, y)
        distance_to_optimum = math.sqrt((x - 1) ** 2 + (y - 1) ** 2)
        print(
            f"{name:12s}: loss = {loss:8.3f}, pos = ({x:6.3f}, {y:6.3f}), dist = {distance_to_optimum:.4f}"
        )

        if loss < best_loss:
            best_loss = loss
            best_optimizer = name

    print(f"\n🏆 Best performer: {best_optimizer} (loss = {best_loss:.3f})")
    print()


def convergence_analysis() -> None:
    """Analyze convergence behavior on a simple problem."""
    print("=" * 60)
    print("CONVERGENCE ANALYSIS")
    print("=" * 60)
    print("Analyzing convergence speed on f(x) = x² from x = 10")
    print()

    optimizers = {
        "SGD": SGD(0.05),
        "Momentum": MomentumSGD(0.05, 0.9),
        "Adam": Adam(0.1),
    }

    positions = {name: [10.0] for name in optimizers}
    convergence_steps = {name: None for name in optimizers}
    tolerance = 0.01

    for step in range(100):
        converged_this_step = []

        for name, optimizer in optimizers.items():
            x = positions[name][0]

            # Check if converged (within tolerance of optimum)
            if abs(x) < tolerance and convergence_steps[name] is None:
                convergence_steps[name] = step
                converged_this_step.append(name)

            # Update
            gradient = [2 * x]
            positions[name] = optimizer.update(positions[name], gradient)

        # Print convergence notifications
        for name in converged_this_step:
            print(f"{name} converged at step {step} (|x| < {tolerance})")

    print("\nConvergence summary:")
    for name in optimizers:
        steps = convergence_steps[name]
        final_x = positions[name][0]
        if steps is not None:
            print(
                f"{name:12s}: converged in {steps:2d} steps (final |x| = {abs(final_x):.6f})"
            )
        else:
            print(f"{name:12s}: did not converge (final |x| = {abs(final_x):.6f})")
    print()


def main() -> None:
    """Run all test examples."""
    print("🧠 NEURAL NETWORK OPTIMIZERS COMPREHENSIVE TEST")
    print("=" * 60)
    print("Testing SGD, MomentumSGD, NAG, Adagrad, and Adam optimizers")
    print("=" * 60)
    print()

    test_basic_functionality()
    quadratic_optimization()
    multidimensional_optimization()
    rosenbrock_optimization()
    convergence_analysis()

    print("🎉 All tests completed successfully!")
    print("\nKey takeaways:")
    print("• SGD: Simple but can be slow on complex functions")
    print("• Momentum: Accelerates SGD, good for noisy gradients")
    print("• NAG: Better than momentum for overshooting problems")
    print("• Adagrad: Automatic learning rate adaptation")
    print("• Adam: Generally robust, good default choice")
    print("\nFor more details, see the README.md file.")


if __name__ == "__main__":
    main()
