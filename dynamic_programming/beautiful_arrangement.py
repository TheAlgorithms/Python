"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers 
perm (1-indexed) is considered a "beautiful arrangement" if for every i (1 <= i <= n), 
either of the following is true:

-> perm[i] is divisible by i.
-> i is divisible by perm[i].
Given an integer n, return the number of the "beautiful arrangements" that you can construct.

"""
# Solution using Backtracking

class beautifularrange:
    # funtion call; n is the size of the permutation (numbers 1..n)
    def countarrangement(self, n: int) -> int:
        
        self.count = 0
        """
        We initialize a counter to record how many valid arrangements we find. 
        Using self.count lets the nested function modify it without nonlocal.
        """
        
        used = [False] * (n + 1)
        """
        A boolean list to mark which numbers have 
        already been placed in the permutation.
        """
        
        def backtrack(pos):
            """
            Define the recursive backtracking function.
            pos is the current position in the permutation we are filling (1-indexed). 
            We try to assign a number to position pos.
            """
            if pos > n:
                
                self.count += 1 
                # We found a complete valid arrangement, so increment the total count.
                return
            for num in range(1, n + 1): 
                # Try every candidate number num for the current position pos.
                
                
                """
                Two checks in one:
                1. not used[num] — the number num has not been placed yet (we can use it).
                2. (num % pos == 0 or pos % num == 0) — the 
                    beautiful-arrangement condition: 
                    either num divides pos or pos divides num.
                If both are true, num is a valid choice for pos.
            
                """
                if not used[num] and (num % pos == 0 or pos % num == 0):
                    used[num] = True
                    backtrack(pos + 1)
                    used[num] = False
        
        backtrack(1)
        return self.count
