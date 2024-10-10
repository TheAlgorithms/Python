import re

"""
Organiser: K. Umut Araz

genel bilgi:
https://en.wikipedia.org/wiki/Naming_convention_(programming)#Python_and_Ruby

pascal case [ üst Camel Case ]: https://en.wikipedia.org/wiki/Camel_case

camel case: https://en.wikipedia.org/wiki/Camel_case

kebab case [ genel bilgi içinde bulunabilir ]:
https://en.wikipedia.org/wiki/Naming_convention_(programming)#Python_and_Ruby

snake case: https://en.wikipedia.org/wiki/Snake_case
"""


# yardımcı fonksiyonlar
def split_input(str_: str) -> list:
    """
    >>> split_input("bir iki 31235üçdört")
    [['bir', 'iki', '31235üçdört']]
    """
    return [char.split() for char in re.split(r"[^ a-z A-Z 0-9 \s]", str_)]


def to_simple_case(str_: str) -> str:
    """
    >>> to_simple_case("bir iki 31235üçdört")
    'Birİki31235üçdört'
    >>> to_simple_case("Bu birleştirilmiş olmalı")
    'BuBirleştirilmişOlmalı'
    >>> to_simple_case("İlk harfler büyük, sonra string birleştiriliyor")
    'İlkHarflerBüyükSonraStringBirleştiriliyor'
    >>> to_simple_case("özel karakterler :, ', %, ^, $, göz ardı edilir")
    'ÖzelKarakterlerGözArdıEdilir'
    """
    string_split = split_input(str_)
    return "".join(
        ["".join([char.capitalize() for char in sub_str]) for sub_str in string_split]
    )


def to_complex_case(text: str, upper: bool, separator: str) -> str:
    """
    Sağladığımız ayırıcı ile birleştirilmiş string döner.

    Parametreler:
    @text: Üzerinde işlem yapmak istediğimiz string
    @upper: Büyük harfli sonuç isteyip istemediğimizi belirten boolean değeri
    @separator: Kelimeleri birleştirmek için kullanmak istediğimiz ayırıcı

    Örnekler:
    >>> to_complex_case("bir iki 31235üçdört", True, "_")
    'BİR_İKİ_31235ÜÇDÖRT'
    >>> to_complex_case("bir iki 31235üçdört", False, "-")
    'bir-iki-31235üçdört'
    """
    try:
        string_split = split_input(text)
        if upper:
            res_str = "".join(
                [
                    separator.join([char.upper() for char in sub_str])
                    for sub_str in string_split
                ]
            )
        else:
            res_str = "".join(
                [
                    separator.join([char.lower() for char in sub_str])
                    for sub_str in string_split
                ]
            )
        return res_str
    except IndexError:
        return "geçersiz string"


# ana içerik
def to_pascal_case(text: str) -> str:
    """
    >>> to_pascal_case("bir iki 31235üçdört")
    'Birİki31235üçdört'
    """
    return to_simple_case(text)


def to_camel_case(text: str) -> str:
    """
    >>> to_camel_case("bir iki 31235üçdört")
    'birİki31235üçdört'
    """
    try:
        res_str = to_simple_case(text)
        return res_str[0].lower() + res_str[1:]
    except IndexError:
        return "geçersiz string"


def to_snake_case(text: str, upper: bool) -> str:
    """
    >>> to_snake_case("bir iki 31235üçdört", True)
    'BİR_İKİ_31235ÜÇDÖRT'
    >>> to_snake_case("bir iki 31235üçdört", False)
    'bir_iki_31235üçdört'
    """
    return to_complex_case(text, upper, "_")


def to_kebab_case(text: str, upper: bool) -> str:
    """
    >>> to_kebab_case("bir iki 31235üçdört", True)
    'BİR-İKİ-31235ÜÇDÖRT'
    >>> to_kebab_case("bir iki 31235üçdört", False)
    'bir-iki-31235üçdört'
    """
    return to_complex_case(text, upper, "-")


if __name__ == "__main__":
    __import__("doctest").testmod()
