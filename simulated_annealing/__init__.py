"""Simulated Annealing package

Exports:
- SimulatedAnnealing: core optimizer class
- example_functions: a small collection of test functions
"""

from .simulated_annealing import SimulatedAnnealing
from .example import example_functions

__all__ = ["SimulatedAnnealing", "example_functions"]
