"""
Hash map with open addressing.

https://en.wikipedia.org/wiki/Hash_table

Another hash map implementation, with a good explanation.
Modern Dictionaries by Raymond Hettinger
https://www.youtube.com/watch?v=p33CVV29OG8
"""
from collections.abc import Iterator, MutableMapping
from dataclasses import dataclass
from typing import Generic, TypeVar

KEY = TypeVar("KEY")
VAL = TypeVar("VAL")


@dataclass(frozen=True, slots=True)
class _Item(Generic[KEY, VAL]):
    key: KEY
    val: VAL


class _DeletedItem(_Item):
    def __init__(self) -> None:
        super().__init__(None, None)

    def __bool__(self) -> bool:
        return False


_deleted = _DeletedItem()


class HashMap(MutableMapping[KEY, VAL]):
    """
    Hash map with open addressing.
    """

    def __init__(
        self, initial_block_size: int = 8, capacity_factor: float = 0.75
    ) -> None:
        self._initial_block_size = initial_block_size
        self._buckets: list[_Item | None] = [None] * initial_block_size
        assert 0.0 < capacity_factor < 1.0
        self._capacity_factor = capacity_factor
        self._len = 0

    def _get_bucket_index(self, key: KEY) -> int:
        return hash(key) % len(self._buckets)

    def _get_next_ind(self, ind: int) -> int:
        """
        Get next index.

        Implements linear open addressing.
        """
        return (ind + 1) % len(self._buckets)

    def _try_set(self, ind: int, key: KEY, val: VAL) -> bool:
        """
        Try to add value to the bucket.

        If bucket is empty or key is the same, does insert and return True.

        If bucket has another key or deleted placeholder,
        that means that we need to check next bucket.
        """
        stored = self._buckets[ind]
        if not stored:
            self._buckets[ind] = _Item(key, val)
            self._len += 1
            return True
        elif stored.key == key:
            self._buckets[ind] = _Item(key, val)
            return True
        else:
            return False

    def _is_full(self) -> bool:
        """
        Return true if we have reached safe capacity.

        So we need to increase the number of buckets to avoid collisions.
        """
        limit = len(self._buckets) * self._capacity_factor
        return len(self) >= int(limit)

    def _is_sparse(self) -> bool:
        """Return true if we need twice fewer buckets when we have now."""
        if len(self._buckets) <= self._initial_block_size:
            return False
        limit = len(self._buckets) * self._capacity_factor / 2
        return len(self) < limit

    def _resize(self, new_size: int) -> None:
        old_buckets = self._buckets
        self._buckets = [None] * new_size
        self._len = 0
        for item in old_buckets:
            if item:
                self._add_item(item.key, item.val)

    def _size_up(self) -> None:
        self._resize(len(self._buckets) * 2)

    def _size_down(self) -> None:
        self._resize(len(self._buckets) // 2)

    def _iterate_buckets(self, key: KEY) -> Iterator[int]:
        ind = self._get_bucket_index(key)
        for _ in range(len(self._buckets)):
            yield ind
            ind = self._get_next_ind(ind)

    def _add_item(self, key: KEY, val: VAL) -> None:
        for ind in self._iterate_buckets(key):
            if self._try_set(ind, key, val):
                break

    def __setitem__(self, key: KEY, val: VAL) -> None:
        if self._is_full():
            self._size_up()

        self._add_item(key, val)

    def __delitem__(self, key: KEY) -> None:
        for ind in self._iterate_buckets(key):
            item = self._buckets[ind]
            if item is None:
                raise KeyError(key)
            if item is _deleted:
                continue
            if item.key == key:
                self._buckets[ind] = _deleted
                self._len -= 1
                break
        if self._is_sparse():
            self._size_down()

    def __getitem__(self, key: KEY) -> VAL:
        for ind in self._iterate_buckets(key):
            item = self._buckets[ind]
            if item is None:
                break
            if item is _deleted:
                continue
            if item.key == key:
                return item.val
        raise KeyError(key)

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterator[KEY]:
        yield from (item.key for item in self._buckets if item)

    def __repr__(self) -> str:
        val_string = " ,".join(
            f"{item.key}: {item.val}" for item in self._buckets if item
        )
        return f"HashMap({val_string})"
