import sys
import auxiliary as aux


class Schedule:

    def __init__(self, ready_queue):
        self.rq = ready_queue.processes
        self.n = ready_queue.n

    def ps_time(self):
        remaining = self.n
        cpu_time = 0
        min_bt_index = 0
        min_bt = sys.maxsize
        flag = False

        r_times = [0] * self.n
        for i in range(self.n):
            r_times[i] = self.rq[i][2]

        while remaining:

            for j in range(self.n):
                if (self.rq[j][1] <= cpu_time) and (r_times[j] < min_bt) and r_times[j] > 0:
                    min_bt = r_times[j]
                    min_bt_index = j
                    flag = True
            if not flag:
                cpu_time += 1
                continue

            r_times[min_bt_index] -= 1

            min_bt = r_times[min_bt_index]
            if min_bt == 0:
                min_bt = sys.maxsize

            if r_times[min_bt_index] == 0:

                remaining -= 1
                flag = False

                finish_time = cpu_time + 1

                self.rq[min_bt_index][4] = finish_time - self.rq[min_bt_index][2] - self.rq[min_bt_index][1]

                if self.rq[min_bt_index][4] < 0:
                    self.rq[min_bt_index][4] = 0

            self.rq[min_bt_index][5] = self.rq[min_bt_index][2] + self.rq[min_bt_index][4]

            cpu_time += 1

    def show(self):
        self.ps_time()
        print('\nSRTF SCHEDULING')
        aux.show(self.rq, self.n)
