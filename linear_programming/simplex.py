"""
Tablo formunda doğrusal programları çözmek için simplex algoritmasının Python
uygulaması
- `>=`, `<=` ve `=` kısıtlamaları ve
- her değişken `x1, x2, ...>= 0`.

Doğrusal programları simplex tablolarına dönüştürme ve simplex algoritmasında
atılan adımlar için https://gist.github.com/imengus/f9619a568f7da5bc74eaf20169a24d98
adresine bakın.

Kaynaklar:
https://tr.wikipedia.org/wiki/Simplex_algoritması
https://tinyurl.com/simplex4beginners
Katkı:K. Umut Araz
"""

from typing import Any

import numpy as np


class Tablo:
    """Simplex tabloları üzerinde işlem yapar

    >>> Tablo(np.array([[-1,-1,0,0,1],[1,3,1,0,4],[3,1,0,1,4]]), 2, 2)
    Traceback (most recent call last):
    ...
    TypeError: Tablo float64 türünde olmalıdır

    >>> Tablo(np.array([[-1,-1,0,0,-1],[1,3,1,0,4],[3,1,0,1,4.]]), 2, 2)
    Traceback (most recent call last):
    ...
    ValueError: RHS > 0 olmalıdır

    >>> Tablo(np.array([[-1,-1,0,0,1],[1,3,1,0,4],[3,1,0,1,4.]]), -2, 2)
    Traceback (most recent call last):
    ...
    ValueError: (yapay) değişkenlerin sayısı doğal bir sayı olmalıdır
    """

    # Döngüden kaçınmak için maksimum iterasyon sayısı
    maxiter = 100

    def __init__(
        self, tablo: np.ndarray, n_vars: int, n_yapay_vars: int
    ) -> None:
        if tablo.dtype != "float64":
            raise TypeError("Tablo float64 türünde olmalıdır")

        # RHS'nin negatif olup olmadığını kontrol et
        if not (tablo[:, -1] >= 0).all():
            raise ValueError("RHS > 0 olmalıdır")

        if n_vars < 2 or n_yapay_vars < 0:
            raise ValueError(
                "(yapay) değişkenlerin sayısı doğal bir sayı olmalıdır"
            )

        self.tablo = tablo
        self.n_satirlar, n_sutunlar = tablo.shape

        # Karar değişkenlerinin sayısı x1, x2, x3...
        self.n_vars, self.n_yapay_vars = n_vars, n_yapay_vars

        # >= veya == kısıtlamaları varsa 2 (standart olmayan), aksi takdirde 1 (standart)
        self.n_asamalar = (self.n_yapay_vars > 0) + 1

        # Eşitsizlikleri eşitliklere dönüştürmek için eklenen gevşeklik değişkenlerinin sayısı
        self.n_gevseklik = n_sutunlar - self.n_vars - self.n_yapay_vars - 1

        # Her aşama için hedefler
        self.hedefler = ["max"]

        # İki aşamalı simplex'te önce minimize et, sonra maksimize et
        if self.n_yapay_vars:
            self.hedefler.append("min")

        self.sutun_basliklari = self.sutun_basliklari_olustur()

        # Mevcut pivot satır ve sütununun indeksi
        self.satir_idx = None
        self.sutun_idx = None

        # Hedef satır sadece (negatif olmayan) değerler içeriyor mu?
        self.dur_iter = False

    def sutun_basliklari_olustur(self) -> list[str]:
        """Belirli boyutlardaki tablo için sütun başlıklarını oluşturur

        >>> Tablo(np.array([[-1,-1,0,0,1],[1,3,1,0,4],[3,1,0,1,4.]]),
        ... 2, 0).sutun_basliklari_olustur()
        ['x1', 'x2', 's1', 's2', 'RHS']

        >>> Tablo(np.array([[-1,-1,0,0,1],[1,3,1,0,4],[3,1,0,1,4.]]),
        ... 2, 2).sutun_basliklari_olustur()
        ['x1', 'x2', 'RHS']
        """
        args = (self.n_vars, self.n_gevseklik)

        # karar | gevseklik
        string_baslangiclari = ["x", "s"]
        basliklar = []
        for i in range(2):
            for j in range(args[i]):
                basliklar.append(string_baslangiclari[i] + str(j + 1))
        basliklar.append("RHS")
        return basliklar

    def pivot_bul(self) -> tuple[Any, Any]:
        """Pivot satır ve sütunu bulur.
        >>> tuple(int(x) for x in Tablo(np.array([[-2,1,0,0,0], [3,1,1,0,6],
        ... [1,2,0,1,7.]]), 2, 0).pivot_bul())
        (1, 0)
        """
        hedef = self.hedefler[-1]

        # Hedef satırlardaki en yüksek büyüklükteki girişleri bulun
        isaret = (hedef == "min") - (hedef == "max")
        sutun_idx = np.argmax(isaret * self.tablo[0, :-1])

        # Seçim yalnızca maksimize için 0'ın altında ve minimize için üstünde geçerlidir
        if isaret * self.tablo[0, sutun_idx] <= 0:
            self.dur_iter = True
            return 0, 0

        # Pivot satırı, pivot sütunundaki elemanların sağ tarafı böldüğünde
        # en düşük bölümü olan olarak seçilir

        # Hedef satırları hariç tutarak dilimle
        s = slice(self.n_asamalar, self.n_satirlar)

        # RHS
        bolunen = self.tablo[s, -1]

        # Dilim içindeki pivot sütununun elemanları
        bolen = self.tablo[s, sutun_idx]

        # NaN'larla dolu dizi
        nans = np.full(self.n_satirlar - self.n_asamalar, np.nan)

        # Pivot sütunundaki eleman sıfırdan büyükse, bölümü veya aksi takdirde nan'ı döndür
        bolumler = np.divide(bolunen, bolen, out=nans, where=bolen > 0)

        # NaN değerleri hariç tutarak en düşük bölümün argümanı. n_asamalar,
        # daha önce hedef sütunların hariç tutulmasını telafi etmek için eklenir
        satir_idx = np.nanargmin(bolumler) + self.n_asamalar
        return satir_idx, sutun_idx

    def pivot(self, satir_idx: int, sutun_idx: int) -> np.ndarray:
        """Pivot satır ve sütunun kesişimindeki değeri pivotlar.

        >>> Tablo(np.array([[-2,-3,0,0,0],[1,3,1,0,4],[3,1,0,1,4.]]),
        ... 2, 2).pivot(1, 0).tolist()
        ... # doctest: +NORMALIZE_WHITESPACE
        [[0.0, 3.0, 2.0, 0.0, 8.0],
        [1.0, 3.0, 1.0, 0.0, 4.0],
        [0.0, -8.0, -3.0, 1.0, -8.0]]
        """
        # Orijinal tabloya değişiklik yapmaktan kaçının
        pivot_satir = self.tablo[satir_idx].copy()

        pivot_deger = pivot_satir[sutun_idx]

        # Giriş 1 olur
        pivot_satir *= 1 / pivot_deger

        # Pivot sütunundaki değişken temel hale gelir, yani tek sıfır olmayan giriş
        for idx, katsayi in enumerate(self.tablo[:, sutun_idx]):
            self.tablo[idx] += -katsayi * pivot_satir
        self.tablo[satir_idx] = pivot_satir
        return self.tablo

    def asama_degistir(self) -> np.ndarray:
        """İki aşamalı yöntemin ilk aşamasından çıkarak yapay satır ve sütunları
        siler veya standart durumu tamamlayarak algoritmayı tamamlar.

        >>> Tablo(np.array([
        ... [3, 3, -1, -1, 0, 0, 4],
        ... [2, 1, 0, 0, 0, 0, 0.],
        ... [1, 2, -1, 0, 1, 0, 2],
        ... [2, 1, 0, -1, 0, 1, 2]
        ... ]), 2, 2).asama_degistir().tolist()
        ... # doctest: +NORMALIZE_WHITESPACE
        [[2.0, 1.0, 0.0, 0.0, 0.0],
        [1.0, 2.0, -1.0, 0.0, 2.0],
        [2.0, 1.0, 0.0, -1.0, 2.0]]
        """
        # Orijinal hedef satırının hedefi kalır
        self.hedefler.pop()

        if not self.hedefler:
            return self.tablo

        # Yapay sütunlar için kimlikleri içeren dilim
        s = slice(-self.n_yapay_vars - 1, -1)

        # Yapay değişken sütunlarını sil
        self.tablo = np.delete(self.tablo, s, axis=1)

        # İlk aşamanın hedef satırını sil
        self.tablo = np.delete(self.tablo, 0, axis=0)

        self.n_asamalar = 1
        self.n_satirlar -= 1
        self.n_yapay_vars = 0
        self.dur_iter = False
        return self.tablo

    def simplex_calistir(self) -> dict[Any, Any]:
        """Tablo üzerinde hedef fonksiyon daha fazla iyileştirilemeyecek
        duruma gelene kadar işlem yapar.

        # Standart doğrusal program:
        Max:  x1 +  x2
        ST:   x1 + 3x2 <= 4
             3x1 +  x2 <= 4
        >>> {key: float(value) for key, value in Tablo(np.array([[-1,-1,0,0,0],
        ... [1,3,1,0,4],[3,1,0,1,4.]]), 2, 0).simplex_calistir().items()}
        {'P': 2.0, 'x1': 1.0, 'x2': 1.0}

        # 3 değişkenli standart doğrusal program:
        Max: 3x1 +  x2 + 3x3
        ST:  2x1 +  x2 +  x3 ≤ 2
              x1 + 2x2 + 3x3 ≤ 5
             2x1 + 2x2 +  x3 ≤ 6
        >>> {key: float(value) for key, value in Tablo(np.array([
        ... [-3,-1,-3,0,0,0,0],
        ... [2,1,1,1,0,0,2],
        ... [1,2,3,0,1,0,5],
        ... [2,2,1,0,0,1,6.]
        ... ]),3,0).simplex_calistir().items()} # doctest: +ELLIPSIS
        {'P': 5.4, 'x1': 0.199..., 'x3': 1.6}


        # Optimal tablo girişi:
        >>> {key: float(value) for key, value in Tablo(np.array([
        ... [0, 0, 0.25, 0.25, 2],
        ... [0, 1, 0.375, -0.125, 1],
        ... [1, 0, -0.125, 0.375, 1]
        ... ]), 2, 0).simplex_calistir().items()}
        {'P': 2.0, 'x1': 1.0, 'x2': 1.0}

        # Standart olmayan: >= kısıtlamaları
        Max: 2x1 + 3x2 +  x3
        ST:   x1 +  x2 +  x3 <= 40
             2x1 +  x2 -  x3 >= 10
                 -  x2 +  x3 >= 10
        >>> {key: float(value) for key, value in Tablo(np.array([
        ... [2, 0, 0, 0, -1, -1, 0, 0, 20],
        ... [-2, -3, -1, 0, 0, 0, 0, 0, 0],
        ... [1, 1, 1, 1, 0, 0, 0, 0, 40],
        ... [2, 1, -1, 0, -1, 0, 1, 0, 10],
        ... [0, -1, 1, 0, 0, -1, 0, 1, 10.]
        ... ]), 3, 2).simplex_calistir().items()}
        {'P': 70.0, 'x1': 10.0, 'x2': 10.0, 'x3': 20.0}

        # Standart olmayan: minimizasyon ve eşitlikler
        Min: x1 +  x2
        ST: 2x1 +  x2 = 12
            6x1 + 5x2 = 40
        >>> {key: float(value) for key, value in Tablo(np.array([
        ... [8, 6, 0, 0, 52],
        ... [1, 1, 0, 0, 0],
        ... [2, 1, 1, 0, 12],
        ... [6, 5, 0, 1, 40.],
        ... ]), 2, 2).simplex_calistir().items()}
        {'P': 7.0, 'x1': 5.0, 'x2': 2.0}


        # Gevşeklik değişkenlerinde pivot
        Max: 8x1 + 6x2
        ST:   x1 + 3x2 <= 33
             4x1 + 2x2 <= 48
             2x1 + 4x2 <= 48
              x1 +  x2 >= 10
             x1        >= 2
        >>> {key: float(value) for key, value in Tablo(np.array([
        ... [2, 1, 0, 0, 0, -1, -1, 0, 0, 12.0],
        ... [-8, -6, 0, 0, 0, 0, 0, 0, 0, 0.0],
        ... [1, 3, 1, 0, 0, 0, 0, 0, 0, 33.0],
        ... [4, 2, 0, 1, 0, 0, 0, 0, 0, 60.0],
        ... [2, 4, 0, 0, 1, 0, 0, 0, 0, 48.0],
        ... [1, 1, 0, 0, 0, -1, 0, 1, 0, 10.0],
        ... [1, 0, 0, 0, 0, 0, -1, 0, 1, 2.0]
        ... ]), 2, 2).simplex_calistir().items()} # doctest: +ELLIPSIS
        {'P': 132.0, 'x1': 12.000... 'x2': 5.999...}
        """
        # Simplex algoritmasının döngüden kaçınmasını durdurun.
        for _ in range(Tablo.maxiter):
            # Her aşamanın tamamlanması bir hedefi kaldırır. Eğer her iki aşama
            # da tamamsa, artık hedef kalmaz
            if not self.hedefler:
                # Optimal çözümde her değişkenin değerlerini bulun
                return self.tabloyu_yorumla()

            satir_idx, sutun_idx = self.pivot_bul()

            # Hedef satırda daha fazla negatif değer yoksa
            if self.dur_iter:
                # Yapay değişken sütunlarını ve satırlarını sil. Öznitelikleri güncelle
                self.tablo = self.asama_degistir()
            else:
                self.tablo = self.pivot(satir_idx, sutun_idx)
        return {}

    def tabloyu_yorumla(self) -> dict[str, float]:
        """Son tablo verildiğinde, temel karar değişkenlerinin
        karşılık gelen değerlerini `output_dict`e ekleyin
        >>> {key: float(value) for key, value in Tablo(np.array([
        ... [0,0,0.875,0.375,5],
        ... [0,1,0.375,-0.125,1],
        ... [1,0,-0.125,0.375,1]
        ... ]),2, 0).tabloyu_yorumla().items()}
        {'P': 5.0, 'x1': 1.0, 'x2': 1.0}
        """
        # P = son tablonun RHS'si
        output_dict = {"P": abs(self.tablo[0, -1])}

        for i in range(self.n_vars):
            # i. sütundaki sıfır olmayan girişlerin dizinlerini verir
            nonzero = np.nonzero(self.tablo[:, i])
            n_nonzero = len(nonzero[0])

            # Sıfır olmayan dizinlerdeki ilk giriş
            nonzero_satiridx = nonzero[0][0]
            nonzero_deger = self.tablo[nonzero_satiridx, i]

            # Sütunda yalnızca bir sıfır olmayan değer varsa, bu bir
            if n_nonzero == 1 and nonzero_deger == 1:
                rhs_deger = self.tablo[nonzero_satiridx, -1]
                output_dict[self.sutun_basliklari[i]] = rhs_deger
        return output_dict


if __name__ == "__main__":
    import doctest

    doctest.testmod()
