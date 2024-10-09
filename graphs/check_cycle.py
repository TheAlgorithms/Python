"""
Bir grafikte döngü olup olmadığını kontrol eden program
"""


def döngü_var_mı(graf: dict) -> bool:
    """
    Graf döngüsel ise True, değilse False döner
    >>> döngü_var_mı(graf={0:[], 1:[0, 3], 2:[0, 4], 3:[5], 4:[5], 5:[]})
    False
    >>> döngü_var_mı(graf={0:[1, 2], 1:[2], 2:[0, 3], 3:[3]})
    True
    """
    # Ziyaret edilen düğümleri takip et
    ziyaret_edilen: set[int] = set()
    # Geri kenarı tespit etmek için, şu anda özyineleme yığında olan düğümleri takip et
    yığın: set[int] = set()
    return any(
        düğüm not in ziyaret_edilen and derinlik_oncelikli_arama(graf, düğüm, ziyaret_edilen, yığın)
        for düğüm in graf
    )


def derinlik_oncelikli_arama(graf: dict, düğüm: int, ziyaret_edilen: set, yığın: set) -> bool:
    """
    Tüm komşular için yinele.
    Eğer herhangi bir komşu ziyaret edilmişse ve yığındaysa, graf döngüseldir.
    >>> graf = {0:[], 1:[0, 3], 2:[0, 4], 3:[5], 4:[5], 5:[]}
    >>> düğüm, ziyaret_edilen, yığın = 0, set(), set()
    >>> derinlik_oncelikli_arama(graf, düğüm, ziyaret_edilen, yığın)
    False
    """
    # Mevcut düğümü ziyaret edildi olarak işaretle ve özyineleme yığına ekle
    ziyaret_edilen.add(düğüm)
    yığın.add(düğüm)

    for komsu in graf[düğüm]:
        if komsu not in ziyaret_edilen:
            if derinlik_oncelikli_arama(graf, komsu, ziyaret_edilen, yığın):
                return True
        elif komsu in yığın:
            return True

    # Fonksiyon bitmeden önce düğüm özyineleme yığından çıkarılmalıdır
    yığın.remove(düğüm)
    return False


if __name__ == "__main__":
    from doctest import testmod

    testmod()
