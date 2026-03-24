# Primality Testing with the Rabin-Miller Algorithm

import secrets


def rabin_miller(num: int) -> bool:
    """
    Rabin-Miller primality test using a cryptographically secure PRNG.

    Uses 40 witness rounds (vs the original 5) to reduce the probability of
    a composite passing to at most 4^-40 ≈ 8.3e-25.

    Requires num >= 5; smaller values are handled by is_prime_low_num via the
    low_primes list and never reach this function in normal use.

    >>> rabin_miller(17)
    True
    >>> rabin_miller(21)
    False
    >>> rabin_miller(561)  # Carmichael number, composite
    False
    >>> rabin_miller(7919)  # prime
    True
    """
    if num < 5:
        raise ValueError(f"rabin_miller requires num >= 5, got {num}")

    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1

    for _ in range(40):  # 40 rounds: false-positive probability ≤ 4^-40
        # Witness a must be in [2, num-2]; num >= 5 guarantees num-3 >= 2.
        a = secrets.randbelow(num - 3) + 2  # range [2, num-2]
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v**2) % num
    return True


def is_prime_low_num(num: int) -> bool:
    """
    >>> is_prime_low_num(1)
    False
    >>> is_prime_low_num(2)
    True
    >>> is_prime_low_num(97)
    True
    >>> is_prime_low_num(100)
    False
    """
    if num < 2:
        return False

    low_primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
        313,
        317,
        331,
        337,
        347,
        349,
        353,
        359,
        367,
        373,
        379,
        383,
        389,
        397,
        401,
        409,
        419,
        421,
        431,
        433,
        439,
        443,
        449,
        457,
        461,
        463,
        467,
        479,
        487,
        491,
        499,
        503,
        509,
        521,
        523,
        541,
        547,
        557,
        563,
        569,
        571,
        577,
        587,
        593,
        599,
        601,
        607,
        613,
        617,
        619,
        631,
        641,
        643,
        647,
        653,
        659,
        661,
        673,
        677,
        683,
        691,
        701,
        709,
        719,
        727,
        733,
        739,
        743,
        751,
        757,
        761,
        769,
        773,
        787,
        797,
        809,
        811,
        821,
        823,
        827,
        829,
        839,
        853,
        857,
        859,
        863,
        877,
        881,
        883,
        887,
        907,
        911,
        919,
        929,
        937,
        941,
        947,
        953,
        967,
        971,
        977,
        983,
        991,
        997,
    ]

    if num in low_primes:
        return True

    for prime in low_primes:
        if (num % prime) == 0:
            return False

    return rabin_miller(num)


def generate_large_prime(keysize: int = 1024) -> int:
    """
    Generate a large prime using a cryptographically secure PRNG.

    >>> p = generate_large_prime(16)
    >>> is_prime_low_num(p)
    True
    >>> p.bit_length() >= 15  # at least keysize-1 bits
    True
    """
    while True:
        # secrets.randbits produces a CSPRNG integer; set the high bit to
        # guarantee the result is in [2^(keysize-1), 2^keysize - 1].
        num = secrets.randbits(keysize) | (1 << (keysize - 1))
        if is_prime_low_num(num):
            return num


if __name__ == "__main__":
    num = generate_large_prime()
    print(("Prime number:", num))
    print(("is_prime_low_num:", is_prime_low_num(num)))
