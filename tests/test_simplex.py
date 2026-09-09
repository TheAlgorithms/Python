import numpy as np
import pytest

from linear_programming.simplex import Tableau


def test_run_simplex_raises_when_max_iterations_are_exhausted(monkeypatch):
    monkeypatch.setattr(Tableau, "maxiter", 0)
    tableau = Tableau(
        np.array([[-1.0, -1.0, 0.0, 0.0, 1.0], [1.0, 1.0, 1.0, 0.0, 2.0]]),
        2,
        0,
    )

    with pytest.raises(
        ValueError,
        match=r"Simplex did not converge within 0 iterations\. "
        r"The problem may be cycling or unbounded\.",
    ):
        tableau.run_simplex()
