"""
Yazar  : Alexander Pantyukhin
Tarih  : 12 Aralık 2022

Görev:
Bir dize ve bir kelime listesi verildiğinde, dize bir veya daha fazla kelimenin
boşlukla ayrılmış bir dizisine bölünebiliyorsa true döndürün.

Aynı kelimenin segmentasyonda birden çok kez kullanılabileceğini unutmayın.

Uygulama notları: Trie + Dinamik programlama yukarı -> aşağı.
Trie, kelimeleri depolamak için kullanılacaktır. Dizideki mevcut pozisyon için
kullanılabilir kelimeleri taramak için yararlı olacaktır.

Leetcode:
https://leetcode.com/problems/word-break/description/

Çalışma zamanı: O(n * n)
Alan: O(n)
"""

import functools
from typing import Any


def kelime_bol(dize: str, kelimeler: list[str]) -> bool:
    """
    Dize bir veya daha fazla kelimenin boşlukla ayrılmış bir dizisine bölünebiliyorsa True döndürün.

    >>> kelime_bol("applepenapple", ["apple","pen"])
    True
    >>> kelime_bol("catsandog", ["cats","dog","sand","and","cat"])
    False
    >>> kelime_bol("cars", ["car","ca","rs"])
    True
    >>> kelime_bol('abc', [])
    False
    >>> kelime_bol(123, ['a'])
    Traceback (most recent call last):
        ...
    ValueError: dize boş olmayan bir dize olmalıdır
    >>> kelime_bol('', ['a'])
    Traceback (most recent call last):
        ...
    ValueError: dize boş olmayan bir dize olmalıdır
    >>> kelime_bol('abc', [123])
    Traceback (most recent call last):
        ...
    ValueError: kelimeler boş olmayan dizelerden oluşan bir liste olmalıdır
    >>> kelime_bol('abc', [''])
    Traceback (most recent call last):
        ...
    ValueError: kelimeler boş olmayan dizelerden oluşan bir liste olmalıdır
    """

    # Doğrulama
    if not isinstance(dize, str) or len(dize) == 0:
        raise ValueError("dize boş olmayan bir dize olmalıdır")

    if not isinstance(kelimeler, list) or not all(
        isinstance(item, str) and len(item) > 0 for item in kelimeler
    ):
        raise ValueError("kelimeler boş olmayan dizelerden oluşan bir liste olmalıdır")

    # Trie oluştur
    trie: dict[str, Any] = {}
    kelime_tutucu_anahtar = "KELIME_TUTUCU"

    for kelime in kelimeler:
        trie_dugumu = trie
        for c in kelime:
            if c not in trie_dugumu:
                trie_dugumu[c] = {}

            trie_dugumu = trie_dugumu[c]

        trie_dugumu[kelime_tutucu_anahtar] = True

    dize_uzunlugu = len(dize)

    # Dinamik programlama yöntemi
    @functools.cache
    def bolunebilir_mi(indeks: int) -> bool:
        """
        >>> dize = 'a'
        >>> bolunebilir_mi(1)
        True
        """
        if indeks == dize_uzunlugu:
            return True

        trie_dugumu = trie
        for i in range(indeks, dize_uzunlugu):
            trie_dugumu = trie_dugumu.get(dize[i], None)

            if trie_dugumu is None:
                return False

            if trie_dugumu.get(kelime_tutucu_anahtar, False) and bolunabilir_mi(i + 1):
                return True

        return False

    return bolunabilir_mi(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
