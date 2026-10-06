"""
This is an implementation of odd-even transposition sort.

It works by performing a series of parallel swaps between odd and even pairs of
variables in the list.

This implementation represents each variable in the list with a process and
each process communicates with its neighboring processes in the list to perform
comparisons.
They are synchronized with locks and message passing but other forms of
synchronization could be used.
"""

import multiprocessing as mp
from typing import Any, Protocol

# lock used to ensure that two processes do not access a pipe at the same time
# NOTE This breaks testing on build runner. May work better locally
# process_lock = mp.Lock()


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def oe_process[T: Comparable](
    position: int,
    value: T,
    l_send: tuple[mp.connection.Connection, mp.connection.Connection] | None,
    r_send: tuple[mp.connection.Connection, mp.connection.Connection] | None,
    lr_cv: tuple[mp.connection.Connection, mp.connection.Connection] | None,
    rr_cv: tuple[mp.connection.Connection, mp.connection.Connection] | None,
    result_pipe: tuple[mp.connection.Connection, mp.connection.Connection],
    multiprocessing_context: Any,
) -> None:
    """
    The function run by the processes that sorts the list.

    position = the position in the list the process represents, used to know
               which neighbor we pass our value to
    value    = the initial value at list[position]
    l_send, r_send  = the pipes we use to send to our left and right neighbors
    lr_cv,  rr_cv   = the pipes we use to receive from our left and right
                      neighbors
    result_pipe     = the pipe used to send results back to main
    """
    process_lock = multiprocessing_context.Lock()

    # we perform n swaps since after n swaps we know we are sorted
    # we *could* stop early if we are sorted already, but it takes as long to
    # find out we are sorted as it does to sort the list with this algorithm
    try:
        for i in range(10):
            if (i + position) % 2 == 0 and r_send is not None:
                # send your value to your right neighbor
                with process_lock:
                    r_send[1].send(value)

                # receive your right neighbor's value
                with process_lock:
                    temp = rr_cv[0].recv()

                # take the lower value since you are on the left
                value = min(value, temp)
            elif (i + position) % 2 != 0 and l_send is not None:
                # send your value to your left neighbor
                with process_lock:
                    l_send[1].send(value)

                # receive your left neighbor's value
                with process_lock:
                    temp = lr_cv[0].recv()

                # take the higher value since you are on the right
                value = max(value, temp)
        # after all swaps are performed, send the value back to main
        result_pipe[1].send((False, value))
    except Exception as e:  # noqa: BLE001
        result_pipe[1].send((True, e))


def odd_even_transposition[T: Comparable](arr: list[T]) -> list[T]:
    """
    Sort a list of comparable items using the parallel odd-even transposition
    sort algorithm.

    Each element is represented by a separate process; neighboring processes
    exchange values in alternating odd/even rounds via message-passing pipes.
    Items must be mutually comparable (support ``<``); passing a list whose
    elements cannot be compared with each other (e.g. mixing ``int`` and
    ``str``) raises ``TypeError`` inside the worker processes.

    :param arr: a list of mutually comparable items
    :return: the same list sorted in ascending order

    Examples:
    >>> odd_even_transposition([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> odd_even_transposition([3, 3, 1, 2, 2, 1])
    [1, 1, 2, 2, 3, 3]
    >>> odd_even_transposition(['c', 'a', 'b'])
    ['a', 'b', 'c']
    >>> odd_even_transposition([3.3, 1.1, 2.2])
    [1.1, 2.2, 3.3]
    >>> odd_even_transposition(list(range(10)[::-1])) == sorted(range(10))
    True
    >>> unsorted_list = [-442, -98, -554, 266, -491, 985, -53, -529, 82, -429]
    >>> odd_even_transposition(unsorted_list) == sorted(unsorted_list)
    True
    """
    if not arr:
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
                multiprocessing_context,
            ),
        )
    )
    temp_lr = temp_rs
    temp_ls = temp_rr

    for i in range(1, len(arr) - 1):
        temp_rs = multiprocessing_context.Pipe()
        temp_rr = multiprocessing_context.Pipe()
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
                    multiprocessing_context,
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
                multiprocessing_context,
            ),
        )
    )

    # start the processes
    for p in process_array_:
        p.start()

    # wait for the processes to end and write their values to the list
    for p in range(len(result_pipe)):
        is_error, result = result_pipe[p][0].recv()
        if is_error:
            for proc in process_array_:
                proc.terminate()
            raise result
        arr[p] = result
        process_array_[p].join()
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
