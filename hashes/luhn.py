"""Luhn Algoritması"""

from __future__ import annotations


def luhn_mu(string: str) -> bool:
    """
    Bir girdi stringi üzerinde Luhn doğrulaması yapar
    Algoritma:
    * Sondan 2. basamaktan başlayarak her ikinci basamağı ikiyle çarp.
    * Sayı 9'dan büyükse 9 çıkar.
    * Sayıları topla
    *
    >>> test_durumlari = (79927398710, 79927398711, 79927398712, 79927398713,
    ...     79927398714, 79927398715, 79927398716, 79927398717, 79927398718,
    ...     79927398719)
    >>> [luhn_mu(str(test_durumu)) for test_durumu in test_durumlari]
    [False, False, False, True, False, False, False, False, False, False]
    """
    kontrol_basamagi: int
    _vektor: list[str] = list(string)
    __vektor, kontrol_basamagi = _vektor[:-1], int(_vektor[-1])
    vektor: list[int] = [int(rakam) for rakam in __vektor]

    vektor.reverse()
    for i, rakam in enumerate(vektor):
        if i % 2 == 0:
            ikiyle_carp: int = rakam * 2
            if ikiyle_carp > 9:
                ikiyle_carp -= 9
            kontrol_basamagi += ikiyle_carp
        else:
            kontrol_basamagi += rakam

    return kontrol_basamagi % 10 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    assert luhn_mu("79927398713")
    assert not luhn_mu("79927398714")
