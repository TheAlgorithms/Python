
memo={}

def fib(y,memorise={}):
    if(y in memorise.keys()):
        return memorise[y]
    if(y<=1):
        return 1
    
    memorise[y] =fib(y-1)+fib(y-2)

    return memorise[y]


def fibslow(y):
    
    if(y<=1):
        return 1
    
    return fibslow(y-1)+fibslow(y-2)


if __name__ == "__main__":
    x= int(input())
    print(fib(x))
