from time import sleep
from threading import Timer

def sleep_sort(l):
    res = []
    def add1(x):
        res.append(x)
    mx = l[0]
    for i in l:
        if mx < i:
            mx = i
        Timer(i, add1, [i]).start()
    sleep(mx+1)
    return res

l1 = [4,1,2,8,5]
print("Initial Array")
print(l1)

print("Final Array is Arriving! Please wait..")
r = sleep_sort(l1)
print(r)
