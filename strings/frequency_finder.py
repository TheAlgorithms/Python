# Harf Sıklığı Bulucu

# Organiser: K. Umut Araz

import string

# sıklık bilgisi https://en.wikipedia.org/wiki/Letter_frequency adresinden alınmıştır
ingilizce_harf_sikliklari = {
    "E": 12.70,
    "T": 9.06,
    "A": 8.17,
    "O": 7.51,
    "I": 6.97,
    "N": 6.75,
    "S": 6.33,
    "H": 6.09,
    "R": 5.99,
    "D": 4.25,
    "L": 4.03,
    "C": 2.78,
    "U": 2.76,
    "M": 2.41,
    "W": 2.36,
    "F": 2.23,
    "G": 2.02,
    "Y": 1.97,
    "P": 1.93,
    "B": 1.29,
    "V": 0.98,
    "K": 0.77,
    "J": 0.15,
    "X": 0.15,
    "Q": 0.10,
    "Z": 0.07,
}
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
HARFLER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def harf_sayisi_bul(mesaj: str) -> dict[str, int]:
    harf_sayisi = {harf: 0 for harf in string.ascii_uppercase}
    for harf in mesaj.upper():
        if harf in HARFLER:
            harf_sayisi[harf] += 1

    return harf_sayisi


def indeks_sifir_ogesini_al(x: tuple) -> str:
    return x[0]


def harf_siklik_sirasi_bul(mesaj: str) -> str:
    """
    Verilen stringdeki harflerin sıklık sırasını alır
    >>> harf_siklik_sirasi_bul('Merhaba Dünya')
    'MRBAHDUYENLGCİFOSKQTJXWZ'
    >>> harf_siklik_sirasi_bul('Merhaba@')
    'MRBAHDUYENLGCİFOSKQTJXWZ'
    >>> harf_siklik_sirasi_bul('h')
    'HZQXJKVBPYGFWMUCLDRSNIOATE'
    """
    harf_sayisi = harf_sayisi_bul(mesaj)
    siklik_harf: dict[int, list[str]] = {
        siklik: [] for harf, siklik in harf_sayisi.items()
    }
    for harf in HARFLER:
        siklik_harf[harf_sayisi[harf]].append(harf)

    siklik_harf_str: dict[int, str] = {}

    for siklik in siklik_harf:
        siklik_harf[siklik].sort(key=ETAOIN.find, reverse=True)
        siklik_harf_str[siklik] = "".join(siklik_harf[siklik])

    siklik_pareleri = list(siklik_harf_str.items())
    siklik_pareleri.sort(key=indeks_sifir_ogesini_al, reverse=True)

    siklik_sirasi: list[str] = [siklik_pare[1] for siklik_pare in siklik_pareleri]

    return "".join(siklik_sirasi)


def ingilizce_siklik_eslesme_puani(mesaj: str) -> int:
    """
    >>> ingilizce_siklik_eslesme_puani('Merhaba Dünya')
    1
    """
    siklik_sirasi = harf_siklik_sirasi_bul(mesaj)
    eslesme_puani = 0
    for yaygin_harf in ETAOIN[:6]:
        if yaygin_harf in siklik_sirasi[:6]:
            eslesme_puani += 1

    for yaygin_olmayan_harf in ETAOIN[-6:]:
        if yaygin_olmayan_harf in siklik_sirasi[-6:]:
            eslesme_puani += 1

    return eslesme_puani


if __name__ == "__main__":
    import doctest

    doctest.testmod()
