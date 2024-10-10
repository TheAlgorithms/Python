from __future__ import annotations

#Organiser: K. Umut Araz


def labirenti_çöz(
    labirent: list[list[int]],
    başlangıç_satırı: int,
    başlangıç_sütunu: int,
    varış_satırı: int,
    varış_sütunu: int,
) -> list[list[int]]:
    """
    Bu yöntem "labirentteki fare" problemini çözer.
    Parametreler:
        - labirent: Sıfır ve birlerden oluşan iki boyutlu matris.
        - başlangıç_satırı: Başlangıç noktasının satır indeksi.
        - başlangıç_sütunu: Başlangıç noktasının sütun indeksi.
        - varış_satırı: Varış noktasının satır indeksi.
        - varış_sütunu: Varış noktasının sütun indeksi.
    Dönüş:
        - çözüm: Eğer varsa çözüm yolunu temsil eden 2D matris.
    Hatalar:
        - ValueError: Eğer çözüm yoksa veya başlangıç ya da varış koordinatları geçersizse.
    Açıklama:
        Bu yöntem, n x n matris olarak temsil edilen bir labirentte gezinir,
        belirli bir başlangıç hücresinden başlayarak bir varış hücresine ulaşmayı amaçlar.
        Labirent duvarlardan (1'ler) ve açık yollardan (0'lar) oluşur.
        Başlangıç ve varış hücreleri, özel satır ve sütun değerleri ile ayarlanabilir.
    >>> labirent = [[0, 1, 0, 1, 1],
    ...             [0, 0, 0, 0, 0],
    ...             [1, 0, 1, 0, 1],
    ...             [0, 0, 1, 0, 0],
    ...             [1, 0, 0, 1, 0]]
    >>> labirenti_çöz(labirent, 0, 0, len(labirent)-1, len(labirent)-1)    # doctest: +NORMALIZE_WHITESPACE
    [[0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0]]

    Not:
        Çıktı labirentinde, sıfırlar (0'lar) başlangıçtan varışa kadar olan
        olası yollardan birini temsil eder.

    >>> labirent = [[0, 1, 0, 1, 1],
    ...             [0, 0, 0, 0, 0],
    ...             [0, 0, 0, 0, 1],
    ...             [0, 0, 0, 0, 0],
    ...             [0, 0, 0, 0, 0]]
    >>> labirenti_çöz(labirent, 0, 0, len(labirent)-1, len(labirent)-1)    # doctest: +NORMALIZE_WHITESPACE
    [[0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]

    >>> labirent = [[0, 0, 0],
    ...             [0, 1, 0],
    ...             [1, 0, 0]]
    >>> labirenti_çöz(labirent, 0, 0, len(labirent)-1, len(labirent)-1)    # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]]

    >>> labirent = [[1, 0, 0],
    ...             [0, 1, 0],
    ...             [1, 0, 0]]
    >>> labirenti_çöz(labirent, 0, 1, len(labirent)-1, len(labirent)-1)    # doctest: +NORMALIZE_WHITESPACE
    [[1, 0, 0],
    [1, 1, 0],
    [1, 1, 0]]

    >>> labirent = [[1, 1, 0, 0, 1, 0, 0, 1],
    ...             [1, 0, 1, 0, 0, 1, 1, 1],
    ...             [0, 1, 0, 1, 0, 0, 1, 0],
    ...             [1, 1, 1, 0, 0, 1, 0, 1],
    ...             [0, 1, 0, 0, 1, 0, 1, 1],
    ...             [0, 0, 0, 1, 1, 1, 0, 1],
    ...             [0, 1, 0, 1, 0, 1, 1, 1],
    ...             [1, 1, 0, 0, 0, 0, 0, 1]]
    >>> labirenti_çöz(labirent, 0, 2, len(labirent)-1, 2)  # doctest: +NORMALIZE_WHITESPACE
    [[1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1]]
    >>> labirent = [[1, 0, 0],
    ...             [0, 1, 1],
    ...             [1, 0, 1]]
    >>> labirenti_çöz(labirent, 0, 1, len(labirent)-1, len(labirent)-1)
    Traceback (most recent call last):
        ...
    ValueError: Çözüm yok!

    >>> labirent = [[0, 0],
    ...             [1, 1]]
    >>> labirenti_çöz(labirent, 0, 0, len(labirent)-1, len(labirent)-1)
    Traceback (most recent call last):
        ...
    ValueError: Çözüm yok!

    >>> labirent = [[0, 1],
    ...             [1, 0]]
    >>> labirenti_çöz(labirent, 2, 0, len(labirent)-1, len(labirent)-1)
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz başlangıç veya varış koordinatları

    >>> labirent = [[1, 0, 0],
    ...             [0, 1, 0],
    ...             [1, 0, 0]]
    >>> labirenti_çöz(labirent, 0, 1, len(labirent), len(labirent)-1)
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz başlangıç veya varış koordinatları
    """
    boyut = len(labirent)
    # Başlangıç ve varış koordinatlarının geçersiz olup olmadığını kontrol et.
    if not (0 <= başlangıç_satırı <= boyut - 1 and 0 <= başlangıç_sütunu <= boyut - 1) or (
        not (0 <= varış_satırı <= boyut - 1 and 0 <= varış_sütunu <= boyut - 1)
    ):
        raise ValueError("Geçersiz başlangıç veya varış koordinatları")
    # Çözüm yolunu kaydetmek için çözüm nesnesi oluşturmalıyız.
    çözümler = [[1 for _ in range(boyut)] for _ in range(boyut)]
    çözüldü = labirenti_çalıştır(
        labirent, başlangıç_satırı, başlangıç_sütunu, varış_satırı, varış_sütunu, çözümler
    )
    if çözüldü:
        return çözümler
    else:
        raise ValueError("Çözüm yok!")


def labirenti_çalıştır(
    labirent: list[list[int]],
    i: int,
    j: int,
    varış_satırı: int,
    varış_sütunu: int,
    çözümler: list[list[int]],
) -> bool:
    """
    Bu yöntem (i, j) noktasından başlayarak dört yönde (yukarı, aşağı, sol, sağ) rekürsif olarak ilerler.
    Eğer varış noktasına bir yol bulunursa True, aksi takdirde False döner.
    Parametreler:
        labirent: Sıfır ve birlerden oluşan iki boyutlu matris.
        i, j: Matrisin koordinatları.
        çözümler: Çözümleri içeren iki boyutlu matris.
    Dönüş:
        Eğer yol bulunursa True, aksi takdirde False.
    """
    boyut = len(labirent)
    # Son kontrol noktası.
    if i == varış_satırı - j == varış_sütunu - labirent[i][j] == 0:
        çözümler[i][j] = 0
        return True

    alt_sınır = (not i < 0) and (not j < 0)  # Alt sınırları kontrol et
    üst_sınır = (i < boyut) and (j < boyut)  # Üst sınırları kontrol et

    if alt_sınır and üst_sınır:
        # Zaten ziyaret edilmiş ve blok noktalarını kontrol et.
        blok_durumu = (çözümler[i][j] == 1) and (labirent[i][j] == 0)
        if blok_durumu:
            # Ziyaret edildiğini kontrol et
            çözümler[i][j] = 0

            # Yönleri kontrol et
            if (
                labirenti_çalıştır(labirent, i + 1, j, varış_satırı, varış_sütunu, çözümler)
                or labirenti_çalıştır(
                    labirent, i, j + 1, varış_satırı, varış_sütunu, çözümler
                )
                or labirenti_çalıştır(
                    labirent, i - 1, j, varış_satırı, varış_sütunu, çözümler
                )
                or labirenti_çalıştır(
                    labirent, i, j - 1, varış_satırı, varış_sütunu, çözümler
                )
            ):
                return True

            çözümler[i][j] = 1
            return False
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
