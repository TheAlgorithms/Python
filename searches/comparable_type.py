from abc import abstractmethod
from typing import Protocol, TypeVar

ComparableType = TypeVar('ComparableType', bound='Comparable')


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: ComparableType, other: ComparableType) -> bool:
        pass

    @abstractmethod
    def __le__(self: ComparableType, other: ComparableType) -> bool:
        pass

    @abstractmethod
    def __gt__(self: ComparableType, other: ComparableType) -> bool:
        pass

    @abstractmethod
    def __ge__(self: ComparableType, other: ComparableType) -> bool:
        pass

    @abstractmethod
    def __eq__(self: ComparableType, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        raise NotImplemented
