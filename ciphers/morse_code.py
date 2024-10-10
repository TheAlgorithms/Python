#!/usr/bin/env python3

"""
Morse koduna ve Morse kodundan çeviri yapan Python programı.

https://tr.wikipedia.org/wiki/Morse_kodu

Organiser: K. Umut Araz
"""

# fmt: off
MORSE_KODU_SÖZLÜĞÜ = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}  # Ünlem işareti ITU-R önerisinde yoktur
# fmt: on
TERS_SÖZLÜK = {değer: anahtar for anahtar, değer in MORSE_KODU_SÖZLÜĞÜ.items()}


def şifrele(mesaj: str) -> str:
    """
    >>> şifrele("Sos!")
    '... --- ... -.-.--'
    >>> şifrele("SOS!") == şifrele("sos!")
    True
    """
    return " ".join(MORSE_KODU_SÖZLÜĞÜ[char] for char in mesaj.upper())


def şifre_çöz(mesaj: str) -> str:
    """
    >>> şifre_çöz('... --- ... -.-.--')
    'SOS!'
    """
    return "".join(TERS_SÖZLÜK[char] for char in mesaj.split())


def main() -> None:
    """
    >>> s = "".join(MORSE_KODU_SÖZLÜĞÜ)
    >>> şifre_çöz(şifrele(s)) == s
    True
    """
    mesaj = "Morse kodu burada!"
    print(mesaj)
    mesaj = şifrele(mesaj)
    print(mesaj)
    mesaj = şifre_çöz(mesaj)
    print(mesaj)


if __name__ == "__main__":
    main()
