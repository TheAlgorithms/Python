# Search Algorithms

This directory contains implementations of various search algorithms, including optimization algorithms like Simulated Annealing.

## Simulated Annealing

Simulated Annealing is a probabilistic optimization technique inspired by the annealing process in metallurgy. It's particularly effective for finding approximate solutions to complex optimization problems.

### Implementations

1. **simulated_annealing.py** - Basic implementation for 2D function optimization
2. **simulated_annealing_with_gui.py** - Enhanced implementation with interactive GUI
3. **simulated_annealing_tsp.py** - Specialized implementation for the Traveling Salesman Problem

### Features

#### simulated_annealing_with_gui.py
- Interactive Tkinter-based GUI
- Real-time visualization of optimization progress
- Multiple test functions:
  - Sphere Function
  - Rastrigin Function (multimodal)
  - Rosenbrock Function
  - Ackley Function
- Live plots showing:
  - Cost history (current and best)
  - Temperature decay
  - Acceptance rate
- Configurable parameters (temperature, cooling rate, iterations)
- Pause/resume functionality

#### simulated_annealing_tsp.py
- Specialized for Traveling Salesman Problem
- Interactive GUI with city visualization
- Real-time route optimization display
- Random city generation
- 2-opt neighborhood search
- Distance plot over iterations

### Usage

#### Basic Usage (Command Line)

```python
from searches.simulated_annealing_with_gui import SimulatedAnnealingOptimizer

# Define a cost function to minimize
def sphere(x):
    return sum(xi**2 for xi in x)

# Create optimizer
optimizer = SimulatedAnnealingOptimizer(
    cost_function=sphere,
    initial_state=[5.0, -5.0, 3.0],
    bounds=[(-10, 10)] * 3,
    initial_temp=1000,
    cooling_rate=0.95,
    max_iterations=1000,
)

# Run optimization
best_state, best_cost = optimizer.optimize()
print(f"Best solution: {best_state}")
print(f"Best cost: {best_cost}")
```

#### GUI Usage

##### General Optimization Problems
```bash
python searches/simulated_annealing_with_gui.py
```

Features:
- Select from predefined test functions
- Adjust optimization parameters
- Visualize the optimization process in real-time
- See cost reduction, temperature decay, and acceptance rates

##### Traveling Salesman Problem
```bash
python searches/simulated_annealing_tsp.py
```

Features:
- Generate random cities
- Visualize the route as it optimizes
- Watch the total distance decrease
- Adjust number of cities and optimization parameters

### Algorithm Parameters

- **initial_temp**: Starting temperature (higher = more exploration)
- **cooling_rate**: Rate of temperature decrease (typically 0.9-0.99)
- **min_temp**: Minimum temperature before stopping
- **max_iterations**: Maximum number of iterations

### How It Works

1. **Start** with an initial solution and high temperature
2. **Generate** a random neighbor solution
3. **Accept** better solutions always
4. **Accept** worse solutions with probability $e^{-\Delta E / T}$ where:
   - $\Delta E$ is the cost increase
   - $T$ is the current temperature
5. **Cool down** by reducing temperature
6. **Repeat** until temperature is very low or max iterations reached

The acceptance of worse solutions helps escape local minima, and this tendency decreases as temperature drops.

### When to Use Simulated Annealing

- Complex optimization landscapes with many local minima
- Combinatorial optimization (TSP, scheduling, etc.)
- When gradient-based methods aren't applicable
- When a good approximate solution is acceptable
- NP-hard problems

### Advantages

✓ Can escape local minima  
✓ Simple to implement  
✓ Widely applicable  
✓ No gradient required  
✓ Works with discrete and continuous problems  

### Disadvantages

✗ Requires careful parameter tuning  
✗ No guarantee of finding global optimum  
✗ Can be slow for very large problems  
✗ Performance depends on cooling schedule  

## Other Search Algorithms

This directory also contains other search algorithms such as:
- Binary Search
- Jump Search
- Interpolation Search
- Hill Climbing
- Tabu Search
- And more...

## Contributing

When adding new search algorithms, please:
1. Include comprehensive docstrings
2. Add test cases or examples
3. Update this README
4. Update DIRECTORY.md in the root
