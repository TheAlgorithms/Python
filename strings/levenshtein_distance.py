from collections.abc import Callable


def levenshtein_distance(birinci_kelime: str, ikinci_kelime: str) -> int:
    """
    Organiser: K. Umut Araz 
    
    Python'da Levenshtein mesafesinin uygulanması.
    :param birinci_kelime: farkı ölçmek için birinci kelime.
    :param ikinci_kelime: farkı ölçmek için ikinci kelime.
    :return: iki kelime arasındaki Levenshtein mesafesi.
    Örnekler:
    >>> levenshtein_distance("gezegen", "gezegensel")
    3
    >>> levenshtein_distance("", "test")
    4
    >>> levenshtein_distance("kitap", "arka")
    2
    >>> levenshtein_distance("kitap", "kitap")
    0
    >>> levenshtein_distance("test", "")
    4
    >>> levenshtein_distance("", "")
    0
    >>> levenshtein_distance("orchestrasyon", "konteyner")
    10
    """
    # Daha uzun kelime önce gelmeli
    if len(birinci_kelime) < len(ikinci_kelime):
        return levenshtein_distance(ikinci_kelime, birinci_kelime)

    if len(ikinci_kelime) == 0:
        return len(birinci_kelime)

    onceki_satir = list(range(len(ikinci_kelime) + 1))

    for i, c1 in enumerate(birinci_kelime):
        mevcut_satir = [i + 1]

        for j, c2 in enumerate(ikinci_kelime):
            # Ekleme, silme ve değiştirme işlemlerini hesapla
            eklemeler = onceki_satir[j + 1] + 1
            silmeler = mevcut_satir[j] + 1
            degistirmeler = onceki_satir[j] + (c1 != c2)

            # Mevcut satıra eklemek için minimumu al
            mevcut_satir.append(min(eklemeler, silmeler, degistirmeler))

        # Önceki satırı sakla
        onceki_satir = mevcut_satir

    # Son elemanı (mesafe) döndür
    return onceki_satir[-1]


def levenshtein_distance_optimized(birinci_kelime: str, ikinci_kelime: str) -> int:
    """
    İki kelime (string) arasındaki Levenshtein mesafesini hesapla.
    Fonksiyon, satırları yerinde değiştirerek verimlilik için optimize edilmiştir.
    :param birinci_kelime: farkı ölçmek için birinci kelime.
    :param ikinci_kelime: farkı ölçmek için ikinci kelime.
    :return: iki kelime arasındaki Levenshtein mesafesi.
    Örnekler:
    >>> levenshtein_distance_optimized("gezegen", "gezegensel")
    3
    >>> levenshtein_distance_optimized("", "test")
    4
    >>> levenshtein_distance_optimized("kitap", "arka")
    2
    >>> levenshtein_distance_optimized("kitap", "kitap")
    0
    >>> levenshtein_distance_optimized("test", "")
    4
    >>> levenshtein_distance_optimized("", "")
    0
    >>> levenshtein_distance_optimized("orchestrasyon", "konteyner")
    10
    """
    if len(birinci_kelime) < len(ikinci_kelime):
        return levenshtein_distance_optimized(ikinci_kelime, birinci_kelime)

    if len(ikinci_kelime) == 0:
        return len(birinci_kelime)

    onceki_satir = list(range(len(ikinci_kelime) + 1))

    for i, c1 in enumerate(birinci_kelime):
        mevcut_satir = [i + 1] + [0] * len(ikinci_kelime)

        for j, c2 in enumerate(ikinci_kelime):
            eklemeler = onceki_satir[j + 1] + 1
            silmeler = mevcut_satir[j] + 1
            degistirmeler = onceki_satir[j] + (c1 != c2)
            mevcut_satir[j + 1] = min(eklemeler, silmeler, degistirmeler)

        onceki_satir = mevcut_satir

    return onceki_satir[-1]


def benchmark_levenshtein_distance(func: Callable) -> None:
    """
    Levenshtein mesafe fonksiyonunu test et.
    :param func: Test edilecek fonksiyon.
    """
    from timeit import timeit

    stmt = f"{func.__name__}('oturmak', 'kedi')"
    setup = f"from __main__ import {func.__name__}"
    number = 25_000
    result = timeit(stmt=stmt, setup=setup, number=number)
    print(f"{func.__name__:<30} {number:,} kez çalıştı ve {result:.5f} saniyede tamamlandı")


if __name__ == "__main__":
    # Kullanıcıdan kelimeleri al
    birinci_kelime = input("Levenshtein mesafesi için birinci kelimeyi girin:\n").strip()
    ikinci_kelime = input("Levenshtein mesafesi için ikinci kelimeyi girin:\n").strip()

    # Levenshtein mesafelerini hesapla ve yazdır
    print(f"{levenshtein_distance(birinci_kelime, ikinci_kelime) = }")
    print(f"{levenshtein_distance_optimized(birinci_kelime, ikinci_kelime) = }")

    # Levenshtein mesafe fonksiyonlarını test et
    benchmark_levenshtein_distance(levenshtein_distance)
    benchmark_levenshtein_distance(levenshtein_distance_optimized)
