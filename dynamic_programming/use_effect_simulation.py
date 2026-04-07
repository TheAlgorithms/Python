"""
Simulation of a simple useEffect-like behavior in Python.

This demonstrates executing a function when a dependency changes.
Reference:
https://en.wikipedia.org/wiki/Reactive_programming
"""

from typing import Callable, Any


def use_effect_simulation(callback: Callable[[], None], dependency: Any) -> None:
    """
    Executes the callback when the dependency changes.

    >>> calls = []
    >>> def cb():
    ...     calls.append("called")
    >>> use_effect_simulation(cb, 1)
    >>> use_effect_simulation(cb, 1)
    >>> use_effect_simulation(cb, 2)
    >>> calls
    ['called', 'called']
    """
    if not hasattr(use_effect_simulation, "_prev"):
        use_effect_simulation._prev = None  # type: ignore

    if use_effect_simulation._prev != dependency:
        callback()
        use_effect_simulation._prev = dependency


if __name__ == "__main__":
    def example():
        print("Effect triggered!")

    use_effect_simulation(example, 1)
    use_effect_simulation(example, 1)
    use_effect_simulation(example, 2)