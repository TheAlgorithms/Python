"""
Kelime Merdiveni, bilgisayar bilimlerinde klasik bir problemdir.
Bu problemde, bir başlangıç kelimesini bir bitiş kelimesine
her seferinde bir harf değiştirerek dönüştürmek amaçlanır.
Her ara kelime, verilen bir kelime listesinden geçerli bir kelime olmalıdır.
Amaç, başlangıç kelimesinden bitiş kelimesine bir dönüşüm dizisi bulmaktır.

Wikipedia: https://en.wikipedia.org/wiki/Word_ladder
"""

import string


def geri_izleme(
    mevcut_kelime: str, yol: list[str], bitiş_kelime: str, kelime_kümesi: set[str]
) -> list[str]:
    """
    Mevcut kelimeden bitiş kelimesine dönüşümü bulmak için geri izleme
    gerçekleştiren yardımcı fonksiyon.

    Parametreler:
    mevcut_kelime (str): Dönüşüm dizisindeki mevcut kelime.
    yol (list[str]): Başlangıç kelimesinden mevcut kelimeye kadar olan dönüşümler listesi.
    bitiş_kelime (str): Dönüşüm için hedef kelime.
    kelime_kümesi (set[str]): Dönüşüm için geçerli kelimelerin kümesi.

    Dönüş:
    list[str]: Başlangıç kelimesinden bitiş kelimesine kadar olan dönüşümler listesi.
               Eğer mevcut kelimeden bitiş kelimesine geçerli bir dönüşüm yoksa
               boş bir liste döner.

    Örnek:
    >>> geri_izleme("hit", ["hit"], "cog", {"hot", "dot", "dog", "lot", "log", "cog"})
    ['hit', 'hot', 'dot', 'lot', 'log', 'cog']

    >>> geri_izleme("hit", ["hit"], "cog", {"hot", "dot", "dog", "lot", "log"})
    []

    >>> geri_izleme("lead", ["lead"], "gold", {"load", "goad", "gold", "lead", "lord"})
    ['lead', 'lead', 'load', 'goad', 'gold']

    >>> geri_izleme("game", ["game"], "code", {"came", "cage", "code", "cade", "gave"})
    ['game', 'came', 'cade', 'code']
    """

    # Temel durum: Eğer mevcut kelime bitiş kelimesi ise, yolu döndür
    if mevcut_kelime == bitiş_kelime:
        return yol

    # Tüm olası tek harfli dönüşümleri dene
    for i in range(len(mevcut_kelime)):
        for c in string.ascii_lowercase:  # Her harfi değiştirmeyi dene
            dönüştürülmüş_kelime = mevcut_kelime[:i] + c + mevcut_kelime[i + 1 :]
            if dönüştürülmüş_kelime in kelime_kümesi:
                kelime_kümesi.remove(dönüştürülmüş_kelime)
                # Yeni kelimeyi yola ekleyerek rekürsif olarak çağır
                sonuç = geri_izleme(
                    dönüştürülmüş_kelime, [*yol, dönüştürülmüş_kelime], bitiş_kelime, kelime_kümesi
                )
                if sonuç:  # geçerli dönüşüm bulundu
                    return sonuç
                kelime_kümesi.add(dönüştürülmüş_kelime)  # geri izleme

    return []  # Geçerli dönüşüm bulunamadı


def kelime_merdiveni(başlangıç_kelime: str, bitiş_kelime: str, kelime_kümesi: set[str]) -> list[str]:
    """
    Kelime Merdiveni problemini Geri İzleme kullanarak çözer ve
    başlangıç kelimesinden bitiş kelimesine kadar olan dönüşümler listesini döner.

    Parametreler:
    başlangıç_kelime (str): Dönüşümün başladığı kelime.
    bitiş_kelime (str): Dönüşüm için hedef kelime.
    kelime_listesi (list[str]): Dönüşüm için geçerli kelimelerin listesi.

    Dönüş:
    list[str]: Başlangıç kelimesinden bitiş kelimesine kadar olan dönüşümler listesi.
               Eğer geçerli bir dönüşüm yoksa boş bir liste döner.

    Örnek:
    >>> kelime_merdiveni("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    ['hit', 'hot', 'dot', 'lot', 'log', 'cog']

    >>> kelime_merdiveni("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    []

    >>> kelime_merdiveni("lead", "gold", ["load", "goad", "gold", "lead", "lord"])
    ['lead', 'lead', 'load', 'goad', 'gold']

    >>> kelime_merdiveni("game", "code", ["came", "cage", "code", "cade", "gave"])
    ['game', 'came', 'cade', 'code']
    """

    if bitiş_kelime not in kelime_kümesi:  # geçerli dönüşüm mümkün değil
        return []

    # Başlangıç kelimesinden başlayarak geri izleme gerçekleştir
    return geri_izleme(başlangıç_kelime, [başlangıç_kelime], bitiş_kelime, kelime_kümesi)
