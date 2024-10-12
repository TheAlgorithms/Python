def egyptian_fraction(numerator, denominator):
    fractions = []
    while numerator != 0:
        x = denominator // numerator + 1
        fractions.append(f"1/{x}")
        numerator = x * numerator - denominator
        denominator *= x
    return fractions


num, den = 6, 14
print(f"Egyptian Fraction of {num}/{den}: {egyptian_fraction(num, den)}")
