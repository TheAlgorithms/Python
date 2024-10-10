"""
yazar: Christian Bender

Organiser: K. Umut Araz
tarih: 21.12.2017
sınıf: XORCipher

Bu sınıf, XOR şifreleme algoritmasını uygular ve
string ve dosyaları şifrelemek ve şifre çözmek için
bazı kullanışlı yöntemler sağlar.

Yöntemler hakkında genel bilgi

- encrypt : karakter listesi
- decrypt : karakter listesi
- encrypt_string : string
- decrypt_string : string
- encrypt_file : boolean
- decrypt_file : boolean
"""

from __future__ import annotations




class XORCipher:
    def __init__(self, anahtar: int = 0):
        """
        Anahtar alan basit bir yapıcıdır, bir anahtar alır veya
        varsayılan anahtar = 0 kullanır.
        """

        # özel alan
        self.__anahtar = anahtar

    def encrypt(self, içerik: str, anahtar: int) -> list[str]:
        """
        girdi: 'içerik' string türünde ve 'anahtar' int türünde
        çıktı: şifrelenmiş 'içerik' karakter listesi olarak
        anahtar verilmezse, yöntem yapıcıda belirtilen anahtarı kullanır.
        aksi takdirde anahtar = 1

        Boş liste
        >>> XORCipher().encrypt("", 5)
        []

        Bir anahtar
        >>> XORCipher().encrypt("merhaba dünya", 1)
        ['i', '`', 'm', 'm', 'n', '!', 'v', 'd', 'm', 'u']

        Normal anahtar
        >>> XORCipher().encrypt("MERHABA DÜNYA", 32)
        ['m', 'e', 'r', 'h', 'a', '\\x00', 'd', 'ü', 'n', 'y', 'a']

        Anahtar 255'ten büyük
        >>> XORCipher().encrypt("merhaba dünya", 256)
        ['m', 'e', 'r', 'h', 'a', ' ', 'd', 'ü', 'n', 'y', 'a']
        """

        # ön koşul
        assert isinstance(anahtar, int)
        assert isinstance(içerik, str)

        anahtar = anahtar or self.__anahtar or 1

        # anahtarın uygun boyutta olduğundan emin ol
        anahtar %= 256

        return [chr(ord(ch) ^ anahtar) for ch in içerik]

    def decrypt(self, içerik: str, anahtar: int) -> list[str]:
        """
        girdi: 'içerik' string türünde ve 'anahtar' int türünde
        çıktı: şifrelenmiş 'içerik' karakter listesi olarak
        anahtar verilmezse, yöntem yapıcıda belirtilen anahtarı kullanır.
        aksi takdirde anahtar = 1

        Boş liste
        >>> XORCipher().decrypt("", 5)
        []

        Bir anahtar
        >>> XORCipher().decrypt("merhaba dünya", 1)
        ['i', '`', 'm', 'm', 'n', '!', 'v', 'd', 'm', 'u']

        Normal anahtar
        >>> XORCipher().decrypt("MERHABA DÜNYA", 32)
        ['m', 'e', 'r', 'h', 'a', '\\x00', 'd', 'ü', 'n', 'y', 'a']

        Anahtar 255'ten büyük
        >>> XORCipher().decrypt("merhaba dünya", 256)
        ['m', 'e', 'r', 'h', 'a', ' ', 'd', 'ü', 'n', 'y', 'a']
        """

        # ön koşul
        assert isinstance(anahtar, int)
        assert isinstance(içerik, str)

        anahtar = anahtar or self.__anahtar or 1

        # anahtarın uygun boyutta olduğundan emin ol
        anahtar %= 256

        return [chr(ord(ch) ^ anahtar) for ch in içerik]

    def encrypt_string(self, içerik: str, anahtar: int = 0) -> str:
        """
        girdi: 'içerik' string türünde ve 'anahtar' int türünde
        çıktı: şifrelenmiş 'içerik' string olarak
        anahtar verilmezse, yöntem yapıcıda belirtilen anahtarı kullanır.
        aksi takdirde anahtar = 1

        Boş liste
        >>> XORCipher().encrypt_string("", 5)
        ''

        Bir anahtar
        >>> XORCipher().encrypt_string("merhaba dünya", 1)
        'i`mmn!vdmu'

        Normal anahtar
        >>> XORCipher().encrypt_string("MERHABA DÜNYA", 32)
        'merhaba\\x00dünya'

        Anahtar 255'ten büyük
        >>> XORCipher().encrypt_string("merhaba dünya", 256)
        'merhaba dünya'
        """

        # ön koşul
        assert isinstance(anahtar, int)
        assert isinstance(içerik, str)

        anahtar = anahtar or self.__anahtar or 1

        # anahtarın uygun boyutta olduğundan emin ol
        anahtar %= 256

        # Bu döndürülecek
        sonuç = ""

        for ch in içerik:
            sonuç += chr(ord(ch) ^ anahtar)

        return sonuç

    def decrypt_string(self, içerik: str, anahtar: int = 0) -> str:
        """
        girdi: 'içerik' string türünde ve 'anahtar' int türünde
        çıktı: şifrelenmiş 'içerik' string olarak
        anahtar verilmezse, yöntem yapıcıda belirtilen anahtarı kullanır.
        aksi takdirde anahtar = 1

        Boş liste
        >>> XORCipher().decrypt_string("", 5)
        ''

        Bir anahtar
        >>> XORCipher().decrypt_string("merhaba dünya", 1)
        'i`mmn!vdmu'

        Normal anahtar
        >>> XORCipher().decrypt_string("MERHABA DÜNYA", 32)
        'merhaba\\x00dünya'

        Anahtar 255'ten büyük
        >>> XORCipher().decrypt_string("merhaba dünya", 256)
        'merhaba dünya'
        """

        # ön koşul
        assert isinstance(anahtar, int)
        assert isinstance(içerik, str)

        anahtar = anahtar or self.__anahtar or 1

        # anahtarın uygun boyutta olduğundan emin ol
        anahtar %= 256

        # Bu döndürülecek
        sonuç = ""

        for ch in içerik:
            sonuç += chr(ord(ch) ^ anahtar)

        return sonuç

    def encrypt_file(self, dosya: str, anahtar: int = 0) -> bool:
        """
        girdi: dosya adı (str) ve bir anahtar (int)
        çıktı: şifreleme işlemi başarılıysa true, aksi takdirde false döner
        anahtar verilmezse, yöntem yapıcıda belirtilen anahtarı kullanır.
        aksi takdirde anahtar = 1
        """

        # ön koşul
        assert isinstance(dosya, str)
        assert isinstance(anahtar, int)

        # anahtarın uygun boyutta olduğundan emin ol
        anahtar %= 256

        try:
            with open(dosya) as fin, open("encrypt.out", "w+") as fout:
                # gerçek şifreleme işlemi
                for satır in fin:
                    fout.write(self.encrypt_string(satır, anahtar))

        except OSError:
            return False

        return True

    def decrypt_file(self, dosya: str, anahtar: int) -> bool:
        """
        girdi: dosya adı (str) ve bir anahtar (int)
        çıktı: şifre çözme işlemi başarılıysa true, aksi takdirde false döner
        anahtar verilmezse, yöntem yapıcıda belirtilen anahtarı kullanır.
        aksi takdirde anahtar = 1
        """

        # ön koşul
        assert isinstance(dosya, str)
        assert isinstance(anahtar, int)

        # anahtarın uygun boyutta olduğundan emin ol
        anahtar %= 256

        try:
            with open(dosya) as fin, open("decrypt.out", "w+") as fout:
                # gerçek şifre çözme işlemi
                for satır in fin:
                    fout.write(self.decrypt_string(satır, anahtar))

        except OSError:
            return False

        return True


if __name__ == "__main__":
    from doctest import testmod

    testmod()

# Testler
# kript = XORCipher()
# anahtar = 67

# # şifreleme testi
# print(kript.encrypt("merhaba dünya", anahtar))
# # şifre çözme testi
# print(kript.decrypt(kript.encrypt("merhaba dünya", anahtar), anahtar))

# # encrypt_string testi
# print(kript.encrypt_string("merhaba dünya", anahtar))

# # decrypt_string testi
# print(kript.decrypt_string(kript.encrypt_string("merhaba dünya", anahtar), anahtar))

# if (kript.encrypt_file("test.txt", anahtar)):
#       print("şifreleme başarılı")
# else:
#       print("şifreleme başarısız")

# if (kript.decrypt_file("encrypt.out", anahtar)):
#       print("şifre çözme başarılı")
# else:
#       print("şifre çözme başarısız")
