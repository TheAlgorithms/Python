def FastModularExponentiation(b, k, m):
    b %= m
    for _ in range(k):
        b = b ** 2 % m
    return b
