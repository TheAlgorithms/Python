from time import sleep
from threading import Timer
 
def sleepsort(values):
    sleepsort.result = []
    def add1(x):
        sleepsort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleepsort.result
 
numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)
 
numbers = sleepsort(numbers)
print(numbers)
