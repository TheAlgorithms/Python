"""
https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
Smith-Waterman algoritması, dizi hizalaması için kullanılan bir dinamik programlama algoritmasıdır.
Özellikle iki dizi arasındaki benzerlikleri bulmak için kullanışlıdır, örneğin DNA veya protein dizileri.
Bu uygulamada, boşluklar doğrusal olarak cezalandırılır, yani hizalamada her boşluk için puan sabit bir miktar
azaltılır. Ancak, Smith-Waterman algoritması diğer boşluk ceza yöntemlerini de destekler.
"""


def puan_fonksiyonu(
    kaynak_karakter: str,
    hedef_karakter: str,
    eslesme: int = 1,
    eslesmeme: int = -1,
    bosluk: int = -2,
) -> int:
    """
    Karakter çiftleri için puanı hesaplar, eşleşme veya eşleşmeme durumuna göre.
    Karakterler eşleşirse 1, eşleşmezse -1 ve karakterlerden biri boşluksa -2 döner.
    >>> puan_fonksiyonu('A', 'A')
    1
    >>> puan_fonksiyonu('A', 'C')
    -1
    >>> puan_fonksiyonu('-', 'A')
    -2
    >>> puan_fonksiyonu('A', '-')
    -2
    >>> puan_fonksiyonu('-', '-')
    -2
    """
    if "-" in (kaynak_karakter, hedef_karakter):
        return bosluk
    return eslesme if kaynak_karakter == hedef_karakter else eslesmeme


def smith_waterman(
    sorgu: str,
    konu: str,
    eslesme: int = 1,
    eslesmeme: int = -1,
    bosluk: int = -2,
) -> list[list[int]]:
    """
    Smith-Waterman yerel dizi hizalama algoritmasını gerçekleştirir.
    Puan matrisini temsil eden 2D bir liste döner. Matristeki her değer, o noktada biten
    en iyi yerel hizalamanın puanına karşılık gelir.
    >>> smith_waterman('ACAC', 'CA')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    >>> smith_waterman('acac', 'ca')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    >>> smith_waterman('ACAC', 'ca')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    >>> smith_waterman('acac', 'CA')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    >>> smith_waterman('ACAC', '')
    [[0], [0], [0], [0], [0]]
    >>> smith_waterman('', 'CA')
    [[0, 0, 0]]
    >>> smith_waterman('AGT', 'AGT')
    [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]]
    >>> smith_waterman('AGT', 'GTA')
    [[0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 2, 0]]
    >>> smith_waterman('AGT', 'GTC')
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0]]
    >>> smith_waterman('AGT', 'G')
    [[0, 0], [0, 0], [0, 1], [0, 0]]
    >>> smith_waterman('G', 'AGT')
    [[0, 0, 0, 0], [0, 0, 1, 0]]
    >>> smith_waterman('AGT', 'AGTCT')
    [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0], [0, 0, 0, 3, 1, 1]]
    >>> smith_waterman('AGTCT', 'AGT')
    [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 1], [0, 0, 0, 1]]
    >>> smith_waterman('AGTCT', 'GTC')
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 1, 1]]
    """
    # sorgu ve konuyu büyük harfe çevir
    sorgu = sorgu.upper()
    konu = konu.upper()

    # Puan matrisini başlat
    m = len(sorgu)
    n = len(konu)
    puan = [[0] * (n + 1) for _ in range(m + 1)]
    kwargs = {"eslesme": eslesme, "eslesmeme": eslesmeme, "bosluk": bosluk}

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Her hücre için puanları hesapla
            eslesme_puani = puan[i - 1][j - 1] + puan_fonksiyonu(
                sorgu[i - 1], konu[j - 1], **kwargs
            )
            silme_puani = puan[i - 1][j] + bosluk
            ekleme_puani = puan[i][j - 1] + bosluk

            # Maksimum puanı al
            puan[i][j] = max(0, eslesme_puani, silme_puani, ekleme_puani)

    return puan


def geri_izleme(puan: list[list[int]], sorgu: str, konu: str) -> str:
    r"""
    En iyi yerel hizalamayı bulmak için geri izleme yapar.
    Matristeki en yüksek puanlı hücreden başlayarak, 0 puanına ulaşana kadar geriye doğru izler.
    Hizalama dizelerini döner.
    >>> geri_izleme([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'ACAC', 'CA')
    'CA\nCA'
    >>> geri_izleme([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'acac', 'ca')
    'CA\nCA'
    >>> geri_izleme([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'ACAC', 'ca')
    'CA\nCA'
    >>> geri_izleme([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'acac', 'CA')
    'CA\nCA'
    >>> geri_izleme([[0, 0, 0]], 'ACAC', '')
    ''
    """
    # sorgu ve konuyu büyük harfe çevir
    sorgu = sorgu.upper()
    konu = konu.upper()
    # Puan matrisindeki maksimum değerin indekslerini bul
    max_deger = float("-inf")
    i_max = j_max = 0
    for i, satir in enumerate(puan):
        for j, deger in enumerate(satir):
            if deger > max_deger:
                max_deger = deger
                i_max, j_max = i, j
    # En iyi hizalamayı bulmak için geri izleme mantığı
    i = i_max
    j = j_max
    hizalama1 = ""
    hizalama2 = ""
    bosluk = puan_fonksiyonu("-", "-")
    # Boş sorgu veya konuya karşı koruma
    if i == 0 or j == 0:
        return ""
    while i > 0 and j > 0:
        if puan[i][j] == puan[i - 1][j - 1] + puan_fonksiyonu(
            sorgu[i - 1], konu[j - 1]
        ):
            # optimal yol çapraz, her iki harfi al
            hizalama1 = sorgu[i - 1] + hizalama1
            hizalama2 = konu[j - 1] + hizalama2
            i -= 1
            j -= 1
        elif puan[i][j] == puan[i - 1][j] + bosluk:
            # optimal yol dikey
            hizalama1 = sorgu[i - 1] + hizalama1
            hizalama2 = f"-{hizalama2}"
            i -= 1
        else:
            # optimal yol yatay
            hizalama1 = f"-{hizalama1}"
            hizalama2 = konu[j - 1] + hizalama2
            j -= 1

    return f"{hizalama1}\n{hizalama2}"


if __name__ == "__main__":
    sorgu = "HEAGAWGHEE"
    konu = "PAWHEAE"

    puan = smith_waterman(sorgu, konu, eslesme=1, eslesmeme=-1, bosluk=-2)
    print(geri_izleme(puan, sorgu, konu))
