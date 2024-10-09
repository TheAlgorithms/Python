from typing import Any


def viterbi(
    gozlem_alani: list,
    durum_alani: list,
    baslangic_olasiliklari: dict,
    gecis_olasiliklari: dict,
    yayilim_olasiliklari: dict,
) -> list:
    """
        Viterbi Algoritması, başlangıçtan itibaren en olası durum yolunu
        ve beklenen çıktıyı bulmak için.
        https://en.wikipedia.org/wiki/Viterbi_algorithm

        Wikipedia örneği
        >>> gozlemler = ["normal", "cold", "dizzy"]
        >>> durumlar = ["Healthy", "Fever"]
        >>> baslangic_p = {"Healthy": 0.6, "Fever": 0.4}
        >>> gecis_p = {
        ...     "Healthy": {"Healthy": 0.7, "Fever": 0.3},
        ...     "Fever": {"Healthy": 0.4, "Fever": 0.6},
        ... }
        >>> yayilim_p = {
        ...     "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
        ...     "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
        ... }
        >>> viterbi(gozlemler, durumlar, baslangic_p, gecis_p, yayilim_p)
        ['Healthy', 'Healthy', 'Fever']

        >>> viterbi((), durumlar, baslangic_p, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: Boş bir parametre var

        >>> viterbi(gozlemler, (), baslangic_p, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: Boş bir parametre var

        >>> viterbi(gozlemler, durumlar, {}, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: Boş bir parametre var

        >>> viterbi(gozlemler, durumlar, baslangic_p, {}, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: Boş bir parametre var

        >>> viterbi(gozlemler, durumlar, baslangic_p, gecis_p, {})
        Traceback (most recent call last):
            ...
        ValueError: Boş bir parametre var

        >>> viterbi("gecersiz", durumlar, baslangic_p, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: gozlem_alani bir liste olmalı

        >>> viterbi(["gecerli", 123], durumlar, baslangic_p, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: gozlem_alani bir dizi stringlerden oluşmalı

        >>> viterbi(gozlemler, "gecersiz", baslangic_p, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: durum_alani bir liste olmalı

        >>> viterbi(gozlemler, ["gecerli", 123], baslangic_p, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: durum_alani bir dizi stringlerden oluşmalı

        >>> viterbi(gozlemler, durumlar, "gecersiz", gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: baslangic_olasiliklari bir sözlük olmalı

        >>> viterbi(gozlemler, durumlar, {2:2}, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: baslangic_olasiliklari tüm anahtarlar string olmalı

        >>> viterbi(gozlemler, durumlar, {"a":2}, gecis_p, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: baslangic_olasiliklari tüm değerler float olmalı

        >>> viterbi(gozlemler, durumlar, baslangic_p, "gecersiz", yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: gecis_olasiliklari bir sözlük olmalı

        >>> viterbi(gozlemler, durumlar, baslangic_p, {"a":2}, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: gecis_olasiliklari tüm değerler sözlük olmalı

        >>> viterbi(gozlemler, durumlar, baslangic_p, {2:{2:2}}, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: gecis_olasiliklari tüm anahtarlar string olmalı

        >>> viterbi(gozlemler, durumlar, baslangic_p, {"a":{2:2}}, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: gecis_olasiliklari tüm anahtarlar string olmalı

        >>> viterbi(gozlemler, durumlar, baslangic_p, {"a":{"b":2}}, yayilim_p)
        Traceback (most recent call last):
            ...
        ValueError: gecis_olasiliklari iç içe geçmiş sözlüklerin tüm değerleri float olmalı

        >>> viterbi(gozlemler, durumlar, baslangic_p, gecis_p, "gecersiz")
        Traceback (most recent call last):
            ...
        ValueError: yayilim_olasiliklari bir sözlük olmalı

        >>> viterbi(gozlemler, durumlar, baslangic_p, gecis_p, None)
        Traceback (most recent call last):
            ...
        ValueError: Boş bir parametre var

    """
    _dogrulama(
        gozlem_alani,
        durum_alani,
        baslangic_olasiliklari,
        gecis_olasiliklari,
        yayilim_olasiliklari,
    )
    # Veri yapıları oluşturulur ve ilk adım doldurulur
    olasiliklar: dict = {}
    isaretciler: dict = {}
    for durum in durum_alani:
        gozlem = gozlem_alani[0]
        olasiliklar[(durum, gozlem)] = (
            baslangic_olasiliklari[durum] * yayilim_olasiliklari[durum][gozlem]
        )
        isaretciler[(durum, gozlem)] = None

    # Farklı geçişlerin olasılıkları ve önceki durumlara işaretçileri
    # ile veri yapısı doldurulur
    for o in range(1, len(gozlem_alani)):
        gozlem = gozlem_alani[o]
        onceki_gozlem = gozlem_alani[o - 1]
        for durum in durum_alani:
            # Olasılık fonksiyonu için argmax hesaplanır
            arg_max = ""
            max_olasilik = -1
            for k_durum in durum_alani:
                olasilik = (
                    olasiliklar[(k_durum, onceki_gozlem)]
                    * gecis_olasiliklari[k_durum][durum]
                    * yayilim_olasiliklari[durum][gozlem]
                )
                if olasilik > max_olasilik:
                    max_olasilik = olasilik
                    arg_max = k_durum

            # Olasılık ve işaretçi sözlükleri güncellenir
            olasiliklar[(durum, gozlem)] = (
                olasiliklar[(arg_max, onceki_gozlem)]
                * gecis_olasiliklari[arg_max][durum]
                * yayilim_olasiliklari[durum][gozlem]
            )

            isaretciler[(durum, gozlem)] = arg_max

    # Son gözlem
    son_gozlem = gozlem_alani[len(gozlem_alani) - 1]

    # Verilen son gözlem için argmax
    arg_max = ""
    max_olasilik = -1
    for k_durum in durum_alani:
        olasilik = olasiliklar[(k_durum, son_gozlem)]
        if olasilik > max_olasilik:
            max_olasilik = olasilik
            arg_max = k_durum
    son_durum = arg_max

    # İşaretçiler geriye doğru işlenir
    onceki = son_durum
    sonuc = []
    for o in range(len(gozlem_alani) - 1, -1, -1):
        sonuc.append(onceki)
        onceki = isaretciler[onceki, gozlem_alani[o]]
    sonuc.reverse()

    return sonuc


def _dogrulama(
    gozlem_alani: Any,
    durum_alani: Any,
    baslangic_olasiliklari: Any,
    gecis_olasiliklari: Any,
    yayilim_olasiliklari: Any,
) -> None:
    """
    >>> gozlemler = ["normal", "cold", "dizzy"]
    >>> durumlar = ["Healthy", "Fever"]
    >>> baslangic_p = {"Healthy": 0.6, "Fever": 0.4}
    >>> gecis_p = {
    ...     "Healthy": {"Healthy": 0.7, "Fever": 0.3},
    ...     "Fever": {"Healthy": 0.4, "Fever": 0.6},
    ... }
    >>> yayilim_p = {
    ...     "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
    ...     "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
    ... }
    >>> _dogrulama(gozlemler, durumlar, baslangic_p, gecis_p, yayilim_p)

    >>> _dogrulama([], durumlar, baslangic_p, gecis_p, yayilim_p)
    Traceback (most recent call last):
            ...
    ValueError: Boş bir parametre var
    """
    _bos_olmayan_dogrulama(
        gozlem_alani,
        durum_alani,
        baslangic_olasiliklari,
        gecis_olasiliklari,
        yayilim_olasiliklari,
    )
    _listeleri_dogrula(gozlem_alani, durum_alani)
    _sozlukleri_dogrula(
        baslangic_olasiliklari, gecis_olasiliklari, yayilim_olasiliklari
    )


def _bos_olmayan_dogrulama(
    gozlem_alani: Any,
    durum_alani: Any,
    baslangic_olasiliklari: Any,
    gecis_olasiliklari: Any,
    yayilim_olasiliklari: Any,
) -> None:
    """
    >>> _bos_olmayan_dogrulama(["a"], ["b"], {"c":0.5},
    ... {"d": {"e": 0.6}}, {"f": {"g": 0.7}})

    >>> _bos_olmayan_dogrulama(["a"], ["b"], {"c":0.5}, {}, {"f": {"g": 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: Boş bir parametre var
    >>> _bos_olmayan_dogrulama(["a"], ["b"], None, {"d": {"e": 0.6}}, {"f": {"g": 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: Boş bir parametre var
    """
    if not all(
        [
            gozlem_alani,
            durum_alani,
            baslangic_olasiliklari,
            gecis_olasiliklari,
            yayilim_olasiliklari,
        ]
    ):
        raise ValueError("Boş bir parametre var")


def _listeleri_dogrula(gozlem_alani: Any, durum_alani: Any) -> None:
    """
    >>> _listeleri_dogrula(["a"], ["b"])

    >>> _listeleri_dogrula(1234, ["b"])
    Traceback (most recent call last):
            ...
    ValueError: gozlem_alani bir liste olmalı

    >>> _listeleri_dogrula(["a"], [3])
    Traceback (most recent call last):
            ...
    ValueError: durum_alani bir dizi stringlerden oluşmalı
    """
    _listeyi_dogrula(gozlem_alani, "gozlem_alani")
    _listeyi_dogrula(durum_alani, "durum_alani")


def _listeyi_dogrula(nesne: Any, degisken_adi: str) -> None:
    """
    >>> _listeyi_dogrula(["a"], "ornek_adi")

    >>> _listeyi_dogrula("a", "ornek_adi")
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi bir liste olmalı
    >>> _listeyi_dogrula([0.5], "ornek_adi")
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi bir dizi stringlerden oluşmalı

    """
    if not isinstance(nesne, list):
        msg = f"{degisken_adi} bir liste olmalı"
        raise ValueError(msg)
    else:
        for x in nesne:
            if not isinstance(x, str):
                msg = f"{degisken_adi} bir dizi stringlerden oluşmalı"
                raise ValueError(msg)


def _sozlukleri_dogrula(
    baslangic_olasiliklari: Any,
    gecis_olasiliklari: Any,
    yayilim_olasiliklari: Any,
) -> None:
    """
    >>> _sozlukleri_dogrula({"c":0.5}, {"d": {"e": 0.6}}, {"f": {"g": 0.7}})

    >>> _sozlukleri_dogrula("gecersiz", {"d": {"e": 0.6}}, {"f": {"g": 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: baslangic_olasiliklari bir sözlük olmalı
    >>> _sozlukleri_dogrula({"c":0.5}, {2: {"e": 0.6}}, {"f": {"g": 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: gecis_olasiliklari tüm anahtarlar string olmalı
    >>> _sozlukleri_dogrula({"c":0.5}, {"d": {"e": 0.6}}, {"f": {2: 0.7}})
    Traceback (most recent call last):
            ...
    ValueError: yayilim_olasiliklari tüm anahtarlar string olmalı
    >>> _sozlukleri_dogrula({"c":0.5}, {"d": {"e": 0.6}}, {"f": {"g": "h"}})
    Traceback (most recent call last):
            ...
    ValueError: yayilim_olasiliklari iç içe geçmiş sözlüklerin tüm değerleri float olmalı
    """
    _sozluk_dogrula(baslangic_olasiliklari, "baslangic_olasiliklari", float)
    _ic_ice_sozluk_dogrula(gecis_olasiliklari, "gecis_olasiliklari")
    _ic_ice_sozluk_dogrula(yayilim_olasiliklari, "yayilim_olasiliklari")


def _ic_ice_sozluk_dogrula(nesne: Any, degisken_adi: str) -> None:
    """
    >>> _ic_ice_sozluk_dogrula({"a":{"b": 0.5}}, "ornek_adi")

    >>> _ic_ice_sozluk_dogrula("gecersiz", "ornek_adi")
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi bir sözlük olmalı
    >>> _ic_ice_sozluk_dogrula({"a": 8}, "ornek_adi")
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi tüm değerler sözlük olmalı
    >>> _ic_ice_sozluk_dogrula({"a":{2: 0.5}}, "ornek_adi")
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi tüm anahtarlar string olmalı
    >>> _ic_ice_sozluk_dogrula({"a":{"b": 4}}, "ornek_adi")
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi iç içe geçmiş sözlüklerin tüm değerleri float olmalı
    """
    _sozluk_dogrula(nesne, degisken_adi, dict)
    for x in nesne.values():
        _sozluk_dogrula(x, degisken_adi, float, True)


def _sozluk_dogrula(
    nesne: Any, degisken_adi: str, deger_tipi: type, ic_ice: bool = False
) -> None:
    """
    >>> _sozluk_dogrula({"b": 0.5}, "ornek_adi", float)

    >>> _sozluk_dogrula("gecersiz", "ornek_adi", float)
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi bir sözlük olmalı
    >>> _sozluk_dogrula({"a": 8}, "ornek_adi", dict)
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi tüm değerler sözlük olmalı
    >>> _sozluk_dogrula({2: 0.5}, "ornek_adi",float, True)
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi tüm anahtarlar string olmalı
    >>> _sozluk_dogrula({"b": 4}, "ornek_adi", float,True)
    Traceback (most recent call last):
            ...
    ValueError: ornek_adi iç içe geçmiş sözlüklerin tüm değerleri float olmalı
    """
    if not isinstance(nesne, dict):
        msg = f"{degisken_adi} bir sözlük olmalı"
        raise ValueError(msg)
    if not all(isinstance(x, str) for x in nesne):
        msg = f"{degisken_adi} tüm anahtarlar string olmalı"
        raise ValueError(msg)
    if not all(isinstance(x, deger_tipi) for x in nesne.values()):
        ic_ice_metin = "iç içe geçmiş sözlüklerin " if ic_ice else ""
        msg = f"{degisken_adi} {ic_ice_metin}tüm değerleri {deger_tipi.__name__} olmalı"
        raise ValueError(msg)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
