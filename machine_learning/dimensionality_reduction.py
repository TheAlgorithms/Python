#  Copyright (c) 2023 Diego Gasco (diego.gasco99@gmail.com), Diegomangasco on GitHub

"""
Gereksinimler:
  - numpy sürüm 1.21
  - scipy sürüm 1.3.3
Notlar:
  - Özellikler matrisinin her sütunu bir sınıf öğesine karşılık gelir
"""

import logging

import numpy as np
import pytest
from scipy.linalg import eigh

logging.basicConfig(level=logging.INFO, format="%(message)s")


def sütun_yeniden_şekillendir(girdi_dizisi: np.ndarray) -> np.ndarray:
    """Bir satır Numpy dizisini bir sütun Numpy dizisine yeniden şekillendirme işlevi
    >>> girdi_dizisi = np.array([1, 2, 3])
    >>> sütun_yeniden_şekillendir(girdi_dizisi)
    array([[1],
           [2],
           [3]])
    """

    return girdi_dizisi.reshape((girdi_dizisi.size, 1))


def sınıf_içi_kovaryans(
    özellikler: np.ndarray, etiketler: np.ndarray, sınıflar: int
) -> np.ndarray:
    """Her sınıf içindeki kovaryans matrisini hesaplama işlevi.
    >>> özellikler = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> etiketler = np.array([0, 1, 0])
    >>> sınıf_içi_kovaryans(özellikler, etiketler, 2)
    array([[0.66666667, 0.66666667, 0.66666667],
           [0.66666667, 0.66666667, 0.66666667],
           [0.66666667, 0.66666667, 0.66666667]])
    """

    kovaryans_toplamı = np.nan
    for i in range(sınıflar):
        veri = özellikler[:, etiketler == i]
        veri_ort = veri.mean(1)
        # Sınıf i verilerini merkezileştir
        merkezileştirilmiş_veri = veri - sütun_yeniden_şekillendir(veri_ort)
        if i > 0:
            # Eğer kovaryans_toplamı None değilse
            kovaryans_toplamı += np.dot(merkezileştirilmiş_veri, merkezileştirilmiş_veri.T)
        else:
            # Eğer kovaryans_toplamı np.nan ise (yani ilk döngü)
            kovaryans_toplamı = np.dot(merkezileştirilmiş_veri, merkezileştirilmiş_veri.T)

    return kovaryans_toplamı / özellikler.shape[1]


def sınıflar_arası_kovaryans(
    özellikler: np.ndarray, etiketler: np.ndarray, sınıflar: int
) -> np.ndarray:
    """Birden fazla sınıf arasındaki kovaryans matrisini hesaplama işlevi
    >>> özellikler = np.array([[9, 2, 3], [4, 3, 6], [1, 8, 9]])
    >>> etiketler = np.array([0, 1, 0])
    >>> sınıflar_arası_kovaryans(özellikler, etiketler, 2)
    array([[ 3.55555556,  1.77777778, -2.66666667],
           [ 1.77777778,  0.88888889, -1.33333333],
           [-2.66666667, -1.33333333,  2.        ]])
    """

    genel_veri_ort = özellikler.mean(1)
    kovaryans_toplamı = np.nan
    for i in range(sınıflar):
        veri = özellikler[:, etiketler == i]
        cihaz_verisi = veri.shape[1]
        veri_ort = veri.mean(1)
        if i > 0:
            # Eğer kovaryans_toplamı None değilse
            kovaryans_toplamı += cihaz_verisi * np.dot(
                sütun_yeniden_şekillendir(veri_ort) - sütun_yeniden_şekillendir(genel_veri_ort),
                (sütun_yeniden_şekillendir(veri_ort) - sütun_yeniden_şekillendir(genel_veri_ort)).T,
            )
        else:
            # Eğer kovaryans_toplamı np.nan ise (yani ilk döngü)
            kovaryans_toplamı = cihaz_verisi * np.dot(
                sütun_yeniden_şekillendir(veri_ort) - sütun_yeniden_şekillendir(genel_veri_ort),
                (sütun_yeniden_şekillendir(veri_ort) - sütun_yeniden_şekillendir(genel_veri_ort)).T,
            )

    return kovaryans_toplamı / özellikler.shape[1]


def ana_bileşen_analizi(özellikler: np.ndarray, boyutlar: int) -> np.ndarray:
    """
    Ana Bileşen Analizi.

    Daha fazla ayrıntı için bkz: https://en.wikipedia.org/wiki/Principal_component_analysis.
    Parametreler:
        * özellikler: veri setinden çıkarılan özellikler
        * boyutlar: istenen boyut için projeksiyon verilerini filtrelemek

    >>> test_ana_bileşen_analizi()
    """

    # Özelliklerin yüklendiğini kontrol et
    if özellikler.any():
        veri_ort = özellikler.mean(1)
        # Veri setini merkezileştir
        merkezileştirilmiş_veri = özellikler - np.reshape(veri_ort, (veri_ort.size, 1))
        kovaryans_matrisi = np.dot(merkezileştirilmiş_veri, merkezileştirilmiş_veri.T) / özellikler.shape[1]
        _, özvektörler = np.linalg.eigh(kovaryans_matrisi)
        # Tüm sütunları ters sırayla al (-1) ve ardından sadece ilk sütunları al
        filtrelenmiş_özvektörler = özvektörler[:, ::-1][:, 0:boyutlar]
        # Veritabanını yeni uzaya projekte et
        projekte_veri = np.dot(filtrelenmiş_özvektörler.T, özellikler)
        logging.info("Ana Bileşen Analizi hesaplandı")

        return projekte_veri
    else:
        logging.basicConfig(level=logging.ERROR, format="%(message)s", force=True)
        logging.error("Veri seti boş")
        raise AssertionError


def doğrusal_ayrımcı_analiz(
    özellikler: np.ndarray, etiketler: np.ndarray, sınıflar: int, boyutlar: int
) -> np.ndarray:
    """
    Doğrusal Ayrımcı Analiz.

    Daha fazla ayrıntı için bkz: https://en.wikipedia.org/wiki/Linear_discriminant_analysis.
    Parametreler:
        * özellikler: veri setinden çıkarılan özellikler
        * etiketler: özelliklerin sınıf etiketleri
        * sınıflar: veri setinde bulunan sınıf sayısı
        * boyutlar: istenen boyut için projeksiyon verilerini filtrelemek

    >>> test_doğrusal_ayrımcı_analiz()
    """

    # İstenen boyutun sınıf sayısından az olduğunu kontrol et
    assert sınıflar > boyutlar

    # Özelliklerin yüklendiğini kontrol et
    if özellikler.any:
        _, özvektörler = eigh(
            sınıflar_arası_kovaryans(özellikler, etiketler, sınıflar),
            sınıf_içi_kovaryans(özellikler, etiketler, sınıflar),
        )
        filtrelenmiş_özvektörler = özvektörler[:, ::-1][:, :boyutlar]
        svd_matrisi, _, _ = np.linalg.svd(filtrelenmiş_özvektörler)
        filtrelenmiş_svd_matrisi = svd_matrisi[:, 0:boyutlar]
        projekte_veri = np.dot(filtrelenmiş_svd_matrisi.T, özellikler)
        logging.info("Doğrusal Ayrımcı Analiz hesaplandı")

        return projekte_veri
    else:
        logging.basicConfig(level=logging.ERROR, format="%(message)s", force=True)
        logging.error("Veri seti boş")
        raise AssertionError


def test_doğrusal_ayrımcı_analiz() -> None:
    # 2 sınıf ve 3 özellik içeren sahte veri seti oluştur
    özellikler = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]])
    etiketler = np.array([0, 0, 0, 1, 1])
    sınıflar = 2
    boyutlar = 2

    # Fonksiyonun boyutlar > sınıflar olduğunda AssertionError verdiğini doğrula
    with pytest.raises(AssertionError) as hata_bilgisi:  # noqa: PT012
        projekte_veri = doğrusal_ayrımcı_analiz(
            özellikler, etiketler, sınıflar, boyutlar
        )
        if isinstance(projekte_veri, np.ndarray):
            raise AssertionError(
                "boyutlar > sınıflar için AssertionError yükseltilmedi"
            )
        assert hata_bilgisi.type is AssertionError


def test_ana_bileşen_analizi() -> None:
    özellikler = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    boyutlar = 2
    beklenen_çıktı = np.array([[6.92820323, 8.66025404, 10.39230485], [3.0, 3.0, 3.0]])

    with pytest.raises(AssertionError) as hata_bilgisi:  # noqa: PT012
        çıktı = ana_bileşen_analizi(özellikler, boyutlar)
        if not np.allclose(beklenen_çıktı, çıktı):
            raise AssertionError
        assert hata_bilgisi.type is AssertionError


if __name__ == "__main__":
    import doctest

    doctest.testmod()
