from collections.abc import Callable, Sequence
from typing import Any, TypeVar

T = TypeVar("T")


class Pipeline:
    """
    Functional Programming implementation of a Pipeline with Unix Pipe Syntax.
    Instead of using the "dot" notation for applying a function on a given object,
    it uses `|` inspired from unix pipeline.

    Examples:
        >>> pipeline = Pipeline()
        >>> pipeline = pipeline | (lambda x: x + 1) | (lambda x: x * 2)
        >>> pipeline(1)
        4
        >>> pipeline = Pipeline() | (lambda x: x * x) | (lambda x: x - 3)
        >>> pipeline(3)
        6
        >>> from functools import reduce
        >>> def f1(ls): return map(lambda x: x**2, ls)
        >>> def f2(ls): return filter(lambda x: x % 2 == 0, ls)
        >>> def f3(ls): return reduce(lambda x, y: x + y, ls)
        >>> pipeline = Pipeline() | f1 | f2 | f3
        >>> pipeline([1, 2, 3, 4])
        20
    """

    def __init__(self, f_ls: Sequence[Callable] | None = None) -> None:
        self._f_ls = f_ls or []

    def __or__(self, other: Callable) -> "Pipeline":
        return Pipeline(f_ls=[*self._f_ls, other])

    def __call__(self, input_object: T, f_ls_: Sequence[Callable] | None = None) -> Any:
        f_ls = f_ls_ or self._f_ls
        if len(f_ls) == 1:
            return f_ls[0](input_object)
        return self(f_ls[0](input_object), f_ls_=f_ls[1:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
