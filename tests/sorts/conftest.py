"""This file contains some pytest fixtures that are usable throughout the tests
in this directory, and any subdirectory.

Read more about fixtures here: https://docs.pytest.org/en/latest/fixture.html
"""
import random

import pytest


@pytest.fixture
def randlist():
    """Return a function that deterministically creates a list of random
    elements.
    """

    def _randlist(num_elems=1000, min_=-500, max_=500):
        """Return a list of random elements.

        Calling this function several times with the same arguments always
        returns the same list (on any given machine). This is important for
        test reproducibility.
        """
        # Sets a seed to ensure the same number sequence
        random.seed(52346)
        return [random.randint(min_, max_) for _ in range(num_elems)]

    return _randlist
