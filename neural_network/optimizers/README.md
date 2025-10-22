# Neural Network Optimizers

This module provides implementations of various optimization algorithms commonly used for training neural networks. Each optimizer is designed to be educational, well-documented, and follows standard mathematical definitions.

## Available Optimizers

### 1. SGD (Stochastic Gradient Descent)
The most basic optimizer that updates parameters in the direction opposite to the gradient.

**Update Rule:** `θ = θ - α * g`

**Use Case:** Simple problems, baseline comparisons, when you want to understand gradient descent fundamentals.

### 2. MomentumSGD (SGD with Momentum)
Adds a momentum term that accumulates past gradients to accelerate convergence and reduce oscillations.

**Update Rule:**
```
v = β * v + (1-β) * g
θ = θ - α * v
```

**Use Case:** When dealing with noisy gradients or ill-conditioned optimization landscapes.

### 3. NAG (Nesterov Accelerated Gradient)
An improved version of momentum that evaluates gradients at a "lookahead" position.

**Update Rule:**
```
v = β * v + (1-β) * g
θ = θ - α * (β * v + (1-β) * g)
```

**Use Case:** When you need better convergence properties than standard momentum, especially for convex problems.

### 4. Adagrad (Adaptive Gradient Algorithm)
Adapts learning rates for each parameter based on historical gradient magnitudes.

**Update Rule:**
```
G = G + g²
θ = θ - (α / √(G + ε)) * g
```

**Use Case:** Sparse data, different parameter scales, when you want automatic learning rate adaptation.

### 5. Adam (Adaptive Moment Estimation)
Combines momentum and adaptive learning rates with bias correction.

**Update Rule:**
```
m = β₁ * m + (1-β₁) * g
v = β₂ * v + (1-β₂) * g²
m̂ = m / (1 - β₁^t)
v̂ = v / (1 - β₂^t)
θ = θ - α * m̂ / (√v̂ + ε)
```

**Use Case:** Most general-purpose optimizer, good default choice for many deep learning problems.

## Quick Start

```python
from neural_network.optimizers import SGD, Adam

# Initialize optimizer
optimizer = Adam(learning_rate=0.001)

# In your training loop:
parameters = [1.0, 2.0, 3.0]  # Your model parameters
gradients = [0.1, 0.2, 0.3]   # Computed gradients

# Update parameters
updated_parameters = optimizer.update(parameters, gradients)
```

## Detailed Usage Examples

### Basic Optimization Example

```python
from neural_network.optimizers import SGD, Adam, Adagrad

# Define a simple quadratic function: f(x) = x²
def gradient_quadratic(x):
    return 2 * x  # f'(x) = 2x

# Initialize optimizers
sgd = SGD(learning_rate=0.1)
adam = Adam(learning_rate=0.1)

# Starting point
x_sgd = [5.0]
x_adam = [5.0]

# Optimization steps
for i in range(20):
    grad_sgd = [gradient_quadratic(x_sgd[0])]
    grad_adam = [gradient_quadratic(x_adam[0])]

    x_sgd = sgd.update(x_sgd, grad_sgd)
    x_adam = adam.update(x_adam, grad_adam)

    print(f"Step {i+1}: SGD={x_sgd[0]:.4f}, Adam={x_adam[0]:.4f}")
```

### Multi-dimensional Parameter Example

```python
from neural_network.optimizers import MomentumSGD

# 2D parameter optimization
optimizer = MomentumSGD(learning_rate=0.01, momentum=0.9)

# Parameters can be nested lists for multi-dimensional cases
parameters = [[1.0, 2.0], [3.0, 4.0]]  # 2x2 parameter matrix
gradients = [[0.1, 0.2], [0.3, 0.4]]   # Corresponding gradients

updated_params = optimizer.update(parameters, gradients)
print("Updated parameters:", updated_params)
```

### Comparative Performance

```python
from neural_network.optimizers import SGD, MomentumSGD, NAG, Adagrad, Adam

# Function with challenging optimization landscape
def rosenbrock(x, y):
    return 100 * (y - x**2)**2 + (1 - x)**2

def rosenbrock_grad(x, y):
    df_dx = -400 * x * (y - x**2) - 2 * (1 - x)
    df_dy = 200 * (y - x**2)
    return [df_dx, df_dy]

# Initialize all optimizers
optimizers = {
    "SGD": SGD(0.001),
    "Momentum": MomentumSGD(0.001, 0.9),
    "NAG": NAG(0.001, 0.9),
    "Adagrad": Adagrad(0.01),
    "Adam": Adam(0.01)
}

# Starting point
start = [-1.0, 1.0]
positions = {name: start.copy() for name in optimizers}

# Run optimization
for step in range(100):
    for name, optimizer in optimizers.items():
        x, y = positions[name]
        grad = rosenbrock_grad(x, y)
        positions[name] = optimizer.update(positions[name], grad)

    if step % 20 == 19:
        print(f"\\nStep {step + 1}:")
        for name, pos in positions.items():
            loss = rosenbrock(pos[0], pos[1])
            print(f"  {name:8s}: loss = {loss:8.3f}, pos = ({pos[0]:6.3f}, {pos[1]:6.3f})")
```

## Design Principles

1. **Educational Focus**: Each optimizer is implemented from scratch with clear mathematical formulations and extensive documentation.

2. **Consistent Interface**: All optimizers inherit from `BaseOptimizer` and implement the same `update()` method signature.

3. **Type Safety**: Full type hints for all methods and parameters.

4. **Comprehensive Testing**: Each optimizer includes doctests and example usage.

5. **Pure Python**: No external dependencies except built-in modules for maximum compatibility.

6. **Flexible Data Structures**: Support for both 1D parameter lists and nested lists for multi-dimensional parameters.

## Parameter Guidelines

### Learning Rates
- **SGD**: 0.01 - 0.1 (higher values often work)
- **Momentum/NAG**: 0.001 - 0.01 (momentum helps with larger steps)
- **Adagrad**: 0.01 - 0.1 (adaptive nature handles larger initial rates)
- **Adam**: 0.001 - 0.01 (most robust to learning rate choice)

### Momentum Values
- **MomentumSGD/NAG**: 0.9 - 0.99 (0.9 is most common)
- **Adam β₁**: 0.9 (standard value, rarely changed)
- **Adam β₂**: 0.999 (controls second moment, occasionally tuned to 0.99)

### When to Use Each Optimizer

| Optimizer | Best For | Avoid When |
|-----------|----------|------------|
| SGD | Understanding basics, simple problems, fine-tuning | Complex landscapes, limited time |
| Momentum | Noisy gradients, oscillatory behavior | Memory constraints |
| NAG | Convex problems, when momentum overshoots | Non-convex with many local minima |
| Adagrad | Sparse features, automatic LR adaptation | Long training (LR decay too aggressive) |
| Adam | General purpose, unknown problem characteristics | When you need theoretical guarantees |

## Mathematical Background

Each optimizer represents a different approach to the fundamental optimization problem:

**minimize f(θ) over θ**

where `f(θ)` is typically a loss function and `θ` represents the parameters of a neural network.

The optimizers differ in how they use gradient information `g = ∇f(θ)` to update parameters:

1. **SGD** uses gradients directly
2. **Momentum** accumulates gradients over time
3. **NAG** uses lookahead to reduce overshooting
4. **Adagrad** adapts learning rates based on gradient history
5. **Adam** combines momentum with adaptive learning rates

## References

- Ruder, S. (2016). "An overview of gradient descent optimization algorithms"
- Kingma, D.P. & Ba, J. (2014). "Adam: A Method for Stochastic Optimization"
- Nesterov, Y. (1983). "A method for unconstrained convex minimization problem"
- Duchi, J., Hazan, E., & Singer, Y. (2011). "Adaptive Subgradient Methods"