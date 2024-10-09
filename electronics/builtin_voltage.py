from math import log

from scipy.constants import Boltzmann, physical_constants

T = 300  # SICAKLIK (birim = K)


def yerlesik_gerilim(
    bagislayici_kons: float,  # bağışlayıcı konsantrasyonu
    alıcı_kons: float,  # alıcı konsantrasyonu
    iç_kons: float,  # içsel konsantrasyon
) -> float:
    """
    Bu fonksiyon bir pn eklem diyotunun yerleşik gerilimini hesaplayabilir.
    Bu, verilen üç değerden hesaplanır.
    Örnekler -
    >>> yerlesik_gerilim(bagislayici_kons=1e17, alıcı_kons=1e17, iç_kons=1e10)
    0.833370010652644
    >>> yerlesik_gerilim(bagislayici_kons=0, alıcı_kons=1600, iç_kons=200)
    Traceback (most recent call last):
      ...
    ValueError: Bağışlayıcı konsantrasyonu pozitif olmalıdır
    >>> yerlesik_gerilim(bagislayici_kons=1000, alıcı_kons=0, iç_kons=1200)
    Traceback (most recent call last):
      ...
    ValueError: Alıcı konsantrasyonu pozitif olmalıdır
    >>> yerlesik_gerilim(bagislayici_kons=1000, alıcı_kons=1000, iç_kons=0)
    Traceback (most recent call last):
      ...
    ValueError: İçsel konsantrasyon pozitif olmalıdır
    >>> yerlesik_gerilim(bagislayici_kons=1000, alıcı_kons=3000, iç_kons=2000)
    Traceback (most recent call last):
      ...
    ValueError: Bağışlayıcı konsantrasyonu içsel konsantrasyondan büyük olmalıdır
    >>> yerlesik_gerilim(bagislayici_kons=3000, alıcı_kons=1000, iç_kons=2000)
    Traceback (most recent call last):
      ...
    ValueError: Alıcı konsantrasyonu içsel konsantrasyondan büyük olmalıdır
    """

    if bagislayici_kons <= 0:
        raise ValueError("Bağışlayıcı konsantrasyonu pozitif olmalıdır")
    elif alıcı_kons <= 0:
        raise ValueError("Alıcı konsantrasyonu pozitif olmalıdır")
    elif iç_kons <= 0:
        raise ValueError("İçsel konsantrasyon pozitif olmalıdır")
    elif bagislayici_kons <= iç_kons:
        raise ValueError(
            "Bağışlayıcı konsantrasyonu içsel konsantrasyondan büyük olmalıdır"
        )
    elif alıcı_kons <= iç_kons:
        raise ValueError(
            "Alıcı konsantrasyonu içsel konsantrasyondan büyük olmalıdır"
        )
    else:
        return (
            Boltzmann
            * T
            * log((bagislayici_kons * alıcı_kons) / iç_kons**2)
            / physical_constants["electron volt"][0]
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
