#!/usr/bin/env python3

"""
Author : Mohit Kumar
Job Sequencing Problem implemented in Python
"""
from __future__ import annotations


class Job:
    def __init__(self, deadline: int, profit: int) -> None:
        self.deadline = deadline
        self.profit = profit

    def __repr__(self) -> str:
        """
        >>> repr(Job(1, 2))
        'Job(1, 2)
        """
        return f"{self.__class__.__name__}({self.deadline}, {self.profit})"

test_jobs: list[Job] = [
    Job(0, 0),
    Job(2, 46),
    Job(4, 52),
    Job(3, 30),
    Job(3, 36),
    Job(2, 56),
    Job(1, 40),
]


def schedule(jobs: list[Job] = test_jobs) -> list[Job]:
    """
    Parameteres: jobs is a list of jobs to be scheduled

    Returns : List of jobs which are profitable and can be done before
                their deadline

    >>> a = Scheduling([(0, 13, 10),(1, 2, 20),(2, 33, 30),(3, 16, 40)])
    >>> a.schedule( 3, [3, 4, 5])
    [(1, 2, 20), (2, 33, 30)]

    >>> a = Scheduling([(0, 13, 10),(1, 2, 20),(2, 33, 30),(3, 16, 40)])
    >>> a.schedule( 4, [13, 2, 33, 16])
    [(1, 2, 20), (2, 33, 30), (3, 16, 40)]

    """
    self.j = [self.jobs[1]]
    self.x = 2
    while self.x < total_jobs:
        self.k = self.j.copy()
        self.k.append(self.jobs[self.x])
        self.x += 1
        if self.feasible(self.k, deadline):
            self.j = self.k.copy()

    return self.j

def is_feasible(jobs: list[Job] = test_jobs) -> bool:
    """
    Parameters : list of current profitable jobs within deadline
                    list of deadline of jobs

    Returns : true if k[-1] job is profitable to us else false

    >>> a = Scheduling([(0, 13, 10),(1, 2, 20),(2, 33, 30),(3, 16, 40)])
    >>> a.feasible( [0], [2, 13, 16, 33] )
    True
    >>> a = Scheduling([(0, 13, 10),(1, 2, 20),(2, 33, 30),(3, 16, 40)])
    >>> a.feasible([0], [2, 13, 16, 33] )
    True
    """

    self.tmp = profit_jobs
    self.is_feasible = True

    i = 0
    j = 1
    k = 0

    while i < len(self.tmp):
        while j < len(self.tmp):
            self.index1 = self.jobs.index(self.tmp[i])
            self.index2 = self.jobs.index(self.tmp[j])
            j += 1
            if deadline[self.index1] > deadline[self.index2]:
                (self.tmp[i], self.tmp[j]) = (
                    self.tmp[j],
                    self.tmp[i],
                )
        i += 1

    while k < len(self.tmp):
        self.job = self.tmp[k]
        if self.job in self.jobs:
            self.jobindex = self.jobs.index(self.job)
        else:
            self.jobindex = 0
        self.dlineval = deadline[self.jobindex]
        self.ftest = k + 1
        k += 1
        if self.dlineval < self.ftest:
            self.is_feasible = False
            break
    return self.is_feasible


def main(jobs: list[Job] = test_jobs):
    # midresult stores jobs in sorting order of deadline
    midresult = []
    for i in range(len(jobs)):
        current_job = []
        current_job.extend((jobs[i].deadline, jobs[i].profit, jobs[i].job_id))
        midresult.append(current_job)
    midresult.sort(key=lambda k: (k[0], -k[1]))
    (deadline, profit, jobs) = map(list, zip(*midresult))

    scheduling_jobs = Scheduling(jobs)
    scheduled_jobs = scheduling_jobs.schedule(len(jobs), deadline)
    print(f"\n Jobs {scheduled_jobs}")

    finalprofit = []
    finaldl = []

    for i, item in enumerate(scheduled_jobs):
        jobsindex = jobs.index(item)
        finalprofit.append(profit[jobsindex])
        finaldl.append(deadline[jobsindex])

    print(f"\n Profit {finalprofit}")
    print(f"\n Deadline {finaldl}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main(jobs=test_jobs)
