from __future__ import annotations

from typing import Any


class Matris:
    """
    <class Matris>
    Matris yapısı.
    

    Organizatör: K. Umut Araz

    """

    def __init__(self, satir: int, sutun: int, varsayılan_değer: float = 0) -> None:
        """
        <method Matris.__init__>
        Verilen boyut ve varsayılan değer ile matrisi başlat.
        Örnek:
        >>> a = Matris(2, 3, 1)
        >>> a
        2 satır ve 3 sütundan oluşan matris
        [1, 1, 1]
        [1, 1, 1]
        """

        self.satir, self.sutun = satir, sutun
        self.dizi = [[varsayılan_değer for _ in range(sutun)] for _ in range(satir)]

    def __str__(self) -> str:
        """
        <method Matris.__str__>
        Bu matrisin string temsilini döndür.
        """

        # Ön ek
        s = f"{self.satir} satır ve {self.sutun} sütundan oluşan matris\n"

        # String format tanımlayıcı
        max_eleman_uzunluğu = max(len(str(obj)) for satir_vektörü in self.dizi for obj in satir_vektörü)
        string_format_tanımlayıcı = f"%{max_eleman_uzunluğu}s"

        # String oluştur ve döndür
        def tek_satir(satir_vektörü: list[float]) -> str:
            satir = "["
            satir += ", ".join(string_format_tanımlayıcı % (obj,) for obj in satir_vektörü)
            satir += "]"
            return satir

        s += "\n".join(tek_satir(satir_vektörü) for satir_vektörü in self.dizi)
        return s

    def __repr__(self) -> str:
        return str(self)

    def indeksleri_doğrula(self, konum: tuple[int, int]) -> bool:
        """
        <method Matris.indeksleri_doğrula>
        Verilen indekslerin matristen eleman almak için geçerli olup olmadığını kontrol et.
        Örnek:
        >>> a = Matris(2, 6, 0)
        >>> a.indeksleri_doğrula((2, 7))
        False
        >>> a.indeksleri_doğrula((0, 0))
        True
        """
        if not (isinstance(konum, (list, tuple)) and len(konum) == 2):  # noqa: SIM114
            return False
        elif not (0 <= konum[0] < self.satir and 0 <= konum[1] < self.sutun):
            return False
        return True

    def __getitem__(self, konum: tuple[int, int]) -> Any:
        """
        <method Matris.__getitem__>
        loc = (satir, sütun) iken dizi[satir][sütun] döndür.
        Örnek:
        >>> a = Matris(3, 2, 7)
        >>> a[1, 0]
        7
        """
        assert self.indeksleri_doğrula(konum)
        return self.dizi[konum[0]][konum[1]]

    def __setitem__(self, konum: tuple[int, int], değer: float) -> None:
        """
        <method Matris.__setitem__>
        loc = (satir, sütun) iken dizi[satir][sütun] = değer olarak ayarla.
        Örnek:
        >>> a = Matris(2, 3, 1)
        >>> a[1, 2] = 51
        >>> a
        2 satır ve 3 sütundan oluşan matris
        [ 1,  1,  1]
        [ 1,  1, 51]
        """
        assert self.indeksleri_doğrula(konum)
        self.dizi[konum[0]][konum[1]] = değer

    def __add__(self, başka: Matris) -> Matris:
        """
        <method Matris.__add__>
        self + başka döndür.
        Örnek:
        >>> a = Matris(2, 1, -4)
        >>> b = Matris(2, 1, 3)
        >>> a + b
        2 satır ve 1 sütundan oluşan matris
        [-1]
        [-1]
        """

        # Doğrulama
        assert isinstance(başka, Matris)
        assert self.satir == başka.satir
        assert self.sutun == başka.sutun

        # Topla
        sonuç = Matris(self.satir, self.sutun)
        for r in range(self.satir):
            for c in range(self.sutun):
                sonuç[r, c] = self[r, c] + başka[r, c]
        return sonuç

    def __neg__(self) -> Matris:
        """
        <method Matris.__neg__>
        -self döndür.
        Örnek:
        >>> a = Matris(2, 2, 3)
        >>> a[0, 1] = a[1, 0] = -2
        >>> -a
        2 satır ve 2 sütundan oluşan matris
        [-3,  2]
        [ 2, -3]
        """

        sonuç = Matris(self.satir, self.sutun)
        for r in range(self.satir):
            for c in range(self.sutun):
                sonuç[r, c] = -self[r, c]
        return sonuç

    def __sub__(self, başka: Matris) -> Matris:
        return self + (-başka)

    def __mul__(self, başka: float | Matris) -> Matris:
        """
        <method Matris.__mul__>
        self * başka döndür.
        Örnek:
        >>> a = Matris(2, 3, 1)
        >>> a[0, 2] = a[1, 2] = 3
        >>> a * -2
        2 satır ve 3 sütundan oluşan matris
        [-2, -2, -6]
        [-2, -2, -6]
        """

        if isinstance(başka, (int, float)):  # Skalar çarpma
            sonuç = Matris(self.satir, self.sutun)
            for r in range(self.satir):
                for c in range(self.sutun):
                    sonuç[r, c] = self[r, c] * başka
            return sonuç
        elif isinstance(başka, Matris):  # Matris çarpma
            assert self.sutun == başka.satir
            sonuç = Matris(self.satir, başka.sutun)
            for r in range(self.satir):
                for c in range(başka.sutun):
                    for i in range(self.sutun):
                        sonuç[r, c] += self[r, i] * başka[i, c]
            return sonuç
        else:
            msg = f"Başka için desteklenmeyen tür verildi ({type(başka)})"
            raise TypeError(msg)

    def transpoze(self) -> Matris:
        """
        <method Matris.transpoze>
        self^T döndür.
        Örnek:
        >>> a = Matris(2, 3)
        >>> for r in range(2):
        ...     for c in range(3):
        ...             a[r, c] = r * c
        ...
        >>> a.transpoze()
        3 satır ve 2 sütundan oluşan matris
        [0, 0]
        [0, 1]
        [0, 2]
        """

        sonuç = Matris(self.sutun, self.satir)
        for r in range(self.satir):
            for c in range(self.sutun):
                sonuç[c, r] = self[r, c]
        return sonuç

    def sherman_morrison(self, u: Matris, v: Matris) -> Any:
        """
        <method Matris.sherman_morrison>
        Sherman-Morrison formülünü O(n^2) zaman karmaşıklığı ile uygula.
        Bu formülü öğrenmek için lütfen şu kaynağa bakın:
        https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula
        Bu yöntem (A + uv^T)^(-1) döndürür, burada A^(-1) kendisidir. Hesaplamak imkansızsa None döner.
        Uyarı: Bu yöntem kendisinin tersinir olup olmadığını kontrol etmez.
        Bu yöntemi çalıştırmadan önce kendisinin tersinir olduğundan emin olun.
        Örnek:
        >>> ainv = Matris(3, 3, 0)
        >>> for i in range(3): ainv[i, i] = 1
        ...
        >>> u = Matris(3, 1, 0)
        >>> u[0, 0], u[1, 0], u[2, 0] = 1, 2, -3
        >>> v = Matris(3, 1, 0)
        >>> v[0, 0], v[1, 0], v[2, 0] = 4, -2, 5
        >>> ainv.sherman_morrison(u, v)
        3 satır ve 3 sütundan oluşan matris
        [  1.2857142857142856, -0.14285714285714285,   0.3571428571428571]
        [  0.5714285714285714,   0.7142857142857143,   0.7142857142857142]
        [ -0.8571428571428571,  0.42857142857142855,  -0.0714285714285714]
        """

        # Boyut doğrulaması
        assert isinstance(u, Matris)
        assert isinstance(v, Matris)
        assert self.satir == self.sutun == u.satir == v.satir  # u, v sütun vektörü olmalı
        assert u.sutun == v.sutun == 1  # u, v sütun vektörü olmalı

        # Hesapla
        v_t = v.transpoze()
        payda_faktörü = (v_t * self * u)[0, 0] + 1
        if payda_faktörü == 0:
            return None  # Tersinir değil
        return self - ((self * u) * (v_t * self) * (1.0 / payda_faktörü))


# Test
if __name__ == "__main__":

    def test1() -> None:
        # a^(-1)
        ainv = Matris(3, 3, 0)
        for i in range(3):
            ainv[i, i] = 1
        print(f"a^(-1) = {ainv}")
        # u, v
        u = Matris(3, 1, 0)
        u[0, 0], u[1, 0], u[2, 0] = 1, 2, -3
        v = Matris(3, 1, 0)
        v[0, 0], v[1, 0], v[2, 0] = 4, -2, 5
        print(f"u = {u}")
        print(f"v = {v}")
        print(f"uv^T = {u * v.transpoze()}")
        # Sherman Morrison
        print(f"(a + uv^T)^(-1) = {ainv.sherman_morrison(u, v)}")

    def test2() -> None:
        import doctest

        doctest.testmod()

    test2()
