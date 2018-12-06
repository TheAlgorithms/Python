from Maths.abs  import absVal

def absMax(x):
    """
    #>>>absMax([0,5,1,11])
    11
    >>absMax([3,-10,-2])
    -10
    """
    j =x[0]
    for i in x:
        if absVal(i) > absVal(j):
            j = i
    return j
 

def main():
    a = [-13, 2, -11, -12]
    print(absMax(a)) # = -13

if __name__ == '__main__':
    main()

"""
print abs Max
"""
