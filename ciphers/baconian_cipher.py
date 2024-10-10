"""
Baconian şifreleme ve çözme programı
Vikipedi referansı: https://tr.wikipedia.org/wiki/Bacon%27s_cipher

Organiser: K. Umut Araz
"""

şifreleme_sözlüğü = {
    "a": "AAAAA",
    "b": "AAAAB",
    "c": "AAABA",
    "d": "AAABB",
    "e": "AABAA",
    "f": "AABAB",
    "g": "AABBA",
    "h": "AABBB",
    "i": "ABAAA",
    "j": "BBBAA",
    "k": "ABAAB",
    "l": "ABABA",
    "m": "ABABB",
    "n": "ABBAA",
    "o": "ABBAB",
    "p": "ABBBA",
    "q": "ABBBB",
    "r": "BAAAA",
    "s": "BAAAB",
    "t": "BAABA",
    "u": "BAABB",
    "v": "BBBAB",
    "w": "BABAA",
    "x": "BABAB",
    "y": "BABBA",
    "z": "BABBB",
    " ": " ",
}

çözme_sözlüğü = {değer: anahtar for anahtar, değer in şifreleme_sözlüğü.items()}

def şifrele(kelime: str) -> str:
    """
    Baconian şifrelemesine çevirir.

    >>> şifrele("merhaba")
    'AABBBAABAAABABAABABAABBAB'
    >>> şifrele("merhaba dünya")
    'AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB'
    >>> şifrele("merhaba dünya!")
    Traceback (most recent call last):
        ...
    Exception: şifrele() yalnızca alfabedeki harfleri ve boşlukları kabul eder
    """
    şifrelenmiş = ""
    for harf in kelime.lower():
        if harf.isalpha() or harf == " ":
            şifrelenmiş += şifreleme_sözlüğü[harf]
        else:
            raise Exception("şifrele() yalnızca alfabedeki harfleri ve boşlukları kabul eder")
    return şifrelenmiş

def çöz(coded: str) -> str:
    """
    Baconian şifresinden çözer.

    >>> çöz("AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB")
    'merhaba dünya'
    >>> çöz("AABBBAABAAABABAABABAABBAB")
    'merhaba'
    >>> çöz("AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB!")
    Traceback (most recent call last):
        ...
    Exception: çöz() yalnızca 'A', 'B' ve boşlukları kabul eder
    """
    if set(coded) - {"A", "B", " "} != set():
        raise Exception("çöz() yalnızca 'A', 'B' ve boşlukları kabul eder")
    çözülen = ""
    for kelime in coded.split():
        while len(kelime) != 0:
            çözülen += çözme_sözlüğü[kelime[:5]]
            kelime = kelime[5:]
        çözülen += " "
    return çözülen.strip()

if __name__ == "__main__":
    from doctest import testmod

    testmod()
