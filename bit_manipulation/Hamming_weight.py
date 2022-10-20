def hammingWeight(self, n):
    weight = 0
    if n == 0:
        return n
    while n >= 1:
        remainder = n % 2
        n = n / 2
        if remainder != 0:
            weight += 1
    return weight
