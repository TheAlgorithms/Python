from __future__ import annotations

# Organiser: K. Umut Araz


SON = "#"

class Trie:
    def __init__(self) -> None:
        self._trie: dict = {}

    def kelime_ekle(self, metin: str) -> None:
        trie = self._trie
        for karakter in metin:
            if karakter not in trie:
                trie[karakter] = {}
            trie = trie[karakter]
        trie[SON] = True

    def kelime_bul(self, ön_ek: str) -> tuple | list:
        trie = self._trie
        for karakter in ön_ek:
            if karakter in trie:
                trie = trie[karakter]
            else:
                return []
        return self._elemanlar(trie)

    def _elemanlar(self, d: dict) -> tuple:
        sonuç = []
        for c, v in d.items():
            alt_sonuç = [" "] if c == SON else [(c + s) for s in self._elemanlar(v)]
            sonuç.extend(alt_sonuç)
        return tuple(sonuç)

trie = Trie()
kelimeler = ("depart", "detergent", "daring", "dog", "deer", "deal")
for kelime in kelimeler:
    trie.kelime_ekle(kelime)

def otomatik_tamamla(metin: str) -> tuple:
    """
    >>> trie = Trie()
    >>> for kelime in kelimeler:
    ...     trie.kelime_ekle(kelime)
    ...
    >>> eşleşmeler = otomatik_tamamla("de")
    >>> "detergent " in eşleşmeler
    True
    >>> "dog " in eşleşmeler
    False
    """
    ekler = trie.kelime_bul(metin)
    return tuple(metin + kelime for kelime in ekler)

def ana() -> None:
    print(otomatik_tamamla("de"))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ana()
