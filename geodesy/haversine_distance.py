from math import asin, atan, cos, radians, sin, sqrt, tan

AXIS_A = 6378137.0
AXIS_B = 6356752.314245
YARIÇAP = 6378137


def haversine_mesafesi(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Bir küredeki iki nokta arasındaki büyük çember mesafesini hesapla,
    verilen boylam ve enlemlerle https://en.wikipedia.org/wiki/Haversine_formula

    Dünyanın "bir tür" küresel olduğunu biliyoruz, bu yüzden iki nokta arasındaki
    yol tam olarak düz bir çizgi değildir. Nokta A'dan B'ye olan mesafeyi hesaplarken
    Dünya'nın eğriliğini dikkate almamız gerekir. Bu etki küçük mesafeler için ihmal
    edilebilir ancak mesafe arttıkça birikir. Haversine yöntemi, dünyayı bir küre
    olarak ele alır ve bu, iki nokta A ve B'yi o kürenin yüzeyine "projeksiyon"
    yapmamıza ve aralarındaki küresel mesafeyi yaklaşık olarak hesaplamamıza olanak tanır.
    Dünya mükemmel bir küre olmadığından, Dünya'nın elipsoidal doğasını modelleyen
    diğer yöntemler daha doğrudur, ancak Haversine gibi hızlı ve modifiye edilebilir
    bir hesaplama, daha kısa mesafeler için kullanışlı olabilir.

    Argümanlar:
        lat1, lon1: koordinat 1'in enlem ve boylamı
        lat2, lon2: koordinat 2'nin enlem ve boylamı
    Dönüş:
        iki nokta arasındaki coğrafi mesafe (metre cinsinden)
    >>> from collections import namedtuple
    >>> nokta_2d = namedtuple("nokta_2d", "enlem boylam")
    >>> SAN_FRANCISCO = nokta_2d(37.774856, -122.424227)
    >>> YOSEMITE = nokta_2d(37.864742, -119.537521)
    >>> f"{haversine_mesafesi(*SAN_FRANCISCO, *YOSEMITE):0,.0f} metre"
    '254,352 metre'
    """
    # WGS84'e göre SABİTLER https://en.wikipedia.org/wiki/World_Geodetic_System
    # Mesafe metre cinsinden (m)
    # Denklem parametreleri
    # Denklem https://en.wikipedia.org/wiki/Haversine_formula#Formulation
    yassilik = (AXIS_A - AXIS_B) / AXIS_A
    phi_1 = atan((1 - yassilik) * tan(radians(lat1)))
    phi_2 = atan((1 - yassilik) * tan(radians(lat2)))
    lambda_1 = radians(lon1)
    lambda_2 = radians(lon2)
    # Denklem
    sin_kare_phi = sin((phi_2 - phi_1) / 2)
    sin_kare_lambda = sin((lambda_2 - lambda_1) / 2)
    # Her iki değeri de kare al
    sin_kare_phi *= sin_kare_phi
    sin_kare_lambda *= sin_kare_lambda
    h_degeri = sqrt(sin_kare_phi + (cos(phi_1) * cos(phi_2) * sin_kare_lambda))
    return 2 * YARIÇAP * asin(h_degeri)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
