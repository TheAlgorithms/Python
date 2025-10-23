"""
Simulated Annealing for Traveling Salesman Problem (TSP)

This module implements the Simulated Annealing algorithm specifically for solving
the Traveling Salesman Problem with an interactive GUI visualization.

The TSP asks: "Given a list of cities and the distances between each pair of cities,
what is the shortest possible route that visits each city exactly once and returns
to the origin city?"

Author: GitHub Copilot
Date: October 23, 2025
Reference: https://en.wikipedia.org/wiki/Travelling_salesman_problem
"""

import math
import random
import tkinter as tk
from tkinter import ttk
from typing import Any

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")


class City:
    """Represents a city with x, y coordinates."""

    def __init__(self, x: float, y: float, name: str = ""):
        """
        Initialize a city.

        Args:
            x: X coordinate
            y: Y coordinate
            name: Optional name for the city
        """
        self.x = x
        self.y = y
        self.name = name or f"City({x:.1f}, {y:.1f})"

    def distance_to(self, other: "City") -> float:
        """
        Calculate Euclidean distance to another city.

        Args:
            other: Another City object

        Returns:
            Euclidean distance
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self) -> str:
        """String representation of the city."""
        return f"{self.name}({self.x:.2f}, {self.y:.2f})"


class TSPRoute:
    """Represents a route through all cities."""

    def __init__(self, cities: list[City], order: list[int] | None = None):
        """
        Initialize a TSP route.

        Args:
            cities: List of City objects
            order: Order in which to visit cities (indices). If None, use sequential order.
        """
        self.cities = cities
        self.order = order if order is not None else list(range(len(cities)))
        self._distance: float | None = None

    def total_distance(self) -> float:
        """
        Calculate total distance of the route.

        Returns:
            Total distance traveling through all cities and back to start
        """
        if self._distance is None:
            distance = 0.0
            for i in range(len(self.order)):
                from_city = self.cities[self.order[i]]
                to_city = self.cities[self.order[(i + 1) % len(self.order)]]
                distance += from_city.distance_to(to_city)
            self._distance = distance
        return self._distance

    def swap_cities(self, i: int, j: int) -> "TSPRoute":
        """
        Create a new route with two cities swapped.

        Args:
            i: Index of first city in order
            j: Index of second city in order

        Returns:
            New TSPRoute with cities swapped
        """
        new_order = self.order.copy()
        new_order[i], new_order[j] = new_order[j], new_order[i]
        return TSPRoute(self.cities, new_order)

    def reverse_segment(self, i: int, j: int) -> "TSPRoute":
        """
        Create a new route with a segment reversed (2-opt move).

        Args:
            i: Start index of segment
            j: End index of segment

        Returns:
            New TSPRoute with segment reversed
        """
        new_order = self.order.copy()
        if i > j:
            i, j = j, i
        new_order[i : j + 1] = reversed(new_order[i : j + 1])
        return TSPRoute(self.cities, new_order)

    def copy(self) -> "TSPRoute":
        """Create a copy of this route."""
        return TSPRoute(self.cities, self.order.copy())


class TSPSimulatedAnnealing:
    """Simulated Annealing solver for TSP."""

    def __init__(
        self,
        cities: list[City],
        initial_temp: float = 1000.0,
        cooling_rate: float = 0.995,
        min_temp: float = 1e-3,
        max_iterations: int = 10000,
    ):
        """
        Initialize TSP solver.

        Args:
            cities: List of City objects
            initial_temp: Starting temperature
            cooling_rate: Rate at which temperature decreases
            min_temp: Minimum temperature (stopping criterion)
            max_iterations: Maximum iterations
        """
        self.cities = cities
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp
        self.max_iterations = max_iterations

        # Initialize with random route
        initial_order = list(range(len(cities)))
        random.shuffle(initial_order)
        self.current_route = TSPRoute(cities, initial_order)
        self.best_route = self.current_route.copy()

        self.temperature = initial_temp
        self.iteration = 0

        # History
        self.distance_history: list[float] = [self.current_route.total_distance()]
        self.best_distance_history: list[float] = [self.best_route.total_distance()]
        self.temp_history: list[float] = [self.temperature]

    def _acceptance_probability(self, old_dist: float, new_dist: float) -> float:
        """
        Calculate acceptance probability for a new route.

        Args:
            old_dist: Current route distance
            new_dist: Neighbor route distance

        Returns:
            Acceptance probability
        """
        if new_dist < old_dist:
            return 1.0
        return math.exp(-(new_dist - old_dist) / self.temperature)

    def step(self) -> bool:
        """
        Perform one iteration.

        Returns:
            True if should continue, False if done
        """
        if self.temperature < self.min_temp or self.iteration >= self.max_iterations:
            return False

        # Generate neighbor by reversing a random segment (2-opt)
        i, j = sorted(random.sample(range(len(self.cities)), 2))
        neighbor_route = self.current_route.reverse_segment(i, j)

        current_dist = self.current_route.total_distance()
        neighbor_dist = neighbor_route.total_distance()

        # Acceptance criterion
        if random.random() < self._acceptance_probability(current_dist, neighbor_dist):
            self.current_route = neighbor_route

            # Update best
            if neighbor_dist < self.best_route.total_distance():
                self.best_route = neighbor_route.copy()

        # Cool down
        self.temperature *= self.cooling_rate

        # Record history
        self.distance_history.append(self.current_route.total_distance())
        self.best_distance_history.append(self.best_route.total_distance())
        self.temp_history.append(self.temperature)
        self.iteration += 1

        return True

    def solve(self) -> TSPRoute:
        """
        Run complete optimization.

        Returns:
            Best route found
        """
        while self.step():
            pass
        return self.best_route


class TSPGUI:
    """GUI for TSP Simulated Annealing visualization."""

    def __init__(self, root: tk.Tk):
        """Initialize the GUI."""
        self.root = root
        self.root.title("TSP - Simulated Annealing")
        self.root.geometry("1400x800")

        self.cities: list[City] = []
        self.solver: TSPSimulatedAnnealing | None = None
        self.is_running = False
        self.animation_id: str | None = None

        self._create_widgets()
        self._generate_random_cities(20)

    def _create_widgets(self):
        """Create all GUI widgets."""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Control panel
        control_frame = ttk.LabelFrame(main_frame, text="Controls", padding="10")
        control_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Number of cities
        ttk.Label(control_frame, text="Number of Cities:").grid(
            row=0, column=0, sticky=tk.W
        )
        self.num_cities_var = tk.StringVar(value="20")
        ttk.Entry(control_frame, textvariable=self.num_cities_var, width=10).grid(
            row=0, column=1
        )

        ttk.Button(
            control_frame, text="Generate Cities", command=self._generate_cities_from_input
        ).grid(row=0, column=2, padx=5)

        # Parameters
        ttk.Label(control_frame, text="Initial Temp:").grid(row=0, column=3, padx=(20, 5))
        self.temp_var = tk.StringVar(value="1000")
        ttk.Entry(control_frame, textvariable=self.temp_var, width=10).grid(
            row=0, column=4
        )

        ttk.Label(control_frame, text="Cooling Rate:").grid(row=0, column=5, padx=(20, 5))
        self.cooling_var = tk.StringVar(value="0.995")
        ttk.Entry(control_frame, textvariable=self.cooling_var, width=10).grid(
            row=0, column=6
        )

        # Buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.grid(row=1, column=0, columnspan=7, pady=10)

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

        # Status
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(control_frame, textvariable=self.status_var).grid(
            row=2, column=0, columnspan=7
        )

        # Visualization
        viz_frame = ttk.Frame(main_frame)
        viz_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.fig = Figure(figsize=(14, 7))
        self.canvas = FigureCanvasTkAgg(self.fig, master=viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Create subplots: route visualization and metrics
        self.ax_route = self.fig.add_subplot(121)
        self.ax_metrics = self.fig.add_subplot(122)

        self._setup_plots()

    def _setup_plots(self):
        """Initialize plots."""
        self.ax_route.set_title("Current Best Route")
        self.ax_route.set_xlabel("X")
        self.ax_route.set_ylabel("Y")
        self.ax_route.set_aspect("equal")
        self.ax_route.grid(True, alpha=0.3)

        self.ax_metrics.set_title("Distance Over Time")
        self.ax_metrics.set_xlabel("Iteration")
        self.ax_metrics.set_ylabel("Distance")
        self.ax_metrics.grid(True, alpha=0.3)

        self.fig.tight_layout()

    def _generate_random_cities(self, n: int):
        """Generate n random cities."""
        self.cities = [
            City(random.uniform(0, 100), random.uniform(0, 100), f"C{i}") for i in range(n)
        ]
        self._plot_initial_cities()

    def _generate_cities_from_input(self):
        """Generate cities based on user input."""
        try:
            n = int(self.num_cities_var.get())
            if n < 3:
                self.status_var.set("Error: Need at least 3 cities")
                return
            if n > 100:
                self.status_var.set("Error: Maximum 100 cities")
                return
            self._generate_random_cities(n)
            self._reset_optimization()
        except ValueError:
            self.status_var.set("Error: Invalid number of cities")

    def _plot_initial_cities(self):
        """Plot initial city positions."""
        self.ax_route.clear()
        x = [city.x for city in self.cities]
        y = [city.y for city in self.cities]
        self.ax_route.scatter(x, y, c="red", s=100, zorder=2)
        for i, city in enumerate(self.cities):
            self.ax_route.annotate(
                str(i), (city.x, city.y), xytext=(5, 5), textcoords="offset points"
            )
        self.ax_route.set_title("Cities")
        self.ax_route.set_xlabel("X")
        self.ax_route.set_ylabel("Y")
        self.ax_route.set_aspect("equal")
        self.ax_route.grid(True, alpha=0.3)
        self.fig.tight_layout()
        self.canvas.draw()

    def _start_optimization(self):
        """Start the optimization."""
        if len(self.cities) < 3:
            self.status_var.set("Error: Need at least 3 cities")
            return

        if self.solver is None:
            try:
                initial_temp = float(self.temp_var.get())
                cooling_rate = float(self.cooling_var.get())
            except ValueError:
                self.status_var.set("Error: Invalid parameters")
                return

            self.solver = TSPSimulatedAnnealing(
                cities=self.cities,
                initial_temp=initial_temp,
                cooling_rate=cooling_rate,
                max_iterations=50000,
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
        self.solver = None
        if self.animation_id:
            self.root.after_cancel(self.animation_id)

        self.start_button.config(state=tk.NORMAL, text="Start")
        self.pause_button.config(state=tk.DISABLED)

        self._plot_initial_cities()
        self.ax_metrics.clear()
        self.ax_metrics.set_title("Distance Over Time")
        self.ax_metrics.set_xlabel("Iteration")
        self.ax_metrics.set_ylabel("Distance")
        self.ax_metrics.grid(True, alpha=0.3)
        self.canvas.draw()

        self.status_var.set("Ready")

    def _animate(self):
        """Animation loop."""
        if not self.is_running or self.solver is None:
            return

        # Multiple steps per frame
        for _ in range(20):
            if not self.solver.step():
                self._optimization_complete()
                return

        self._update_plots()

        # Update status
        self.status_var.set(
            f"Iteration: {self.solver.iteration} | "
            f"Best Distance: {self.solver.best_route.total_distance():.2f} | "
            f"Temp: {self.solver.temperature:.3f}"
        )

        self.animation_id = self.root.after(50, self._animate)

    def _update_plots(self):
        """Update visualization."""
        if self.solver is None:
            return

        # Plot best route
        self.ax_route.clear()
        route = self.solver.best_route
        x_coords = [self.cities[i].x for i in route.order]
        y_coords = [self.cities[i].y for i in route.order]

        # Close the loop
        x_coords.append(x_coords[0])
        y_coords.append(y_coords[0])

        # Plot route
        self.ax_route.plot(x_coords, y_coords, "b-", alpha=0.6, linewidth=2)
        self.ax_route.scatter(
            [city.x for city in self.cities], [city.y for city in self.cities],
            c="red", s=100, zorder=2
        )

        self.ax_route.set_title(
            f"Best Route (Distance: {route.total_distance():.2f})"
        )
        self.ax_route.set_xlabel("X")
        self.ax_route.set_ylabel("Y")
        self.ax_route.set_aspect("equal")
        self.ax_route.grid(True, alpha=0.3)

        # Plot distance history
        self.ax_metrics.clear()
        self.ax_metrics.plot(
            self.solver.distance_history, label="Current", alpha=0.5, linewidth=1
        )
        self.ax_metrics.plot(
            self.solver.best_distance_history, label="Best", color="red", linewidth=2
        )
        self.ax_metrics.set_title("Distance Over Time")
        self.ax_metrics.set_xlabel("Iteration")
        self.ax_metrics.set_ylabel("Distance")
        self.ax_metrics.legend()
        self.ax_metrics.grid(True, alpha=0.3)

        self.fig.tight_layout()
        self.canvas.draw()

    def _optimization_complete(self):
        """Handle completion."""
        self.is_running = False
        self.start_button.config(state=tk.NORMAL, text="Start")
        self.pause_button.config(state=tk.DISABLED)

        if self.solver:
            self.status_var.set(
                f"Complete! Best Distance: {self.solver.best_route.total_distance():.2f} "
                f"(Iterations: {self.solver.iteration})"
            )


def main():
    """Main entry point."""
    root = tk.Tk()
    app = TSPGUI(root)
    root.mainloop()


if __name__ == "__main__":
    # Example: Solve TSP without GUI
    print("Traveling Salesman Problem - Simulated Annealing")
    print("=" * 60)

    # Create 10 random cities
    cities = [City(random.uniform(0, 100), random.uniform(0, 100), f"City{i}") for i in range(10)]

    print(f"\nSolving TSP for {len(cities)} cities...")

    # Solve
    solver = TSPSimulatedAnnealing(cities, initial_temp=1000, cooling_rate=0.995)
    best_route = solver.solve()

    print(f"\nBest route found:")
    print(f"Distance: {best_route.total_distance():.2f}")
    print(f"Order: {best_route.order}")
    print(f"Iterations: {solver.iteration}")

    # Launch GUI
    print("\nLaunching GUI...")
    main()
