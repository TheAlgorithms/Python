# Matrisleri temsil etmek ve manipüle etmek için OOP yaklaşımı

from __future__ import annotations


class Matris:
    """
    Organised By K. Umut Araz

    
    Her bir elemanı bir satırı temsil eden 2D bir diziden oluşturulan Matris nesnesi.
    Satırlar int veya float türünde değerler içerebilir.
    Yaygın işlemler ve bilgiler mevcuttur.
    >>> satirlar = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> matris = Matris(satirlar)
    >>> print(matris)
    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]]

    Matris satırları ve sütunları 2D diziler olarak mevcuttur.
    >>> matris.satirlar
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matris.sutunlar()
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    Boyut bir tuple olarak döner.
    >>> matris.boyut
    (3, 3)

    Karelik ve terslenebilirlik bool olarak temsil edilir.
    >>> matris.kare_mi
    True
    >>> matris.terslenebilir_mi()
    False

    Kimlik, Minörler, Cofaktörler ve Adjugate Matris olarak döner. Tersi
    bir Matris veya NoneType olabilir.
    >>> print(matris.kimlik())
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    >>> print(matris.minorler())
    [[-3. -6. -3.]
     [-6. -12. -6.]
     [-3. -6. -3.]]
    >>> print(matris.cofaktörler())
    [[-3. 6. -3.]
     [6. -12. 6.]
     [-3. 6. -3.]]
    >>> print(matris.adjugate())
    [[-3. 6. -3.]
     [6. -12. 6.]
     [-3. 6. -3.]]
    >>> matris.ters()
    Traceback (most recent call last):
        ...
    TypeError: Sadece sıfırdan farklı determinantı olan matrislerin tersi vardır.

    Determinant bir int, float veya NoneType'tır.
    >>> matris.determinant()
    0

    Negasyon, skalar çarpma, toplama, çıkarma, çarpma ve
    üstel işlemler mevcuttur ve hepsi bir Matris döner.
    >>> print(-matris)
    [[-1. -2. -3.]
     [-4. -5. -6.]
     [-7. -8. -9.]]
    >>> matris2 = matris * 3
    >>> print(matris2)
    [[3. 6. 9.]
     [12. 15. 18.]
     [21. 24. 27.]]
    >>> print(matris + matris2)
    [[4. 8. 12.]
     [16. 20. 24.]
     [28. 32. 36.]]
    >>> print(matris - matris2)
    [[-2. -4. -6.]
     [-8. -10. -12.]
     [-14. -16. -18.]]
    >>> print(matris ** 3)
    [[468. 576. 684.]
     [1062. 1305. 1548.]
     [1656. 2034. 2412.]]

    Matrisler de değiştirilebilir.
    >>> matris.satir_ekle([10, 11, 12])
    >>> print(matris)
    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]
     [10. 11. 12.]]
    >>> matris2.sutun_ekle([8, 16, 32])
    >>> print(matris2)
    [[3. 6. 9. 8.]
     [12. 15. 18. 16.]
     [21. 24. 27. 32.]]
    >>> print(matris *  matris2)
    [[90. 108. 126. 136.]
     [198. 243. 288. 304.]
     [306. 378. 450. 472.]
     [414. 513. 612. 640.]]
    """

    def __init__(self, satirlar: list[list[int]]):
        hata = TypeError(
            "Matrisler, en az bir ve aynı sayıda değer içeren, sıfır veya daha fazla "
            "liste içeren bir listeden oluşmalıdır. Her bir değer int veya float türünde olmalıdır."
        )
        if len(satirlar) != 0:
            sutunlar = len(satirlar[0])
            if sutunlar == 0:
                raise hata
            for satir in satirlar:
                if len(satir) != sutunlar:
                    raise hata
                for deger in satir:
                    if not isinstance(deger, (int, float)):
                        raise hata
            self.satirlar = satirlar
        else:
            self.satirlar = []

    # MATRIS BİLGİLERİ
    def sutunlar(self) -> list[list[int]]:
        return [[satir[i] for satir in self.satirlar] for i in range(len(self.satirlar[0]))]

    @property
    def satir_sayisi(self) -> int:
        return len(self.satirlar)

    @property
    def sutun_sayisi(self) -> int:
        return len(self.satirlar[0])

    @property
    def boyut(self) -> tuple[int, int]:
        return self.satir_sayisi, self.sutun_sayisi

    @property
    def kare_mi(self) -> bool:
        return self.boyut[0] == self.boyut[1]

    def kimlik(self) -> Matris:
        degerler = [
            [0 if sutun_num != satir_num else 1 for sutun_num in range(self.satir_sayisi)]
            for satir_num in range(self.satir_sayisi)
        ]
        return Matris(degerler)

    def determinant(self) -> int:
        if not self.kare_mi:
            return 0
        if self.boyut == (0, 0):
            return 1
        if self.boyut == (1, 1):
            return int(self.satirlar[0][0])
        if self.boyut == (2, 2):
            return int(
                (self.satirlar[0][0] * self.satirlar[1][1])
                - (self.satirlar[0][1] * self.satirlar[1][0])
            )
        else:
            return sum(
                self.satirlar[0][sutun] * self.cofaktörler().satirlar[0][sutun]
                for sutun in range(self.sutun_sayisi)
            )

    def terslenebilir_mi(self) -> bool:
        return bool(self.determinant())

    def minor_al(self, satir: int, sutun: int) -> int:
        degerler = [
            [
                self.satirlar[dig_satir][dig_sutun]
                for dig_sutun in range(self.sutun_sayisi)
                if dig_sutun != sutun
            ]
            for dig_satir in range(self.satir_sayisi)
            if dig_satir != satir
        ]
        return Matris(degerler).determinant()

    def cofactor_al(self, satir: int, sutun: int) -> int:
        if (satir + sutun) % 2 == 0:
            return self.minor_al(satir, sutun)
        return -1 * self.minor_al(satir, sutun)

    def minorler(self) -> Matris:
        return Matris(
            [
                [self.minor_al(satir, sutun) for sutun in range(self.sutun_sayisi)]
                for satir in range(self.satir_sayisi)
            ]
        )

    def cofactörler(self) -> Matris:
        return Matris(
            [
                [
                    self.minorler().satirlar[satir][sutun]
                    if (satir + sutun) % 2 == 0
                    else self.minorler().satirlar[satir][sutun] * -1
                    for sutun in range(self.minorler().sutun_sayisi)
                ]
                for satir in range(self.minorler().satir_sayisi)
            ]
        )

    def adjugate(self) -> Matris:
        degerler = [
            [self.cofaktörler().satirlar[sutun][satir] for sutun in range(self.sutun_sayisi)]
            for satir in range(self.satir_sayisi)
        ]
        return Matris(degerler)

    def ters(self) -> Matris:
        determinant = self.determinant()
        if not determinant:
            raise TypeError("Sadece sıfırdan farklı determinantı olan matrislerin tersi vardır.")
        return self.adjugate() * (1 / determinant)

    def __repr__(self) -> str:
        return str(self.satirlar)

    def __str__(self) -> str:
        if self.satir_sayisi == 0:
            return "[]"
        if self.satir_sayisi == 1:
            return "[[" + ". ".join(str(self.satirlar[0])) + "]]"
        return (
            "["
            + "\n ".join(
                [
                    "[" + ". ".join([str(deger) for deger in satir]) + ".]"
                    for satir in self.satirlar
                ]
            )
            + "]"
        )

    # MATRIS MANİPÜLASYONU
    def satir_ekle(self, satir: list[int], konum: int | None = None) -> None:
        tip_hatasi = TypeError("Satır, tüm int ve/veya float değerlerini içeren bir liste olmalıdır.")
        if not isinstance(satir, list):
            raise tip_hatasi
        for deger in satir:
            if not isinstance(deger, (int, float)):
                raise tip_hatasi
        if len(satir) != self.sutun_sayisi:
            raise ValueError(
                "Satır, matrisin diğer satırlarıyla aynı uzunlukta olmalıdır."
            )
        if konum is None:
            self.satirlar.append(satir)
        else:
            self.satirlar = self.satirlar[0:konum] + [satir] + self.satirlar[konum:]

    def sutun_ekle(self, sutun: list[int], konum: int | None = None) -> None:
        tip_hatasi = TypeError(
            "Sütun, tüm int ve/veya float değerlerini içeren bir liste olmalıdır."
        )
        if not isinstance(sutun, list):
            raise tip_hatasi
        for deger in sutun:
            if not isinstance(deger, (int, float)):
                raise tip_hatasi
        if len(sutun) != self.satir_sayisi:
            raise ValueError(
                "Sütun, matrisin diğer sütunlarıyla aynı uzunlukta olmalıdır."
            )
        if konum is None:
            self.satirlar = [self.satirlar[i] + [sutun[i]] for i in range(self.satir_sayisi)]
        else:
            self.satirlar = [
                self.satirlar[i][0:konum] + [sutun[i]] + self.satirlar[i][konum:]
                for i in range(self.satir_sayisi)
            ]

    # MATRIS İŞLEMLERİ
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matris):
            return NotImplemented
        return self.satirlar == other.satirlar

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __neg__(self) -> Matris:
        return self * -1

    def __add__(self, other: Matris) -> Matris:
        if self.boyut != other.boyut:
            raise ValueError("Toplama, aynı boyuttaki matrisleri gerektirir.")
        return Matris(
            [
                [self.satirlar[i][j] + other.satirlar[i][j] for j in range(self.sutun_sayisi)]
                for i in range(self.satir_sayisi)
            ]
        )

    def __sub__(self, other: Matris) -> Matris:
        if self.boyut != other.boyut:
            raise ValueError("Çıkarma, aynı boyuttaki matrisleri gerektirir.")
        return Matris(
            [
                [self.satirlar[i][j] - other.satirlar[i][j] for j in range(self.sutun_sayisi)]
                for i in range(self.satir_sayisi)
            ]
        )

    def __mul__(self, other: Matris | float) -> Matris:
        if isinstance(other, (int, float)):
            return Matris(
                [[int(eleman * other) for eleman in satir] for satir in self.satirlar]
            )
        elif isinstance(other, Matris):
            if self.sutun_sayisi != other.satir_sayisi:
                raise ValueError(
                    "İlk matrisin sütun sayısı, ikinci matrisin satır sayısına eşit olmalıdır."
                )
            return Matris(
                [
                    [Matris.nokta_çarpımı(satir, sutun) for sutun in other.sutunlar()]
                    for satir in self.satirlar
                ]
            )
        else:
            raise TypeError(
                "Bir Matris yalnızca bir int, float veya başka bir matris ile çarpılabilir."
            )

    def __pow__(self, other: int) -> Matris:
        if not isinstance(other, int):
            raise TypeError("Bir Matris yalnızca bir int kuvvetine yükseltilebilir.")
        if not self.kare_mi:
            raise ValueError("Yalnızca kare matrisler kuvvet alınabilir.")
        if other == 0:
            return self.kimlik()
        if other < 0:
            if self.terslenebilir_mi():
                return self.ters() ** (-other)
            raise ValueError(
                "Yalnızca terslenebilir matrisler negatif kuvvet alınabilir."
            )
        sonuc = self
        for _ in range(other - 1):
            sonuc *= self
        return sonuc

    @classmethod
    def nokta_çarpımı(cls, satir: list[int], sutun: list[int]) -> int:
        return sum(satir[i] * sutun[i] for i in range(len(satir)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
