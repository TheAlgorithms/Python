'''
This program calculate N-th Tribonacci Number.
For better understanding of tribonacci number
go through https://brilliant.org/wiki/tribonacci-sequence/
'''
#'n' refers to the desired n-th tribonacci number
def tribonacci(n: int) -> int:
    '''
    This program takes n integer as user input which refers to the
    desired n-th tribonacci number. Generally, the Tribonacci series
    is initialize as 0, 1, 1......so on
    '''

    #initializing first three tribonacci numbers
    prev1, prev2, prev3 = 1, 1, 0

    #evaluating edge cases
    if n < 0:
        raise ValueError("n must be >=0")
    if n == 0: 
        return prev3
    if n == 1: 
        return prev2
    if n == 2: 
        return prev1

    #initialzing required_tribo_num as 0
    required_tribo_num = 0

    #looping will start from 3 as previous numbers are evaluated above
    for _ in range(3, n + 1):
        result = prev1 + prev2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = required_tribo_num

    return required_tribo_num

if __name__ == '__main__':
    print(tribonacci(7))
