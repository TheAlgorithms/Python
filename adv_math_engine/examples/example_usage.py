from __future__ import annotations

import numpy as np

from adv_math_engine.series_expansion import maclaurin_series
from adv_math_engine.vector_algebra import dot_product, gram_schmidt
from adv_math_engine.vector_calculus import gradient


if __name__ == "__main__":
    print("Dot:", dot_product([1, 2, 3], [4, 5, 6]))
    print("Orthonormal basis:\n", gram_schmidt([[1, 1, 0], [1, 0, 1], [0, 1, 1]]))

    f = lambda x, y, z: x**2 + y**2 + z**2
    print("Gradient at (1,2,3):", gradient(f, [1, 2, 3]))

    x = np.array([0.1, 0.2, 0.3])
    print("sin(x) Maclaurin order=7:", maclaurin_series(x, order=7, function_name="sin"))
