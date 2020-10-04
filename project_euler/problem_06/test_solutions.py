from .sol1 import solution as sol1
from .sol2 import solution as sol2
from .sol3 import solution as sol3
from .sol4 import solution as sol4


def test_solutions() -> None:
    """
    >>> test_solutions()
    """
    assert sol1(10) == sol2(10) == sol3(10) == sol4(10) == 2640
    assert sol1(15) == sol2(15) == sol3(15) == sol4(15) == 13160
    assert sol1(20) == sol2(20) == sol3(20) == sol4(20) == 41230
    assert sol1(50) == sol2(50) == sol3(50) == sol4(50) == 1582700


if __name__ == "__main__":
    test_solutions()
