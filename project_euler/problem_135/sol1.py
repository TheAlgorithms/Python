"""
Project Euler Problem 135: https://projecteuler.net/problem=135

Given the positive integers, x, y, and z,
are consecutive terms of an arithmetic progression,
the least value of the positive integer, n,
for which the equation,
x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value
which has exactly ten solutions.

How many values of n less than one million
have exactly ten distinct solutions?


Taking x,y,z of the form a+d,a,a-d respectively,
the given equation reduces to a*(4d-a)=n.
Calculating no of solutions for every n till 1 million by fixing a
,and n must be multiple of a.
Total no of steps=n*(1/1+1/2+1/3+1/4..+1/n)
,so roughly O(nlogn) time complexity.

"""
import time
start_time = time.time()
def solution(limit: int = 1000000) -> int:
    """
    Returns the values of n less than or equal to the limit
    that have exactly ten distinct solutions.
    """
    limit += 1
    count = 0
    for first_term in range(1, limit):
        for n in range(4*first_term, limit, 4*first_term):
            common_difference = first_term + n // first_term
            if common_difference >= limit:
                break
            if common_difference % 4 == 0:
                c = common_difference // 4
                if first_term > c and 3*c > first_term:
                    count += 1
                    if count == 10:
                        return n
    return count


if __name__ == "__main__":
    print(f"{solution() = }")
print("Process finished --- %s seconds ---" % (time.time() - start_time))