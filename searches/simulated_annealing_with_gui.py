"""
Simulated Annealing Algorithm with GUI Visualization

This module provides an implementation of the Simulated Annealing optimization
algorithm with an interactive GUI to visualize the optimization process.

Simulated Annealing is a probabilistic technique for approximating the global
optimum of a given function. It is inspired by the annealing process in metallurgy.

Author: GitHub Copilot
Date: October 23, 2025
Reference: https://en.wikipedia.org/wiki/Simulated_annealing
"""

import math
import random
import tkinter as tk
from tkinter import ttk
from typing import Callable

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")


class SimulatedAnnealingOptimizer:
    """
    Simulated Annealing optimizer for continuous optimization problems.
    """

    def __init__(
        self,
        cost_function: Callable[[list[float]], float],
        initial_state: list[float],
        bounds: list[tuple[float, float]],
        initial_temp: float = 1000.0,
        cooling_rate: float = 0.95,
        min_temp: float = 1e-3,
        max_iterations: int = 1000,
    ):
        """
        Initialize the Simulated Annealing optimizer.

        Args:
            cost_function: Function to minimize (takes a list of floats, returns float)
            initial_state: Starting point for optimization
            bounds: List of (min, max) tuples for each dimension
            initial_temp: Starting temperature
            cooling_rate: Rate at which temperature decreases (0 < rate < 1)
            min_temp: Minimum temperature (stopping criterion)
            max_iterations: Maximum number of iterations
        """
        self.cost_function = cost_function
        self.current_state = initial_state.copy()
        self.best_state = initial_state.copy()
        self.bounds = bounds
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp
        self.max_iterations = max_iterations

        self.current_cost = cost_function(self.current_state)
        self.best_cost = self.current_cost
        self.temperature = initial_temp
        self.iteration = 0

        # History for visualization
        self.cost_history: list[float] = [self.current_cost]
        self.best_cost_history: list[float] = [self.best_cost]
        self.temp_history: list[float] = [self.temperature]
        self.acceptance_history: list[float] = []

    def _generate_neighbor(self) -> list[float]:
        """
        Generate a neighboring solution by perturbing the current state.

        Returns:
            A new state near the current state
        """
        neighbor = []
        for i, (current_val, (min_val, max_val)) in enumerate(
            zip(self.current_state, self.bounds)
        ):
            # Adaptive step size based on temperature
            step_size = (max_val - min_val) * 0.1 * (self.temperature / self.initial_temp)
            new_val = current_val + random.uniform(-step_size, step_size)
            # Ensure within bounds
            new_val = max(min_val, min(max_val, new_val))
            neighbor.append(new_val)
        return neighbor

    def _acceptance_probability(self, old_cost: float, new_cost: float) -> float:
        """
        Calculate the probability of accepting a worse solution.

        Args:
            old_cost: Cost of current state
            new_cost: Cost of neighbor state

        Returns:
            Acceptance probability (0 to 1)
        """
        if new_cost < old_cost:
            return 1.0
        return math.exp(-(new_cost - old_cost) / self.temperature)

    def step(self) -> bool:
        """
        Perform one iteration of the algorithm.

        Returns:
            True if optimization should continue, False otherwise
        """
        if self.temperature < self.min_temp or self.iteration >= self.max_iterations:
            return False

        # Generate neighbor
        neighbor_state = self._generate_neighbor()
        neighbor_cost = self.cost_function(neighbor_state)

        # Acceptance criterion
        acceptance_prob = self._acceptance_probability(self.current_cost, neighbor_cost)

        if random.random() < acceptance_prob:
            self.current_state = neighbor_state
            self.current_cost = neighbor_cost
            self.acceptance_history.append(1)

            # Update best solution
            if neighbor_cost < self.best_cost:
                self.best_state = neighbor_state.copy()
                self.best_cost = neighbor_cost
        else:
            self.acceptance_history.append(0)

        # Cool down
        self.temperature *= self.cooling_rate

        # Record history
        self.cost_history.append(self.current_cost)
        self.best_cost_history.append(self.best_cost)
        self.temp_history.append(self.temperature)
        self.iteration += 1

        return True

    def optimize(self) -> tuple[list[float], float]:
        """
        Run the complete optimization.

        Returns:
            Tuple of (best_state, best_cost)
        """
        while self.step():
            pass
        return self.best_state, self.best_cost


class SimulatedAnnealingGUI:
    """
    GUI application for visualizing Simulated Annealing optimization.
    """

    def __init__(self, root: tk.Tk):
        """
        Initialize the GUI.

        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Simulated Annealing Optimizer")
        self.root.geometry("1200x800")

        self.optimizer: SimulatedAnnealingOptimizer | None = None
        self.is_running = False
        self.animation_id: str | None = None

        self._create_widgets()
        self._load_default_problem()

    def _create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Control panel
        control_frame = ttk.LabelFrame(main_frame, text="Controls", padding="10")
        control_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Problem selection
        ttk.Label(control_frame, text="Problem:").grid(row=0, column=0, sticky=tk.W)
        self.problem_var = tk.StringVar(value="Sphere Function")
        problem_combo = ttk.Combobox(
            control_frame,
            textvariable=self.problem_var,
            values=[
                "Sphere Function",
                "Rastrigin Function",
                "Rosenbrock Function",
                "Ackley Function",
            ],
            state="readonly",
            width=20,
        )
        problem_combo.grid(row=0, column=1, padx=5)
        problem_combo.bind("<<ComboboxSelected>>", lambda e: self._load_default_problem())

        # Parameters
        ttk.Label(control_frame, text="Initial Temp:").grid(row=0, column=2, padx=(20, 5))
        self.temp_var = tk.StringVar(value="1000")
        ttk.Entry(control_frame, textvariable=self.temp_var, width=10).grid(
            row=0, column=3
        )

        ttk.Label(control_frame, text="Cooling Rate:").grid(row=0, column=4, padx=(20, 5))
        self.cooling_var = tk.StringVar(value="0.95")
        ttk.Entry(control_frame, textvariable=self.cooling_var, width=10).grid(
            row=0, column=5
        )

        ttk.Label(control_frame, text="Max Iterations:").grid(
            row=0, column=6, padx=(20, 5)
        )
        self.max_iter_var = tk.StringVar(value="1000")
        ttk.Entry(control_frame, textvariable=self.max_iter_var, width=10).grid(
            row=0, column=7
        )

        # Buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.grid(row=1, column=0, columnspan=8, pady=10)

        self.start_button = ttk.Button(
            button_frame, text="Start", command=self._start_optimization
        )
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = ttk.Button(
            button_frame, text="Pause", command=self._pause_optimization, state=tk.DISABLED
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = ttk.Button(
            button_frame, text="Reset", command=self._reset_optimization
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(control_frame, textvariable=self.status_var)
        status_label.grid(row=2, column=0, columnspan=8)

        # Visualization area
        viz_frame = ttk.Frame(main_frame)
        viz_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create matplotlib figure
        self.fig = Figure(figsize=(12, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Create subplots
        self.ax1 = self.fig.add_subplot(131)
        self.ax2 = self.fig.add_subplot(132)
        self.ax3 = self.fig.add_subplot(133)

        self._setup_plots()

    def _setup_plots(self):
        """Initialize the plot areas."""
        self.ax1.set_title("Cost History")
        self.ax1.set_xlabel("Iteration")
        self.ax1.set_ylabel("Cost")
        self.ax1.grid(True, alpha=0.3)

        self.ax2.set_title("Temperature")
        self.ax2.set_xlabel("Iteration")
        self.ax2.set_ylabel("Temperature")
        self.ax2.grid(True, alpha=0.3)

        self.ax3.set_title("Acceptance Rate")
        self.ax3.set_xlabel("Iteration Window")
        self.ax3.set_ylabel("Acceptance Rate")
        self.ax3.grid(True, alpha=0.3)
        self.ax3.set_ylim([0, 1])

        self.fig.tight_layout()

    def _get_test_function(self, name: str) -> tuple[Callable, list[float], list[tuple]]:
        """
        Get test function, initial state, and bounds.

        Args:
            name: Name of the test function

        Returns:
            Tuple of (function, initial_state, bounds)
        """
        if name == "Sphere Function":
            # f(x) = sum(x_i^2), minimum at (0, 0, ..., 0) = 0
            func = lambda x: sum(xi**2 for xi in x)
            initial = [random.uniform(-5, 5) for _ in range(3)]
            bounds = [(-10, 10)] * 3

        elif name == "Rastrigin Function":
            # Highly multimodal function
            func = lambda x: 10 * len(x) + sum(
                xi**2 - 10 * math.cos(2 * math.pi * xi) for xi in x
            )
            initial = [random.uniform(-5, 5) for _ in range(3)]
            bounds = [(-5.12, 5.12)] * 3

        elif name == "Rosenbrock Function":
            # f(x) = sum(100*(x_{i+1} - x_i^2)^2 + (1-x_i)^2)
            func = lambda x: sum(
                100 * (x[i + 1] - x[i] ** 2) ** 2 + (1 - x[i]) ** 2
                for i in range(len(x) - 1)
            )
            initial = [random.uniform(-2, 2) for _ in range(3)]
            bounds = [(-5, 5)] * 3

        elif name == "Ackley Function":
            # Highly multimodal with global minimum at (0, 0, ..., 0) = 0
            n = 3
            func = lambda x: (
                -20 * math.exp(-0.2 * math.sqrt(sum(xi**2 for xi in x) / n))
                - math.exp(sum(math.cos(2 * math.pi * xi) for xi in x) / n)
                + 20
                + math.e
            )
            initial = [random.uniform(-2, 2) for _ in range(n)]
            bounds = [(-5, 5)] * n

        else:
            func = lambda x: sum(xi**2 for xi in x)
            initial = [0.0, 0.0]
            bounds = [(-10, 10)] * 2

        return func, initial, bounds

    def _load_default_problem(self):
        """Load the default problem based on selection."""
        self._reset_optimization()

    def _start_optimization(self):
        """Start or resume the optimization."""
        if self.optimizer is None:
            # Create new optimizer
            problem_name = self.problem_var.get()
            func, initial, bounds = self._get_test_function(problem_name)

            try:
                initial_temp = float(self.temp_var.get())
                cooling_rate = float(self.cooling_var.get())
                max_iter = int(self.max_iter_var.get())
            except ValueError:
                self.status_var.set("Error: Invalid parameters")
                return

            self.optimizer = SimulatedAnnealingOptimizer(
                cost_function=func,
                initial_state=initial,
                bounds=bounds,
                initial_temp=initial_temp,
                cooling_rate=cooling_rate,
                max_iterations=max_iter,
            )

        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self._animate()

    def _pause_optimization(self):
        """Pause the optimization."""
        self.is_running = False
        self.start_button.config(state=tk.NORMAL, text="Resume")
        self.pause_button.config(state=tk.DISABLED)
        if self.animation_id:
            self.root.after_cancel(self.animation_id)
        self.status_var.set("Paused")

    def _reset_optimization(self):
        """Reset the optimization."""
        self.is_running = False
        self.optimizer = None
        if self.animation_id:
            self.root.after_cancel(self.animation_id)

        self.start_button.config(state=tk.NORMAL, text="Start")
        self.pause_button.config(state=tk.DISABLED)

        # Clear plots
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self._setup_plots()
        self.canvas.draw()

        self.status_var.set("Ready")

    def _animate(self):
        """Animate one step of the optimization."""
        if not self.is_running or self.optimizer is None:
            return

        # Perform multiple steps per frame for speed
        steps_per_frame = 5
        for _ in range(steps_per_frame):
            if not self.optimizer.step():
                self._optimization_complete()
                return

        # Update plots
        self._update_plots()

        # Update status
        self.status_var.set(
            f"Iteration: {self.optimizer.iteration} | "
            f"Best Cost: {self.optimizer.best_cost:.6f} | "
            f"Current Cost: {self.optimizer.current_cost:.6f} | "
            f"Temp: {self.optimizer.temperature:.3f}"
        )

        # Schedule next frame
        self.animation_id = self.root.after(50, self._animate)

    def _update_plots(self):
        """Update all plots with current data."""
        if self.optimizer is None:
            return

        # Cost history
        self.ax1.clear()
        self.ax1.plot(
            self.optimizer.cost_history, label="Current Cost", alpha=0.6, linewidth=1
        )
        self.ax1.plot(
            self.optimizer.best_cost_history,
            label="Best Cost",
            color="red",
            linewidth=2,
        )
        self.ax1.set_title("Cost History")
        self.ax1.set_xlabel("Iteration")
        self.ax1.set_ylabel("Cost")
        self.ax1.legend()
        self.ax1.grid(True, alpha=0.3)

        # Temperature
        self.ax2.clear()
        self.ax2.plot(self.optimizer.temp_history, color="orange", linewidth=2)
        self.ax2.set_title("Temperature")
        self.ax2.set_xlabel("Iteration")
        self.ax2.set_ylabel("Temperature")
        self.ax2.grid(True, alpha=0.3)

        # Acceptance rate (rolling window)
        if len(self.optimizer.acceptance_history) > 20:
            window_size = 50
            acceptance_rates = []
            for i in range(window_size, len(self.optimizer.acceptance_history)):
                window = self.optimizer.acceptance_history[i - window_size : i]
                acceptance_rates.append(sum(window) / len(window))

            self.ax3.clear()
            self.ax3.plot(acceptance_rates, color="green", linewidth=2)
            self.ax3.set_title("Acceptance Rate (50-iteration window)")
            self.ax3.set_xlabel("Iteration Window")
            self.ax3.set_ylabel("Acceptance Rate")
            self.ax3.set_ylim([0, 1])
            self.ax3.grid(True, alpha=0.3)

        self.fig.tight_layout()
        self.canvas.draw()

    def _optimization_complete(self):
        """Handle optimization completion."""
        self.is_running = False
        self.start_button.config(state=tk.NORMAL, text="Start")
        self.pause_button.config(state=tk.DISABLED)

        if self.optimizer:
            self.status_var.set(
                f"Optimization Complete! Best Cost: {self.optimizer.best_cost:.6f} | "
                f"Best State: {[f'{x:.4f}' for x in self.optimizer.best_state]}"
            )


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = SimulatedAnnealingGUI(root)
    root.mainloop()


if __name__ == "__main__":
    # Example of using the optimizer without GUI
    print("Running Simulated Annealing Optimizer")
    print("=" * 50)

    # Test with Sphere function
    sphere = lambda x: sum(xi**2 for xi in x)
    optimizer = SimulatedAnnealingOptimizer(
        cost_function=sphere,
        initial_state=[5.0, -5.0, 3.0],
        bounds=[(-10, 10)] * 3,
        initial_temp=1000,
        cooling_rate=0.95,
        max_iterations=1000,
    )

    best_state, best_cost = optimizer.optimize()
    print(f"\nSphere Function Optimization:")
    print(f"Best solution: {best_state}")
    print(f"Best cost: {best_cost:.6f}")
    print(f"Iterations: {optimizer.iteration}")

    # Launch GUI
    print("\nLaunching GUI...")
    main()
