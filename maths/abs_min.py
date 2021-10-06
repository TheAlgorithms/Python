import doctest
    
class abshead:
    def abs_min(self, x: list[int]) -> int:
        
        '''
        >> abs_min([4,73,12,0])
        0
        >> abs_min([-4,-73,12,-1])
        -1
        >>> abs_max([])
        Traceback (most recent call last):
        ValueError: abs_min() arg is an empty sequence
        
        '''
                
        if len(x) == 0:
            raise ValueError("abs_min() arg is an empty sequence")
        j = x[0]
        for i in x:
            if abs(i) < abs(j):
                j = i
        return j

a1 = abshead()  #defining class object

def main():
    a = [-3, -4, 2, -1, -11]
    print(a1.abs_min(a))  # abs_min = -1


if __name__ == "__main__":
    
    doctest.testmod(verbose=True)
    main()
