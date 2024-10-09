"""
author: Aayush Soni
Verilen n çift parantez için, tüm iyi biçimlendirilmiş parantez kombinasyonlarını
oluşturmak için bir fonksiyon yazın.
Girdi: n = 2
Çıktı: ["(())","()()"]
Leetcode link: https://leetcode.com/problems/generate-parentheses/description/
"""


def geri_izleme(
    kısmi: str, açık_sayısı: int, kapalı_sayısı: int, n: int, sonuç: list[str]
) -> None:
    """
    Özyineleme kullanarak dengeli parantezlerin geçerli kombinasyonlarını oluşturun.

    :param kısmi: Mevcut kombinasyonu temsil eden bir string.
    :param açık_sayısı: Açık parantez sayısını temsil eden bir tamsayı.
    :param kapalı_sayısı: Kapalı parantez sayısını temsil eden bir tamsayı.
    :param n: Toplam çift sayısını temsil eden bir tamsayı.
    :param sonuç: Geçerli kombinasyonları saklamak için bir liste.
    :return: Yok

    Bu fonksiyon, her adımda parantezlerin dengeli kalmasını sağlayarak
    tüm olası kombinasyonları keşfetmek için özyinelemeyi kullanır.

    Örnek:
    >>> sonuç = []
    >>> geri_izleme("", 0, 0, 2, sonuç)
    >>> sonuç
    ['(())', '()()']
    """
    if len(kısmi) == 2 * n:
        # Kombinasyon tamamlandığında, sonucu ekleyin.
        sonuç.append(kısmi)
        return

    if açık_sayısı < n:
        # Eğer açık parantez ekleyebilirsek, ekleyin ve özyineleme yapın.
        geri_izleme(kısmi + "(", açık_sayısı + 1, kapalı_sayısı, n, sonuç)

    if kapalı_sayısı < açık_sayısı:
        # Eğer kapalı parantez ekleyebilirsek (kombinasyonu geçersiz kılmayacaksa),
        # ekleyin ve özyineleme yapın.
        geri_izleme(kısmi + ")", açık_sayısı, kapalı_sayısı + 1, n, sonuç)


def parantez_oluştur(n: int) -> list[str]:
    """
    Verilen n için dengeli parantezlerin geçerli kombinasyonlarını oluşturun.

    :param n: Parantez çiftlerinin sayısını temsil eden bir tamsayı.
    :return: Geçerli kombinasyonların bulunduğu bir string listesi.

    Bu fonksiyon, kombinasyonları oluşturmak için özyinelemeli bir yaklaşım kullanır.

    Zaman Karmaşıklığı: O(2^(2n)) - En kötü durumda, 2^(2n) kombinasyonumuz var.
    Alan Karmaşıklığı: O(n) - 'n' çift sayısıdır.

    Örnek 1:
    >>> parantez_oluştur(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']

    Örnek 2:
    >>> parantez_oluştur(1)
    ['()']
    """

    sonuç: list[str] = []
    geri_izleme("", 0, 0, n, sonuç)
    return sonuç


if __name__ == "__main__":
    import doctest

    doctest.testmod()
