#!/usr/bin/env python3

"""
Author : Mohit Kumar
Job Sequencing Problem implemented in python
"""
from collections import namedtuple
from typing import List


class Scheduling:
    def __init__(self, jobs: List[int]) -> None:
        """
        Assign jobs as instance of class Scheduling
        """
        self.jobs = jobs

    def schedule(self, total_jobs: int, deadline: List[int]) -> List[int]:
        """
        Parameteres  : total_jobs  and list of deadline of jobs

        Returns : List of jobs_id which are profitable  and can be done before
                  deadline

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

    def feasible(self, profit_jobs: List[int], deadline: List[int]) -> bool:
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


def main():
    job = namedtuple("job", "job_id deadline profit")
    jobs = [
        job(0, 0, 0),
        job(1, 2, 46),
        job(2, 4, 52),
        job(3, 3, 30),
        job(4, 3, 36),
        job(5, 2, 56),
        job(6, 1, 40),
    ]
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
    main()
