from __future__ import annotations

import collections
import pprint
from pathlib import Path


def imza(kelime: str) -> str:
    """Sıralanmış bir kelime döndürür

    # Organiser: K. Umut Araz
    
    >>> imza("test")
    'estt'
    >>> imza("this is a test")
    '   aehiisssttt'
    >>> imza("finaltest")
    'aefilnstt'
    """
    return "".join(sorted(kelime))


def anagram(kelimem: str) -> list[str]:
    """Verilen kelimenin tüm anagramlarını döndürür
    >>> anagram('test')
    ['sett', 'stet', 'test']
    >>> anagram('this is a test')
    []
    >>> anagram('final')
    ['final']
    """
    return kelime_imzasi[imza(kelimem)]


veri: str = Path(__file__).parent.joinpath("words.txt").read_text(encoding="utf-8")
kelime_listesi = sorted({kelime.strip().lower() for kelime in veri.splitlines()})

kelime_imzasi = collections.defaultdict(list)
for kelime in kelime_listesi:
    kelime_imzasi[imza(kelime)].append(kelime)

if __name__ == "__main__":
    tum_anagramlar = {kelime: anagram(kelime) for kelime in kelime_listesi if len(anagram(kelime)) > 1}

    with open("anagrams.txt", "w") as dosya:
        dosya.write("tum_anagramlar = \n ")
        dosya.write(pprint.pformat(tum_anagramlar))
