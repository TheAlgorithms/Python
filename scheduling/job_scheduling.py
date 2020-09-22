#!/usr/bin/env python3

"""
Author : Mohit Kumar
Job Sequencing Problem implemented in python
"""


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
    jobs = [0, 1, 2, 3, 4, 5, 6]  # jobs id
    deadline = [0, 2, 4, 3, 3, 2, 1]  # deadline to job[i]
    profit = [0, 46, 52, 30, 36, 56, 40]  # profit associated wrt job[i]

    midresult = [list(x) for x in zip(deadline, profit, jobs)]
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

    print(f'\n Profit {finalprofit}')
    print(f'\n Deadline {finaldl}')


if __name__ == "__main__":
    main()
