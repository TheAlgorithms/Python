"""
Otomatik Türev (Ters Mod) Gösterimi.

Referans: https://en.wikipedia.org/wiki/Automatic_differentiation

Yazar: Poojan Smart
Email: smrtpoojan@gmail.com
"""

from __future__ import annotations

from collections import defaultdict
from enum import Enum
from types import TracebackType
from typing import Any

import numpy as np
from typing_extensions import Self  # noqa: UP035


class OpType(Enum):
    """
    Değişken üzerinde türev hesaplaması için desteklenen işlemler listesini temsil eder.
    """

    TOPLA = 0
    ÇIKAR = 1
    ÇARP = 2
    BÖL = 3
    MATMUL = 4
    ÜS = 5
    NOOP = 6


class Değişken:
    """
    N-boyutlu nesneyi temsil eden sınıf, numpy dizisini sarmak için kullanılır ve
    işlemler bu değişken üzerinde gerçekleştirilir ve türev hesaplanır.

    Örnekler:
    >>> Değişken(5.0)
    Değişken(5.0)
    >>> Değişken([5.0, 2.9])
    Değişken([5.  2.9])
    >>> Değişken([5.0, 2.9]) + Değişken([1.0, 5.5])
    Değişken([6.  8.4])
    >>> Değişken([[8.0, 10.0]])
    Değişken([[ 8. 10.]])
    """

    def __init__(self, değer: Any) -> None:
        self.değer = np.array(değer)

        # Değişkenin girdi olduğu işlemlere işaretçiler
        self.param_to: list[İşlem] = []
        # Değişkenin çıktısı olduğu işleme işaretçi
        self.result_of: İşlem = İşlem(OpType.NOOP)

    def __repr__(self) -> str:
        return f"Değişken({self.değer})"

    def to_ndarray(self) -> np.ndarray:
        return self.değer

    def __add__(self, diğer: Değişken) -> Değişken:
        sonuç = Değişken(self.değer + diğer.değer)

        with Türevİzleyici() as izleyici:
            # izleyici etkinse, hesaplama grafiği güncellenecek
            if izleyici.etkin:
                izleyici.ekle(OpType.TOPLA, params=[self, diğer], output=sonuç)
        return sonuç

    def __sub__(self, diğer: Değişken) -> Değişken:
        sonuç = Değişken(self.değer - diğer.değer)

        with Türevİzleyici() as izleyici:
            # izleyici etkinse, hesaplama grafiği güncellenecek
            if izleyici.etkin:
                izleyici.ekle(OpType.ÇIKAR, params=[self, diğer], output=sonuç)
        return sonuç

    def __mul__(self, diğer: Değişken) -> Değişken:
        sonuç = Değişken(self.değer * diğer.değer)

        with Türevİzleyici() as izleyici:
            # izleyici etkinse, hesaplama grafiği güncellenecek
            if izleyici.etkin:
                izleyici.ekle(OpType.ÇARP, params=[self, diğer], output=sonuç)
        return sonuç

    def __truediv__(self, diğer: Değişken) -> Değişken:
        sonuç = Değişken(self.değer / diğer.değer)

        with Türevİzleyici() as izleyici:
            # izleyici etkinse, hesaplama grafiği güncellenecek
            if izleyici.etkin:
                izleyici.ekle(OpType.BÖL, params=[self, diğer], output=sonuç)
        return sonuç

    def __matmul__(self, diğer: Değişken) -> Değişken:
        sonuç = Değişken(self.değer @ diğer.değer)

        with Türevİzleyici() as izleyici:
            # izleyici etkinse, hesaplama grafiği güncellenecek
            if izleyici.etkin:
                izleyici.ekle(OpType.MATMUL, params=[self, diğer], output=sonuç)
        return sonuç

    def __pow__(self, güç: int) -> Değişken:
        sonuç = Değişken(self.değer**güç)

        with Türevİzleyici() as izleyici:
            # izleyici etkinse, hesaplama grafiği güncellenecek
            if izleyici.etkin:
                izleyici.ekle(
                    OpType.ÜS,
                    params=[self],
                    output=sonuç,
                    other_params={"güç": güç},
                )
        return sonuç

    def add_param_to(self, param_to: İşlem) -> None:
        self.param_to.append(param_to)

    def add_result_of(self, result_of: İşlem) -> None:
        self.result_of = result_of


class İşlem:
    """
    Tek veya iki Değişken nesnesi arasındaki işlemi temsil eden sınıf.
    İşlem nesneleri, işlem türünü, giriş Değişken nesnelerine işaretçileri ve
    işlemin çıktısına işaretçiyi içerir.
    """

    def __init__(
        self,
        op_type: OpType,
        other_params: dict | None = None,
    ) -> None:
        self.op_type = op_type
        self.other_params = {} if other_params is None else other_params

    def add_params(self, params: list[Değişken]) -> None:
        self.params = params

    def add_output(self, output: Değişken) -> None:
        self.output = output

    def __eq__(self, value) -> bool:
        return self.op_type == value if isinstance(value, OpType) else False


class Türevİzleyici:
    """
    Hesaplama grafiğine dayalı olarak Değişkenin kısmi türevlerini hesaplamak için
    yöntemler içeren sınıf.

    Örnekler:

    >>> with Türevİzleyici() as izleyici:
    ...     a = Değişken([2.0, 5.0])
    ...     b = Değişken([1.0, 2.0])
    ...     m = Değişken([1.0, 2.0])
    ...     c = a + b
    ...     d = a * b
    ...     e = c / d
    >>> izleyici.türev(e, a)
    array([-0.25, -0.04])
    >>> izleyici.türev(e, b)
    array([-1.  , -0.25])
    >>> izleyici.türev(e, m) is None
    True

    >>> with Türevİzleyici() as izleyici:
    ...     a = Değişken([[2.0, 5.0]])
    ...     b = Değişken([[1.0], [2.0]])
    ...     c = a @ b
    >>> izleyici.türev(c, a)
    array([[1., 2.]])
    >>> izleyici.türev(c, b)
    array([[2.],
           [5.]])

    >>> with Türevİzleyici() as izleyici:
    ...     a = Değişken([[2.0, 5.0]])
    ...     b = a ** 3
    >>> izleyici.türev(b, a)
    array([[12., 75.]])
    """

    instance = None

    def __new__(cls) -> Self:
        """
        Sınıf nesnesi oluşturulduğunda çalışır ve nesne zaten oluşturulmuşsa döner.
        Bu sınıf singleton tasarım desenini takip eder.
        """
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.etkin = False

    def __enter__(self) -> Self:
        self.etkin = True
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.etkin = False

    def ekle(
        self,
        op_type: OpType,
        params: list[Değişken],
        output: Değişken,
        other_params: dict | None = None,
    ) -> None:
        """
        Hesaplama grafiği oluşturmak için ilgili Değişken nesnelerine İşlem nesnesi ekler.

        Args:
            op_type: İşlem türü
            params: İşleme giriş parametreleri
            output: İşlemin çıktı değişkeni
        """
        işlem = İşlem(op_type, other_params=other_params)
        param_düğümleri = []
        for param in params:
            param.add_param_to(işlem)
            param_düğümleri.append(param)
        output.add_result_of(işlem)

        işlem.add_params(param_düğümleri)
        işlem.add_output(output)

    def türev(self, hedef: Değişken, kaynak: Değişken) -> np.ndarray | None:
        """
        Hedef değişkenin kaynak değişkenine göre türevlerini hesaplamak için
        kısmi türevlerin ters birikimi.

        Args:
            hedef: Türevlerin hesaplandığı hedef değişken.
            kaynak: Türevlerin hesaplandığı kaynak değişken.

        Returns:
            Hedef değişkenin kaynak değişkenine göre türevi
        """

        # hedefe göre kısmi türevler
        kısmi_türev = defaultdict(lambda: 0)
        kısmi_türev[hedef] = np.ones_like(hedef.to_ndarray())

        # hesaplama grafiğindeki her işlemi yineleme
        işlem_kuyruğu = [hedef.result_of]
        while len(işlem_kuyruğu) > 0:
            işlem = işlem_kuyruğu.pop()
            for param in işlem.params:
                # zincir kuralına göre, değişkenlerin hedefe göre kısmi türevlerini çarpma
                dparam_doutput = self.türev_hesapla(param, işlem)
                dparam_dhedef = dparam_doutput * kısmi_türev[işlem.output]
                kısmi_türev[param] += dparam_dhedef

                if param.result_of and param.result_of != OpType.NOOP:
                    işlem_kuyruğu.append(param.result_of)

        return kısmi_türev.get(kaynak)

    def türev_hesapla(self, param: Değişken, işlem: İşlem) -> np.ndarray:
        """
        Verilen işlem/fonksiyonun türevini hesapla

        Args:
            param: türev alınacak değişken
            işlem: giriş değişkeni üzerinde gerçekleştirilen fonksiyon

        Returns:
            Giriş değişkeninin işlemin çıktısına göre türevi
        """
        params = işlem.params

        if işlem == OpType.TOPLA:
            return np.ones_like(params[0].to_ndarray(), dtype=np.float64)
        if işlem == OpType.ÇIKAR:
            if params[0] == param:
                return np.ones_like(params[0].to_ndarray(), dtype=np.float64)
            return -np.ones_like(params[1].to_ndarray(), dtype=np.float64)
        if işlem == OpType.ÇARP:
            return (
                params[1].to_ndarray().T
                if params[0] == param
                else params[0].to_ndarray().T
            )
        if işlem == OpType.BÖL:
            if params[0] == param:
                return 1 / params[1].to_ndarray()
            return -params[0].to_ndarray() / (params[1].to_ndarray() ** 2)
        if işlem == OpType.MATMUL:
            return (
                params[1].to_ndarray().T
                if params[0] == param
                else params[0].to_ndarray().T
            )
        if işlem == OpType.ÜS:
            güç = işlem.other_params["güç"]
            return güç * (params[0].to_ndarray() ** (güç - 1))

        err_msg = f"geçersiz işlem türü: {işlem.op_type}"
        raise ValueError(err_msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
