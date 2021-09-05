"""
Shortest job first - non preemptive scheduling algorithm.
It selects for execution the waiting process with the smallest execution time.
Only after one process has been completed, the next process is selected for execution.
Please enter arrival time and burst time.
Please use spaces to separate the entered times.
https://en.wikipedia.org/wiki/Shortest_job_next
"""

def scheduleProcess(process_details:list) -> tuple([list, float, float]): 

    """
    Calculate the turnaround and waiting time of each process
    Return: Updated process_details list and average turnaround and average waiting time.
    >>> scheduleProcess([[1, 0, 4, 0], [2, 0, 2, 0], [3, 5, 1, 0]])
    ([[2, 0, 2, 1, 2, 2, 0], [1, 0, 4, 1, 6, 6, 2], [3, 5, 1, 1, 7, 2, 1]], 3.3333333333333335, 1.0)
    """

    start_time = []
    end_time = []
    process_start = 0
    process_details.sort(key=lambda x: x[1])

    """
    Sort processes according to the Arrival Time
    """

    for i in range(len(process_details)):
        ready_queue = []
        temp = []
        normal_queue = []

        for j in range(len(process_details)):
            if (process_details[j][1] <= process_start) and (process_details[j][3] == 0):
                temp.extend([process_details[j][0], process_details[j][1], process_details[j][2]])
                ready_queue.append(temp)
                temp = []
            elif process_details[j][3] == 0:
                temp.extend([process_details[j][0], process_details[j][1], process_details[j][2]])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[2])
      
            """
            Sort the processes according to the Burst Time
            """
      
            start_time.append(process_start)
            process_start = process_start + ready_queue[0][2]
            process_end = process_start
            end_time.append(process_end)
            for k in range(len(process_details)):
                if process_details[k][0] == ready_queue[0][0]:
                    break
            process_details[k][3] = 1
            process_details[k].append(process_end)

        elif len(ready_queue) == 0:
            if process_start < normal_queue[0][1]:
                process_start = normal_queue[0][1]
            start_time.append(process_start)
            process_start = process_start + normal_queue[0][2]
            process_end = process_start
            end_time.append(process_end)
            for k in range(len(process_details)):
                if process_details[k][0] == normal_queue[0][0]:
                    break
            process_details[k][3] = 1
            process_details[k].append(process_end)

    process_details ,process_turnaround_time = calculateTurnaroundTime(process_details)
    process_details, process_waiting_time = calculateWaitingTime(process_details)

    process_details.sort(key=lambda x: x[4])
    
    """
    Sort processes according to the Completion Time
    """

    return process_details, process_turnaround_time, process_waiting_time


def calculateTurnaroundTime(process_details:list) -> tuple([list, float]):

    """
    Calculate the turnaround time of each process
    Return: Updated process_details list and average turnaround time.
    >>> calculateTurnaroundTime([[1, 0, 4, 1, 6], [2, 0, 2, 1, 2], [3, 5, 1, 1, 7]])
    ([[1, 0, 4, 1, 6, 6], [2, 0, 2, 1, 2, 2], [3, 5, 1, 1, 7, 2]], 3.3333333333333335)
    """

    total_turnaround_time = 0
    for i in range(len(process_details)):
        turnaround_time = process_details[i][4] - process_details[i][1]
  
        """
        turnaround_time = completion_time - arrival_time
        """
  
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_details[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_details)
  
    """
    average_turnaround_time = total_turnaround_time / number_of_processes
    """
    return process_details, average_turnaround_time


def calculateWaitingTime(process_details:list) -> tuple([list, float]):

    """
    Calculate the waiting time of each process
    Return: Updated process_details list and average waiting time.
    >>> calculateWaitingTime([[1, 0, 4, 1, 6, 6], [2, 0, 2, 1, 2, 2], [3, 5, 1, 1, 7, 2]])
    ([[1, 0, 4, 1, 6, 6, 2], [2, 0, 2, 1, 2, 2, 0], [3, 5, 1, 1, 7, 2, 1]], 1.0)
    """

    total_waiting_time = 0
    for i in range(len(process_details)):
        waiting_time = process_details[i][5] - process_details[i][2]

        """
        waiting_time = turnaround_time - burst_time
        """

        total_waiting_time = total_waiting_time + waiting_time
        process_details[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_details)
 
    """
    average_waiting_time = total_waiting_time / number_of_processes
    """
    return process_details, average_waiting_time


def printData(process_details:list, average_turnaround_time:float, average_waiting_time:float) -> None:

    print("Process ID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")

    for i in range(len(process_details)):
        for j in range(len(process_details[i])):
            if j != 3:

                print(process_details[i][j], end="\t\t")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')

    print(f'Average Waiting Time: {average_waiting_time}')



if __name__ == "__main__":
    print("Enter number of processes: ")
    number_of_processes = int(input())

    arrival_time = [0] * number_of_processes
    burst_time = [0] * number_of_processes
    process_details = []
    
    for i in range(number_of_processes):
        temp_list = []
        print(f"Enter process id, arrival time and burst time for process number {i+1}: ")
        arrival_time[i], burst_time[i] = map(int, input().split())
        temp_list.extend([i+1, arrival_time[i], burst_time[i], 0])
        
        """ 
        0 means the process has not been executed yet
        """
        
        process_details.append(temp_list)
    process_details, process_turnaround_time, process_waiting_time = scheduleProcess(process_details)
    printData(process_details, process_turnaround_time, process_waiting_time)

