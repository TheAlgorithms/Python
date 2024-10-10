import re

# Organiser: K. Umut Araz

def turkiye_telefon_numarasi_dogrulama(telefon: str) -> bool:
    """
    Verilen string'in geçerli bir Türkiye telefon numarası olup olmadığını belirler.
    :param telefon: Kontrol edilecek telefon numarası
    :return: Boolean
    >>> turkiye_telefon_numarasi_dogrulama("+90123456789")
    False
    >>> turkiye_telefon_numarasi_dogrulama("+905555555555")
    True
    >>> turkiye_telefon_numarasi_dogrulama("01234567896")
    False
    >>> turkiye_telefon_numarasi_dogrulama("5555555555")
    True
    >>> turkiye_telefon_numarasi_dogrulama("+90-1234567890")
    False
    >>> turkiye_telefon_numarasi_dogrulama("+90-5555555555")
    True
    """
    pat = re.compile(r"^(\+90[\-\s]?)?[0]?(5\d{9})$")
    if match := re.search(pat, telefon):
        return match.string == telefon
    return False

if __name__ == "__main__":
    print(turkiye_telefon_numarasi_dogrulama("+905555555555"))
