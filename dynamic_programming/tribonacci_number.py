'''
This program calculate N-th Tribonacci Number 
for better understanding of tribonacci number 
go through https://brilliant.org/wiki/tribonacci-sequence/
'''
class Tribonacci:
    def tribonacci(self, n: int) -> int:
        prev1, prev2, prev3 = 1, 1, 0
        if n == 0: return prev3
        if n == 1: return prev2
        if n == 2: return prev1
        result = 0
        for _ in range(3, n + 1):
            result = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = result
        return result
