import random


class Onepad:
    @staticmethod
    def sifrele(metin: str) -> tuple[list[int], list[int]]:
        """
        Metni sahte rastgele sayılar kullanarak şifrelemek için fonksiyon

        Organiser: K. Umut Araz

        >>> Onepad().sifrele("")
        ([], [])
        >>> Onepad().sifrele([])
        ([], [])
        >>> random.seed(1)
        >>> Onepad().sifrele(" ")
        ([6969], [69])
        >>> random.seed(1)
        >>> Onepad().sifrele("Merhaba")
        ([9729, 114756, 4653, 31309, 10492], [69, 292, 33, 131, 61])
        >>> Onepad().sifrele(1)
        Traceback (most recent call last):
        ...
        TypeError: 'int' nesnesi yineleyici değildir
        >>> Onepad().sifrele(1.1)
        Traceback (most recent call last):
        ...
        TypeError: 'float' nesnesi yineleyici değildir
        """
        düz_metin = [ord(i) for i in metin]
        anahtar = []
        şifreli = []
        for i in düz_metin:
            k = random.randint(1, 300)
            c = (i + k) * k
            şifreli.append(c)
            anahtar.append(k)
        return şifreli, anahtar

    @staticmethod
    def şifre_çöz(şifreli: list[int], anahtar: list[int]) -> str:
        """
        Metni sahte rastgele sayılar kullanarak çözmek için fonksiyon.
        >>> Onepad().şifre_çöz([], [])
        ''
        >>> Onepad().şifre_çöz([35], [])
        ''
        >>> Onepad().şifre_çöz([], [35])
        Traceback (most recent call last):
        ...
        IndexError: liste dışı aralık
        >>> random.seed(1)
        >>> Onepad().şifre_çöz([9729, 114756, 4653, 31309, 10492], [69, 292, 33, 131, 61])
        'Merhaba'
        """
        düz_metin = []
        for i in range(len(anahtar)):
            p = int((şifreli[i] - (anahtar[i]) ** 2) / anahtar[i])
            düz_metin.append(chr(p))
        return "".join(düz_metin)


if __name__ == "__main__":
    c, k = Onepad().sifrele("Merhaba")
    print(c, k)
    print(Onepad().şifre_çöz(c, k))
