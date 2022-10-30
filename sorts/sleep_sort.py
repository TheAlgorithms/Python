from time import sleep
from threading import Timer

""" In sleep sort, the thread having 
the least amount of sleeping time
wakes up first and the number gets 
printed and hence list is sorted"""

def sleep_sort(values):
    sleep_sort.result = []
    def add1(x):
        sleep_sort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleep_sort.result

if __name__ == "__main__":
    x = [3,2,4,7,3,6,9,1]
    print(sleep_sort(x))
    #[1, 2, 3, 3, 4, 6, 7, 9]