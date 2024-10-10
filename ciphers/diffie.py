from __future__ import annotations


def asal_kök_bul(modulus: int) -> int | None:
    """
    Modül için bir asal kök bul, eğer varsa.

    Organiser: K. Umut Araz

    Argümanlar:
        modulus : Asal kök bulunacak modül.

    Döndürür:
        Eğer varsa asal kök, yoksa None döner.

    Örnekler:
    >>> asal_kök_bul(7)  # Modül 7'nin asal kökü 3'tür
    3
    >>> asal_kök_bul(11)  # Modül 11'nin asal kökü 2'dir
    2
    >>> asal_kök_bul(8) == None  # Modül 8'nin asal kökü yoktur
    True
    """
    for r in range(1, modulus):
        li = []
        for x in range(modulus - 1):
            val = pow(r, x, modulus)
            if val in li:
                break
            li.append(val)
        else:
            return r
    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    asal_sayi = int(input("Bir asal sayı q girin: "))
    asal_kök = asal_kök_bul(asal_sayi)
    if asal_kök is None:
        print(f"Değer için asal kök bulunamadı: {asal_kök!r}")
    else:
        a_özel = int(input("A'nın özel anahtarını girin: "))
        a_genel = pow(asal_kök, a_özel, asal_sayi)
        b_özel = int(input("B'nin özel anahtarını girin: "))
        b_genel = pow(asal_kök, b_özel, asal_sayi)

        a_gizli = pow(b_genel, a_özel, asal_sayi)
        b_gizli = pow(a_genel, b_özel, asal_sayi)

        print("A tarafından üretilen anahtar değeri: ", a_gizli)
        print("B tarafından üretilen anahtar değeri: ", b_gizli)
