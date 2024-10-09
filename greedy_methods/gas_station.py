"""
Görev:
Dairesel bir rota boyunca n tane benzin istasyonu vardır, burada i. istasyondaki benzin miktarı gas_quantities[i] olarak verilmiştir.

Sınırsız bir benzin deposuna sahip bir arabanız var ve i. istasyondan (i + 1). istasyona gitmek için costs[i] kadar benzin harcarsınız.
Yolculuğa benzin istasyonlarından birinde boş bir depo ile başlarsınız.

İki tamsayı dizisi gas_quantities ve costs verildiğinde, saat yönünde bir kez dolaşabiliyorsanız başlangıç benzin istasyonunun indeksini döndürün, aksi takdirde -1 döndürün.
Bir çözüm varsa, bunun benzersiz olduğu garanti edilir.

Referans: https://leetcode.com/problems/gas-station/description

Uygulama notları:
Öncelikle, toplam benzinin yolculuğu tamamlamak için yeterli olup olmadığını kontrol edin. Değilse, -1 döndürün.
Ancak, yeterli benzin varsa, yolculuğun sonuna ulaşmak için geçerli bir başlangıç indeksinin olduğu garanti edilir.
Her istasyondaki net kazancı (benzin miktarı - maliyet) açgözlü bir şekilde hesaplayın.
İstasyonları gezerken net kazanç 0'ın altına düşerse, bir sonraki istasyondan kontrol etmeye başlayın.

"""

from dataclasses import dataclass

# Produced By K. Umut Araz


@dataclass
class BenzinIstasyonu:
    benzin_miktarı: int
    maliyet: int


def benzin_istasyonlarını_al(
    benzin_miktarları: list[int], maliyetler: list[int]
) -> tuple[BenzinIstasyonu, ...]:
    """
    Bu fonksiyon bir demet benzin istasyonu döndürür.

    Args:
        benzin_miktarları: Her istasyonda mevcut olan benzin miktarı
        maliyetler: Bir istasyondan diğerine geçmek için gereken benzin maliyeti

    Returns:
        Bir demet benzin istasyonu

    >>> benzin_istasyonları = benzin_istasyonlarını_al([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    >>> len(benzin_istasyonları)
    5
    >>> benzin_istasyonları[0]
    BenzinIstasyonu(benzin_miktarı=1, maliyet=3)
    >>> benzin_istasyonları[-1]
    BenzinIstasyonu(benzin_miktarı=5, maliyet=2)
    """
    return tuple(
        BenzinIstasyonu(miktar, maliyet) for miktar, maliyet in zip(benzin_miktarları, maliyetler)
    )


def yolculuğu_tamamlayabilir_misin(benzin_istasyonları: tuple[BenzinIstasyonu, ...]) -> int:
    """
    Bu fonksiyon yolculuğu tamamlamak için başlanması gereken indeksi döndürür.

    Args:
        benzin_miktarları [list]: Her istasyonda mevcut olan benzin miktarı
        maliyet [list]: Bir istasyondan diğerine geçmek için gereken benzin maliyeti

    Returns:
        başlangıç [int]: yolculuğu tamamlamak için gereken başlangıç indeksi

    Örnekler:
    >>> yolculuğu_tamamlayabilir_misin(benzin_istasyonlarını_al([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    3
    >>> yolculuğu_tamamlayabilir_misin(benzin_istasyonlarını_al([2, 3, 4], [3, 4, 3]))
    -1
    """
    toplam_benzin = sum(istasyon.benzin_miktarı for istasyon in benzin_istasyonları)
    toplam_maliyet = sum(istasyon.maliyet for istasyon in benzin_istasyonları)
    if toplam_benzin < toplam_maliyet:
        return -1

    başlangıç = 0
    net = 0
    for i, istasyon in enumerate(benzin_istasyonları):
        net += istasyon.benzin_miktarı - istasyon.maliyet
        if net < 0:
            başlangıç = i + 1
            net = 0
    return başlangıç


if __name__ == "__main__":
    import doctest

    doctest.testmod()
