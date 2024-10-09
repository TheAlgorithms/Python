"""
Bu, fibonacci dizisi problemine Dinamik Programlama çözümünün saf Python uygulamasıdır.
"""


class Fibonacci:
    def __init__(self) -> None:
        self.dizi = [0, 1]

    def al(self, indeks: int) -> list:
        """
        `indeks` numaralı Fibonacci sayısını alır. Eğer sayı mevcut değilse,
        `indeks` numaralı sayıya kadar eksik olan tüm sayıları hesaplar.

        >>> Fibonacci().al(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        >>> Fibonacci().al(5)
        [0, 1, 1, 2, 3]
        """
        if (fark := indeks - (len(self.dizi) - 2)) >= 1:
            for _ in range(fark):
                self.dizi.append(self.dizi[-1] + self.dizi[-2])
        return self.dizi[:indeks]


def ana() -> None:
    print(
        "Dinamik Programlama Kullanarak Fibonacci Serisi\n",
        "Hesaplamak istediğiniz Fibonacci sayısının indeksini aşağıdaki isteme girin. ",
        "(Çıkmak için 'exit' veya Ctrl-C tuşlayın)\n",
        sep="",
    )
    fibonacci = Fibonacci()

    while True:
        istem: str = input(">> ")
        if istem in {"exit", "quit"}:
            break

        try:
            indeks: int = int(istem)
        except ValueError:
            print("Bir sayı veya 'exit' girin")
            continue

        print(fibonacci.al(indeks))


if __name__ == "__main__":
    ana()
