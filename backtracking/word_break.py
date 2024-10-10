"""
Kelime Bölme Problemi, bilgisayar bilimlerinde iyi bilinen bir problemdir.
Bir dize ve bir kelime sözlüğü verildiğinde, göreviniz dizenin bir veya daha fazla
sözlük kelimesi dizisine bölünüp bölünemeyeceğini belirlemektir.

Wikipedia: https://en.wikipedia.org/wiki/Word_break_problem

Organiser: K. Umut Araz
"""


def geri_izleme(girdi_dizesi: str, kelime_sözlüğü: set[str], başlangıç: int) -> bool:
    """
    Belirli bir 'başlangıç' indeksinden başlayarak geçerli bir kelime segmentasyonu
    mümkün olup olmadığını belirlemek için geri izleme kullanan yardımcı fonksiyon.

    Parametreler:
    girdi_dizesi (str): Segmentlenecek girdi dizesi.
    kelime_sözlüğü (set[str]): Geçerli sözlük kelimelerinin kümesi.
    başlangıç (int): Kontrol edilecek alt dizenin başlangıç indeksi.

    Dönüş:
    bool: Geçerli bir segmentasyon mümkünse True, aksi takdirde False.

    Örnek:
    >>> geri_izleme("leetcode", {"leet", "code"}, 0)
    True

    >>> geri_izleme("applepenapple", {"apple", "pen"}, 0)
    True

    >>> geri_izleme("catsandog", {"cats", "dog", "sand", "and", "cat"}, 0)
    False
    """

    # Temel durum: başlangıç indeksi dizenin sonuna ulaştıysa
    if başlangıç == len(girdi_dizesi):
        return True

    # 'başlangıç' ile 'son' arasındaki her olası alt diziyi dene
    for son in range(başlangıç + 1, len(girdi_dizesi) + 1):
        if girdi_dizesi[başlangıç:son] in kelime_sözlüğü and geri_izleme(
            girdi_dizesi, kelime_sözlüğü, son
        ):
            return True

    return False


def kelime_bölme(girdi_dizesi: str, kelime_sözlüğü: set[str]) -> bool:
    """
    Girdi dizesinin geçerli sözlük kelimelerinin bir dizisine bölünüp bölünemeyeceğini
    geri izleme kullanarak belirler.

    Parametreler:
    girdi_dizesi (str): Segmentlenecek girdi dizesi.
    kelime_sözlüğü (set[str]): Geçerli kelimelerin kümesi.

    Dönüş:
    bool: Dize geçerli kelimelere bölünebiliyorsa True, aksi takdirde False.

    Örnek:
    >>> kelime_bölme("leetcode", {"leet", "code"})
    True

    >>> kelime_bölme("applepenapple", {"apple", "pen"})
    True

    >>> kelime_bölme("catsandog", {"cats", "dog", "sand", "and", "cat"})
    False
    """

    return geri_izleme(girdi_dizesi, kelime_sözlüğü, 0)
