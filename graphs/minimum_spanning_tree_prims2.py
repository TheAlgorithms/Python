"""
Prim'in (Jarník olarak da bilinir) algoritması, ağırlıklı yönsüz bir grafik için minimum yayılım ağacı bulan açgözlü bir algoritmadır.
Bu, her düğümü içeren ve ağaçtaki tüm kenarların toplam ağırlığının en aza indirildiği bir alt küme bulduğu anlamına gelir. 
Algoritma, bu ağacı her seferinde bir düğüm ekleyerek, rastgele bir başlangıç düğümünden başlayarak, her adımda ağaca başka bir düğümden en ucuz bağlantıyı ekleyerek çalışır.
"""

from __future__ import annotations

from sys import maxsize
from typing import Generic, TypeVar

T = TypeVar("T")

#Produced By K. Umut Araz


def ebeveyn_pozisyonu_al(pozisyon: int) -> int:
    """
    Yığın yardımcı fonksiyonu, mevcut düğümün ebeveyninin pozisyonunu alır

    >>> ebeveyn_pozisyonu_al(1)
    0
    >>> ebeveyn_pozisyonu_al(2)
    0
    """
    return (pozisyon - 1) // 2


def sol_cocuk_pozisyonu_al(pozisyon: int) -> int:
    """
    Yığın yardımcı fonksiyonu, mevcut düğümün sol çocuğunun pozisyonunu alır

    >>> sol_cocuk_pozisyonu_al(0)
    1
    """
    return (2 * pozisyon) + 1


def sag_cocuk_pozisyonu_al(pozisyon: int) -> int:
    """
    Yığın yardımcı fonksiyonu, mevcut düğümün sağ çocuğunun pozisyonunu alır

    >>> sag_cocuk_pozisyonu_al(0)
    2
    """
    return (2 * pozisyon) + 2


class MinOncelikKuyrugu(Generic[T]):
    """
    Minimum Öncelik Kuyruğu Sınıfı

    Fonksiyonlar:
    bos_mu: öncelik kuyruğunun boş olup olmadığını kontrol eden fonksiyon
    ekle: kuyruğa verilen öncelikle bir eleman ekleyen fonksiyon
    min_cikar: en düşük ağırlığa (en yüksek önceliğe) sahip elemanı çıkaran ve döndüren fonksiyon
    anahtar_guncelle: verilen anahtarın ağırlığını güncelleyen fonksiyon
    yukari_kaydir: bir düğümü uygun pozisyona yerleştiren yardımcı fonksiyon (yukarı hareket)
    asagi_kaydir: bir düğümü uygun pozisyona yerleştiren yardımcı fonksiyon (aşağı hareket)
    dugum_degistir: verilen pozisyonlardaki düğümleri değiştiren yardımcı fonksiyon

    >>> kuyruk = MinOncelikKuyrugu()

    >>> kuyruk.ekle(1, 1000)
    >>> kuyruk.ekle(2, 100)
    >>> kuyruk.ekle(3, 4000)
    >>> kuyruk.ekle(4, 3000)

    >>> kuyruk.min_cikar()
    2

    >>> kuyruk.anahtar_guncelle(4, 50)

    >>> kuyruk.min_cikar()
    4
    >>> kuyruk.min_cikar()
    1
    >>> kuyruk.min_cikar()
    3
    """

    def __init__(self) -> None:
        self.yigin: list[tuple[T, int]] = []
        self.pozisyon_haritasi: dict[T, int] = {}
        self.eleman_sayisi: int = 0

    def __len__(self) -> int:
        return self.eleman_sayisi

    def __repr__(self) -> str:
        return str(self.yigin)

    def bos_mu(self) -> bool:
        # Öncelik kuyruğunun boş olup olmadığını kontrol et
        return self.eleman_sayisi == 0

    def ekle(self, eleman: T, agirlik: int) -> None:
        # Kuyruğa verilen öncelikle bir eleman ekle
        self.yigin.append((eleman, agirlik))
        self.pozisyon_haritasi[eleman] = self.eleman_sayisi
        self.eleman_sayisi += 1
        self.yukari_kaydir(eleman)

    def min_cikar(self) -> T:
        # En düşük ağırlığa (en yüksek önceliğe) sahip elemanı çıkar ve döndür
        if self.eleman_sayisi > 1:
            self.dugum_degistir(0, self.eleman_sayisi - 1)
        eleman, _ = self.yigin.pop()
        del self.pozisyon_haritasi[eleman]
        self.eleman_sayisi -= 1
        if self.eleman_sayisi > 0:
            asagi_kaydir_eleman, _ = self.yigin[0]
            self.asagi_kaydir(asagi_kaydir_eleman)
        return eleman

    def anahtar_guncelle(self, eleman: T, agirlik: int) -> None:
        # Verilen anahtarın ağırlığını güncelle
        pozisyon = self.pozisyon_haritasi[eleman]
        self.yigin[pozisyon] = (eleman, agirlik)
        if pozisyon > 0:
            ebeveyn_pozisyon = ebeveyn_pozisyonu_al(pozisyon)
            _, ebeveyn_agirlik = self.yigin[ebeveyn_pozisyon]
            if ebeveyn_agirlik > agirlik:
                self.yukari_kaydir(eleman)
            else:
                self.asagi_kaydir(eleman)
        else:
            self.asagi_kaydir(eleman)

    def yukari_kaydir(self, eleman: T) -> None:
        # Bir düğümü uygun pozisyona yerleştir (yukarı hareket) [sadece dahili kullanım için]
        mevcut_pozisyon = self.pozisyon_haritasi[eleman]
        if mevcut_pozisyon == 0:
            return None
        ebeveyn_pozisyon = ebeveyn_pozisyonu_al(mevcut_pozisyon)
        _, agirlik = self.yigin[mevcut_pozisyon]
        _, ebeveyn_agirlik = self.yigin[ebeveyn_pozisyon]
        if ebeveyn_agirlik > agirlik:
            self.dugum_degistir(ebeveyn_pozisyon, mevcut_pozisyon)
            return self.yukari_kaydir(eleman)
        return None

    def asagi_kaydir(self, eleman: T) -> None:
        # Bir düğümü uygun pozisyona yerleştir (aşağı hareket) [sadece dahili kullanım için]
        mevcut_pozisyon = self.pozisyon_haritasi[eleman]
        _, agirlik = self.yigin[mevcut_pozisyon]
        sol_cocuk_pozisyon = sol_cocuk_pozisyonu_al(mevcut_pozisyon)
        sag_cocuk_pozisyon = sag_cocuk_pozisyonu_al(mevcut_pozisyon)
        if sol_cocuk_pozisyon < self.eleman_sayisi and sag_cocuk_pozisyon < self.eleman_sayisi:
            _, sol_cocuk_agirlik = self.yigin[sol_cocuk_pozisyon]
            _, sag_cocuk_agirlik = self.yigin[sag_cocuk_pozisyon]
            if sag_cocuk_agirlik < sol_cocuk_agirlik and sag_cocuk_agirlik < agirlik:
                self.dugum_degistir(sag_cocuk_pozisyon, mevcut_pozisyon)
                return self.asagi_kaydir(eleman)
        if sol_cocuk_pozisyon < self.eleman_sayisi:
            _, sol_cocuk_agirlik = self.yigin[sol_cocuk_pozisyon]
            if sol_cocuk_agirlik < agirlik:
                self.dugum_degistir(sol_cocuk_pozisyon, mevcut_pozisyon)
                return self.asagi_kaydir(eleman)
        else:
            return None
        if sag_cocuk_pozisyon < self.eleman_sayisi:
            _, sag_cocuk_agirlik = self.yigin[sag_cocuk_pozisyon]
            if sag_cocuk_agirlik < agirlik:
                self.dugum_degistir(sag_cocuk_pozisyon, mevcut_pozisyon)
                return self.asagi_kaydir(eleman)
        return None

    def dugum_degistir(self, dugum1_pozisyon: int, dugum2_pozisyon: int) -> None:
        # Verilen pozisyonlardaki düğümleri değiştir
        dugum1_eleman = self.yigin[dugum1_pozisyon][0]
        dugum2_eleman = self.yigin[dugum2_pozisyon][0]
        self.yigin[dugum1_pozisyon], self.yigin[dugum2_pozisyon] = (
            self.yigin[dugum2_pozisyon],
            self.yigin[dugum1_pozisyon],
        )
        self.pozisyon_haritasi[dugum1_eleman] = dugum2_pozisyon
        self.pozisyon_haritasi[dugum2_eleman] = dugum1_pozisyon


class YonsuzAgirlikliGrafik(Generic[T]):
    """
    Yönsüz Ağırlıklı Grafik Sınıfı

    Fonksiyonlar:
    dugum_ekle: grafiğe bir düğüm ekleyen fonksiyon
    kenar_ekle: grafikte 2 düğüm arasında bir kenar ekleyen fonksiyon
    """

    def __init__(self) -> None:
        self.baglantilar: dict[T, dict[T, int]] = {}
        self.dugum_sayisi: int = 0

    def __repr__(self) -> str:
        return str(self.baglantilar)

    def __len__(self) -> int:
        return self.dugum_sayisi

    def dugum_ekle(self, dugum: T) -> None:
        # Düğüm grafikte yoksa ekle
        if dugum not in self.baglantilar:
            self.baglantilar[dugum] = {}
            self.dugum_sayisi += 1

    def kenar_ekle(self, dugum1: T, dugum2: T, agirlik: int) -> None:
        # Grafikte 2 düğüm arasında bir kenar ekle
        self.dugum_ekle(dugum1)
        self.dugum_ekle(dugum2)
        self.baglantilar[dugum1][dugum2] = agirlik
        self.baglantilar[dugum2][dugum1] = agirlik


def prims_algoritmasi(
    grafik: YonsuzAgirlikliGrafik[T],
) -> tuple[dict[T, int], dict[T, T | None]]:
    """
    >>> grafik = YonsuzAgirlikliGrafik()

    >>> grafik.kenar_ekle("a", "b", 3)
    >>> grafik.kenar_ekle("b", "c", 10)
    >>> grafik.kenar_ekle("c", "d", 5)
    >>> grafik.kenar_ekle("a", "c", 15)
    >>> grafik.kenar_ekle("b", "d", 100)

    >>> mesafe, ebeveyn = prims_algoritmasi(grafik)

    >>> abs(mesafe["a"] - mesafe["b"])
    3
    >>> abs(mesafe["d"] - mesafe["b"])
    15
    >>> abs(mesafe["a"] - mesafe["c"])
    13
    """
    # Prim'in minimum yayılım ağacı algoritması
    mesafe: dict[T, int] = {dugum: maxsize for dugum in grafik.baglantilar}
    ebeveyn: dict[T, T | None] = {dugum: None for dugum in grafik.baglantilar}

    oncelik_kuyrugu: MinOncelikKuyrugu[T] = MinOncelikKuyrugu()
    for dugum, agirlik in mesafe.items():
        oncelik_kuyrugu.ekle(dugum, agirlik)

    if oncelik_kuyrugu.bos_mu():
        return mesafe, ebeveyn

    # Başlangıç
    dugum = oncelik_kuyrugu.min_cikar()
    mesafe[dugum] = 0
    for komsu in grafik.baglantilar[dugum]:
        if mesafe[komsu] > mesafe[dugum] + grafik.baglantilar[dugum][komsu]:
            mesafe[komsu] = mesafe[dugum] + grafik.baglantilar[dugum][komsu]
            oncelik_kuyrugu.anahtar_guncelle(komsu, mesafe[komsu])
            ebeveyn[komsu] = dugum

    # Prim'in algoritmasını çalıştırma
    while not oncelik_kuyrugu.bos_mu():
        dugum = oncelik_kuyrugu.min_cikar()
        for komsu in grafik.baglantilar[dugum]:
            if mesafe[komsu] > mesafe[dugum] + grafik.baglantilar[dugum][komsu]:
                mesafe[komsu] = mesafe[dugum] + grafik.baglantilar[dugum][komsu]
                oncelik_kuyrugu.anahtar_guncelle(komsu, mesafe[komsu])
                ebeveyn[komsu] = dugum
    return mesafe, ebeveyn
