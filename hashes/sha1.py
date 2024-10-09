"""
SHA1 hash fonksiyonunun implementasyonu ve bir stringin veya bir dosyadan metnin hash'ini bulmak için yardımcı araçlar sağlar. Ayrıca, oluşturulan hash'in hashlib kütüphanesi tarafından döndürülen hash ile eşleşip eşleşmediğini doğrulamak için bir Test sınıfı içerir.

Kullanım: python sha1.py --string "Hello World!!"
       python sha1.py --file "hello_world.txt"
       Herhangi bir argüman olmadan çalıştırıldığında, "Hello World!! Welcome to Cryptography" stringinin hash'ini yazdırır.

SHA1 hash veya SHA1 sum bir kriptografik fonksiyondur, bu da ileriye doğru hesaplamanın kolay, geriye doğru hesaplamanın ise son derece zor olduğu anlamına gelir. Bu, bir stringin hash'ini kolayca hesaplayabileceğiniz, ancak hash'e sahipseniz orijinal stringi bilmenin son derece zor olduğu anlamına gelir. Bu özellik, güvenli iletişim kurmak, şifreli mesajlar göndermek ve ödeme sistemlerinde, blockchain ve kripto para birimlerinde çok kullanışlıdır.

Algoritma referansta açıklandığı gibi:
Önce bir mesajla başlıyoruz. Mesaj doldurulur ve mesajın uzunluğu sona eklenir. Daha sonra 512 bit veya 64 byte'lık bloklara bölünür. Bloklar birer birer işlenir. Her blok genişletilmeli ve sıkıştırılmalıdır. Her sıkıştırmadan sonraki değer, geçerli hash durumu olarak adlandırılan 160 bitlik bir arabelleğe eklenir. Son blok işlendiğinde, geçerli hash durumu nihai hash olarak döndürülür.

Referans: https://deadhacker.com/2006/02/21/sha-1-illustrated/
"""

import argparse
import hashlib  # hashlib sadece Test sınıfı içinde kullanılır
import struct


class SHA1Hash:
    """
    SHA1 hash algoritması için tüm işlemleri içeren sınıf
    >>> SHA1Hash(bytes('Allan', 'utf-8')).final_hash()
    '872af2d8ac3d8695387e7c804bf0e02c18df9e6e'
    """

    def __init__(self, data):
        """
        data ve h değişkenlerini başlatır. h, sırasıyla (1732584193, 4023233417, 2562383102, 271733878, 3285377520) sayılarına karşılık gelen 5 adet 8 basamaklı onaltılık sayıdan oluşan bir listedir. Bu, bir mesaj özeti olarak başlayacağımız değerdir. 0x, Python'da onaltılık sayı yazma şeklidir.
        """
        self.data = data
        self.h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

    @staticmethod
    def rotate(n, b):
        """
        Diğer metodlar içinde kullanılacak statik metod. n'i b kadar sola döndürür.
        >>> SHA1Hash('').rotate(12,2)
        48
        """
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    def padding(self):
        """
        Giriş mesajını sıfırlarla doldurur, böylece padded_data 64 byte veya 512 bit olur
        """
        padding = b"\x80" + b"\x00" * (63 - (len(self.data) + 8) % 64)
        padded_data = self.data + padding + struct.pack(">Q", 8 * len(self.data))
        return padded_data

    def split_blocks(self):
        """
        Her biri 64 byte uzunluğunda olan byte string bloklarının bir listesini döndürür
        """
        return [
            self.padded_data[i : i + 64] for i in range(0, len(self.padded_data), 64)
        ]

    def expand_block(self, block):
        """
        64 byte uzunluğunda bir byte string bloğunu alır, bir tamsayı listesine açar ve bazı bit işlemlerinden sonra 80 tamsayıdan oluşan bir liste döndürür
        """
        w = list(struct.unpack(">16L", block)) + [0] * 64
        for i in range(16, 80):
            w[i] = self.rotate((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        return w

    def final_hash(self):
        """
        Girişi işlemek için diğer metodları çağırır. Veriyi doldurur, ardından bloklara böler ve her blok için bir dizi işlem yapar (genişletme dahil).
        Her blok için, başlatılan h değişkeni a, b, c, d, e'ye kopyalanır ve bu 5 değişken a, b, c, d, e çeşitli değişikliklere uğrar. Tüm bloklar işlendiğinde, bu 5 değişken h ile eşleştirilir, yani a h[0]'a, b h[1]'e ve bu şekilde devam eder. Bu h, nihai hash'imiz olur ve döndürülür.
        """
        self.padded_data = self.padding()
        self.blocks = self.split_blocks()
        for block in self.blocks:
            expanded_block = self.expand_block(block)
            a, b, c, d, e = self.h
            for i in range(80):
                if 0 <= i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                a, b, c, d, e = (
                    self.rotate(a, 5) + f + e + k + expanded_block[i] & 0xFFFFFFFF,
                    a,
                    self.rotate(b, 30),
                    c,
                    d,
                )
            self.h = (
                self.h[0] + a & 0xFFFFFFFF,
                self.h[1] + b & 0xFFFFFFFF,
                self.h[2] + c & 0xFFFFFFFF,
                self.h[3] + d & 0xFFFFFFFF,
                self.h[4] + e & 0xFFFFFFFF,
            )
        return ("{:08x}" * 5).format(*self.h)


def test_sha1_hash():
    msg = b"Test String"
    assert SHA1Hash(msg).final_hash() == hashlib.sha1(msg).hexdigest()  # noqa: S324


def main():
    """
    Giriş almak için 'string' veya 'file' seçeneği sağlar ve hesaplanan SHA1 hash'ini yazdırır. unittest.main() her seferinde testi çalıştırmak istemeyebileceğimiz için yorum satırına alınmıştır.
    """
    # unittest.main()
    parser = argparse.ArgumentParser(description="Bazı stringleri veya dosyaları işleyin")
    parser.add_argument(
        "--string",
        dest="input_string",
        default="Hello World!! Welcome to Cryptography",
        help="Stringi hash'le",
    )
    parser.add_argument("--file", dest="input_file", help="Bir dosyanın içeriğini hash'le")
    args = parser.parse_args()
    input_string = args.input_string
    # Her durumda hash girişi bir byte string olmalıdır
    if args.input_file:
        with open(args.input_file, "rb") as f:
            hash_input = f.read()
    else:
        hash_input = bytes(input_string, "utf-8")
    print(SHA1Hash(hash_input).final_hash())


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod()
