#Project Euler Problem 114

def solution(n):

    #min block size
    m = 3

    ways = [1]*(m) + [0]*(n-m+1)
    for k in range(m, n+1):
        ways[k] = ways[k-1] + sum(ways[:k-m]) + 1
    
    return ways[n]

if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(solution(50))
