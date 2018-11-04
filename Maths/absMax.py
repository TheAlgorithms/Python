from abs import absVal
def absMax(x):
    """
    >>>absMax([0,5,1,11])
    11
    >>absMax([3,-10,-2])
    -10
    """
    j = x[0]
    for i in x:
        if absVal(i) < j:
            j = i
    return j
    #BUG: i is apparently a list, TypeError: '<' not supported between instances of 'list' and 'int' in absVal


def main():
    a = [1,2,-11]
    print(absVal(a)) # = -11

if __name__ == '__main__':
    main()
