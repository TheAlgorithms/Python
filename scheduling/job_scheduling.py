#!/usr/bin/env python3

"""
Author : Mohit Kumar
Job Sequencing Problem implemented in python
"""
from collections import namedtuple


class Scheduling:
    def __init__(self, jobs):
        self.jobs = jobs

    def schedule(self, n, deadline):
        self.sdl = deadline
        self.J = [self.jobs[1]]
        self.x = 2
        while self.x < n:
            self.K = self.J.copy()
            self.K.append(self.jobs[self.x])
            self.x = self.x + 1
            if self.feasible(self.K, self.sdl):
                self.J = self.K.copy()

        return self.J

    def feasible(self, K, fdl):
        self.tmp = K
        self.is_feasible = True

        i = 0
        j = 1
        k = 0

        while i < len(self.tmp):
            while j < len(self.tmp):
                self.index1 = self.jobs.index(self.tmp[i])
                self.index2 = self.jobs.index(self.tmp[j])
                j += 1
                if fdl[self.index1] > fdl[self.index2]:
                    (self.tmp[i], self.tmp[j]) = (
                        self.tmp[j],
                        self.tmp[i],
                    )
            i += 1

        while k < len(self.tmp):
            self.job = self.tmp[k]
            self.jobindex = self.jobs.index(self.job)
            self.dlineval = fdl[self.jobindex]
            self.ftest = k + 1
            k += 1
            if self.dlineval < self.ftest:
                self.is_feasible = False
                break

        return self.is_feasible


def main():
    n = 7  # Number of jobs
    job = namedtuple("job", "jobs deadline profit")
    jobs = [
        job(0, 0, 0),
        job(1, 2, 46),
        job(2, 4, 52),
        job(3, 3, 30),
        job(4, 3, 36),
        job(5, 2, 56),
        job(6, 1, 40),
    ]

    midresult = []
    for i in range(n):
        cur_job = []
        cur_job.extend((jobs[i].deadline, jobs[i].profit, jobs[i].jobs))
        midresult.append(cur_job)
    midresult.sort(key=lambda k: (k[0], -k[1]))
    (deadline, profit, jobs) = map(list, zip(*midresult))

    sins = Scheduling(jobs)
    sjobs = sins.schedule(n, deadline)
    print("\n Jobs", sjobs)

    finalprofit = []
    finaldl = []

    for i, item in enumerate(sjobs):
        jobsindex = jobs.index(item)
        finalprofit.append(profit[jobsindex])
        finaldl.append(deadline[jobsindex])

    print(f"\n Profit {finalprofit}")
    print(f"\n Deadline {finaldl}")


if __name__ == "__main__":
    main()
