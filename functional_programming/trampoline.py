# Implementation of trampolining concept for optimization tail-recursive functions

# Class-based version.
class trampoline:
    def __init__(self,func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, *kwargs)
        while callable(result):
            result = result()
        return result
        
    def call(self,*args,**kwargs):
        return lambda : self.func(*args, **kwargs)

@trampoline
def range_rec(elem,stop,res=None):
    res = res or []
    res.append(elem)
    if elem == stop:
        return res
    else:
        return range_rec.call(elem+1 if elem < stop else elem-1, stop, res)

print(range_rec(1,30000))

@trampoline
def sum_natural(x, result=0):
    if x == 0:
        return result
    else:
        return sum_natural.call(x - 1, result + x)


print(sum_natural(1000000))


# Function - based version. Can`t be used as decorator
def trampoline_func(func):
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        while callable(result):
            result = result()
        return result
    return wrapper

def range_lambda(elem,stop,res=None):
    res = res or []
    res.append(elem)
    if elem == stop:
        return res
    else:
        return lambda : range_rec(elem+1 if elem < stop else elem-1, stop, res)

print(trampoline_func(range_lambda)(1,30000))