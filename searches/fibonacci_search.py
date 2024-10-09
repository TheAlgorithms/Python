"""
Bu, Fibonacci arama algoritmasının saf Python uygulamasıdır.

Kullanılan kaynaklar:
https://en.wikipedia.org/wiki/Fibonacci_search_technique

Doctest'leri çalıştırmak için aşağıdaki komutu kullanın:
python3 -m doctest -v fibonacci_search.py

Organiser: K. Umut Araz

Manuel test için çalıştırın:
python3 fibonacci_search.py
"""

from functools import lru_cache


@lru_cache
def fibonacci(k: int) -> int:
    """K indeksindeki Fibonacci sayısını bulur.

    Parametreler
    ----------
    k :
        Fibonacci indeksidir.

    Dönüş
    -------
    int
        k pozisyonundaki Fibonacci sayısı.

    >>> fibonacci(0)
    0
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(15)
    610
    >>> fibonacci('a')
    Traceback (most recent call last):
    TypeError: k bir tamsayı olmalıdır.
    >>> fibonacci(-5)
    Traceback (most recent call last):
    ValueError: k tamsayısı sıfır veya daha büyük olmalıdır.
    """
    if not isinstance(k, int):
        raise TypeError("k bir tamsayı olmalıdır.")
    if k < 0:
        raise ValueError("k tamsayısı sıfır veya daha büyük olmalıdır.")
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)


def fibonacci_search(arr: list, val: int) -> int:
    """Fibonacci arama algoritmasının saf Python uygulamasıdır.

    Parametreler
    ----------
    arr
        Sıralı elemanlar listesi.
    val
        Listede aranacak eleman.

    Dönüş
    -------
    int
        Elemanın dizideki indeksi.
        Eleman bulunamazsa -1 döner.

    >>> fibonacci_search([4, 5, 6, 7], 4)
    0
    >>> fibonacci_search([4, 5, 6, 7], -10)
    -1
    >>> fibonacci_search([-18, 2], -18)
    0
    >>> fibonacci_search([5], 5)
    0
    >>> fibonacci_search(['a', 'c', 'd'], 'c')
    1
    >>> fibonacci_search(['a', 'c', 'd'], 'f')
    -1
    >>> fibonacci_search([], 1)
    -1
    >>> fibonacci_search([.1, .4 , 7], .4)
    1
    >>> fibonacci_search([], 9)
    -1
    >>> fibonacci_search(list(range(100)), 63)
    63
    >>> fibonacci_search(list(range(100)), 99)
    99
    >>> fibonacci_search(list(range(-100, 100, 3)), -97)
    1
    >>> fibonacci_search(list(range(-100, 100, 3)), 0)
    -1
    >>> fibonacci_search(list(range(-100, 100, 5)), 0)
    20
    >>> fibonacci_search(list(range(-100, 100, 5)), 95)
    39
    """
    len_list = len(arr)
    # F_m >= n olacak şekilde m'yi bul.
    i = 0
    while True:
        if fibonacci(i) >= len_list:
            fibb_k = i
            break
        i += 1
    offset = 0
    while fibb_k > 0:
        index_k = min(
            offset + fibonacci(fibb_k - 1), len_list - 1
        )  # Dışarı çıkmayı önle
        item_k_1 = arr[index_k]
        if item_k_1 == val:
            return index_k
        elif val < item_k_1:
            fibb_k -= 1
        elif val > item_k_1:
            offset += fibonacci(fibb_k - 1)
            fibb_k -= 2
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
