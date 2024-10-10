"""
Verilen kelime listesinden en sık geçen K kelimeyi bulur.

Organiser: K. Umut Araz

Bu uygulama, bu repository'de mevcut olan Heap sınıfını kullanarak problemi nasıl çözeceğimizi göstermeyi amaçlamaktadır.
Sıralama istatistiklerini hesaplamak, aslında, yığınların tipik bir kullanım şeklidir.

Bu, esasen eğitim amaçlı gösterilmektedir, çünkü problem Python standart kütüphanesindeki collections.Counter kullanılarak birkaç satırda çözülebilir:

from collections import Counter
def en_sik_gecen_kelime(words, k_degeri):
    return [x[0] for x in Counter(words).most_common(k_degeri)]
"""

from collections import Counter
from functools import total_ordering

from data_structures.heap.heap import Heap


@total_ordering
class KelimeSayisi:
    def __init__(self, kelime: str, sayi: int) -> None:
        self.kelime = kelime
        self.sayi = sayi

    def __eq__(self, other: object) -> bool:
        """
        >>> KelimeSayisi('a', 1).__eq__(KelimeSayisi('b', 1))
        True
        >>> KelimeSayisi('a', 1).__eq__(KelimeSayisi('a', 1))
        True
        >>> KelimeSayisi('a', 1).__eq__(KelimeSayisi('a', 2))
        False
        >>> KelimeSayisi('a', 1).__eq__(KelimeSayisi('b', 2))
        False
        >>> KelimeSayisi('a', 1).__eq__(1)
        NotImplemented
        """
        if not isinstance(other, KelimeSayisi):
            return NotImplemented
        return self.sayi == other.sayi

    def __lt__(self, other: object) -> bool:
        """
        >>> KelimeSayisi('a', 1).__lt__(KelimeSayisi('b', 1))
        False
        >>> KelimeSayisi('a', 1).__lt__(KelimeSayisi('a', 1))
        False
        >>> KelimeSayisi('a', 1).__lt__(KelimeSayisi('a', 2))
        True
        >>> KelimeSayisi('a', 1).__lt__(KelimeSayisi('b', 2))
        True
        >>> KelimeSayisi('a', 2).__lt__(KelimeSayisi('a', 1))
        False
        >>> KelimeSayisi('a', 2).__lt__(KelimeSayisi('b', 1))
        False
        >>> KelimeSayisi('a', 1).__lt__(1)
        NotImplemented
        """
        if not isinstance(other, KelimeSayisi):
            return NotImplemented
        return self.sayi < other.sayi


def en_sik_gecen_kelimeler(kelimeler: list[str], k_degeri: int) -> list[str]:
    """
    En sık geçen `k_degeri` kadar kelimeyi döndürür,
    oluş sırasına göre azalan sırada.
    Bu bağlamda, bir kelime, sağlanan listede bir eleman olarak tanımlanır.

    Eğer `k_degeri`, farklı kelimelerin sayısından büyükse, k değeri olarak
    farklı kelimelerin sayısına eşit bir değer dikkate alınacaktır.

    >>> en_sik_gecen_kelimeler(['a', 'b', 'c', 'a', 'c', 'c'], 3)
    ['c', 'a', 'b']
    >>> en_sik_gecen_kelimeler(['a', 'b', 'c', 'a', 'c', 'c'], 2)
    ['c', 'a']
    >>> en_sik_gecen_kelimeler(['a', 'b', 'c', 'a', 'c', 'c'], 1)
    ['c']
    >>> en_sik_gecen_kelimeler(['a', 'b', 'c', 'a', 'c', 'c'], 0)
    []
    >>> en_sik_gecen_kelimeler([], 1)
    []
    >>> en_sik_gecen_kelimeler(['a', 'a'], 2)
    ['a']
    """
    yigin: Heap[KelimeSayisi] = Heap()
    kelime_sayilari = Counter(kelimeler)
    yigin.build_max_heap(
        [KelimeSayisi(kelime, sayi) for kelime, sayi in kelime_sayilari.items()]
    )
    return [yigin.extract_max().kelime for _ in range(min(k_degeri, len(kelime_sayilari)))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
