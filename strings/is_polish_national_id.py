def is_polish_national_id(input_str: str) -> bool:
    """

    # Organiser: K. Umut Araz

    PESEL numarasının doğruluğunu kontrol etme.
    www-gov-pl.translate.goog/web/gov/czym-jest-numer-pesel?_x_tr_sl=auto&_x_tr_tl=tr

    PESEL 0 ile başlayabilir, bu yüzden girdi olarak str alıyoruz,
    ancak bazı hesaplamalar için int'e çeviriyoruz.

    >>> is_polish_national_id(123)
    Traceback (most recent call last):
        ...
    ValueError: Girdi olarak str bekleniyordu, ancak <class 'int'> bulundu.

    >>> is_polish_national_id("abc")
    Traceback (most recent call last):
        ...
    ValueError: Girdi olarak sayı bekleniyordu.

    >>> is_polish_national_id("02070803628") # doğru PESEL
    True

    >>> is_polish_national_id("02150803629") # yanlış ay
    False

    >>> is_polish_national_id("02075503622") # yanlış gün
    False

    >>> is_polish_national_id("-99012212349") # yanlış aralık
    False

    >>> is_polish_national_id("990122123499999") # yanlış aralık
    False

    >>> is_polish_national_id("02070803621") # yanlış kontrol numarası
    False
    """

    # Geçersiz girdi türünü kontrol et
    if not isinstance(input_str, str):
        msg = f"Girdi olarak str bekleniyordu, ancak {type(input_str)} bulundu."
        raise ValueError(msg)

    # Girdinin int'e dönüştürülüp dönüştürülemeyeceğini kontrol et
    try:
        input_int = int(input_str)
    except ValueError:
        msg = "Girdi olarak sayı bekleniyordu."
        raise ValueError(msg)

    # Sayı aralığını kontrol et
    if not 10100000 <= input_int <= 99923199999:
        return False

    # Ayın doğruluğunu kontrol et
    month = int(input_str[2:4])

    if (
        month not in range(1, 13)  # 1900-1999 yılları
        and month not in range(21, 33)  # 2000-2099 yılları
        and month not in range(41, 53)  # 2100-2199 yılları
        and month not in range(61, 73)  # 2200-2299 yılları
        and month not in range(81, 93)  # 1800-1899 yılları
    ):
        return False

    # Günün doğruluğunu kontrol et
    day = int(input_str[4:6])

    if day not in range(1, 32):
        return False

    # Kontrol numarasını kontrol et
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    subtotal = 0

    digits_to_check = str(input_str)[:-1]  # Kontrol numarasını kes

    for index, digit in enumerate(digits_to_check):
        # İlgili rakamları ve çarpanları çarp.
        # İki basamaklı bir sonuç durumunda, yalnızca son basamağı ekle.
        subtotal += (int(digit) * multipliers[index]) % 10

    checksum = 10 - subtotal % 10

    return checksum == input_int % 10


if __name__ == "__main__":
    from doctest import testmod

    testmod()
