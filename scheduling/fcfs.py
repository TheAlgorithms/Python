# Implementation of First Come First Served CPU sheduling Algorithm
# In this Algorithm we just care about the order that the processes arrived
# without carring about their duration time

# Function to calculate the waiting time of each process


def findWaitingTime(processes, n, duration_time, waiting_time):

    # Initialising the first prosecces' waiting time with 0
    waiting_time[0] = 0

    # calculating waiting time
    for i in range(1, n):
        waiting_time[i] = duration_time[i - 1] + waiting_time[i - 1]


# Function to calculate the turn-around time of each process


def findTurnAroundTime(processes, n, duration_time, waiting_time, turn_around_time):

    # calculating turnaround time by
    # adding duration_time[i] + waiting_time[i]

    for i in range(n):
        turn_around_time[i] = duration_time[i] + waiting_time[i]


# Function to calculate the average time of each process


def findavgTime(processes, n, duration_time):

    waiting_time = [0] * n
    turn_around_time = [0] * n
    total_waiting_time = 0
    total_turn_around_time = 0

    # Function to find waiting time of each process

    findWaitingTime(processes, n, duration_time, waiting_time)

    # Function to find turn-around time of each process

    findTurnAroundTime(processes, n, duration_time, waiting_time, turn_around_time)

    # Display processes along their details

    print("Processes Burst time " + " Waiting time " + " Turn around time")

    # Calculate total waiting time
    # and total turn around time

    for i in range(n):
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_turn_around_time = total_turn_around_time + turn_around_time[i]
        print(f" {i+1}\t\t{duration_time[i]}\t {waiting_time[i]}\t\t {turn_around_time[i]}")
    print(f"Average waiting time = {total_waiting_time / n}")
    print(f"Average turn around time = {total_turn_around_time / n}")


# Driver code
if __name__ == "__main__":

    # process id's
    processes = [1, 2, 3]

    # ensure that we actually have prosecces
    if len(processes) == 0:
        print("Zero amount of processes")
        exit()
    n = len(processes)

    # duration time of all processes
    duration_time = [19, 8, 9]

    # ensure we can match each id to a duration time
    if len(duration_time) != len(processes):
        print("Unable to match all id's with their duration time")
        exit()

    findavgTime(processes, n, duration_time)
