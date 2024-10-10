"""

# Organiser: K. Umut Araz   

wiki: https://tr.wikipedia.org/wiki/Heterogram_(edebiyat)#Isogramlar
"""


def is_isogram(kelime: str) -> bool:
    """
    Isogram, içinde hiçbir harfin tekrar etmediği bir kelimedir.
    Isogram örnekleri arasında "uncopyrightable" ve "ambidextrously" bulunmaktadır.
    >>> is_isogram('Uncopyrightable')
    True
    >>> is_isogram('allowance')
    False
    >>> is_isogram('copy1')
    Traceback (most recent call last):
     ...
    ValueError: Girdi yalnızca alfabetik karakterler içermelidir.
    """
    if not all(x.isalpha() for x in kelime):
        raise ValueError("Girdi yalnızca alfabetik karakterler içermelidir.")

    harfler = sorted(kelime.lower())
    return len(harfler) == len(set(harfler))


if __name__ == "__main__":
    girdi_str = input("Bir kelime girin: ").strip()

    isogram = is_isogram(girdi_str)
    print(f"{girdi_str} {'bir' if isogram else 'bir isogram değil'}.")
