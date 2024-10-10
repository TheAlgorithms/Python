"""Ondalık Sayıyı Sekizlik Sayıya Dönüştür."""
# Organiser: K. Umut Araz
import math

# Değiştirildiği yer:
# https://github.com/TheAlgorithms/Javascript/blob/master/Conversions/DecimalToOctal.js


def ondalik_to_sekizlik(num: int) -> str:
    """Ondalık Sayıyı Sekizlik Sayıya Dönüştür.

    >>> all(ondalik_to_sekizlik(i) == oct(i) for i
    ...     in (0, 2, 8, 64, 65, 216, 255, 256, 512))
    True
    """
    sekizlik = 0
    sayac = 0
    while num > 0:
        kalan = num % 8
        sekizlik = sekizlik + (kalan * math.floor(math.pow(10, sayac)))
        sayac += 1
        num = math.floor(num / 8)  # temelde /= 8, kalan olmadan
    return f"0o{int(sekizlik)}"


def main() -> None:
    """Ondalık sayıların sekizlik karşılıklarını yazdırır."""
    print("\n2'nin sekizlik karşılığı:")
    print(ondalik_to_sekizlik(2))  # = 2
    print("\n8'in sekizlik karşılığı:")
    print(ondalik_to_sekizlik(8))  # = 10
    print("\n65'in sekizlik karşılığı:")
    print(ondalik_to_sekizlik(65))  # = 101
    print("\n216'nın sekizlik karşılığı:")
    print(ondalik_to_sekizlik(216))  # = 330
    print("\n512'nin sekizlik karşılığı:")
    print(ondalik_to_sekizlik(512))  # = 1000
    print("\n")


if __name__ == "__main__":
    main()
