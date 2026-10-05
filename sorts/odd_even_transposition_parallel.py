"""
This is an implementation of odd-even transposition sort.

It works by performing a series of parallel swaps between odd and even pairs of
variables in the list.

This implementation represents each variable in the list with a process and
each process communicates with its neighboring processes in the list to perform
comparisons.
They are synchronized with message passing but other forms of
synchronization could be used.
"""

import multiprocessing as mp
from multiprocessing.connection import Connection, wait
from multiprocessing.reduction import ForkingPickler
from typing import Any, Protocol

"""
The function run by the processes that sorts the list

position = the position in the list the process represents, used to know which
            neighbor we pass our value to
value = the initial value at list[position]
LSend, RSend = the pipes we use to send to our left and right neighbors
LRcv, RRcv = the pipes we use to receive from our left and right neighbors
resultPipe = the pipe used to send results back to main
"""


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def oe_process[T: Comparable](
    position: int,
    value: T,
    l_send: tuple[Connection, Connection] | None,
    r_send: tuple[Connection, Connection] | None,
    lr_cv: tuple[Connection, Connection] | None,
    rr_cv: tuple[Connection, Connection] | None,
    result_pipe: tuple[Connection, Connection],
) -> None:
    # we perform n swaps since after n swaps we know we are sorted
    # we *could* stop early if we are sorted already, but it takes as long to
    # find out we are sorted as it does to sort the list with this algorithm
    try:
        for i in range(10):
            if (i + position) % 2 == 0 and r_send is not None and rr_cv is not None:
                # send your value to your right neighbor
                r_send[1].send(value)

                # receive your right neighbor's value
                temp = rr_cv[0].recv()

                # take the lower value since you are on the left
                value = temp if temp < value else value
            elif (i + position) % 2 != 0 and l_send is not None and lr_cv is not None:
                # send your value to your left neighbor
                l_send[1].send(value)

                # receive your left neighbor's value
                temp = lr_cv[0].recv()

                # take the higher value since you are on the right
                value = temp if value < temp else value
        # after all swaps are performed, send the values back to main
        result_pipe[1].send((value, None))
    except Exception as error:  # noqa: BLE001 -- propagate worker errors to the caller
        try:
            payload = ForkingPickler.dumps((None, error))
        except Exception:  # noqa: BLE001 -- user exceptions can fail to pickle
            fallback = RuntimeError(f"{type(error).__name__}: {error}")
            payload = ForkingPickler.dumps((None, fallback))
        result_pipe[1].send_bytes(payload)
    finally:
        for pipe in (l_send, r_send, lr_cv, rr_cv, result_pipe):
            if pipe is not None:
                for connection in pipe:
                    connection.close()


"""
the function which creates the processes that perform the parallel swaps

arr = the list to be sorted
"""


def odd_even_transposition[T: Comparable](arr: list[T]) -> list[T]:
    """
    Sort in place, propagating worker errors to the caller. Unpickleable
    exceptions become RuntimeError with the original type name and message.

    >>> odd_even_transposition([])
    []
    >>> values = [42]
    >>> odd_even_transposition(values) is values
    True
    >>> odd_even_transposition(list(range(10)[::-1])) == sorted(list(range(10)[::-1]))
    True
    >>> odd_even_transposition(["a", "x", "c"]) == sorted(["x", "a", "c"])
    True
    >>> odd_even_transposition([1.9, 42.0, 2.8]) == sorted([1.9, 42.0, 2.8])
    True
    >>> odd_even_transposition([False, True, False]) == sorted([False, False, True])
    True
    >>> odd_even_transposition([1, 32.0, 9]) == sorted([False, False, True])
    False
    >>> odd_even_transposition([1, 32.0, 9]) == sorted([1.0, 32, 9.0])
    True
    >>> unsorted_list = [-442, -98, -554, 266, -491, 985, -53, -529, 82, -429]
    >>> odd_even_transposition(unsorted_list) == sorted(unsorted_list)
    True
    >>> unsorted_list = [-442, -98, -554, 266, -491, 985, -53, -529, 82, -429]
    >>> odd_even_transposition(unsorted_list) == sorted(unsorted_list + [1])
    False
    >>> values = ["c", "a", "b"]
    >>> odd_even_transposition(values) is values
    True
    >>> values
    ['a', 'b', 'c']
    >>> odd_even_transposition([2.5, -1, 0.0])
    [-1, 0.0, 2.5]
    >>> odd_even_transposition([1, "a"])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if len(arr) < 2:
        return arr

    # spawn method is considered safer than fork
    multiprocessing_context = mp.get_context("spawn")

    process_array_ = []
    result_pipe = []
    # initialize the list of pipes where the values will be retrieved
    for _ in arr:
        result_pipe.append(multiprocessing_context.Pipe())
    # creates the processes
    # the first and last process only have one neighbor so they are made outside
    # of the loop
    temp_rs = multiprocessing_context.Pipe()
    temp_rr = multiprocessing_context.Pipe()
    neighbor_pipes = [temp_rs, temp_rr]
    process_array_.append(
        multiprocessing_context.Process(
            target=oe_process,
            args=(
                0,
                arr[0],
                None,
                temp_rs,
                None,
                temp_rr,
                result_pipe[0],
            ),
        )
    )
    temp_lr = temp_rs
    temp_ls = temp_rr

    for i in range(1, len(arr) - 1):
        temp_rs = multiprocessing_context.Pipe()
        temp_rr = multiprocessing_context.Pipe()
        neighbor_pipes.extend((temp_rs, temp_rr))
        process_array_.append(
            multiprocessing_context.Process(
                target=oe_process,
                args=(
                    i,
                    arr[i],
                    temp_ls,
                    temp_rs,
                    temp_lr,
                    temp_rr,
                    result_pipe[i],
                ),
            )
        )
        temp_lr = temp_rs
        temp_ls = temp_rr

    process_array_.append(
        multiprocessing_context.Process(
            target=oe_process,
            args=(
                len(arr) - 1,
                arr[len(arr) - 1],
                temp_ls,
                None,
                temp_lr,
                None,
                result_pipe[len(arr) - 1],
            ),
        )
    )

    started_processes = []
    try:
        for process in process_array_:
            process.start()
            started_processes.append(process)

        pending = {pipe[0]: position for position, pipe in enumerate(result_pipe)}
        sentinels = {
            process.sentinel: position
            for position, process in enumerate(process_array_)
        }
        values = list(arr)
        while pending:
            ready = set(wait([*pending, *sentinels]))
            for connection in pending.keys() & ready:
                position = pending.pop(connection)
                value, error = connection.recv()
                if error is not None:
                    raise error
                values[position] = value
            for process_sentinel in sentinels.keys() & ready:
                position = sentinels.pop(process_sentinel)
                connection = result_pipe[position][0]
                if connection in pending and not connection.poll():
                    raise RuntimeError(
                        "Sorting worker exited without returning a result"
                    )

        # Do not partially overwrite the input if another worker fails.
        arr[:] = values
    except BaseException:
        for process in started_processes:
            if process.is_alive():
                process.terminate()
        raise
    finally:
        for process in started_processes:
            process.join()
            process.close()
        for pipe in result_pipe + neighbor_pipes:
            for connection in pipe:
                connection.close()
    return arr


# creates a reverse sorted list and sorts it
def main() -> None:
    arr = list(range(10, 0, -1))
    print("Initial List")
    print(*arr)
    arr = odd_even_transposition(arr)
    print("Sorted List\n")
    print(*arr)


if __name__ == "__main__":
    main()
