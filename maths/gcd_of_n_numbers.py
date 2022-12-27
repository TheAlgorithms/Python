from collections import Counter

"""
Gcd of N Numbers
"""

def get_factors(number: int, factors: dict | None = None, min_factor: int = 2) -> Counter:
    """
    get all factors of number:
    >>> get_factors(45)
    Counter({3: 2, 5: 1})
    >>> get_factors(2520)
    Counter({2: 3, 3: 2, 5: 1, 7: 1})
    >>> get_factors(23)
    Counter({23: 1})
    """
    if factors is None:
        factors = Counter()
        
        
    if number == min_factor:
        factors[min_factor] += 1
        return factors
    
    if not number % min_factor:
        factors[min_factor] += 1
        return get_factors(number // min_factor, factors, min_factor)
    else:
        return get_factors(number, factors, min_factor + 1)
    
def get_gcd(*numbers: int) -> int:
    """
    get gcd of n numbers:
    >>> get_gcd(18, 45)
    9
    >>> get_gcd(23, 37)
    1
    >>> get_gcd(2520, 8350)
    10
    """
    data = [get_factors(number) for number in numbers]
    same_factors = data[0]
    for d in data[1:]:
        same_factors = same_factors & d
    mult = 1
    for m in [factor ** same_factors[factor] for factor in same_factors]:
        mult *= m
    return mult

if __name__ == "__main__":
    print(get_gcd(18, 45)) # 9