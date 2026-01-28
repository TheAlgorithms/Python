"""
Neural Network Optimizers

This module provides implementations of various optimization algorithms commonly used
for training neural networks. The optimizers are designed to be educational and
follow standard mathematical definitions.

Available optimizers:
    - SGD: Stochastic Gradient Descent
    - MomentumSGD: SGD with momentum
    - NAG: Nesterov Accelerated Gradient
    - Adagrad: Adaptive Gradient Algorithm
    - Adam: Adaptive Moment Estimation

Each optimizer implements a common interface for updating parameters given gradients.
"""

from .adagrad import Adagrad
from .adam import Adam
from .momentum_sgd import MomentumSGD
from .nag import NAG
from .sgd import SGD

__all__ = ["NAG", "SGD", "Adagrad", "Adam", "MomentumSGD"]
