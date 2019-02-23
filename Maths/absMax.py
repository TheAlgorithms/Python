def absMax(x):
    """
    #>>>absMax([0,5,1,11])
    11
    >>absMax([3,-10,-2])
    -10
    """
    j =x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j


def main():
    a = [1,2,-11]
    print(absMax(a)) # = -11


if __name__ == '__main__':
    main()

"""
print abs Max
"""
