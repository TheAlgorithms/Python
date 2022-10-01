"""Hello World 
To create a shuffled array. Generate a pseudo random number(pseudo number is generate with random time provided as its seed value) , Swap that number with any other element in the list run this swapping len(Array) times to get desired shuffled array

To Understand more of random number generation follow https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator
"""

import random
import time
class solution:
    def __init__(self,array) :
        self.arr = array    
        self.seed = int(str(time.time())[-1:-5:-1])                  #generating a 4 digit number randomly using decimals of current time

    def prng(self,i):                           #pseudo random number generator
        self.seed*=self.seed
        any = str(self.seed)
        if any != '0' :
            self.seed = int(any[2:6])
        else:
            self.seed = int(str(time.time())[-1:-5:-1])
            any = str(self.seed)
        if int(any[4])<i :
            return int(any[4])
        return self.prng(i)

    def reset(self):
        print(self.arr)

    def shuffle(self):
        
        temp = self.arr.copy()
        for i in range(1,len(self.arr)):
            a = self.prng(len(self.arr))
            temp[a],temp[i] = temp[i],temp[a]
        return temp

solclass = solution([1,2,3,4,5,7,8,10,21])
shuffled_Arr = solclass.shuffle()
print(shuffled_Arr)
solclass.reset()

