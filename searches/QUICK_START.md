# 🔥 Simulated Annealing - Quick Start Guide

## 🎯 What is it?
Simulated Annealing is an optimization algorithm inspired by metallurgical annealing. It finds approximate solutions to complex optimization problems by probabilistically exploring the solution space.

## 🚀 Quick Start

### Option 1: Interactive GUI (Recommended for Beginners)

#### General Optimization
```bash
python searches/simulated_annealing_with_gui.py
```
- Select a test function
- Click "Start" and watch it optimize!
- Try different parameters to see effects

#### Traveling Salesman Problem
```bash
python searches/simulated_annealing_tsp.py
```
- Adjust number of cities
- Click "Generate Cities"
- Click "Start" to find the shortest route

### Option 2: Python Code

```python
from searches.simulated_annealing_with_gui import SimulatedAnnealingOptimizer

# Define what to optimize
def my_function(x):
    return x[0]**2 + x[1]**2  # Minimize this

# Create and run optimizer
optimizer = SimulatedAnnealingOptimizer(
    cost_function=my_function,
    initial_state=[5.0, 5.0],      # Starting point
    bounds=[(-10, 10), (-10, 10)], # Search space
    initial_temp=1000,              # How much to explore
    cooling_rate=0.95,              # How fast to focus
    max_iterations=1000             # How long to search
)

best_solution, best_cost = optimizer.optimize()
print(f"Best: {best_solution} with cost {best_cost}")
```

## 📊 Available Test Functions

| Function | Difficulty | Minimum | Good for... |
|----------|------------|---------|-------------|
| **Sphere** | Easy | (0,0,0) = 0 | Learning basics |
| **Rosenbrock** | Medium | (1,1,1) = 0 | Testing convergence |
| **Rastrigin** | Hard | (0,0,0) = 0 | Many local minima |
| **Ackley** | Hard | (0,0,0) = 0 | Nearly flat regions |

## ⚙️ Key Parameters

### Initial Temperature
- **What**: Starting "randomness" level
- **Higher** → More exploration, slower
- **Lower** → Less exploration, faster
- **Try**: 100-1000 for most problems

### Cooling Rate
- **What**: How quickly to reduce randomness
- **Higher (0.99)** → Slower, more thorough
- **Lower (0.90)** → Faster, less thorough
- **Try**: 0.95 for most problems

### Max Iterations
- **What**: When to give up
- **More** → Better solutions, slower
- **Less** → Faster, maybe worse
- **Try**: 1000-5000 for most problems

## 🎨 GUI Controls

### General Optimizer
1. **Problem**: Select test function
2. **Initial Temp**: Starting temperature
3. **Cooling Rate**: Speed of cooling
4. **Max Iterations**: Maximum steps
5. **Start**: Begin optimization
6. **Pause**: Temporarily stop
7. **Reset**: Clear and start over

### TSP Solver
1. **Number of Cities**: How many cities to visit
2. **Generate Cities**: Create random cities
3. **Initial Temp**: Starting temperature
4. **Cooling Rate**: Speed of cooling
5. **Start**: Find best route
6. **Pause**: Temporarily stop
7. **Reset**: New problem

## 📈 Understanding the Plots

### Cost History
- **Blue line**: Current solution cost
- **Red line**: Best solution found so far
- **Goal**: Red line should decrease

### Temperature
- **Orange line**: Current temperature
- **Pattern**: Should decrease smoothly
- **End**: Approaches zero

### Acceptance Rate
- **Green line**: % of accepted moves
- **High early**: Lots of exploration
- **Low late**: Focused refinement

## 💡 Tips for Best Results

### ✅ Do This
- Start with **high temperature** (1000+)
- Use **slow cooling** (0.95-0.99)
- Run **multiple times** (it's random!)
- Watch the **plots** to understand behavior

### ❌ Avoid This
- Temperature too low → Stuck in local minimum
- Cooling too fast → Poor solutions
- Too few iterations → Didn't finish
- Ignoring the visualization

## 🔧 Troubleshooting

### "Not finding good solutions"
→ Increase temperature or cooling rate or iterations

### "Taking too long"
→ Decrease cooling rate or max iterations

### "Same solution every time"
→ Good! But try harder problems

### "Different solutions each run"
→ Normal! It's probabilistic

## 📚 Learn More

- **README**: `searches/README.md`
- **Full Guide**: `searches/SIMULATED_ANNEALING_GUIDE.md`
- **Implementation**: `SIMULATED_ANNEALING_IMPLEMENTATION.md`

## 🎓 Educational Examples

### Example 1: Find Minimum of x² + y²
```python
from searches.simulated_annealing_with_gui import SimulatedAnnealingOptimizer

optimizer = SimulatedAnnealingOptimizer(
    cost_function=lambda x: x[0]**2 + x[1]**2,
    initial_state=[8.0, -6.0],
    bounds=[(-10, 10), (-10, 10)],
    initial_temp=500,
    cooling_rate=0.95,
    max_iterations=1000
)

best, cost = optimizer.optimize()
print(f"Found minimum at {best} = {cost}")
# Should find near [0, 0] = 0
```

### Example 2: Solve 5-City TSP
```python
from searches.simulated_annealing_tsp import City, TSPSimulatedAnnealing

cities = [
    City(0, 0, "A"),
    City(1, 3, "B"),
    City(4, 1, "C"),
    City(3, 4, "D"),
    City(5, 2, "E"),
]

solver = TSPSimulatedAnnealing(cities, initial_temp=100, cooling_rate=0.99)
best_route = solver.solve()

print(f"Best distance: {best_route.total_distance():.2f}")
print(f"Order: {best_route.order}")
```

## 🎯 When to Use

### ✅ Good For
- Complex optimization problems
- Many local minima
- Combinatorial problems (TSP, scheduling)
- When exact solution not needed
- When gradient not available

### ❌ Not Good For
- Simple convex problems (use gradient descent)
- When you need guarantees
- Real-time applications
- Very high-dimensional problems

## 🌟 Quick Comparison

| Algorithm | Speed | Accuracy | Use Case |
|-----------|-------|----------|----------|
| **Hill Climbing** | Fast | Poor | Simple problems |
| **Simulated Annealing** | Medium | Good | Complex problems |
| **Genetic Algorithm** | Slow | Good | Very complex |
| **Gradient Descent** | Fast | Excellent | Smooth functions |

## 📞 Getting Help

1. Read the error message
2. Check parameter values
3. Try the GUI first
4. Look at example code
5. Read full documentation

---

**Ready to optimize?** Just run:
```bash
python searches/simulated_annealing_with_gui.py
```

**Happy Optimizing! 🚀**
