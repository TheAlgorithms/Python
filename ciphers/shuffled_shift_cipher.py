from __future__ import annotations

import random
import string


class KarışıkKaydırmaŞifreleme:
    """
    Bu algoritma, Sezar Şifreleme algoritmasını kullanır ancak mesajı
    çözmek için kaba kuvvet seçeneğini kaldırır.

    Orgahniser: K. Umut Araz

    Şifre, aşağıdaki seçim havuzundan rastgele bir şifre oluşturur:
    1. İngiliz alfabesinin büyük harfleri
    2. İngiliz alfabesinin küçük harfleri
    3. 0'dan 9'a kadar olan rakamlar

    Şifreden elde edilen benzersiz karakterler kullanılarak, düz metinde
    izin verilen normal karakter listesi döndürülür ve karıştırılır. 
    Karıştırma hakkında daha fazla bilgi için __make_key_list() 
    fonksiyonunun açıklamasına bakın.

    Ardından, şifre kullanılarak, düz metin mesajını şifrelemek için
    kullanılan bir sayı hesaplanır. Bu durumda, çözümleme sırasında
    geri dönmek için referans karıştırılmıştır.

    Her şifreleme nesnesi, isteğe bağlı bir argüman olarak şifre alabilir; 
    bu argüman olmadan, o nesne için otomatik olarak yeni bir şifre oluşturulur.
    cip1 = KarışıkKaydırmaŞifreleme('d4usr9TWxw9wMD')
    cip2 = KarışıkKaydırmaŞifreleme()
    """

    def __init__(self, şifre: str | None = None) -> None:
        """
        Şifre ile bir şifreleme nesnesi başlatır.
        Not: Kullanıcı bir şifre sağlarsa, yeni bir şifre oluşturulmaz.
        """
        self.__şifre = şifre or self.__şifre_oluşturucu()
        self.__anahtar_listesi = self.__anahtar_listesi_oluştur()
        self.__kaydırma_anahtarı = self.__kaydırma_anahtarı_oluştur()

    def __str__(self) -> str:
        """
        :return: şifreleme nesnesinin şifresi
        """
        return "".join(self.__şifre)

    def __negatif_pozitif(self, iterlist: list[int]) -> list[int]:
        """
        Listenin her alternatif elemanının işaretini değiştirir.

        :param iterlist: bir liste alır
        :return: değiştirilmiş liste
        """
        for i in range(1, len(iterlist), 2):
            iterlist[i] *= -1
        return iterlist

    def __şifre_oluşturucu(self) -> list[str]:
        """
        Aşağıdaki seçim havuzundan rastgele bir şifre oluşturur:
        1. İngiliz alfabesinin büyük harfleri
        2. İngiliz alfabesinin küçük harfleri
        3. 0'dan 9'a kadar olan rakamlar

        :rtype: list
        :return: 10 ile 20 arasında rastgele bir uzunlukta şifre
        """
        seçimler = string.ascii_letters + string.digits
        şifre = [random.choice(seçimler) for _ in range(random.randint(10, 20))]
        return şifre

    def __anahtar_listesi_oluştur(self) -> list[str]:
        """
        Karakter seçimlerini, kırılma noktalarında döndürerek karıştırır.
        Kırılma noktaları, şifredeki karakterlerdir.

        Örnek:
            Eğer, ABCDEFGHIJKLMNOPQRSTUVWXYZ olası karakterlerse
            ve CAMERA şifre ise
            o zaman, kırılma noktaları = [A,C,E,M,R] # şifreden sıralı karakter seti
            karıştırılmış parçalar: [A,CB,ED,MLKJIHGF,RQPON,ZYXWVUTS]
            karıştırılmış __anahtar_listesi : ACBEDMLKJIHGFRQPONZYXWVUTS

        Sadece 26 İngilizce harfini karıştırmak, karıştırılmış liste için 26!
        kombinasyon oluşturabilir. Programda, 97 karakter (harfler, rakamlar, 
        noktalama işaretleri ve boşluklar dahil) seti dikkate alındığında, 
        97! kombinasyon olasılığı oluşturur (bu kendisi 152 basamaklı bir sayı),
        böylece kaba kuvvet yaklaşımının olasılığını azaltır.
        Ayrıca, kaydırma anahtarları, her bir 97! kombinasyonu için 
        kaba kuvvet yaklaşımına 26 katı ekler.
        """
        # anahtar_listesi_seçenekleri, string.whitespace'tan birkaç eleman hariç
        # neredeyse tüm yazdırılabilir karakterleri içerir
        anahtar_listesi_seçenekleri = (
            string.ascii_letters + string.digits + string.punctuation + " \t\n"
        )

        anahtarlar = []

        # anahtar_listesi_seçeneklerini kırılma noktalarında kırarak
        # geçici alt dizileri döndürür
        kırılma_noktaları = sorted(set(self.__şifre))
        geçici_liste: list[str] = []

        # anahtar_listesi_seçeneklerinden yeni karıştırılmış bir liste oluşturma algoritması
        for i in anahtar_listesi_seçenekleri:
            geçici_liste.extend(i)

            # geçici alt diziyi döndürmek için kırılma noktalarını kontrol etme
            if i in kırılma_noktaları or i == anahtar_listesi_seçenekleri[-1]:
                anahtarlar.extend(geçici_liste[::-1])
                geçici_liste.clear()

        # kaydırma anahtarının kaba kuvvet tahminini önlemek için karıştırılmış anahtarlar döndürülür
        return anahtarlar

    def __kaydırma_anahtarı_oluştur(self) -> int:
        """
        Tüm karakterlerin ascii değerlerinin değiştirilmiş listesinin toplamını döndürür.
        Değiştirilmiş liste, __negatif_pozitif() tarafından döndürülen listedir.
        """
        num = sum(self.__negatif_pozitif([ord(x) for x in self.__şifre]))
        return num if num > 0 else len(self.__şifre)

    def çöz(self, şifreli_mesaj: str) -> str:
        """
        Şifreli mesajın, karıştırılmış __anahtar_listesi'ne göre kaydırılmasını
        gerçekleştirir ve çözülmüş mesajı oluşturur.

        >>> ssc = KarışıkKaydırmaŞifreleme('4PYIXyqeQZr44')
        >>> ssc.çöz("d>**-1z6&'5z'5z:z+-='$'>=zp:>5:#z<'.&>#")
        'Merhaba, bu değiştirilmiş Sezar şifresidir'
        """
        çözülmüş_mesaj = ""

        # Sezar şifreleme algoritması gibi negatif kaydırma uygulayarak
        # çözme işlemi
        for i in şifreli_mesaj:
            konum = self.__anahtar_listesi.index(i)
            çözülmüş_mesaj += self.__anahtar_listesi[
                (konum - self.__kaydırma_anahtarı) % -len(self.__anahtar_listesi)
            ]

        return çözülmüş_mesaj

    def şifrele(self, düz_metin: str) -> str:
        """
        Düz metnin, karıştırılmış __anahtar_listesi'ne göre kaydırılmasını
        gerçekleştirir ve şifreli mesajı oluşturur.

        >>> ssc = KarışıkKaydırmaŞifreleme('4PYIXyqeQZr44')
        >>> ssc.şifrele('Merhaba, bu değiştirilmiş Sezar şifresidir')
        "d>**-1z6&'5z'5z:z+-='$'>=zp:>5:#z<'.&>#"
        """
        şifreli_mesaj = ""

        # Sezar şifreleme algoritması gibi pozitif kaydırma uygulayarak
        # şifreleme işlemi
        for i in düz_metin:
            konum = self.__anahtar_listesi.index(i)
            şifreli_mesaj += self.__anahtar_listesi[
                (konum + self.__kaydırma_anahtarı) % len(self.__anahtar_listesi)
            ]

        return şifreli_mesaj


def test_ucu_uca(msg: str = "Merhaba, bu değiştirilmiş Sezar şifresidir") -> str:
    """
    >>> test_ucu_uca()
    'Merhaba, bu değiştirilmiş Sezar şifresidir'
    """
    cip1 = KarışıkKaydırmaŞifreleme()
    return cip1.çöz(cip1.şifrele(msg))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
