def collatz_sequence(n):
    """
    Collatz conjecture: start with any positive integer n.Next termis obtained from the previous term as follows: 
    if the previous term is even, the next term is one half the previous term. 
    If the previous term is odd, the next term is 3 times the previous term plus 1. 
    The conjecture states the sequence will always reach 1 regaardess of starting n.
    Example:
    >>> collatz_sequence(43)
    [43, 130, 65, 196, 98, 49, 148, 74, 37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:# even
            n //= 2 
        else:
            n = 3*n +1
        sequence.append(n)
    return sequence


def main():
    n = 43
    sequence = collatz_sequence(n)
    print(sequence)
    print("collatz sequence from %d took %d steps."%(n,len(sequence)))

if __name__ == '__main__':
    main()
