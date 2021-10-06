import doctest

class abshead:
    def abs_max(self, x: list[int]) -> int:
        
        '''
        >> abs_max([-8, 5, -13, 9])
        -13
        >> abs_max([10, 0, 12, -1])
        12
        >>> abs_max([])
        Traceback (most recent call last):
        ValueError: abs_max() arg is an empty sequence
        
        '''
        
        if len(x) == 0:
            raise ValueError("abs_max() arg is an empty sequence")
        j = x[0]
        for i in x:
            if abs(i) > abs(j):
                j = i
        return j

a1 = abshead()

def main():
    a = [-8, 5, 2, -1, -14]
    print(a1.abs_max(a))  # abs_max = -1


if __name__ == "__main__":
    
    doctest.testmod(verbose=True)
    main()
