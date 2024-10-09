"""
Apriori Algoritması, pazar sepeti analizi olarak da bilinen bir Birliktelik kuralı madenciliği tekniğidir ve
bir işlem veya ilişkisel veritabanındaki bir dizi öğe arasında ilginç ilişkiler veya birliktelikler keşfetmeyi amaçlar.

Örneğin, Apriori Algoritması şunu belirtir: "Bir müşteri A ve B ürünlerini satın alırsa, muhtemelen C ürününü de satın alır."
Bu kural, A, B ve C ürünleri arasında bir ilişki önerir ve A ve B'yi satın alan müşterilerin C ürününü de satın alma olasılığının yüksek olduğunu gösterir.

WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm
Örnekler: https://www.kaggle.com/code/earthian/apriori-association-rules-mining
"""

from itertools import combinations
from typing import List, Tuple


def veri_yukle() -> List[List[str]]:
    """
    Örnek bir işlem veri seti döndürür.

    >>> veri_yukle()
    [['süt'], ['süt', 'tereyağı'], ['süt', 'ekmek'], ['süt', 'ekmek', 'cips']]
    """
    return [["süt"], ["süt", "tereyağı"], ["süt", "ekmek"], ["süt", "ekmek", "cips"]]


def budama(oge_kumesi: List[str], adaylar: List[List[str]], uzunluk: int) -> List[List[str]]:
    """
    Sık olmayan aday öğe kümelerini budar.
    Budamanın amacı, sık olmayan aday öğe kümelerini filtrelemektir. Bu, bir aday öğe kümesinin tüm (k-1) alt kümelerinin
    önceki iterasyonun sık öğe kümelerinde (önceki iterasyonun sık öğe kümelerinin geçerli alt dizileri) bulunup bulunmadığını
    kontrol ederek yapılır.

    Sık olmayan aday öğe kümelerini budar.

    >>> oge_kumesi = ['X', 'Y', 'Z']
    >>> adaylar = [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]
    >>> budama(oge_kumesi, adaylar, 2)
    [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]

    >>> oge_kumesi = ['1', '2', '3', '4']
    >>> adaylar = [['1', '2'], ['1', '4'], ['2', '4']]
    >>> budama(oge_kumesi, adaylar, 3)
    []
    """
    budanmis = []
    for aday in adaylar:
        alt_dizi_mi = True
        for oge in aday:
            if oge not in oge_kumesi or oge_kumesi.count(oge) < uzunluk - 1:
                alt_dizi_mi = False
                break
        if alt_dizi_mi:
            budanmis.append(aday)
    return budanmis


def apriori(veri: List[List[str]], min_destek: int) -> List[Tuple[List[str], int]]:
    """
    Sık öğe kümelerini ve destek sayılarını döndürür.

    >>> veri = [['A', 'B', 'C'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
    >>> apriori(veri, 2)
    [(['A', 'B'], 2), (['A', 'C'], 2), (['B', 'C'], 2)]

    >>> veri = [['1', '2', '3'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '3']]
    >>> apriori(veri, 3)
    []
    """
    oge_kumesi = [list(islem) for islem in veri]
    sik_oge_kumeleri = []
    uzunluk = 1

    while oge_kumesi:
        # Öğe kümesi desteğini say
        sayimlar = [0] * len(oge_kumesi)
        for islem in veri:
            for j, aday in enumerate(oge_kumesi):
                if all(oge in islem for oge in aday):
                    sayimlar[j] += 1

        # Sık olmayan öğe kümelerini buda
        oge_kumesi = [oge for i, oge in enumerate(oge_kumesi) if sayimlar[i] >= min_destek]

        # Sık öğe kümelerini ekle (sıralamayı korumak için liste olarak)
        for i, oge in enumerate(oge_kumesi):
            sik_oge_kumeleri.append((sorted(oge), sayimlar[i]))

        uzunluk += 1
        oge_kumesi = budama(oge_kumesi, list(combinations(oge_kumesi, uzunluk)), uzunluk)

    return sik_oge_kumeleri


if __name__ == "__main__":
    """
    Sık öğe kümelerini bulmak için Apriori algoritması.

    Args:
        veri: Her işlemin bir öğe listesi olduğu bir işlem listesi.
        min_destek: Sık öğe kümeleri için minimum destek eşiği.

    Returns:
        Sık öğe kümeleri ve destek sayıları ile birlikte bir liste.
    """
    import doctest

    doctest.testmod()

    # kullanıcı tanımlı eşik veya minimum destek seviyesi
    sik_oge_kumeleri = apriori(veri=veri_yukle(), min_destek=2)
    print("\n".join(f"{oge_kumesi}: {destek}" for oge_kumesi, destek in sik_oge_kumeleri))
