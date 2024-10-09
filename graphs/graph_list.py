#!/usr/bin/env python3

# Yazar: OMKAR PATHAK, Nwachukwu Chidiebere

# Grafiği oluşturmak için bir Python sözlüğü kullanın.
from __future__ import annotations

from pprint import pformat
from typing import Generic, TypeVar

T = TypeVar("T")


class KomşulukListesiGrafiği(Generic[T]):
    """
    Yönlendirilmiş ve yönlendirilmemiş grafikleri hesaba katan Komşuluk Listesi türü Grafik Veri Yapısı.
    Grafiğin yönlendirilmiş mi yoksa yönlendirilmemiş mi olduğunu belirterek grafik nesnesini başlatın.

    Yönlendirilmiş grafik örneği:
    >>> y_grafik = KomşulukListesiGrafiği()
    >>> print(y_grafik)
    {}
    >>> y_grafik.kenar_ekle(0, 1)
    {0: [1], 1: []}
    >>> y_grafik.kenar_ekle(1, 2).kenar_ekle(1, 4).kenar_ekle(1, 5)
    {0: [1], 1: [2, 4, 5], 2: [], 4: [], 5: []}
    >>> y_grafik.kenar_ekle(2, 0).kenar_ekle(2, 6).kenar_ekle(2, 7)
    {0: [1], 1: [2, 4, 5], 2: [0, 6, 7], 4: [], 5: [], 6: [], 7: []}
    >>> y_grafik
    {0: [1], 1: [2, 4, 5], 2: [0, 6, 7], 4: [], 5: [], 6: [], 7: []}
    >>> print(repr(y_grafik))
    {0: [1], 1: [2, 4, 5], 2: [0, 6, 7], 4: [], 5: [], 6: [], 7: []}

    Yönlendirilmemiş grafik örneği:
    >>> yn_grafik = KomşulukListesiGrafiği(yönlendirilmiş=False)
    >>> yn_grafik.kenar_ekle(0, 1)
    {0: [1], 1: [0]}
    >>> yn_grafik.kenar_ekle(1, 2).kenar_ekle(1, 4).kenar_ekle(1, 5)
    {0: [1], 1: [0, 2, 4, 5], 2: [1], 4: [1], 5: [1]}
    >>> yn_grafik.kenar_ekle(2, 0).kenar_ekle(2, 6).kenar_ekle(2, 7)
    {0: [1, 2], 1: [0, 2, 4, 5], 2: [1, 0, 6, 7], 4: [1], 5: [1], 6: [2], 7: [2]}
    >>> yn_grafik.kenar_ekle(4, 5)
    {0: [1, 2],
     1: [0, 2, 4, 5],
     2: [1, 0, 6, 7],
     4: [1, 5],
     5: [1, 4],
     6: [2],
     7: [2]}
    >>> print(yn_grafik)
    {0: [1, 2],
     1: [0, 2, 4, 5],
     2: [1, 0, 6, 7],
     4: [1, 5],
     5: [1, 4],
     6: [2],
     7: [2]}
    >>> print(repr(yn_grafik))
    {0: [1, 2],
     1: [0, 2, 4, 5],
     2: [1, 0, 6, 7],
     4: [1, 5],
     5: [1, 4],
     6: [2],
     7: [2]}
     >>> char_grafik = KomşulukListesiGrafiği(yönlendirilmiş=False)
     >>> char_grafik.kenar_ekle('a', 'b')
     {'a': ['b'], 'b': ['a']}
     >>> char_grafik.kenar_ekle('b', 'c').kenar_ekle('b', 'e').kenar_ekle('b', 'f')
     {'a': ['b'], 'b': ['a', 'c', 'e', 'f'], 'c': ['b'], 'e': ['b'], 'f': ['b']}
     >>> char_grafik
     {'a': ['b'], 'b': ['a', 'c', 'e', 'f'], 'c': ['b'], 'e': ['b'], 'f': ['b']}
    """

    def __init__(self, yönlendirilmiş: bool = True) -> None:
        """
        Parametreler:
        yönlendirilmiş: (bool) Grafiğin yönlendirilmiş mi yoksa yönlendirilmemiş mi olduğunu belirtir. Varsayılan True.
        """

        self.komşuluk_listesi: dict[T, list[T]] = {}  # listeler sözlüğü
        self.yönlendirilmiş = yönlendirilmiş

    def kenar_ekle(
        self, kaynak_düğüm: T, hedef_düğüm: T
    ) -> KomşulukListesiGrafiği[T]:
        """
        Düğümleri birbirine bağlar. Kaynak düğümden hedef düğüme bir kenar oluşturur.
        Grafikte bulunmayan düğümler oluşturulacaktır.
        """

        if not self.yönlendirilmiş:  # Yönlendirilmemiş grafikler için
            # Hem kaynak düğüm hem de hedef düğüm komşuluk listesinde mevcutsa,
            # kaynak düğümün komşu düğümler listesine hedef düğümü ekleyin ve
            # hedef düğümün komşu düğümler listesine kaynak düğümü ekleyin.
            if kaynak_düğüm in self.komşuluk_listesi and hedef_düğüm in self.komşuluk_listesi:
                self.komşuluk_listesi[kaynak_düğüm].append(hedef_düğüm)
                self.komşuluk_listesi[hedef_düğüm].append(kaynak_düğüm)
            # Sadece kaynak düğüm komşuluk listesinde mevcutsa, kaynak düğümün
            # komşu düğümler listesine hedef düğümü ekleyin, ardından hedef düğümü
            # anahtar olarak kullanarak yeni bir düğüm oluşturun ve ilk komşu düğüm
            # olarak kaynak düğümü içeren bir liste atayın.
            elif kaynak_düğüm in self.komşuluk_listesi:
                self.komşuluk_listesi[kaynak_düğüm].append(hedef_düğüm)
                self.komşuluk_listesi[hedef_düğüm] = [kaynak_düğüm]
            # Sadece hedef düğüm komşuluk listesinde mevcutsa, hedef düğümün
            # komşu düğümler listesine kaynak düğümü ekleyin, ardından kaynak düğümü
            # anahtar olarak kullanarak yeni bir düğüm oluşturun ve ilk komşu düğüm
            # olarak hedef düğümü içeren bir liste atayın.
            elif hedef_düğüm in self.komşuluk_listesi:
                self.komşuluk_listesi[hedef_düğüm].append(kaynak_düğüm)
                self.komşuluk_listesi[kaynak_düğüm] = [hedef_düğüm]
            # Hem kaynak düğüm hem de hedef düğüm komşuluk listesinde mevcut değilse,
            # kaynak düğümü anahtar olarak kullanarak yeni bir düğüm oluşturun ve
            # ilk komşu düğüm olarak hedef düğümü içeren bir liste atayın. Ayrıca,
            # hedef düğümü anahtar olarak kullanarak yeni bir düğüm oluşturun ve
            # ilk komşu düğüm olarak kaynak düğümü içeren bir liste atayın.
            else:
                self.komşuluk_listesi[kaynak_düğüm] = [hedef_düğüm]
                self.komşuluk_listesi[hedef_düğüm] = [kaynak_düğüm]
        # Yönlendirilmiş grafikler için
        # Hem kaynak düğüm hem de hedef düğüm komşuluk listesinde mevcutsa,
        # kaynak düğümün komşu düğümler listesine hedef düğümü ekleyin.
        elif kaynak_düğüm in self.komşuluk_listesi and hedef_düğüm in self.komşuluk_listesi:
            self.komşuluk_listesi[kaynak_düğüm].append(hedef_düğüm)
        # Sadece kaynak düğüm komşuluk listesinde mevcutsa, kaynak düğümün
        # komşu düğümler listesine hedef düğümü ekleyin ve hedef düğümü anahtar
        # olarak kullanarak yeni bir düğüm oluşturun, bu düğümün komşu düğümü yoktur.
        elif kaynak_düğüm in self.komşuluk_listesi:
            self.komşuluk_listesi[kaynak_düğüm].append(hedef_düğüm)
            self.komşuluk_listesi[hedef_düğüm] = []
        # Sadece hedef düğüm komşuluk listesinde mevcutsa, kaynak düğümü anahtar
        # olarak kullanarak yeni bir düğüm oluşturun ve ilk komşu düğüm olarak
        # hedef düğümü içeren bir liste atayın.
        elif hedef_düğüm in self.komşuluk_listesi:
            self.komşuluk_listesi[kaynak_düğüm] = [hedef_düğüm]
        # Hem kaynak düğüm hem de hedef düğüm komşuluk listesinde mevcut değilse,
        # kaynak düğümü anahtar olarak kullanarak yeni bir düğüm oluşturun ve
        # ilk komşu düğüm olarak hedef düğümü içeren bir liste atayın. Ayrıca,
        # hedef düğümü anahtar olarak kullanarak yeni bir düğüm oluşturun, bu
        # düğümün komşu düğümü yoktur.
        else:
            self.komşuluk_listesi[kaynak_düğüm] = [hedef_düğüm]
            self.komşuluk_listesi[hedef_düğüm] = []

        return self

    def __repr__(self) -> str:
        return pformat(self.komşuluk_listesi)
