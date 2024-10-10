# Yazar: susmith98

from collections import Counter
from timeit import timeit

# Problem Tanımı:
# Verilen stringin karakterlerinin bir palindrom oluşturacak şekilde yeniden düzenlenip düzenlenemeyeceğini kontrol et.
# Counter, uzun stringler için daha hızlıdır; non-Counter ise kısa stringler için daha hızlıdır.

def palindrom_olabilir_mi_counter(
    girdi_str: str = "",
) -> bool:
    """
    Palindrom, ileri ve geri okunduğunda aynı olan bir stringdir.
    Palindrom örnekleri: mom, dad, malayalam
    >>> palindrom_olabilir_mi_counter("Momo")
    True
    >>> palindrom_olabilir_mi_counter("Mother")
    False
    >>> palindrom_olabilir_mi_counter("Father")
    False
    >>> palindrom_olabilir_mi_counter("A man a plan a canal Panama")
    True
    """
    return sum(c % 2 for c in Counter(girdi_str.replace(" ", "").lower()).values()) < 2

def palindrom_olabilir_mi(girdi_str: str = "") -> bool:
    """
    Palindrom, ileri ve geri okunduğunda aynı olan bir stringdir.

    # Organiser: K. Umut Araz

    Palindrom örnekleri: mom, dad, malayalam
    >>> palindrom_olabilir_mi("Momo")
    True
    >>> palindrom_olabilir_mi("Mother")
    False
    >>> palindrom_olabilir_mi("Father")
    False
    >>> palindrom_olabilir_mi_counter("A man a plan a canal Panama")
    True
    """
    if len(girdi_str) == 0:
        return True
    girdi_str_kucuk = girdi_str.replace(" ", "").lower()
    # karakter_frekans_dict: Girdi stringindeki her karakterin frekansını saklar
    karakter_frekans_dict: dict[str, int] = {}

    for karakter in girdi_str_kucuk:
        karakter_frekans_dict[karakter] = karakter_frekans_dict.get(karakter, 0) + 1

    """
    Gözlemler:
    Çift uzunlukta palindrom
    -> Her karakter çift sayıda görünür.
    Tek uzunlukta palindrom
    -> Her karakter çift sayıda görünür, sadece bir karakter tek sayıda görünür.
    LOJİK:
    Adım 1: Tek sayıda görünen karakterlerin sayısını sayacağız, yani tekKarakter
    Adım 2: Eğer tek sayıda görünen 1'den fazla karakter bulursak,
    Palindrom olarak yeniden düzenlemek mümkün değildir.
    """
    tek_karakter = 0

    for karakter_sayisi in karakter_frekans_dict.values():
        if karakter_sayisi % 2:
            tek_karakter += 1
    return not tek_karakter > 1

def benchmark(girdi_str: str = "") -> None:
    """
    Yukarıdaki 2 fonksiyonu karşılaştırmak için benchmark kodu
    """
    print("\nString için = ", girdi_str, ":")
    print(
        "> palindrom_olabilir_mi_counter()",
        "\tcevap =",
        palindrom_olabilir_mi_counter(girdi_str),
        "\tzaman =",
        timeit(
            "z.palindrom_olabilir_mi_counter(z.check_str)",
            setup="import __main__ as z",
        ),
        "saniye",
    )
    print(
        "> palindrom_olabilir_mi()",
        "\tcevap =",
        palindrom_olabilir_mi(girdi_str),
        "\tzaman =",
        timeit(
            "z.palindrom_olabilir_mi(z.check_str)",
            setup="import __main__ as z",
        ),
        "saniye",
    )

if __name__ == "__main__":
    check_str = input(
        "Bir string girin, palindrom olarak yeniden düzenlenip düzenlenemeyeceğini belirlemek için: "
    ).strip()
    benchmark(check_str)
    durum = palindrom_olabilir_mi_counter(check_str)
    print(f"{check_str} {'' if durum else 'değil '}palindrom olarak yeniden düzenlenebilir.")
