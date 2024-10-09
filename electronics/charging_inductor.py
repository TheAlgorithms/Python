# kaynak - ARRL Radyo İletişim El Kitabı
# https://tr.wikipedia.org/wiki/RL_devresi

"""
Açıklama
-----------
İndüktör, enerjiyi depolayan ancak kondansatörün aksine enerjiyi 'manyetik alanında' veya 'manyetostatik alanında' depolayan pasif bir elektronik cihazdır.

İndüktör 'DC' akım kaynağına bağlandığında hiçbir şey olmaz, sadece bir tel gibi çalışır çünkü gerçek etkisi 'DC' bağlıyken görülemez, enerji bile depolamaz. İndüktör sadece 'AC' akım üzerinde çalışırken enerji depolar.

Bir indüktörü bir dirençle (R = 0 olduğunda) seri olarak bir 'AC' potansiyel kaynağına bağlamak, sıfırdan sonlu bir değere kadar indüktörde ani bir voltajın indüklenmesine neden olur ve bu da akıma karşı çıkar. Bu, başlangıçta yavaş bir akım artışına neden olur. Ancak, akımda daha fazla değişiklik olmazsa bu durur. Direnç sıfır olduğunda akım asla durmaz.

'Direnç(ohm) / İndüktans(henry)' RL zaman sabiti olarak bilinir. Ayrıca τ (tau) olarak da temsil edilir. Bir dirençle bir indüktörün şarj edilmesi, üstel bir fonksiyonla sonuçlanır.

İndüktör 'AC' potansiyel kaynağına bağlandığında, enerjiyi 'manyetik alanında' depolamaya başlar. 'RL zaman sabiti' yardımıyla, indüktör şarj olurken herhangi bir zamanda indüktördeki akımı bulabiliriz.
"""

from math import exp  # exp değeri = 2.718281828459…


def sarj_induktoru(
    kaynak_gerilimi: float,  # kaynak_gerilimi volt cinsinden olmalıdır.
    direnç: float,  # direnç ohm cinsinden olmalıdır.
    induktans: float,  # induktans henry cinsinden olmalıdır.
    zaman: float,  # zaman saniye cinsinden olmalıdır.
) -> float:
    """
    Şarj başlatıldıktan sonra herhangi bir n. saniyede indüktör akımını bulun.

    Örnekler
    --------
    >>> sarj_induktoru(kaynak_gerilimi=5.8,direnç=1.5,induktans=2.3,zaman=2)
    2.817

    >>> sarj_induktoru(kaynak_gerilimi=8,direnç=5,induktans=3,zaman=2)
    1.543

    >>> sarj_induktoru(kaynak_gerilimi=8,direnç=5*pow(10,2),induktans=3,zaman=2)
    0.016

    >>> sarj_induktoru(kaynak_gerilimi=-8,direnç=100,induktans=15,zaman=12)
    Traceback (most recent call last):
        ...
    ValueError: Kaynak gerilimi pozitif olmalıdır.

    >>> sarj_induktoru(kaynak_gerilimi=80,direnç=-15,induktans=100,zaman=5)
    Traceback (most recent call last):
        ...
    ValueError: Direnç pozitif olmalıdır.

    >>> sarj_induktoru(kaynak_gerilimi=12,direnç=200,induktans=-20,zaman=5)
    Traceback (most recent call last):
        ...
    ValueError: İndüktans pozitif olmalıdır.

    >>> sarj_induktoru(kaynak_gerilimi=0,direnç=200,induktans=20,zaman=5)
    Traceback (most recent call last):
        ...
    ValueError: Kaynak gerilimi pozitif olmalıdır.

    >>> sarj_induktoru(kaynak_gerilimi=10,direnç=0,induktans=20,zaman=5)
    Traceback (most recent call last):
        ...
    ValueError: Direnç pozitif olmalıdır.

    >>> sarj_induktoru(kaynak_gerilimi=15, direnç=25, induktans=0, zaman=5)
    Traceback (most recent call last):
        ...
    ValueError: İndüktans pozitif olmalıdır.
    """

    if kaynak_gerilimi <= 0:
        raise ValueError("Kaynak gerilimi pozitif olmalıdır.")
    if direnç <= 0:
        raise ValueError("Direnç pozitif olmalıdır.")
    if induktans <= 0:
        raise ValueError("İndüktans pozitif olmalıdır.")
    return round(
        kaynak_gerilimi / direnç * (1 - exp((-zaman * direnç) / induktans)), 3
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
