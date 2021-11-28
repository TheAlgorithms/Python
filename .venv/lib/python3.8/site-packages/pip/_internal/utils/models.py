"""Utilities for defining models
"""

import operator
from typing import Any, Callable, Type


class KeyBasedCompareMixin:
    """Provides comparison capabilities that is based on a key"""

    __slots__ = ["_compare_key", "_defining_class"]

    def __init__(self, key, defining_class):
        # type: (Any, Type[KeyBasedCompareMixin]) -> None
        self._compare_key = key
        self._defining_class = defining_class

    def __hash__(self):
        # type: () -> int
        return hash(self._compare_key)

    def __lt__(self, other):
        # type: (Any) -> bool
        return self._compare(other, operator.__lt__)

    def __le__(self, other):
        # type: (Any) -> bool
        return self._compare(other, operator.__le__)

    def __gt__(self, other):
        # type: (Any) -> bool
        return self._compare(other, operator.__gt__)

    def __ge__(self, other):
        # type: (Any) -> bool
        return self._compare(other, operator.__ge__)

    def __eq__(self, other):
        # type: (Any) -> bool
        return self._compare(other, operator.__eq__)

    def _compare(self, other, method):
        # type: (Any, Callable[[Any, Any], bool]) -> bool
        if not isinstance(other, self._defining_class):
            return NotImplemented

        return method(self._compare_key, other._compare_key)
