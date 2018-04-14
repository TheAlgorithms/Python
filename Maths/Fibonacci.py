class Fibonacci:
    def formula(self, n):
        '''Return nth fibonacci number using formula.''' 
        return int( ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)) )

    def iteration(self, num):
        '''Return nth fibonacci number using iterative formula.'''
        if num == 0: return 0
        if num == 1: return 1
        a = 1
        b = 1
        for i in range(num): 
            a,b = b, a+b
        return b-a
    
    def fibrange(self, start, stop, fast=True):
        ''' Returns sequence of fibonacci number in the supplied range.'''
        fib_range = []
        if not fast:
            # Use the slower iterative formula.
            for i in range(start, stop):
                fib_range.append(self.iteration(i))
            return fib_range
        else:
            # Use the faster mathematical formula.
            for i in range(start, stop):
                fib_range.append(self.formula(i))
            return fib_range

if __name__ == '__main__':
    f = Fibonacci()
    print ( '10th Fibonacci Number by formula', f.formula(10))
    print ( '10th Fibonacci Number by iteration', f.iteration(10))
    print ('List of first 100 Fibonacci Numbers',f.fibrange(0, 100))
