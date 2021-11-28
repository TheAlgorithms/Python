"""Convenient parallelization of higher order functions.

This module provides two helper functions, with appropriate fallbacks on
Python 2 and on systems lacking support for synchronization mechanisms:

- map_multiprocess
- map_multithread

These helpers work like Python 3's map, with two differences:

- They don't guarantee the order of processing of
  the elements of the iterable.
- The underlying process/thread pools chop the iterable into
  a number of chunks, so that for very long iterables using
  a large value for chunksize can make the job complete much faster
  than using the default value of 1.
"""

__all__ = ["map_multiprocess", "map_multithread"]

from contextlib import contextmanager
from multiprocessing import Pool as ProcessPool
from multiprocessing import pool
from multiprocessing.dummy import Pool as ThreadPool
from typing import Callable, Iterable, Iterator, TypeVar, Union

from pip._vendor.requests.adapters import DEFAULT_POOLSIZE

Pool = Union[pool.Pool, pool.ThreadPool]
S = TypeVar("S")
T = TypeVar("T")

# On platforms without sem_open, multiprocessing[.dummy] Pool
# cannot be created.
try:
    import multiprocessing.synchronize  # noqa
except ImportError:
    LACK_SEM_OPEN = True
else:
    LACK_SEM_OPEN = False

# Incredibly large timeout to work around bpo-8296 on Python 2.
TIMEOUT = 2000000


@contextmanager
def closing(pool):
    # type: (Pool) -> Iterator[Pool]
    """Return a context manager making sure the pool closes properly."""
    try:
        yield pool
    finally:
        # For Pool.imap*, close and join are needed
        # for the returned iterator to begin yielding.
        pool.close()
        pool.join()
        pool.terminate()


def _map_fallback(func, iterable, chunksize=1):
    # type: (Callable[[S], T], Iterable[S], int) -> Iterator[T]
    """Make an iterator applying func to each element in iterable.

    This function is the sequential fallback either on Python 2
    where Pool.imap* doesn't react to KeyboardInterrupt
    or when sem_open is unavailable.
    """
    return map(func, iterable)


def _map_multiprocess(func, iterable, chunksize=1):
    # type: (Callable[[S], T], Iterable[S], int) -> Iterator[T]
    """Chop iterable into chunks and submit them to a process pool.

    For very long iterables using a large value for chunksize can make
    the job complete much faster than using the default value of 1.

    Return an unordered iterator of the results.
    """
    with closing(ProcessPool()) as pool:
        return pool.imap_unordered(func, iterable, chunksize)


def _map_multithread(func, iterable, chunksize=1):
    # type: (Callable[[S], T], Iterable[S], int) -> Iterator[T]
    """Chop iterable into chunks and submit them to a thread pool.

    For very long iterables using a large value for chunksize can make
    the job complete much faster than using the default value of 1.

    Return an unordered iterator of the results.
    """
    with closing(ThreadPool(DEFAULT_POOLSIZE)) as pool:
        return pool.imap_unordered(func, iterable, chunksize)


if LACK_SEM_OPEN:
    map_multiprocess = map_multithread = _map_fallback
else:
    map_multiprocess = _map_multiprocess
    map_multithread = _map_multithread
