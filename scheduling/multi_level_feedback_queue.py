from collections import deque


class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int) -> None:
        self.process_name = process_name  # process name
        self.arrival_time = arrival_time  # arrival time of the process
        # completion time of finished process or last interrupted time
        self.stop_time = arrival_time
        self.burst_time = burst_time  # remaining burst time
        self.waiting_time = 0  # total time of the process wait in ready queue
        self.turnaround_time = 0  # time from arrival time to completion time


class MLFQ:
    """
    MLFQ(Multi Level Feedback Queue)
    https://en.wikipedia.org/wiki/Multilevel_feedback_queue
    MLFQ has a lot of queues that have different priority
    In this MLFQ,
    The first Queue(0) to last second Queue(N-2) of MLFQ have Round Robin Algorithm
    The last Queue(N-1) has First Come, First Served Algorithm
    """

    def __init__(
        self,
        number_of_queues: int,
        time_slices: list[int],
        queue: deque[Process],
        current_time: int,
    ) -> None:
        # total number of mlfq's queues
        self.number_of_queues = number_of_queues
        # time slice of queues that round robin algorithm applied
        self.time_slices = time_slices
        # unfinished process is in this ready_queue
        self.ready_queue = queue
        # current time
        self.current_time = current_time
        # finished process is in this sequence queue
        self.finish_queue: deque[Process] = deque()

    def calculate_sequence_of_finish_queue(self) -> list[str]:
        """
        This method returns the sequence of finished processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2', 'P4', 'P1', 'P3']
        """
        sequence = []
        for i in range(len(self.finish_queue)):
            sequence.append(self.finish_queue[i].process_name)
        return sequence

    def calculate_waiting_time(self, queue: list[Process]) -> list[int]:
        """
        This method calculates waiting time of processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_waiting_time([P1, P2, P3, P4])
        [83, 17, 94, 101]
        """
        waiting_times = []
        for i in range(len(queue)):
            waiting_times.append(queue[i].waiting_time)
        return waiting_times

    def calculate_turnaround_time(self, queue: list[Process]) -> list[int]:
        """
        This method calculates turnaround time of processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_turnaround_time([P1, P2, P3, P4])
        [136, 34, 162, 125]
        """
        turnaround_times = []
        for i in range(len(queue)):
            turnaround_times.append(queue[i].turnaround_time)
        return turnaround_times

    def calculate_completion_time(self, queue: list[Process]) -> list[int]:
        """
        This method calculates completion time of processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_turnaround_time([P1, P2, P3, P4])
        [136, 34, 162, 125]
        """
        completion_times = []
        for i in range(len(queue)):
            completion_times.append(queue[i].stop_time)
        return completion_times

    def calculate_remaining_burst_time_of_processes(
        self, queue: deque[Process]
    ) -> list[int]:
        """
        This method calculate remaining burst time of processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue, ready_queue = mlfq.round_robin(deque([P1, P2, P3, P4]), 17)
        >>> mlfq.calculate_remaining_burst_time_of_processes(mlfq.finish_queue)
        [0]
        >>> mlfq.calculate_remaining_burst_time_of_processes(ready_queue)
        [36, 51, 7]
        >>> finish_queue, ready_queue = mlfq.round_robin(ready_queue, 25)
        >>> mlfq.calculate_remaining_burst_time_of_processes(mlfq.finish_queue)
        [0, 0]
        >>> mlfq.calculate_remaining_burst_time_of_processes(ready_queue)
        [11, 26]
        """
        return [q.burst_time for q in queue]

    def update_waiting_time(self, process: Process) -> int:
        """
        This method updates waiting times of unfinished processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> mlfq.current_time = 10
        >>> P1.stop_time = 5
        >>> mlfq.update_waiting_time(P1)
        5
        """
        process.waiting_time += self.current_time - process.stop_time
        return process.waiting_time

    def first_come_first_served(self, ready_queue: deque[Process]) -> deque[Process]:
        """
        FCFS(First Come, First Served)
        FCFS will be applied to MLFQ's last queue
        A first came process will be finished at first
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.first_come_first_served(mlfq.ready_queue)
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P1', 'P2', 'P3', 'P4']
        """
        finished: deque[Process] = deque()  # sequence deque of finished process
        while len(ready_queue) != 0:
            cp = ready_queue.popleft()  # current process

            # if process's arrival time is later than current time, update current time
            if self.current_time < cp.arrival_time:
                self.current_time += cp.arrival_time

            # update waiting time of current process
            self.update_waiting_time(cp)
            # update current time
            self.current_time += cp.burst_time
            # finish the process and set the process's burst-time 0
            cp.burst_time = 0
            # set the process's turnaround time because it is finished
            cp.turnaround_time = self.current_time - cp.arrival_time
            # set the completion time
            cp.stop_time = self.current_time
            # add the process to queue that has finished queue
            finished.append(cp)

        self.finish_queue.extend(finished)  # add finished process to finish queue
        # FCFS will finish all remaining processes
        return finished

    def round_robin(
        self, ready_queue: deque[Process], time_slice: int
    ) -> tuple[deque[Process], deque[Process]]:
        """
        RR(Round Robin)
        RR will be applied to MLFQ's all queues except last queue
        All processes can't use CPU for time more than time_slice
        If the process consume CPU up to time_slice, it will go back to ready queue
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue, ready_queue = mlfq.round_robin(mlfq.ready_queue, 17)
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2']
        """
        finished: deque[Process] = deque()  # sequence deque of terminated process
        # just for 1 cycle and unfinished processes will go back to queue
        for i in range(len(ready_queue)):
            cp = ready_queue.popleft()  # current process

            # if process's arrival time is later than current time, update current time
            if self.current_time < cp.arrival_time:
                self.current_time += cp.arrival_time

            # update waiting time of unfinished processes
            self.update_waiting_time(cp)
            # if the burst time of process is bigger than time-slice
            if cp.burst_time > time_slice:
                # use CPU for only time-slice
                self.current_time += time_slice
                # update remaining burst time
                cp.burst_time -= time_slice
                # update end point time
                cp.stop_time = self.current_time
                # locate the process behind the queue because it is not finished
                ready_queue.append(cp)
            else:
                # use CPU for remaining burst time
                self.current_time += cp.burst_time
                # set burst time 0 because the process is finished
                cp.burst_time = 0
                # set the finish time
                cp.stop_time = self.current_time
                # update the process' turnaround time because it is finished
                cp.turnaround_time = self.current_time - cp.arrival_time
                # add the process to queue that has finished queue
                finished.append(cp)

        self.finish_queue.extend(finished)  # add finished process to finish queue
        # return finished processes queue and remaining processes queue
        return finished, ready_queue

    def multi_level_feedback_queue(self) -> deque[Process]:
        """
        MLFQ(Multi Level Feedback Queue)
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2', 'P4', 'P1', 'P3']
        """

        #  all queues except last one have round_robin algorithm
        for i in range(self.number_of_queues - 1):
            finished, self.ready_queue = self.round_robin(
                self.ready_queue, self.time_slices[i]
            )
        #  the last queue has first_come_first_served algorithm
        self.first_come_first_served(self.ready_queue)

        return self.finish_queue


if __name__ == "__main__":
    import doctest

    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    number_of_queues = 3
    time_slices = [17, 25]
    queue = deque([P1, P2, P3, P4])

    if len(time_slices) != number_of_queues - 1:
        exit()

    doctest.testmod(extraglobs={"queue": deque([P1, P2, P3, P4])})

    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    number_of_queues = 3
    time_slices = [17, 25]
    queue = deque([P1, P2, P3, P4])
    mlfq = MLFQ(number_of_queues, time_slices, queue, 0)
    finish_queue = mlfq.multi_level_feedback_queue()

    # print total waiting times of processes(P1, P2, P3, P4)
    print(
        f"waiting time:\
        \t\t\t{MLFQ.calculate_waiting_time(mlfq, [P1, P2, P3, P4])}"
    )
    # print completion times of processes(P1, P2, P3, P4)
    print(
        f"completion time:\
        \t\t{MLFQ.calculate_completion_time(mlfq, [P1, P2, P3, P4])}"
    )
    # print total turnaround times of processes(P1, P2, P3, P4)
    print(
        f"turnaround time:\
        \t\t{MLFQ.calculate_turnaround_time(mlfq, [P1, P2, P3, P4])}"
    )
    # print sequence of finished processes
    print(
        f"sequnece of finished processes:\
        {mlfq.calculate_sequence_of_finish_queue()}"
    )
