"""
Jump arama algoritmasının saf Python ile uygulanması.
Bu algoritma, sıralı bir koleksiyonda n^(1/2) adım büyüklüğü ile iterasyon yapar,
karşılaştırılan eleman aranan elemandan büyük olana kadar devam eder.
Daha sonra, istenen sayıya ulaşana kadar doğrusal bir arama gerçekleştirir.
Eğer bulunamazsa, -1 döner.

Organiser: K. Umut Araz

https://en.wikipedia.org/wiki/Jump_search
"""

import math
from collections.abc import Sequence
from typing import Any, Protocol, TypeVar


class Karşılaştırılabilir(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Karşılaştırılabilir)


def jump_search(arr: Sequence[T], item: T) -> int:
    """
    Jump arama algoritmasının Python ile uygulanması.
    Eğer `item` bulunursa indeksini döner, aksi takdirde -1 döner.

    Örnekler:
    >>> jump_search([0, 1, 2, 3, 4, 5], 3)
    3
    >>> jump_search([-5, -2, -1], -1)
    2
    >>> jump_search([0, 5, 10, 20], 8)
    -1
    >>> jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55)
    10
    >>> jump_search(["aa", "bb", "cc", "dd", "ee", "ff"], "ee")
    4
    """

    arr_boyutu = len(arr)
    blok_boyutu = int(math.sqrt(arr_boyutu))

    önceki = 0
    adım = blok_boyutu
    while arr[min(adım, arr_boyutu) - 1] < item:
        önceki = adım
        adım += blok_boyutu
        if önceki >= arr_boyutu:
            return -1

    while arr[önceki] < item:
        önceki += 1
        if önceki == min(adım, arr_boyutu):
            return -1
    if arr[önceki] == item:
        return önceki
    return -1


if __name__ == "__main__":
    kullanıcı_girişi = input("Virgülle ayrılmış sayıları girin:\n").strip()
    dizi = [int(item) for item in kullanıcı_girişi.split(",")]
    x = int(input("Aranacak sayıyı girin:\n"))

    sonuç = jump_search(dizi, x)
    if sonuç == -1:
        print("Sayı bulunamadı!")
    else:
        print(f"Sayı {x} indeksinde bulunuyor: {sonuç}")
