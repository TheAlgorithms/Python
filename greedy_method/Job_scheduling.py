#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Author : Mohit Kumar
Job Sequencing Problem implemented in python
'''


class Scheduling:

    def __init__(self, jobs):
        self.jobs = jobs

    def schedule(self, n, deadline):
        self.sdl = deadline
        self.J = []
        self.J.append(self.jobs[1])
        self.x = 2
        while self.x < n:
            self.K = self.J.copy()
            self.K.append(self.jobs[self.x])
            self.x = self.x + 1
            self.feasibility = self.feasible(self.K, self.sdl)
            if self.feasibility is True:
                self.J = self.K.copy()

        return self.J

    def feasible(self, K, fdl):
        self.tmp = K
        self.isFeasible = True

        self.i = 0
        self.j = 1
        self.k = 0

        while self.i < len(self.tmp):
            while self.j < len(self.tmp):
                self.index1 = self.jobs.index(self.tmp[self.i])
                self.index2 = self.jobs.index(self.tmp[self.j])
                self.j = self.j + 1
                if fdl[self.index1] > fdl[self.index2]:
                    (self.tmp[self.i], self.tmp[self.j]) = \
                        (self.tmp[self.j], self.tmp[self.i])
            self.i = self.i + 1

        while self.k < len(self.tmp):
            self.job = self.tmp[self.k]
            self.jobindex = self.jobs.index(self.job)
            self.dlineval = fdl[self.jobindex]
            self.ftest = self.k + 1
            self.k = self.k + 1
            if self.dlineval < self.ftest:
                self.isFeasible = False
                break

        return self.isFeasible


def main():
    n = 7  # Number of jobs
    jobs = [  # jobs id
        0,
        1,
        2,
        3,
        4,
        5,
        6
    ]
    deadline = [  # deadline to job[i]
        0,
        2,
        4,
        3,
        3,
        2,
        1
    ]
    profit = [  # profit associated wrt job[i]
        0,
        46,
        52,
        30,
        36,
        56,
        40
    ]

    midresult = [list(x) for x in zip(deadline, profit, jobs)]
    midresult.sort(key=lambda k: (k[0], -k[1]))
    (deadline, profit, jobs) = map(list, zip(*midresult))

    sins = Scheduling(jobs)
    sjobs = sins.schedule(n, deadline)
    print('\n Jobs', sjobs)

    finalprofit = []
    finaldl = []

    for c in range(len(sjobs)):
        item = sjobs[c]
        jobsindex = jobs.index(item)
        finalprofit.append(profit[jobsindex])
        finaldl.append(deadline[jobsindex])

    print('\n profit', finalprofit)
    print('\n Deadline', finaldl)


if __name__ == '__main__':
    main()
