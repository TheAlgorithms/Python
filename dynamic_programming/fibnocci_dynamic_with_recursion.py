'''
This program provides the addition of fibnocci series with recursion, using memoization technique in dynamic programming
'''

memo={}

def fib(fibvalue :int,memorise={}) -> int:
    if(fibvalue in memorise.keys()):
        return memorise[fibvalue]
    if(fibvalue<=1):
        return 1
    
    memorise[fibvalue] =fib(fibvalue-1)+fib(fibvalue-2)

    return memorise[fibvalue]


def fibslow(fibvalue :int) -> int:
    
    if(fibvalue<=1):
        return 1
    
    return fibslow(y-1)+fibslow(fibvalue-2)


if __name__ == "__main__":
    x= int(input())
    print(fib(x))

