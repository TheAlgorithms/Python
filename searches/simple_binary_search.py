"""
Doğrusal arama algoritmasının saf Python ile uygulanışı.

Doküman testleri için aşağıdaki komutu çalıştırın:
python3 -m doctest -v simple_binary_search.py

Organiser: K. Umut Araz

Manuel test için çalıştırın:
python3 simple_binary_search.py
"""

from __future__ import annotations


def ikili_arama(dizi: list[int], hedef: int) -> bool:
    """
    >>> test_dizisi = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> ikili_arama(test_dizisi, 3)
    False
    >>> ikili_arama(test_dizisi, 13)
    True
    >>> ikili_arama([4, 4, 5, 6, 7], 4)
    True
    >>> ikili_arama([4, 4, 5, 6, 7], -10)
    False
    >>> ikili_arama([-18, 2], -18)
    True
    >>> ikili_arama([5], 5)
    True
    >>> ikili_arama(['a', 'c', 'd'], 'c')
    True
    >>> ikili_arama(['a', 'c', 'd'], 'f')
    False
    >>> ikili_arama([], 1)
    False
    >>> ikili_arama([-.1, .1 , .8], .1)
    True
    >>> ikili_arama(range(-5000, 5000, 10), 80)
    True
    >>> ikili_arama(range(-5000, 5000, 10), 1255)
    False
    >>> ikili_arama(range(0, 10000, 5), 2)
    False
    """
    if len(dizi) == 0:
        return False
    orta = len(dizi) // 2
    if dizi[orta] == hedef:
        return True
    if hedef < dizi[orta]:
        return ikili_arama(dizi[:orta], hedef)
    else:
        return ikili_arama(dizi[orta + 1:], hedef)


if __name__ == "__main__":
    kullanici_girdisi = input("Virgülle ayrılmış sayıları girin:\n").strip()
    dizi = [int(eleman.strip()) for eleman in kullanici_girdisi.split(",")]
    hedef = int(input("Listede bulunması gereken sayıyı girin:\n").strip())
    bulunma_durumu = "" if ikili_arama(dizi, hedef) else "bulunamadı "
    print(f"{hedef} {bulunma_durumu} {dizi} içinde.")
