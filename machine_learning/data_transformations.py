"""
Normalizasyon.

Wikipedia: https://en.wikipedia.org/wiki/Normalization
Normalizasyon, sayısal verilerin standart bir değer aralığına dönüştürülmesi işlemidir.
Bu aralık tipik olarak [0, 1] veya [-1, 1] arasındadır. Normalizasyon denklemi
x_norm = (x - x_min)/(x_max - x_min) şeklindedir. Burada x_norm normalize edilmiş değer,
x orijinal değer, x_min sütun veya veri listesindeki minimum değer ve x_max sütun veya
veri listesindeki maksimum değerdir. Normalizasyon, verilerin eğitimini hızlandırmak ve
tüm verileri benzer bir ölçeğe getirmek için kullanılır. Bu, özellikle Gradient Descent
optimizasyonunda, veri kümesindeki değer aralığındaki varyansın optimizasyonu büyük
ölçüde etkileyebileceği için faydalıdır.

Standardizasyon Wikipedia: https://en.wikipedia.org/wiki/Standardization
Standardizasyon, sayısal verilerin normal dağılımlı bir değer aralığına dönüştürülmesi
işlemidir. Bu aralık, ortalaması 0 ve standart sapması 1 olan bir aralık olacaktır. Bu
aynı zamanda z-puan normalizasyonu olarak da bilinir. Standardizasyon denklemi
x_std = (x - mu)/(sigma) şeklindedir. Burada mu sütun veya değer listesinin ortalaması
ve sigma sütun veya değer listesinin standart sapmasıdır.

Normalizasyon ve Standardizasyon arasında seçim yapmak daha çok bir sanat gibidir, ancak
hangisinin daha iyi performans gösterdiğini görmek için her ikisiyle de deneyler yapmak
genellikle önerilir. Ayrıca, birkaç genel kural şunlardır:
    1. Gauss (normal) dağılımlar standardizasyon ile daha iyi çalışır
    2. Gauss olmayan (normal olmayan) dağılımlar normalizasyon ile daha iyi çalışır
    3. Bir sütun veya değer listesi aşırı değerlere / aykırı değerlere sahipse, standardizasyon kullanın
"""

from statistics import mean, stdev


def normalizasyon(veri: list, ondalik_basamak: int = 3) -> list:
    """
    Normalize edilmiş bir değer listesi döndürür.

    @parametreler: veri, normalize edilecek değerler listesi
    @döndürür: normalize edilmiş değerler listesi (ondalik_basamak kadar yuvarlanmış)
    @örnekler:
    >>> normalizasyon([2, 7, 10, 20, 30, 50])
    [0.0, 0.104, 0.167, 0.375, 0.583, 1.0]
    >>> normalizasyon([5, 10, 15, 20, 25])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # hesaplama için değişkenler
    x_min = min(veri)
    x_max = max(veri)
    # veriyi normalize et
    return [round((x - x_min) / (x_max - x_min), ondalik_basamak) for x in veri]


def standardizasyon(veri: list, ondalik_basamak: int = 3) -> list:
    """
    Standardize edilmiş bir değer listesi döndürür.

    @parametreler: veri, standardize edilecek değerler listesi
    @döndürür: standardize edilmiş değerler listesi (ondalik_basamak kadar yuvarlanmış)
    @örnekler:
    >>> standardizasyon([2, 7, 10, 20, 30, 50])
    [-0.999, -0.719, -0.551, 0.009, 0.57, 1.69]
    >>> standardizasyon([5, 10, 15, 20, 25])
    [-1.265, -0.632, 0.0, 0.632, 1.265]
    """
    # hesaplama için değişkenler
    mu = mean(veri)
    sigma = stdev(veri)
    # veriyi standardize et
    return [round((x - mu) / (sigma), ondalik_basamak) for x in veri]
