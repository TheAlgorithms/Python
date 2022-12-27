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
from multiprocessing import Lock, Pipe, Process

# lock used to ensure that two processes do not access a pipe at the same time
process_lock = Lock()

"""
The function run by the processes that sorts the list

position = the position in the list the process represents, used to know which
            neighbor we pass our value to
value = the initial value at list[position]
LSend, RSend = the pipes we use to send to our left and right neighbors
LRcv, RRcv = the pipes we use to receive from our left and right neighbors
resultPipe = the pipe used to send results back to main
"""


def oe_process(position, value, l_send, r_send, lr_cv, rr_cv, result_pipe):
    global process_lock

    # we perform n swaps since after n swaps we know we are sorted
    # we *could* stop early if we are sorted already, but it takes as long to
    # find out we are sorted as it does to sort the list with this algorithm
    for i in range(0, 10):

        if (i + position) % 2 == 0 and r_send is not None:
            # send your value to your right neighbor
            process_lock.acquire()
            r_send[1].send(value)
            process_lock.release()

            # receive your right neighbor's value
            process_lock.acquire()
            temp = rr_cv[0].recv()
            process_lock.release()

            # take the lower value since you are on the left
            value = min(value, temp)
        elif (i + position) % 2 != 0 and l_send is not None:
            # send your value to your left neighbor
            process_lock.acquire()
            l_send[1].send(value)
            process_lock.release()

            # receive your left neighbor's value
            process_lock.acquire()
            temp = lr_cv[0].recv()
            process_lock.release()

            # take the higher value since you are on the right
            value = max(value, temp)
    # after all swaps are performed, send the values back to main
    result_pipe[1].send(value)


"""
the function which creates the processes that perform the parallel swaps

arr = the list to be sorted
"""


def odd_even_transposition(arr):
    process_array_ = []
    result_pipe = []
    # initialize the list of pipes where the values will be retrieved
    for _ in arr:
        result_pipe.append(Pipe())
    # creates the processes
    # the first and last process only have one neighbor so they are made outside
    # of the loop
    temp_rs = Pipe()
    temp_rr = Pipe()
    process_array_.append(
        Process(
            target=oe_process,
            args=(0, arr[0], None, temp_rs, None, temp_rr, result_pipe[0]),
        )
    )
    temp_lr = temp_rs
    temp_ls = temp_rr

    for i in range(1, len(arr) - 1):
        temp_rs = Pipe()
        temp_rr = Pipe()
        process_array_.append(
            Process(
                target=oe_process,
                args=(i, arr[i], temp_ls, temp_rs, temp_lr, temp_rr, result_pipe[i]),
            )
        )
        temp_lr = temp_rs
        temp_ls = temp_rr

    process_array_.append(
        Process(
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

    # start the processes
    for p in process_array_:
        p.start()

    # wait for the processes to end and write their values to the list
    for p in range(0, len(result_pipe)):
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
