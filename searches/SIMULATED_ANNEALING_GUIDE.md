# Simulated Annealing - Examples and Usage Guide

This guide demonstrates how to use the Simulated Annealing implementations in this repository.

## Table of Contents
1. [Installation](#installation)
2. [Basic Optimization](#basic-optimization)
3. [GUI Applications](#gui-applications)
4. [Advanced Examples](#advanced-examples)

## Installation

Ensure you have the required dependencies:

```bash
pip install matplotlib
```

For GUI features, tkinter should be included with Python. If not:

```bash
# On Ubuntu/Debian
sudo apt-get install python3-tk

# On macOS (with Homebrew)
brew install python-tk

# On Windows
# Tkinter is usually included with Python installation
```

## Basic Optimization

### Example 1: Using the Original Implementation

```python
from searches.simulated_annealing import SearchProblem, simulated_annealing

# Define a function to optimize
def my_function(x, y):
    return (x - 3)**2 + (y + 2)**2

# Create a search problem
problem = SearchProblem(
    x=10,  # Starting x coordinate
    y=10,  # Starting y coordinate
    step_size=1,  # Step size for neighbors
    function_to_optimize=my_function
)

# Run optimization to find minimum
result = simulated_annealing(
    search_prob=problem,
    find_max=False,  # False for minimization
    max_x=20,
    min_x=-20,
    max_y=20,
    min_y=-20,
    visualization=True,  # Show matplotlib plot
    start_temperate=100,
    rate_of_decrease=0.01,
    threshold_temp=1
)

print(f"Optimal point: {result}")
print(f"Optimal value: {result.score()}")
```

### Example 2: Using the Enhanced Optimizer

```python
from searches.simulated_annealing_with_gui import SimulatedAnnealingOptimizer
import math

# Define a multimodal function (Rastrigin)
def rastrigin(x):
    n = len(x)
    return 10*n + sum(xi**2 - 10*math.cos(2*math.pi*xi) for xi in x)

# Create optimizer
optimizer = SimulatedAnnealingOptimizer(
    cost_function=rastrigin,
    initial_state=[4.0, -3.5, 2.0],
    bounds=[(-5.12, 5.12)] * 3,
    initial_temp=1000.0,
    cooling_rate=0.95,
    min_temp=1e-3,
    max_iterations=2000
)

# Run optimization
best_state, best_cost = optimizer.optimize()

print(f"Best solution found: {best_state}")
print(f"Best cost: {best_cost}")
print(f"Total iterations: {optimizer.iteration}")
```

## GUI Applications

### Interactive General Optimizer

Launch the GUI for general optimization problems:

```bash
python searches/simulated_annealing_with_gui.py
```

**Features:**
- Select from predefined benchmark functions
- Adjust parameters in real-time
- Visualize convergence
- See temperature decay
- Monitor acceptance rates

**Available Test Functions:**
1. **Sphere Function**: Simple convex function
   - Minimum at (0, 0, 0) = 0

2. **Rastrigin Function**: Highly multimodal
   - Minimum at (0, 0, 0) = 0
   - Many local minima

3. **Rosenbrock Function**: Narrow valley to global minimum
   - Minimum at (1, 1, 1) = 0

4. **Ackley Function**: Nearly flat outer region, central peak
   - Minimum at (0, 0, 0) = 0

### TSP Solver GUI

Launch the Traveling Salesman Problem solver:

```bash
python searches/simulated_annealing_tsp.py
```

**Features:**
- Generate random cities
- Visualize route optimization in real-time
- Adjust number of cities
- Configure temperature parameters
- Watch distance decrease over iterations

## Advanced Examples

### Example 3: Solving TSP Programmatically

```python
from searches.simulated_annealing_tsp import City, TSPSimulatedAnnealing

# Define cities
cities = [
    City(0, 0, "Warehouse"),
    City(2, 5, "Store A"),
    City(8, 3, "Store B"),
    City(5, 8, "Store C"),
    City(9, 9, "Store D"),
]

# Create solver
solver = TSPSimulatedAnnealing(
    cities=cities,
    initial_temp=1000.0,
    cooling_rate=0.995,
    min_temp=1e-3,
    max_iterations=10000
)

# Solve
best_route = solver.solve()

print(f"Best route distance: {best_route.total_distance():.2f}")
print(f"Visit order: {best_route.order}")
print(f"Iterations used: {solver.iteration}")

# Print the route
print("\nRoute:")
for i in best_route.order:
    city = cities[i]
    print(f"  → {city.name} at ({city.x}, {city.y})")
```

### Example 4: Custom Cooling Schedule

```python
from searches.simulated_annealing_with_gui import SimulatedAnnealingOptimizer

# Sphere function
sphere = lambda x: sum(xi**2 for xi in x)

# Different cooling rates for comparison
cooling_rates = [0.90, 0.95, 0.99]

for rate in cooling_rates:
    optimizer = SimulatedAnnealingOptimizer(
        cost_function=sphere,
        initial_state=[5.0, 5.0],
        bounds=[(-10, 10)] * 2,
        initial_temp=1000,
        cooling_rate=rate,
        max_iterations=1000
    )
    
    best_state, best_cost = optimizer.optimize()
    
    print(f"\nCooling rate: {rate}")
    print(f"  Final cost: {best_cost:.6f}")
    print(f"  Iterations: {optimizer.iteration}")
```

### Example 5: Portfolio Optimization

```python
import random
from searches.simulated_annealing_with_gui import SimulatedAnnealingOptimizer

# Simulated stock returns (mean, std dev)
stocks = [
    (0.12, 0.20),  # Stock 1: 12% return, 20% volatility
    (0.08, 0.10),  # Stock 2: 8% return, 10% volatility
    (0.15, 0.25),  # Stock 3: 15% return, 25% volatility
    (0.06, 0.05),  # Stock 4: 6% return, 5% volatility
]

def portfolio_risk(weights):
    """Minimize risk for given expected return."""
    # Weights must sum to 1
    total = sum(weights)
    if abs(total - 1.0) > 0.01:
        return 1e6  # Penalty for invalid weights
    
    # Simple risk calculation (in reality, use covariance matrix)
    risk = sum(w**2 * std**2 for w, (_, std) in zip(weights, stocks))
    return risk

# Optimize for minimum risk
optimizer = SimulatedAnnealingOptimizer(
    cost_function=portfolio_risk,
    initial_state=[0.25, 0.25, 0.25, 0.25],  # Equal weights
    bounds=[(0, 1)] * 4,  # Each weight between 0 and 1
    initial_temp=10,
    cooling_rate=0.99,
    max_iterations=5000
)

best_weights, best_risk = optimizer.optimize()

# Normalize to ensure sum = 1
best_weights = [w / sum(best_weights) for w in best_weights]

print("\nOptimal Portfolio Allocation:")
for i, (weight, (ret, std)) in enumerate(zip(best_weights, stocks)):
    print(f"  Stock {i+1}: {weight*100:.1f}% (Return: {ret*100:.0f}%, Risk: {std*100:.0f}%)")
print(f"\nPortfolio Risk: {best_risk:.6f}")
```

### Example 6: Function Maximization

```python
from searches.simulated_annealing_with_gui import SimulatedAnnealingOptimizer
import math

# We want to MAXIMIZE this function
def profit_function(x):
    """Simulate a profit function with peak around (5, 5)."""
    return -(x[0] - 5)**2 - (x[1] - 5)**2 + 50

# To maximize, minimize the negative
def cost_to_minimize(x):
    return -profit_function(x)

optimizer = SimulatedAnnealingOptimizer(
    cost_function=cost_to_minimize,
    initial_state=[0.0, 0.0],
    bounds=[(0, 10), (0, 10)],
    initial_temp=100,
    cooling_rate=0.95,
    max_iterations=1000
)

best_state, best_cost = optimizer.optimize()
max_profit = -best_cost  # Convert back

print(f"Optimal parameters: {best_state}")
print(f"Maximum profit: {max_profit:.2f}")
```

## Parameter Tuning Guide

### Temperature Parameters

- **Initial Temperature**: 
  - Higher = more exploration, slower convergence
  - Typical range: 100 - 10000
  - Start high for complex problems

- **Cooling Rate**:
  - Closer to 1.0 = slower cooling, more thorough search
  - Typical range: 0.90 - 0.999
  - Use 0.95-0.99 for most problems

- **Minimum Temperature**:
  - Stopping criterion
  - Typical: 1e-3 to 1e-6
  - Lower = longer run time

### General Tips

1. **Start with high temperature** to explore the solution space
2. **Use slower cooling** (higher rate) for complex landscapes
3. **Increase iterations** if not converging
4. **Multiple runs** can help due to randomness
5. **Monitor acceptance rate**: 
   - Too high? Increase cooling rate
   - Too low? Increase initial temperature

## Troubleshooting

### Problem: Not finding good solutions
- Increase initial temperature
- Increase cooling rate (slower cooling)
- Increase max iterations
- Try multiple runs with different random seeds

### Problem: Too slow
- Decrease cooling rate (faster cooling)
- Reduce max iterations
- Reduce steps per frame in GUI

### Problem: Gets stuck in local minimum
- Increase initial temperature
- Use slower cooling rate
- Consider restart strategy with best solution

## References

- [Wikipedia: Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Wikipedia: Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
- Kirkpatrick, S.; Gelatt, C. D.; Vecchi, M. P. (1983). "Optimization by Simulated Annealing"
