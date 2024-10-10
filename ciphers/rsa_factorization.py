"""
RSA asal çarpan algoritması.

Bu program, özel anahtar d ve
genel anahtar e verildiğinde RSA asal sayısını verimli bir şekilde çarpanlarına ayırabilir.
Kaynak: https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf sayfa 3
Daha okunabilir kaynak: https://www.di-mgt.com.au/rsa_factorize_n.html
Büyük sayılar çarpanlarına ayrılması için dakikalar alabilir, bu nedenle doctest'e dahil edilmemiştir.

#Organiser: K. Umut Araz
"""

from __future__ import annotations

import math
import random


def rsa_carpan(d: int, e: int, n: int) -> list[int]:
    """
    Bu fonksiyon N'nin çarpanlarını döndürür, burada p*q=N
      Dönüş: [p, q]

    N'yi RSA modülü, e'yi şifreleme üssü ve d'yi şifre çözme üssü olarak adlandırıyoruz.
    (N, e) çifti genel anahtardır. Adından da anlaşılacağı gibi, bu anahtar herkese açıktır ve
        mesajları şifrelemek için kullanılır.
    (N, d) çifti ise gizli anahtar veya özel anahtardır ve yalnızca
        şifreli mesajların alıcısı tarafından bilinir.

    >>> rsa_carpan(3, 16971, 25777)
    [149, 173]
    >>> rsa_carpan(7331, 11, 27233)
    [113, 241]
    >>> rsa_carpan(4021, 13, 17711)
    [89, 199]
    """
    k = d * e - 1
    p = 0
    q = 0
    while p == 0:
        g = random.randint(2, n - 1)
        t = k
        while True:
            if t % 2 == 0:
                t = t // 2
                x = (g**t) % n
                y = math.gcd(x - 1, n)
                if x > 1 and y > 1:
                    p = y
                    q = n // y
                    break  # doğru çarpanları bul
            else:
                break  # t 2'ye tam bölünmüyorsa, başka bir g seç
    return sorted([p, q])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
