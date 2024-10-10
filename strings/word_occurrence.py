# Oluşturan: sarathkaul, 17/11/19
# Düzenleyen: Arkadip Bhattacharya(@darkmatter18), 20/04/2020
# Düzenleyen: K. Umut Araz, 10/10/2024
from collections import defaultdict


def kelime_sayisi(cümle: str) -> dict:
    """
    >>> from collections import Counter
    >>> CUMLE = "a b A b c b d b d e f e g e h e i e j e 0"
    >>> kelime_dict = kelime_sayisi(CUMLE)
    >>> all(kelime_dict[kelime] == sayi for kelime, sayi
    ...     in Counter(CUMLE.split()).items())
    True
    >>> dict(kelime_sayisi("İki  boşluk"))
    {'İki': 1, 'boşluk': 1}
    """
    kelime_sayisi: defaultdict[str, int] = defaultdict(int)
    # Her kelimenin sayısını içeren bir sözlük oluşturma
    for kelime in cümle.split():
        kelime_sayisi[kelime] += 1
    return kelime_sayisi


if __name__ == "__main__":
    for kelime, sayi in kelime_sayisi("GİRİŞ DİZİSİ").items():
        print(f"{kelime}: {sayi}")
