# Fuzzy Logic

**Fuzzy logic** generalizes classical (crisp) set theory: instead of an element
either belonging to a set or not, it belongs to a degree between `0` and `1`.
That degree is given by a *membership function* `mu: X -> [0, 1]` over a universe
of discourse `X`. Fuzzy logic is widely used in control systems, decision making,
and pattern recognition where boundaries are naturally vague ("young", "warm",
"fast").

Learn more:

- [Fuzzy logic](https://en.wikipedia.org/wiki/Fuzzy_logic)
- [Fuzzy set](https://en.wikipedia.org/wiki/Fuzzy_set)
- [Membership function](https://en.wikipedia.org/wiki/Membership_function_(mathematics))
- [T-norm](https://en.wikipedia.org/wiki/T-norm) (the family of fuzzy AND/OR operators)

## Contents

| File | What it does |
| --- | --- |
| [`fuzzy_operations.py`](fuzzy_operations.py) | A `FuzzySet` class modelling a **triangular fuzzy number** by its `(left, peak, right)` points, with `membership`, `union`, `intersection`, `complement`, and plotting. Best when your fuzzy sets are triangular and you want to keep working with the parameters. |
| [`fuzzy_set_operations.py`](fuzzy_set_operations.py) | The classic **Zadeh operators on sampled membership vectors**: `union`, `intersection`, `complement`, `difference`, `algebraic_sum`/`product`, and `bounded_sum`/`difference`. Works on *any* membership shape (triangular, trapezoidal, Gaussian, ...) because it operates on the sampled values directly. Dependency-free (NumPy only). |

The two files are complementary: `fuzzy_operations.py` stays in the parametric
`(left, peak, right)` representation, while `fuzzy_set_operations.py` works on the
discretized membership arrays and therefore supports the full set of Zadeh
operators for arbitrary shapes.

## Quick example

```python
import numpy as np
from fuzzy_logic.fuzzy_set_operations import (
    triangular_membership,
    fuzzy_union,
    fuzzy_intersection,
)

universe = np.linspace(0, 75, 75)
young = triangular_membership(universe, 0, 25, 50)
middle_aged = triangular_membership(universe, 25, 50, 75)

young_or_middle_aged = fuzzy_union(young, middle_aged)
young_and_middle_aged = fuzzy_intersection(young, middle_aged)
```

Run the doctests for either module with:

```bash
python -m doctest -v fuzzy_logic/fuzzy_set_operations.py
```
