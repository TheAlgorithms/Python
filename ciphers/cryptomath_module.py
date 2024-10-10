from maths.büyük_ortak_bölgenin_hesaplanması import gcd_by_iterative

"""
Organiser: K. Umut Araz
"""


def mod_tersi_bul(a: int, m: int) -> int:
    if gcd_by_iterative(a, m) != 1:
        msg = f"{a!r} ve {m!r} için mod tersi mevcut değil"
        raise ValueError(msg)
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
