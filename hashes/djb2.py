"""
Bu algoritma (k=33) ilk olarak Dan Bernstein tarafından yıllar önce comp.lang.c'de rapor edilmiştir.
Bu algoritmanın başka bir versiyonu (şimdi Bernstein tarafından tercih edilen) xor kullanır:
    hash(i) = hash(i - 1) * 33 ^ str[i];

    Birinci Sihirli Sabit 33:
    Hiçbir zaman yeterince açıklanmamıştır.
    Sihirlidir çünkü birçok diğer sabitten, asal olsun ya da olmasın, daha iyi çalışır.

    İkinci Sihirli Sabit 5381:

    1. tek sayı
    2. asal sayı
    3. eksik sayı
    4. 001/010/100/000/101 b

    kaynak: http://www.cse.yorku.ca/~oz/hash.html
"""


def djb2(s: str) -> int:
    """
    Sihirli sabitleriyle popüler olan djb2 hash algoritmasının
    implementasyonu.

    >>> djb2('Algoritmalar')
    3782405311

    >>> djb2('bitleri karıştır')
    1609059040
    """
    hash_degeri = 5381
    for x in s:
        hash_degeri = ((hash_degeri << 5) + hash_degeri) + ord(x)
    return hash_degeri & 0xFFFFFFFF
