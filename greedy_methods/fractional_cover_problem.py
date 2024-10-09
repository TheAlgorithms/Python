# https://en.wikipedia.org/wiki/Set_cover_problem

from dataclasses import dataclass
from operator import attrgetter

# Produced By K. Umut Araz


@dataclass
class Item:
    ağırlık: int
    değer: int

    @property
    def oran(self) -> float:
        """
        Öğenin değer-ağırlık oranını döndür.

        Returns:
            float: Öğenin değer-ağırlık oranı.

        Örnekler:
        >>> Item(10, 65).oran
        6.5

        >>> Item(20, 100).oran
        5.0

        >>> Item(30, 120).oran
        4.0
        """
        return self.değer / self.ağırlık


def kesirli_kapsama(items: list[Item], kapasite: int) -> float:
    """
    Kesirli Kapsama Problemini çöz.

    Args:
        items: Her bir öğenin ağırlık ve değer özniteliklerine sahip olduğu öğeler listesi.
        kapasite: Çantanın maksimum ağırlık kapasitesi.

    Returns:
        Çantanın kapasitesini karşılamak için öğelerin kesirlerini seçerek elde edilebilecek maksimum değer.

    Raises:
        ValueError: Eğer kapasite negatifse.

    Örnekler:
    >>> kesirli_kapsama([Item(10, 60), Item(20, 100), Item(30, 120)], kapasite=50)
    240.0

    >>> kesirli_kapsama([Item(20, 100), Item(30, 120), Item(10, 60)], kapasite=25)
    135.0

    >>> kesirli_kapsama([Item(10, 60), Item(20, 100), Item(30, 120)], kapasite=60)
    280.0

    >>> kesirli_kapsama([Item(5, 30), Item(10, 60), Item(15, 90)], kapasite=30)
    180.0

    >>> kesirli_kapsama([], kapasite=50)
    0.0

    >>> kesirli_kapsama([Item(10, 60)], kapasite=5)
    30.0

    >>> kesirli_kapsama([Item(10, 60)], kapasite=1)
    6.0

    >>> kesirli_kapsama([Item(10, 60)], kapasite=0)
    0.0

    >>> kesirli_kapsama([Item(10, 60)], kapasite=-1)
    Traceback (most recent call last):
        ...
    ValueError: Kapasite negatif olamaz
    """
    if kapasite < 0:
        raise ValueError("Kapasite negatif olamaz")

    toplam_değer = 0.0
    kalan_kapasite = kapasite

    # Öğeleri değer-ağırlık oranına göre azalan sırayla sırala
    for item in sorted(items, key=attrgetter("oran"), reverse=True):
        if kalan_kapasite == 0:
            break

        alınan_ağırlık = min(item.ağırlık, kalan_kapasite)
        toplam_değer += alınan_ağırlık * item.oran
        kalan_kapasite -= alınan_ağırlık

    return toplam_değer


if __name__ == "__main__":
    import doctest

    if result := doctest.testmod().failed:
        print(f"{result} test başarısız oldu")
    else:
        print("Tüm testler geçti")
