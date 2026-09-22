from collections.abc import Iterable, Iterator
from sys import stderr


def progress[T](items: Iterable[T], desc: str = "", total: int = 0) -> Iterator[T]:
    """
    A simple progress iterator that yields items from the given iterable while
    displaying a progress indicator in place on a single line of stderr.  The output is
    not written to stdout, so the output of the program remains clean (see doctests).

    for item in progress(range(1_000), desc="Processing"):
        process(item)

    Args:
        items: The iterable of items to process.
        desc: A description to display alongside the progress. Defaults to "".
        total: The total number of items, defaults to 0. If 0, it will be inferred from
            the iterable if possible.

    Yields:
        Iterator[T]: The items from the iterable, one by one.

    >>> tuple(progress(range(5)))
    (0, 1, 2, 3, 4)
    >>> tuple(progress(range(5), desc="Processing", total=3))
    (0, 1, 2, 3, 4)
    >>> tuple(progress(range(5), desc="Processing", total=10))
    (0, 1, 2, 3, 4)
    >>> tuple(progress(range(5), desc="Processing", total=-5))
    (0, 1, 2, 3, 4)
    >>> from string import printable
    >>> tuple(progress(printable, desc="Printable"))  # doctest: +ELLIPSIS
    ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',...
    """
    total = max(total, 0)
    if not total and hasattr(items, "__len__"):
        total = len(items)  # type: ignore[invalid-argument-type]

    for i, item in enumerate(items, 1):
        suffix = f"{i:,}/{total:,}" if total else f"{i:,}"
        print(f"\r\033[K{desc}: {suffix}", end="", file=stderr, flush=True)
        yield item

    print("\r\033[K", end="", file=stderr, flush=True)


if __name__ == "__main__":
    import time

    print("start")
    for _item in progress(range(1_000), desc="Processing"):
        time.sleep(0.02)

    print("stop")
