"""

Hill Şifrelemesi:
Aşağıdaki 'HillCipher' sınıfı, metni şifrelemek ve çözmek için modern lineer cebir tekniklerini kullanan Hill Şifreleme algoritmasını uygular.

Algoritma:
Şifreleme anahtarının sırası N olsun (bir kare matris olarak).
Metniniz N uzunluğunda parçalara ayrılır ve A=0 ile başlayan basit bir eşleme ile sayısal vektörlere dönüştürülür.

Anahtar, yeni oluşturulan parça vektörü ile çarpılır ve şifrelenmiş vektör elde edilir. Her çarpım sonrasında, vektörler üzerinde 36 modüler hesaplamalar yapılır, böylece sayılar 0 ile 36 arasında kalır ve ardından karşılık gelen alfanümerik karakterlerle eşlenir.

Şifre çözme sırasında, şifreleme anahtarının mod 36 tersini bulan çözme anahtarı bulunur. Orijinal mesajı geri almak için şifre çözme işlemi tekrarlanır.

Kısıtlamalar:
Şifreleme anahtar matrisinin determinantı, 36 ile göreceli asal olmalıdır.

Organiser: K. Umut Araz

Not:
Bu uygulama yalnızca metindeki alfanümerikleri dikkate alır. Şifrelenecek metnin uzunluğu, kırılma anahtarının (bir harf parçasının uzunluğu) katı değilse, metnin son karakteri, metnin uzunluğu kırılma anahtarının katı olana kadar metne eklenir. Bu nedenle, şifre çözüldükten sonra metin, orijinal metinden biraz farklı olabilir.

Referanslar:
https://apprendre-en-ligne.net/crypto/hill/Hillciph.pdf
https://www.youtube.com/watch?v=kfmNeskzs2o
https://www.youtube.com/watch?v=4RhLNDqcjpA

"""

import string
import numpy as np
from maths.greatest_common_divisor import greatest_common_divisor


class HillCipher:
    key_string = string.ascii_uppercase + string.digits
    # Bu şifre, alfanümerikleri dikkate alır
    # yani toplamda 36 karakter

    # x al ve x % len(key_string) döndür
    modulus = np.vectorize(lambda x: x % 36)
    to_int = np.vectorize(round)

    def __init__(self, encrypt_key: np.ndarray) -> None:
        """
        encrypt_key bir NxN numpy dizisidir
        """
        self.encrypt_key = self.modulus(encrypt_key)  # şifreleme anahtarında mod36 hesaplamaları
        self.check_determinant()  # şifreleme anahtarının determinantını doğrula
        self.break_key = encrypt_key.shape[0]

    def replace_letters(self, letter: str) -> int:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_letters('T')
        19
        >>> hill_cipher.replace_letters('0')
        26
        """
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_digits(19)
        'T'
        >>> hill_cipher.replace_digits(26)
        '0'
        """
        return self.key_string[round(num)]

    def check_determinant(self) -> None:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.check_determinant()
        """
        det = round(np.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            msg = (
                f"Şifreleme anahtarının determinantı ({det}) mod {req_l} "
                f"{req_l} ile asal değildir.\nBaşka bir anahtar deneyin."
            )
            raise ValueError(msg)

    def process_text(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.process_text('Testing Hill Cipher')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.process_text('hello')
        'HELLOO'
        """
        chars = [char for char in text.upper() if char in self.key_string]

        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)

        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.encrypt('testing hill cipher')
        'WHXYJOLM9C6XT085LL'
        >>> hill_cipher.encrypt('hello')
        '85FF00'
        """
        text = self.process_text(text.upper())
        encrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array([vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[0]
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def make_decrypt_key(self) -> np.ndarray:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.make_decrypt_key()
        array([[ 6, 25],
               [ 5, 26]])
        """
        det = round(np.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)
        det_inv = None
        for i in range(len(self.key_string)):
            if (det * i) % len(self.key_string) == 1:
                det_inv = i
                break

        inv_key = (
            det_inv * np.linalg.det(self.encrypt_key) * np.linalg.inv(self.encrypt_key)
        )

        return self.to_int(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.decrypt('WHXYJOLM9C6XT085LL')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.decrypt('85FF00')
        'HELLOO'
        """
        decrypt_key = self.make_decrypt_key()
        text = self.process_text(text.upper())
        decrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array([vec]).T
            batch_decrypted = self.modulus(decrypt_key.dot(batch_vec)).T.tolist()[0]
            decrypted_batch = "".join(
                self.replace_digits(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        return decrypted


def main() -> None:
    n = int(input("Şifreleme anahtarının sırasını girin: "))
    hill_matrix = []

    print("Şifreleme anahtarının her satırını boşlukla ayrılmış tam sayılarla girin")
    for _ in range(n):
        row = [int(x) for x in input().split()]
        hill_matrix.append(row)

    hc = HillCipher(np.array(hill_matrix))

    print("Metni şifrelemek mi yoksa çözmek mi istersiniz? (1 veya 2)")
    option = input("\n1. Şifrele\n2. Çöz\n")
    if option == "1":
        text_e = input("Hangi metni şifrelemek istersiniz?: ")
        print("Şifrelenmiş metniniz:")
        print(hc.encrypt(text_e))
    elif option == "2":
        text_d = input("Hangi metni çözmek istersiniz?: ")
        print("Çözülmüş metniniz:")
        print(hc.decrypt(text_d))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
