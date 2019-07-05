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
from multiprocessing import Process, Pipe, Lock

#lock used to ensure that two processes do not access a pipe at the same time
processLock = Lock()

"""
The function run by the processes that sorts the list

position = the position in the list the prcoess represents, used to know which
            neighbor we pass our value to
value = the initial value at list[position]
LSend, RSend = the pipes we use to send to our left and right neighbors
LRcv, RRcv = the pipes we use to receive from our left and right neighbors
resultPipe = the pipe used to send results back to main
"""
def oeProcess(position, value, LSend, RSend, LRcv, RRcv, resultPipe):
    global processLock

    #we perform n swaps since after n swaps we know we are sorted
    #we *could* stop early if we are sorted already, but it takes as long to
    #find out we are sorted as it does to sort the list with this algorithm
    for i in range(0, 10):

        if( (i + position) % 2 == 0 and RSend != None):
            #send your value to your right neighbor
            processLock.acquire()
            RSend[1].send(value)
            processLock.release()

            #receive your right neighbor's value
            processLock.acquire()
            temp = RRcv[0].recv()
            processLock.release()

            #take the lower value since you are on the left
            value = min(value, temp)
        elif( (i + position) % 2 != 0 and LSend != None):
            #send your value to your left neighbor
            processLock.acquire()
            LSend[1].send(value)
            processLock.release()

            #receive your left neighbor's value
            processLock.acquire()
            temp = LRcv[0].recv()
            processLock.release()

            #take the higher value since you are on the right
            value = max(value, temp)
    #after all swaps are performed, send the values back to main
    resultPipe[1].send(value)

"""
the function which creates the processes that perform the parallel swaps

arr = the list to be sorted
"""
def OddEvenTransposition(arr):

    processArray = []

    resultPipe = []

    #initialize the list of pipes where the values will be retrieved
    for _ in arr:
        resultPipe.append(Pipe())

    #creates the processes
    #the first and last process only have one neighbor so they are made outside
    #of the loop
    tempRs = Pipe()
    tempRr = Pipe()
    processArray.append(Process(target = oeProcess, args = (0, arr[0], None, tempRs, None, tempRr, resultPipe[0])))
    tempLr = tempRs
    tempLs = tempRr

    for i in range(1, len(arr) - 1):
        tempRs = Pipe()
        tempRr = Pipe()
        processArray.append(Process(target = oeProcess, args = (i, arr[i], tempLs, tempRs, tempLr, tempRr, resultPipe[i])))
        tempLr = tempRs
        tempLs = tempRr

    processArray.append(Process(target = oeProcess, args = (len(arr) - 1, arr[len(arr) - 1], tempLs, None, tempLr, None, resultPipe[len(arr) - 1])))

    #start the processes
    for p in processArray:
        p.start()

    #wait for the processes to end and write their values to the list
    for p in range(0, len(resultPipe)):
        arr[p] = resultPipe[p][0].recv()
        processArray[p].join()

    return(arr)


#creates a reverse sorted list and sorts it
def main():
    arr = []

    for i in range(10, 0, -1):
        arr.append(i)
    print("Initial List")
    print(*arr)

    list = OddEvenTransposition(arr)

    print("Sorted List\n")
    print(*arr)

if __name__ == "__main__":
    main()
