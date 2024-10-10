from __future__ import annotations


def knuth_morris_pratt(metin: str, desen: str) -> int:
    """
    Knuth-Morris-Pratt Algoritması, bir metin içinde bir deseni bulmak için
    O(n + m) karmaşıklığı ile çalışır.

    Organiser: K. Umut Araz

    1) Deseni ön işleme tabi tutarak, ön eklerle aynı olan son ekleri belirleyin.

        Bu, desen ile metin arasında bir karakter uyuşmazlığı olduğunda
        nereden devam edeceğimizi gösterir.

    2) Metin içinde bir karakteri sırayla kontrol edin ve gerekirse
        desen içindeki konumumuzu güncelleyin.

    >>> kmp = "knuth_morris_pratt"
    >>> all(
    ...    knuth_morris_pratt(kmp, s) == kmp.find(s)
    ...    for s in ("kn", "h_m", "rr", "tt", "orada yok")
    ... )
    True
    """

    # 1) Hata dizisini oluştur
    hata_dizisi = get_failure_array(desen)

    # 2) Metin içinde deseni aramak için ilerle
    i, j = 0, 0  # metin ve desen için indeksler
    while i < len(metin):
        if desen[j] == metin[i]:
            if j == (len(desen) - 1):
                return i - j
            j += 1

        # Eğer bu, desenimizde bir ön ekse
        # devam etmek için yeterince geri dön
        elif j > 0:
            j = hata_dizisi[j - 1]
            continue
        i += 1
    return -1


def get_failure_array(desen: str) -> list[int]:
    """
    Bir karşılaştırmayı başaramadığımızda gitmemiz gereken yeni indeksi hesaplar
    :param desen:
    :return:
    """
    hata_dizisi = [0]
    i = 0
    j = 1
    while j < len(desen):
        if desen[i] == desen[j]:
            i += 1
        elif i > 0:
            i = hata_dizisi[i - 1]
            continue
        j += 1
        hata_dizisi.append(i)
    return hata_dizisi


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Test 1)
    desen = "abc1abc12"
    metin1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    metin2 = "alskfjaldsk23adsfabcabc"
    assert knuth_morris_pratt(metin1, desen) != -1
    assert knuth_morris_pratt(metin2, desen) != -1

    # Test 2)
    desen = "ABABX"
    metin = "ABABZABABYABABX"
    assert knuth_morris_pratt(metin, desen) != -1

    # Test 3)
    desen = "AAAB"
    metin = "ABAAAAAB"
    assert knuth_morris_pratt(metin, desen) != -1

    # Test 4)
    desen = "abcdabcy"
    metin = "abcxabcdabxabcdabcdabcy"
    assert knuth_morris_pratt(metin, desen) != -1

    # Test 5) -> Doctest
    kmp = "knuth_morris_pratt"
    assert all(
        knuth_morris_pratt(kmp, s) == kmp.find(s)
        for s in ("kn", "h_m", "rr", "tt", "orada yok")
    )

    # Test 6)
    desen = "aabaabaaa"
    assert get_failure_array(desen) == [0, 1, 0, 1, 2, 3, 4, 5, 2]
