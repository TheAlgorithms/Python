from math import atan, cos, radians, sin, tan

from .haversine_distance import haversine_mesafesi

AXIS_A = 6378137.0
AXIS_B = 6356752.314245
EKVATOR_YARICAPI = 6378137


def lamberts_elipsoidal_mesafe(
    enlem1: float, boylam1: float, enlem2: float, boylam2: float
) -> float:
    """
    İki nokta arasındaki elipsoid yüzeyi boyunca en kısa mesafeyi hesapla,
    verilen boylam ve enlemlerle
    https://en.wikipedia.org/wiki/Geographical_distance#Lambert's_formula_for_long_lines

    NOT: Bu algoritma merkezi açı hesaplamak için geodesy/haversine_distance.py kullanır,
        sigma

    Dünyayı bir elipsoid olarak temsil etmek, yüzeydeki noktalar arasındaki mesafeleri
    bir küreye göre çok daha iyi tahmin etmemizi sağlar. Elipsoidal formüller,
    Dünya'yı kutuplarda yassılaşma olan bir basık elipsoid olarak ele alır. Lambert'in
    formülleri, binlerce kilometre boyunca 10 metre mertebesinde doğruluk sağlar.
    Diğer yöntemler milimetre seviyesinde doğruluk sağlayabilir, ancak bu yöntem,
    uzun mesafeleri hesaplamak için daha basit ve hesaplama yoğunluğunu artırmadan
    kullanılabilir.

    Argümanlar:
        enlem1, boylam1: koordinat 1'in enlem ve boylamı
        enlem2, boylam2: koordinat 2'nin enlem ve boylamı
    Dönüş:
        iki nokta arasındaki coğrafi mesafe (metre cinsinden)

    >>> from collections import namedtuple
    >>> nokta_2d = namedtuple("nokta_2d", "enlem boylam")
    >>> SAN_FRANCISCO = nokta_2d(37.774856, -122.424227)
    >>> YOSEMITE = nokta_2d(37.864742, -119.537521)
    >>> NEW_YORK = nokta_2d(40.713019, -74.012647)
    >>> VENEDİK = nokta_2d(45.443012, 12.313071)
    >>> f"{lamberts_elipsoidal_mesafe(*SAN_FRANCISCO, *YOSEMITE):0,.0f} metre"
    '254,351 metre'
    >>> f"{lamberts_elipsoidal_mesafe(*SAN_FRANCISCO, *NEW_YORK):0,.0f} metre"
    '4,138,992 metre'
    >>> f"{lamberts_elipsoidal_mesafe(*SAN_FRANCISCO, *VENEDİK):0,.0f} metre"
    '9,737,326 metre'
    """

    # WGS84'e göre SABİTLER https://en.wikipedia.org/wiki/World_Geodetic_System
    # Mesafe metre cinsinden (m)
    # Denklem Parametreleri
    # https://en.wikipedia.org/wiki/Geographical_distance#Lambert's_formula_for_long_lines
    yassilik = (AXIS_A - AXIS_B) / AXIS_A
    # Parametrik enlemler
    # https://en.wikipedia.org/wiki/Latitude#Parametric_(or_reduced)_latitude
    b_enlem1 = atan((1 - yassilik) * tan(radians(enlem1)))
    b_enlem2 = atan((1 - yassilik) * tan(radians(enlem2)))

    # İki nokta arasındaki merkezi açıyı hesapla
    # haversine theta kullanarak. sigma = haversine_mesafesi / ekvator yarıçapı
    sigma = haversine_mesafesi(enlem1, boylam1, enlem2, boylam2) / EKVATOR_YARICAPI

    # Ara P ve Q değerleri
    p_degeri = (b_enlem1 + b_enlem2) / 2
    q_degeri = (b_enlem2 - b_enlem1) / 2

    # Ara X değeri
    # X = (sigma - sin(sigma)) * sin^2Pcos^2Q / cos^2(sigma/2)
    x_pay = (sin(p_degeri) ** 2) * (cos(q_degeri) ** 2)
    x_payda = cos(sigma / 2) ** 2
    x_degeri = (sigma - sin(sigma)) * (x_pay / x_payda)

    # Ara Y değeri
    # Y = (sigma + sin(sigma)) * cos^2Psin^2Q / sin^2(sigma/2)
    y_pay = (cos(p_degeri) ** 2) * (sin(q_degeri) ** 2)
    y_payda = sin(sigma / 2) ** 2
    y_degeri = (sigma + sin(sigma)) * (y_pay / y_payda)

    return EKVATOR_YARICAPI * (sigma - ((yassilik / 2) * (x_degeri + y_degeri)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
