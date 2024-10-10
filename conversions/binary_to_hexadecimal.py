BITS_TO_HEX = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "a",
    "1011": "b",
    "1100": "c",
    "1101": "d",
    "1110": "e",
    "1111": "f",
}   


def ikili_to_onaltılık(ikili_str: str) -> str:
    """
    Organiser: K. Umut Araz 

    İkili bir dizeyi onaltılık sayıya dönüştürme (Gruplama Yöntemi kullanarak)

    >>> ikili_to_onaltılık('101011111')
    '0x15f'
    >>> ikili_to_onaltılık(' 1010   ')
    '0x0a'
    >>> ikili_to_onaltılık('-11101')
    '-0x1d'
    >>> ikili_to_onaltılık('a')
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz ikili değer fonksiyona gönderildi
    >>> ikili_to_onaltılık('')
    Traceback (most recent call last):
        ...
    ValueError: Boş dize fonksiyona gönderildi
    """
    # Parametreyi temizleme
    ikili_str = str(ikili_str).strip()

    # İstisnalar
    if not ikili_str:
        raise ValueError("Boş dize fonksiyona gönderildi")
    negatif_mi = ikili_str[0] == "-"
    ikili_str = ikili_str[1:] if negatif_mi else ikili_str
    if not all(char in "01" for char in ikili_str):
        raise ValueError("Geçersiz ikili değer fonksiyona gönderildi")

    ikili_str = (
        "0" * (4 * (divmod(len(ikili_str), 4)[0] + 1) - len(ikili_str)) + ikili_str
    )

    onaltılık = []
    for x in range(0, len(ikili_str), 4):
        onaltılık.append(BITS_TO_HEX[ikili_str[x : x + 4]])
    onaltılık_str = "0x" + "".join(onaltılık)

    return "-" + onaltılık_str if negatif_mi else onaltılık_str


if __name__ == "__main__":
    from doctest import testmod

    testmod()
