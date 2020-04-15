"""
Sleepsort is probably the wierdest of all sorting functions
with time-complexity of O(max(input)+n) which is
quite different from almost all other sorting techniques.
If the number of inputs is small then the complexity
can be approximated to be O(max(input)) which is a constant

If the number of inputs is large then the complexity is
approximately O(n)

This function uses multithreading a kind of higher order programming
and calls n functions, each with a sleep time equal to its number.
Hence each of the functions wake in Sorted form

But this function is not stable for very large values
"""
from time import sleep
from threading import Timer
 
def sleepsort(values):
    sleepsort.result = []
    def add1(x):
        sleepsort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v:
            mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleepsort.result
 
if __name__ == '__main__':
    x = [3,2,4,7,3,6,9,1]
    sorted_x=sleepsort(x)
    print(sorted_x)
