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

# lock used to ensure that two processes do not access a pipe at the same time
# NOTE This breaks testing on build runner. May work better locally
# process_lock = mp.Lock()

"""
The function run by the processes that sorts the list

position = the position in the list the process represents, used to know which
            neighbor we pass our value to
value = the initial value at list[position]
LSend, RSend = the pipes we use to send to our left and right neighbors
LRcv, RRcv = the pipes we use to receive from our left and right neighbors
resultPipe = the pipe used to send results back to main
"""


def oe_process(
    position,
    value,
    l_send,
    r_send,
    lr_cv,
    rr_cv,
    result_pipe,
    multiprocessing_context,
):
    process_lock = multiprocessing_context.Lock()

    # we perform n swaps since after n swaps we know we are sorted
    # we *could* stop early if we are sorted already, but it takes as long to
    # find out we are sorted as it does to sort the list with this algorithm
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
    # after all swaps are performed, send the values back to main
    result_pipe[1].send(value)


"""
the function which creates the processes that perform the parallel swaps

arr = the list to be sorted
"""


def odd_even_transposition(arr):
    """
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
    """
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
        arr[p] = result_pipe[p][0].recv()
        process_array_[p].join()
    return arr


# creates a reverse sorted list and sorts it
def main():
    arr = list(range(10, 0, -1))
    print("Initial List")
    print(*arr)
    arr = odd_even_transposition(arr)
    print("Sorted List\n")
    print(*arr)


if __name__ == "__main__":
    main()
