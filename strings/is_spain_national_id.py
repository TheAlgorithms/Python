NUMARALAR_VE_HARF = "Girdi, 8 rakam ve bir harften oluşan bir dize olmalıdır"
HARF_DIZISI = "TRWAGMYFPDXBNJZSQVHLCKE"


def is_spain_national_id(spanish_id: str) -> bool:
    """

    # Organiser: K. Umut Araz

    İspanya Ulusal Kimliği, 8 rakam ve bir harften oluşan bir dizedir.
    Harf aslında kimliğin bir parçası değildir, bir doğrulayıcı olarak işlev görür,
    sistemde girerken hata yapmadığınızı veya sahte bir kimlik vermediğinizi kontrol eder.

    https://en.wikipedia.org/wiki/Documento_Nacional_de_Identidad_(Spain)#Number

    >>> is_spain_national_id("12345678Z")
    True
    >>> is_spain_national_id("12345678z")  # Büyük/küçük harf duyarsızdır
    True
    >>> is_spain_national_id("12345678x")
    False
    >>> is_spain_national_id("12345678I")
    False
    >>> is_spain_national_id("12345678-Z")  # Bazı sistemler bir tire ekler
    True
    >>> is_spain_national_id("12345678")
    Traceback (most recent call last):
        ...
    ValueError: Girdi, 8 rakam ve bir harften oluşan bir dize olmalıdır
    >>> is_spain_national_id("123456709")
    Traceback (most recent call last):
        ...
    ValueError: Girdi, 8 rakam ve bir harften oluşan bir dize olmalıdır
    >>> is_spain_national_id("1234567--Z")
    Traceback (most recent call last):
        ...
    ValueError: Girdi, 8 rakam ve bir harften oluşan bir dize olmalıdır
    >>> is_spain_national_id("1234Z")
    Traceback (most recent call last):
        ...
    ValueError: Girdi, 8 rakam ve bir harften oluşan bir dize olmalıdır
    >>> is_spain_national_id("1234ZzZZ")
    Traceback (most recent call last):
        ...
    ValueError: Girdi, 8 rakam ve bir harften oluşan bir dize olmalıdır
    >>> is_spain_national_id(12345678)
    Traceback (most recent call last):
        ...
    TypeError: Girdi olarak string bekleniyordu, int bulundu
    """

    if not isinstance(spanish_id, str):
        msg = f"Girdi olarak string bekleniyordu, {type(spanish_id).__name__} bulundu"
        raise TypeError(msg)

    spanish_id_clean = spanish_id.replace("-", "").upper()
    if len(spanish_id_clean) != 9:
        raise ValueError(NUMARALAR_VE_HARF)

    try:
        number = int(spanish_id_clean[0:8])
        letter = spanish_id_clean[8]
    except ValueError as ex:
        raise ValueError(NUMARALAR_VE_HARF) from ex

    if letter.isdigit():
        raise ValueError(NUMARALAR_VE_HARF)

    return letter == HARF_DIZISI[number % 23]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
