"""Produced by K. Umut Araz

Karesel polinomların ve üstel haritaların Julia kümelerini çizer.
 Daha spesifik olarak, bu fonksiyonu belirli bir sayıda iterasyon yapar
 ve ardından son iterasyonun mutlak değerinin belirli bir eşik değerden
 (kaçış yarıçapı olarak adlandırılır) büyük olup olmadığını çizer. Üstel harita için bu
 gerçekten bir kaçış yarıçapı değil, daha çok sınırlı yörüngelerle Julia
 kümesini yaklaşık olarak belirlemenin uygun bir yoludur.

Burada sunulan örnekler şunlardır:
- Karnabahar Julia kümesi, bkz.
https://en.wikipedia.org/wiki/File:Julia_z2%2B0,25.png
- Diğer örnekler: https://en.wikipedia.org/wiki/Julia_set
- Üstel harita Julia kümesi, ambiyant olarak homeomorfik örnekler:
https://www.math.univ-toulouse.fr/~cheritat/GalII/galery.html
 ve
https://ddd.uab.cat/pub/pubmat/02141493v43n1/02141493v43n1p27.pdf

Not: Bazı taşma çalışma zamanı uyarıları bastırılmıştır. Bunun nedeni,
 numpy'nin verimli hesaplamalarını kullanarak iterasyon döngüsünün uygulanma şeklidir.
 Her adımda taşmalar ve sonsuzluklar büyük bir sayı ile değiştirilir.
"""

import warnings
from collections.abc import Callable
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

c_karnabahar = 0.25 + 0.0j
c_polinom_1 = -0.4 + 0.6j
c_polinom_2 = -0.1 + 0.651j
c_ustel = -2.0
iterasyon_sayisi = 56
pencere_boyutu = 2.0
piksel_sayisi = 666


def ustel_degerlendir(c_parametre: complex, z_degerleri: np.ndarray) -> np.ndarray:
    """
    $e^z + c$ fonksiyonunu değerlendirir.
    >>> float(ustel_degerlendir(0, 0))
    1.0
    >>> bool(abs(ustel_degerlendir(1, np.pi*1.j)) < 1e-15)
    True
    >>> bool(abs(ustel_degerlendir(1.j, 0)-1-1.j) < 1e-15)
    True
    """
    return np.exp(z_degerleri) + c_parametre


def karesel_polinom_degerlendir(c_parametre: complex, z_degerleri: np.ndarray) -> np.ndarray:
    """
    >>> karesel_polinom_degerlendir(0, 2)
    4
    >>> karesel_polinom_degerlendir(-1, 1)
    0
    >>> round(karesel_polinom_degerlendir(1.j, 0).imag)
    1
    >>> round(karesel_polinom_degerlendir(1.j, 0).real)
    0
    """
    return z_degerleri * z_degerleri + c_parametre


def grid_hazirla(pencere_boyutu: float, piksel_sayisi: int) -> np.ndarray:
    """
    Gerçek ve sanal kısımları -pencere_boyutu ile pencere_boyutu (dahil) arasında
    değişen, piksel_sayisi*piksel_sayisi boyutunda karmaşık değerler ızgarası oluşturur.
    Bir numpy dizisi döndürür.

    >>> grid_hazirla(1,3)
    array([[-1.-1.j, -1.+0.j, -1.+1.j],
           [ 0.-1.j,  0.+0.j,  0.+1.j],
           [ 1.-1.j,  1.+0.j,  1.+1.j]])
    """
    x = np.linspace(-pencere_boyutu, pencere_boyutu, piksel_sayisi)
    x = x.reshape((piksel_sayisi, 1))
    y = np.linspace(-pencere_boyutu, pencere_boyutu, piksel_sayisi)
    y = y.reshape((1, piksel_sayisi))
    return x + 1.0j * y


def fonksiyon_iterasyonu(
    degerlendir_fonksiyonu: Callable[[Any, np.ndarray], np.ndarray],
    fonksiyon_parametreleri: Any,
    iterasyon_sayisi: int,
    z_0: np.ndarray,
    sonsuzluk: float | None = None,
) -> np.ndarray:
    """
    "degerlendir_fonksiyonu" fonksiyonunu tam olarak iterasyon_sayisi kadar iterasyon yapar.
    Fonksiyonun ilk argümanı, fonksiyon_parametreleri içinde bulunan bir parametredir.
    z_0 değişkeni, iterasyona başlanacak başlangıç değerlerini içeren bir dizidir.
    Bu fonksiyon, son iterasyonları döndürür.

    >>> fonksiyon_iterasyonu(karesel_polinom_degerlendir, 0, 3, np.array([0,1,2])).shape
    (3,)
    >>> complex(np.round(fonksiyon_iterasyonu(karesel_polinom_degerlendir,
    ... 0,
    ... 3,
    ... np.array([0,1,2]))[0]))
    0j
    >>> complex(np.round(fonksiyon_iterasyonu(karesel_polinom_degerlendir,
    ... 0,
    ... 3,
    ... np.array([0,1,2]))[1]))
    (1+0j)
    >>> complex(np.round(fonksiyon_iterasyonu(karesel_polinom_degerlendir,
    ... 0,
    ... 3,
    ... np.array([0,1,2]))[2]))
    (256+0j)
    """

    z_n = z_0.astype("complex64")
    for _ in range(iterasyon_sayisi):
        z_n = degerlendir_fonksiyonu(fonksiyon_parametreleri, z_n)
        if sonsuzluk is not None:
            np.nan_to_num(z_n, copy=False, nan=sonsuzluk)
            z_n[abs(z_n) == np.inf] = sonsuzluk
    return z_n


def sonuclari_goster(
    fonksiyon_etiketi: str,
    fonksiyon_parametreleri: Any,
    kacis_yaricapi: float,
    z_son: np.ndarray,
) -> None:
    """
    z_son'un mutlak değerinin kacis_yaricapi değerinden büyük olup olmadığını çizer.
    Başlığa fonksiyon_etiketi ve fonksiyon_parametreleri ekler.

    >>> sonuclari_goster('80', 0, 1, np.array([[0,1,.5],[.4,2,1.1],[.2,1,1.3]]))
    """

    abs_z_son = (abs(z_son)).transpose()
    abs_z_son[:, :] = abs_z_son[::-1, :]
    plt.matshow(abs_z_son < kacis_yaricapi)
    plt.title(f"Julia kümesi ${fonksiyon_etiketi}$, $c={fonksiyon_parametreleri}$")
    plt.show()


def tasma_uyarilarini_yoksay() -> None:
    """
    Bazı taşma ve geçersiz değer uyarılarını yoksayar.

    >>> tasma_uyarilarini_yoksay()
    """
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in multiply"
    )
    warnings.filterwarnings(
        "ignore",
        category=RuntimeWarning,
        message="invalid value encountered in multiply",
    )
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in absolute"
    )
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in exp"
    )


if __name__ == "__main__":
    z_0 = grid_hazirla(pencere_boyutu, piksel_sayisi)

    tasma_uyarilarini_yoksay()  # Dosya başlığına bakın

    iterasyon_sayisi = 24
    kacis_yaricapi = 2 * abs(c_karnabahar) + 1
    z_son = fonksiyon_iterasyonu(
        karesel_polinom_degerlendir,
        c_karnabahar,
        iterasyon_sayisi,
        z_0,
        sonsuzluk=1.1 * kacis_yaricapi,
    )
    sonuclari_goster("z^2+c", c_karnabahar, kacis_yaricapi, z_son)

    iterasyon_sayisi = 64
    kacis_yaricapi = 2 * abs(c_polinom_1) + 1
    z_son = fonksiyon_iterasyonu(
        karesel_polinom_degerlendir,
        c_polinom_1,
        iterasyon_sayisi,
        z_0,
        sonsuzluk=1.1 * kacis_yaricapi,
    )
    sonuclari_goster("z^2+c", c_polinom_1, kacis_yaricapi, z_son)

    iterasyon_sayisi = 161
    kacis_yaricapi = 2 * abs(c_polinom_2) + 1
    z_son = fonksiyon_iterasyonu(
        karesel_polinom_degerlendir,
        c_polinom_2,
        iterasyon_sayisi,
        z_0,
        sonsuzluk=1.1 * kacis_yaricapi,
    )
    sonuclari_goster("z^2+c", c_polinom_2, kacis_yaricapi, z_son)

    iterasyon_sayisi = 12
    kacis_yaricapi = 10000.0
    z_son = fonksiyon_iterasyonu(
        ustel_degerlendir,
        c_ustel,
        iterasyon_sayisi,
        z_0 + 2,
        sonsuzluk=1.0e10,
    )
    sonuclari_goster("e^z+c", c_ustel, kacis_yaricapi, z_son)
