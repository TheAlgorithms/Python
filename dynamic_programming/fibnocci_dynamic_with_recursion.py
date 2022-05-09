
memo={}

def fib(int fibvalue,memorise={}) -> int:
    if(fibvalue in memorise.keys()):
        return memorise[fibvalue]
    if(fibvalue<=1):
        return 1
    
    memorise[fibvalue] =fib(fibvalue-1)+fib(fibvalue-2)

    return memorise[fibvalue]


def fibslow(int fibvalue) -> int:
    
    if(fibvalue<=1):
        return 1
    
    return fibslow(y-1)+fibslow(fibvalue-2)


if __name__ == "__main__":
    x= int(input())
    print(fib(x))
