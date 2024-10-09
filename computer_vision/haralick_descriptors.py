"""
https://en.wikipedia.org/wiki/Image_texture
https://en.wikipedia.org/wiki/Co-occurrence_matrix#Application_to_image_analysis
"""

import imageio.v2 as imageio
import numpy as np


def kok_ortalama_kare_hatasi(orijinal: np.ndarray, referans: np.ndarray) -> float:
    """İki N boyutlu numpy dizisi için Basit Kök Ortalama Kare Hatası uygulaması.

    Örnekler:
        >>> kok_ortalama_kare_hatasi(np.array([1, 2, 3]), np.array([1, 2, 3]))
        0.0
        >>> kok_ortalama_kare_hatasi(np.array([1, 2, 3]), np.array([2, 2, 2]))
        0.816496580927726
        >>> kok_ortalama_kare_hatasi(np.array([1, 2, 3]), np.array([6, 4, 2]))
        3.1622776601683795
    """
    return float(np.sqrt(((orijinal - referans) ** 2).mean()))


def goruntu_normallestir(
    goruntu: np.ndarray, sinir: float = 255.0, veri_tipi: np.dtype = np.uint8
) -> np.ndarray:
    """
    Numpy 2D dizi formatında görüntüyü, uint8 türüne sığacak şekilde 0-sinir arasında normalleştirir.

    Argümanlar:
        goruntu: Herhangi bir aralıktaki değerlerle matris olarak görüntüyü temsil eden 2D numpy dizisi
        sinir: Normalleştirme için maksimum sınır miktarı
        veri_tipi: Çıkış değişkenine ayarlanacak numpy veri tipi
    Dönüş:
        sınırlı aralık matrisine karşılık gelen uint8 türünde 2D numpy dizisi döndürür

    Örnekler:
        >>> goruntu_normallestir(np.array([[1, 2, 3], [4, 5, 10]]),
        ...                 sinir=1.0, veri_tipi=np.float64)
        array([[0.        , 0.11111111, 0.22222222],
               [0.33333333, 0.44444444, 1.        ]])
        >>> goruntu_normallestir(np.array([[4, 4, 3], [1, 7, 2]]))
        array([[127, 127,  85],
               [  0, 255,  42]], dtype=uint8)
    """
    normal = (goruntu - np.min(goruntu)) / (np.max(goruntu) - np.min(goruntu)) * sinir
    return normal.astype(veri_tipi)


def dizi_normallestir(dizi: np.ndarray, sinir: float = 1) -> np.ndarray:
    """1D diziyi 0-sinir aralığında normalleştirir.

    Argümanlar:
        dizi: Sınır aralığında normalleştirilecek değerleri içeren liste.
        sinir: Normalleştirme için maksimum sınır miktarı.
    Dönüş:
        sınırlı aralık dizisine karşılık gelen 1D numpy dizisi döndürür

    Örnekler:
        >>> dizi_normallestir(np.array([2, 3, 5, 7]))
        array([0. , 0.2, 0.6, 1. ])
        >>> dizi_normallestir(np.array([[5], [7], [11], [13]]))
        array([[0.  ],
               [0.25],
               [0.75],
               [1.  ]])
    """
    fark = np.max(dizi) - np.min(dizi)
    return (dizi - np.min(dizi)) / (1 if fark == 0 else fark) * sinir


def gri_ton(goruntu: np.ndarray) -> np.ndarray:
    """
    RGB kanalı ile ağırlıkların nokta çarpımını alarak, parlaklık ağırlıklarını kullanarak gri tonlamaya dönüştürür.

    Örnek:
        >>> gri_ton(np.array([[[108, 201, 72], [255, 11,  127]],
        ...                     [[56,  56,  56], [128, 255, 107]]]))
        array([[158,  97],
               [ 56, 200]], dtype=uint8)
    """
    return np.dot(goruntu[:, :, 0:3], [0.299, 0.587, 0.114]).astype(np.uint8)


def ikilestir(goruntu: np.ndarray, esik: float = 127.0) -> np.ndarray:
    """
    Bir gri tonlamalı görüntüyü verilen eşik değerine göre ikileştirir,
    değerleri buna göre 1 veya 0 olarak ayarlar.

    Örnekler:
        >>> ikilestir(np.array([[128, 255], [101, 156]]))
        array([[1, 1],
               [0, 1]])
        >>> ikilestir(np.array([[0.07, 1], [0.51, 0.3]]), esik=0.5)
        array([[0, 1],
               [1, 0]])
    """
    return np.where(goruntu > esik, 1, 0)


def donustur(
    goruntu: np.ndarray, tur: str, cekirdek: np.ndarray | None = None
) -> np.ndarray:
    """
    Erozyon ve Genişleme olmak üzere iki mevcut filtre fonksiyonundan birini kullanarak basit görüntü dönüşümü.

    Argümanlar:
        goruntu: dönüşüm uygulanacak ikileştirilmiş giriş görüntüsü
        tur: 'erosion' olabilir, bu durumda :func:np.max fonksiyonu çağrılır, veya 'dilation' olabilir, bu durumda :func:np.min kullanılır.
        cekirdek: orijinal görüntüye konvolüsyon uygularken kullanılacak, < :attr:goruntu.shape şekline sahip n x n çekirdek

    Dönüş:
        uygulanan ikili dönüşüme karşılık gelen, giriş görüntüsüyle aynı şekle sahip bir numpy dizisi döndürür.

    Örnekler:
        >>> img = np.array([[1, 0.5], [0.2, 0.7]])
        >>> img = ikilestir(img, esik=0.5)
        >>> donustur(img, 'erosion')
        array([[1, 1],
               [1, 1]], dtype=uint8)
        >>> donustur(img, 'dilation')
        array([[0, 0],
               [0, 0]], dtype=uint8)
    """
    if cekirdek is None:
        cekirdek = np.ones((3, 3))

    if tur == "erosion":
        sabit = 1
        uygula = np.max
    else:
        sabit = 0
        uygula = np.min

    merkez_x, merkez_y = (x // 2 for x in cekirdek.shape)

    # Orijinal görüntünün sınırlarının dışına çıkmamak için konvolüsyon uygularken dolgu görüntüsü kullanın
    donusturulmus = np.zeros(goruntu.shape, dtype=np.uint8)
    dolgulu = np.pad(goruntu, 1, "constant", constant_values=sabit)

    for x in range(merkez_x, dolgulu.shape[0] - merkez_x):
        for y in range(merkez_y, dolgulu.shape[1] - merkez_y):
            merkez = dolgulu[
                x - merkez_x : x + merkez_x + 1, y - merkez_y : y + merkez_y + 1
            ]
            # Görüntünün merkezlenmiş bölümüne dönüşüm yöntemini uygulayın
            donusturulmus[x - merkez_x, y - merkez_y] = uygula(merkez[cekirdek == 1])

    return donusturulmus


def acma_filtresi(goruntu: np.ndarray, cekirdek: np.ndarray | None = None) -> np.ndarray:
    """
    Erozyon ve ardından aynı görüntü üzerinde genişleme filtresi sırasıyla tanımlanan açma filtresi.

    Örnekler:
        >>> img = np.array([[1, 0.5], [0.2, 0.7]])
        >>> img = ikilestir(img, esik=0.5)
        >>> acma_filtresi(img)
        array([[1, 1],
               [1, 1]], dtype=uint8)
    """
    if cekirdek is None:
        np.ones((3, 3))

    return donustur(donustur(goruntu, "dilation", cekirdek), "erosion", cekirdek)


def kapama_filtresi(goruntu: np.ndarray, cekirdek: np.ndarray | None = None) -> np.ndarray:
    """
    Genişleme ve ardından aynı görüntü üzerinde erozyon filtresi sırasıyla tanımlanan kapama filtresi.

    Örnekler:
        >>> img = np.array([[1, 0.5], [0.2, 0.7]])
        >>> img = ikilestir(img, esik=0.5)
        >>> kapama_filtresi(img)
        array([[0, 0],
               [0, 0]], dtype=uint8)
    """
    if cekirdek is None:
        cekirdek = np.ones((3, 3))
    return donustur(donustur(goruntu, "erosion", cekirdek), "dilation", cekirdek)


def ikili_maske(
    goruntu_gri: np.ndarray, goruntu_harita: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    Bit maske değeri (eşleme maskesi ikili) temelinde ikili maske veya eşik uygular.

    Eşlenen doğru değer maskesini ve tamamlayıcı yanlış değer maskesini döndürür.

    Örnek:
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gri = gri_ton(img)
        >>> ikili = ikilestir(gri)
        >>> morfolojik = acma_filtresi(ikili)
        >>> ikili_maske(gri, morfolojik)
        (array([[1, 1],
               [1, 1]], dtype=uint8), array([[158,  97],
               [ 56, 200]], dtype=uint8))
    """
    dogru_maske, yanlis_maske = goruntu_gri.copy(), goruntu_gri.copy()
    dogru_maske[goruntu_harita == 1] = 1
    yanlis_maske[goruntu_harita == 0] = 0

    return dogru_maske, yanlis_maske


def matris_eszamanlilik(goruntu: np.ndarray, koordinat: tuple[int, int]) -> np.ndarray:
    """
    Giriş görüntüsüne ve görüntüde seçilen koordinatlara göre örnek eş-oluşum matrisini hesaplar.

    Uygulama, işlevin (np.max) doğrusal olmayan ve bu nedenle frekans alanında çağrılamaz olması nedeniyle temel yineleme kullanılarak yapılır.

    Örnek:
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gri = gri_ton(img)
        >>> ikili = ikilestir(gri)
        >>> morfolojik = acma_filtresi(ikili)
        >>> maske_1 = ikili_maske(gri, morfolojik)[0]
        >>> matris_eszamanlilik(maske_1, (0, 1))
        array([[0., 0.],
               [0., 0.]])
    """
    matris = np.zeros([np.max(goruntu) + 1, np.max(goruntu) + 1])

    ofset_x, ofset_y = koordinat

    for x in range(1, goruntu.shape[0] - 1):
        for y in range(1, goruntu.shape[1] - 1):
            temel_pixel = goruntu[x, y]
            ofset_pixel = goruntu[x + ofset_x, y + ofset_y]

            matris[temel_pixel, ofset_pixel] += 1
    matris_toplam = np.sum(matris)
    return matris / (1 if matris_toplam == 0 else matris_toplam)


def haralick_aciklayicilar(matris: np.ndarray) -> list[float]:
    """Eş-oluşum giriş matrisine dayalı olarak tüm 8 Haralick açıklayıcısını hesaplar.
    Tüm açıklayıcılar şunlardır:
    Maksimum olasılık, Ters Fark, Homojenlik, Entropi,
    Enerji, Farklılık, Kontrast ve Korelasyon

    Argümanlar:
        matris: Açıklayıcıları hesaplamak için temel olarak kullanılacak eş-oluşum matrisi.

    Dönüş:
        Elde edilen açıklayıcıların ters sıralı listesi

    Örnek:
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gri = gri_ton(img)
        >>> ikili = ikilestir(gri)
        >>> morfolojik = acma_filtresi(ikili)
        >>> maske_1 = ikili_maske(gri, morfolojik)[0]
        >>> eszamanlilik = matris_eszamanlilik(maske_1, (0, 1))
        >>> [float(f) for f in haralick_aciklayicilar(eszamanlilik)]
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    """
    # Daha büyük giriş türleri için np.indices işlevi kullanılabilir,
    # ancak np.ogrid gayet iyi çalışır
    i, j = np.ogrid[0 : matris.shape[0], 0 : matris.shape[1]]  # np.indices()

    # Sık kullanılan çarpma ve çıkarma işlemlerini önceden hesaplayın
    carpim = np.multiply(i, j)
    cikarma = np.subtract(i, j)

    # Maksimum Olasılığın sayısal değerini hesaplayın
    maksimum_olasilik = np.max(matris)
    # Her açıklayıcı için ayrı ayrı tanımı kullanarak matrisini hesaplayın
    korelasyon = carpim * matris
    enerji = np.power(matris, 2)
    kontrast = matris * np.power(cikarma, 2)

    farklilik = matris * np.abs(cikarma)
    ters_fark = matris / (1 + np.abs(cikarma))
    homojenlik = matris / (1 + np.power(cikarma, 2))
    entropi = -(matris[matris > 0] * np.log(matris[matris > 0]))

    # İlk açıklayıcıdan sonuncusuna kadar olan değerleri toplayın,
    # çünkü hepsi kendi orijin matrisleridir ve henüz elde edilen değer değildir.
    return [
        maksimum_olasilik,
        korelasyon.sum(),
        enerji.sum(),
        kontrast.sum(),
        farklilik.sum(),
        ters_fark.sum(),
        homojenlik.sum(),
        entropi.sum(),
    ]


def aciklayicilari_al(
    maskeler: tuple[np.ndarray, np.ndarray], koordinat: tuple[int, int]
) -> np.ndarray:
    """
    Giriş maskeleri ve koordinatlar verilerek, bir dizi farklı eş-oluşum matrisi için tüm Haralick açıklayıcılarını hesaplar.

    Örnek:
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gri = gri_ton(img)
        >>> ikili = ikilestir(gri)
        >>> morfolojik = acma_filtresi(ikili)
        >>> aciklayicilari_al(ikili_maske(gri, morfolojik), (0, 1))
        array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
    """
    aciklayicilar = np.array(
        [haralick_aciklayicilar(matris_eszamanlilik(maske, koordinat)) for maske in maskeler]
    )

    # Her bir açıklayıcıyı tek bir listeye birleştirin
    # açıklayıcıların sırasını içeren
    return np.concatenate(aciklayicilar, axis=None)


def oklit(a_noktasi: np.ndarray, b_noktasi: np.ndarray) -> float:
    """
    İki nokta arasındaki öklid mesafesini hesaplamak için basit yöntem,
    np.ndarray türünde.

    Örnek:
        >>> a = np.array([1, 0, -2])
        >>> b = np.array([2, -1, 1])
        >>> oklit(a, b)
        3.3166247903554
    """
    return float(np.sqrt(np.sum(np.square(a_noktasi - b_noktasi))))


def mesafeleri_al(aciklayicilar: np.ndarray, temel: int) -> list[tuple[int, float]]:
    """
    Seçilen temel açıklayıcı ile diğer tüm Haralick açıklayıcıları arasındaki tüm Öklid mesafelerini hesaplar.
    Elde edilen karşılaştırma azalan sırayla döndürülür,
    hangi açıklayıcının seçilen temele en çok benzediğini gösterir.

    Argümanlar:
        aciklayicilar: Temel indeksle karşılaştırılacak Haralick açıklayıcıları
        temel: Diğer açıklayıcılara öklid mesafesini hesaplamak için temel olarak kullanılacak Haralick açıklayıcı indeksi.

    Dönüş:
        Açıklayıcılar arasındaki sıralı mesafeler

    Örnek:
        >>> index = 1
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gri = gri_ton(img)
        >>> ikili = ikilestir(gri)
        >>> morfolojik = acma_filtresi(ikili)
        >>> mesafeleri_al(aciklayicilari_al(
        ...                 ikili_maske(gri, morfolojik), (0, 1)),
        ...               index)
        [(0, 0.0), (1, 0.0), (2, 0.0), (3, 0.0), (4, 0.0), (5, 0.0), \
(6, 0.0), (7, 0.0), (8, 0.0), (9, 0.0), (10, 0.0), (11, 0.0), (12, 0.0), \
(13, 0.0), (14, 0.0), (15, 0.0)]
    """
    mesafeler = np.array(
        [oklit(aciklayici, aciklayicilar[temel]) for aciklayici in aciklayicilar]
    )
    distances = np.array(
        [oklit(aciklayici, aciklayicilar[temel]) for aciklayici in aciklayicilar]
    )
    # Mesafeleri [0, 1] aralığında normalize et
    normalize_mesafeler: list[float] = dizi_normallestir(distances, 1).tolist()
    enum_mesafeler = list(enumerate(normalize_mesafeler))
    enum_mesafeler.sort(key=lambda tup: tup[1], reverse=True)
    return enum_mesafeler


if __name__ == "__main__":
    # Haralick açıklayıcılarını karşılaştırmak için indeks
    indeks = int(input())
    q_deger_listesi = [int(deger) for deger in input().split()]
    q_deger = (q_deger_listesi[0], q_deger_listesi[1])

    # Uygulanacak ilgili filtre formatı,
    # 1 açma filtresi için veya kapama filtresi için başka bir değer olabilir
    parametreler = {"format": int(input()), "esik": int(input())}

    # Yöntemlerin uygulanacağı görüntü sayısı
    b_sayisi = int(input())

    dosyalar, aciklayicilar = [], []

    for _ in range(b_sayisi):
        dosya = input().rstrip()
        dosyalar.append(dosya)

        # Verilen görüntüyü aç ve morfolojik filtreyi hesapla,
        # ilgili maskeler ve karşılık gelen Haralick Açıklayıcıları.
        goruntu = imageio.imread(dosya).astype(np.float32)
        gri = gri_ton(goruntu)
        esik = ikilestir(gri, parametreler["esik"])

        morfolojik = (
            acma_filtresi(esik)
            if parametreler["format"] == 1
            else kapama_filtresi(esik)
        )
        maskeler = ikili_maske(gri, morfolojik)
        aciklayicilar.append(aciklayicilari_al(maskeler, q_deger))

    # Sıralı mesafeler dizisini orijinal dosya konumuna karşılık gelen bir diziye dönüştür
    mesafeler = mesafeleri_al(np.array(aciklayicilar), indeks)
    indeksli_mesafeler = np.array(mesafeler).astype(np.uint8)[:, 0]

    # Son olarak, temel dosyadan tüm diğer görüntülere kadar olan Haralick açıklamalarını dikkate alarak mesafeleri yazdır.
    print(f"Sorgu: {dosyalar[indeks]}")
    print("Sıralama:")
    for idx, dosya_indeks in enumerate(indeksli_mesafeler):
        print(f"({idx}) {dosyalar[dosya_indeks]}", end="\n")
