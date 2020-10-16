"""
Self Powers
Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def solution():
    """
    this is simple using power method to calculate answer
    
    solution()
    "9110846700"
    """
    t_sum = 0
    for i in range(1, 1001):
        t_sum += i ** i
    return str(t_sum)[-10:]

if __name__ == "__main__":
    print(solution())
