from enum import Enum
from typing import ClassVar, Literal


class SayıSistemi(Enum):
    KISALTILMIŞ = (
        (15, "katrilyon"),
        (12, "trilyon"),
        (9, "milyar"),
        (6, "milyon"),
        (3, "bin"),
        (2, "yüz"),
    )

    UZUN = (
        (15, "bilyon"),
        (9, "milyar"),
        (6, "milyon"),
        (3, "bin"),
        (2, "yüz"),
    )

    HİNDİSTAN = (
        (14, "krorekro"),
        (12, "lakh krore"),
        (7, "krorek"),
        (5, "lakh"),
        (3, "bin"),
        (2, "yüz"),
    )

    @classmethod
    def max_değer(cls, sistem: str) -> int:
        """
        Verilen sayı sisteminin desteklediği maksimum değeri alır.

        >>> SayıSistemi.max_değer("kısaltılmış") == 10**18 - 1
        True
        >>> SayıSistemi.max_değer("uzun") == 10**21 - 1
        True
        >>> SayıSistemi.max_değer("hindistan") == 10**19 - 1
        True
        """
        match sistem_enum := cls[sistem.upper()]:
            case cls.KISALTILMIŞ:
                max_exp = sistem_enum.value[0][0] + 3
            case cls.UZUN:
                max_exp = sistem_enum.value[0][0] + 6
            case cls.HİNDİSTAN:
                max_exp = 19
            case _:
                raise ValueError("Geçersiz sayı sistemi")
        return 10**max_exp - 1


class SayıKelime(Enum):
    BİRİLER: ClassVar[dict[int, str]] = {
        0: "",
        1: "bir",
        2: "iki",
        3: "üç",
        4: "dört",
        5: "beş",
        6: "altı",
        7: "yedi",
        8: "sekiz",
        9: "dokuz",
    }

    ONLAR: ClassVar[dict[int, str]] = {
        0: "on",
        1: "on bir",
        2: "on iki",
        3: "on üç",
        4: "on dört",
        5: "on beş",
        6: "on altı",
        7: "on yedi",
        8: "on sekiz",
        9: "on dokuz",
    }

    ONLUKLAR: ClassVar[dict[int, str]] = {
        2: "yirmi",
        3: "otuz",
        4: "kırk",
        5: "elli",
        6: "altmış",
        7: "yetmiş",
        8: "seksen",
        9: "doksan",
    }


def küçük_sayı_dönüştür(num: int) -> str:
    """
    Küçük, negatif olmayan tam sayıları (yani, 100'den küçük sayılar) kelimelere dönüştürür.

    >>> küçük_sayı_dönüştür(0)
    'sıfır'
    >>> küçük_sayı_dönüştür(5)
    'beş'
    >>> küçük_sayı_dönüştür(10)
    'on'
    >>> küçük_sayı_dönüştür(15)
    'on beş'
    >>> küçük_sayı_dönüştür(20)
    'yirmi'
    >>> küçük_sayı_dönüştür(25)
    'yirmi-beş'
    >>> küçük_sayı_dönüştür(-1)
    Traceback (most recent call last):
    ...
    ValueError: Bu fonksiyon yalnızca negatif olmayan tam sayıları kabul eder
    >>> küçük_sayı_dönüştür(123)
    Traceback (most recent call last):
    ...
    ValueError: Bu fonksiyon yalnızca 100'den küçük sayıları dönüştürür
    """
    if num < 0:
        raise ValueError("Bu fonksiyon yalnızca negatif olmayan tam sayıları kabul eder")
    if num >= 100:
        raise ValueError("Bu fonksiyon yalnızca 100'den küçük sayıları dönüştürür")
    onluklar, biriler = divmod(num, 10)
    if onluklar == 0:
        return SayıKelime.BİRİLER.value[biriler] or "sıfır"
    if onluklar == 1:
        return SayıKelime.ONLAR.value[biriler]
    return (
        SayıKelime.ONLUKLAR.value[onluklar]
        + ("-" if SayıKelime.BİRİLER.value[biriler] else "")
        + SayıKelime.BİRİLER.value[biriler]
    )


def sayıyı_dönüştür(
    num: int, sistem: Literal["kısaltılmış", "uzun", "hindistan"] = "kısaltılmış"
) -> str:
    """
    Bir tam sayıyı Türkçe kelimelere dönüştürür.

    :param num: Dönüştürülecek tam sayı
    :param sistem: Sayı sistemi (kısaltılmış, uzun veya hindistan)

    >>> sayıyı_dönüştür(0)
    'sıfır'
    >>> sayıyı_dönüştür(1)
    'bir'
    >>> sayıyı_dönüştür(100)
    'bir yüz'
    >>> sayıyı_dönüştür(-100)
    'eksi bir yüz'
    >>> sayıyı_dönüştür(123_456_789_012_345) # doctest: +NORMALIZE_WHITESPACE
    'bir yüz yirmi üç trilyon dört yüz elli altı milyar
    yedi yüz seksen dokuz milyon on iki bin üç yüz kırk beş'
    >>> sayıyı_dönüştür(123_456_789_012_345, "uzun") # doctest: +NORMALIZE_WHITESPACE
    'bir yüz yirmi üç bin dört yüz elli altı bilyon
    yedi yüz seksen dokuz milyon on iki bin üç yüz kırk beş'
    >>> sayıyı_dönüştür(12_34_56_78_90_12_345, "hindistan") # doctest: +NORMALIZE_WHITESPACE
    'bir krorekro yirmi üç lakh krore
    kırk beş bin altı yüz yetmiş sekiz krore
    doksan lakh on iki bin üç yüz kırk beş'
    >>> sayıyı_dönüştür(10**18)
    Traceback (most recent call last):
    ...
    ValueError: Girdi sayısı çok büyük
    >>> sayıyı_dönüştür(10**21, "uzun")
    Traceback (most recent call last):
    ...
    ValueError: Girdi sayısı çok büyük
    >>> sayıyı_dönüştür(10**19, "hindistan")
    Traceback (most recent call last):
    ...
    ValueError: Girdi sayısı çok büyük
    """
    kelime_grupları = []

    if num < 0:
        kelime_grupları.append("eksi")
        num *= -1

    if num > SayıSistemi.max_değer(sistem):
        raise ValueError("Girdi sayısı çok büyük")

    SAYILAR: ClassVar[dict[int, str]] = {
        1: "bir",
        2: "iki",
        3: "üç",
        4: "dört",
        5: "beş",
        6: "altı",
        7: "yedi",
        8: "sekiz",
        9: "dokuz",
    }

    TEENS: ClassVar[dict[int, str]] = {
        0: "on",
        1: "on bir",
        2: "on iki",
        3: "thirteen",
        4: "fourteen",
        5: "fifteen",
        6: "sixteen",
        7: "seventeen",
        8: "eighteen",
        9: "nineteen",
    }

    TENS: ClassVar[dict[int, str]] = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }


def convert_small_number(num: int) -> str:
    """
    Converts small, non-negative integers with irregular constructions in English (i.e.,
    numbers under 100) into words.

    >>> convert_small_number(0)
    'zero'
    >>> convert_small_number(5)
    'five'
    >>> convert_small_number(10)
    'ten'
    >>> convert_small_number(15)
    'fifteen'
    >>> convert_small_number(20)
    'twenty'
    >>> convert_small_number(25)
    'twenty-five'
    >>> convert_small_number(-1)
    Traceback (most recent call last):
    ...
    ValueError: This function only accepts non-negative integers
    >>> convert_small_number(123)
    Traceback (most recent call last):
    ...
    ValueError: This function only converts numbers less than 100
    """
    if num < 0:
        raise ValueError("This function only accepts non-negative integers")
    if num >= 100:
        raise ValueError("This function only converts numbers less than 100")
    tens, ones = divmod(num, 10)
    if tens == 0:
        return NumberWords.ONES.value[ones] or "zero"
    if tens == 1:
        return NumberWords.TEENS.value[ones]
    return (
        NumberWords.TENS.value[tens]
        + ("-" if NumberWords.ONES.value[ones] else "")
        + NumberWords.ONES.value[ones]
    )


def convert_number(
    num: int, system: Literal["short", "long", "indian"] = "short"
) -> str:
    """
    Converts an integer to English words.

    :param num: The integer to be converted
    :param system: The numbering system (short, long, or Indian)

    >>> convert_number(0)
    'zero'
    >>> convert_number(1)
    'one'
    >>> convert_number(100)
    'one hundred'
    >>> convert_number(-100)
    'negative one hundred'
    >>> convert_number(123_456_789_012_345) # doctest: +NORMALIZE_WHITESPACE
    'one hundred twenty-three trillion four hundred fifty-six billion
    seven hundred eighty-nine million twelve thousand three hundred forty-five'
    >>> convert_number(123_456_789_012_345, "long") # doctest: +NORMALIZE_WHITESPACE
    'one hundred twenty-three thousand four hundred fifty-six milliard
    seven hundred eighty-nine million twelve thousand three hundred forty-five'
    >>> convert_number(12_34_56_78_90_12_345, "indian") # doctest: +NORMALIZE_WHITESPACE
    'one crore crore twenty-three lakh crore
    forty-five thousand six hundred seventy-eight crore
    ninety lakh twelve thousand three hundred forty-five'
    >>> convert_number(10**18)
    Traceback (most recent call last):
    ...
    ValueError: Input number is too large
    >>> convert_number(10**21, "long")
    Traceback (most recent call last):
    ...
    ValueError: Input number is too large
    >>> convert_number(10**19, "indian")
    Traceback (most recent call last):
    ...
    ValueError: Input number is too large
    """
    word_groups = []

    if num < 0:
        word_groups.append("negative")
        num *= -1

    if num > NumberingSystem.max_value(system):
        raise ValueError("Input number is too large")

    for power, unit in NumberingSystem[system.upper()].value:
        digit_group, num = divmod(num, 10**power)
        if digit_group > 0:
            word_group = (
                convert_number(digit_group, system)
                if digit_group >= 100
                else convert_small_number(digit_group)
            )
            word_groups.append(f"{word_group} {unit}")
    if num > 0 or not word_groups:  # word_groups is only empty if input num was 0
        word_groups.append(convert_small_number(num))
    return " ".join(word_groups)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{convert_number(123456789) = }")
