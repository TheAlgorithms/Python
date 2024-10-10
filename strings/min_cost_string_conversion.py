"""

Organiser: K. Umut Araz

Bir stringi başka bir stringe dönüştürmek için en maliyet etkin diziyi hesaplayan algoritma.
İzin verilen tek işlemler şunlardır:
--- Bir karakteri kopyalamanın maliyeti copy_cost
--- Bir karakteri değiştirmenin maliyeti replace_cost
--- Bir karakteri silmenin maliyeti delete_cost
--- Bir karakter eklemenin maliyeti insert_cost
"""


def maliyet_hesapla(
    kaynak_string: str,
    hedef_string: str,
    kopyalama_maliyeti: int,
    degistirme_maliyeti: int,
    silme_maliyeti: int,
    ekleme_maliyeti: int,
) -> tuple[list[list[int]], list[list[str]]]:
    """
    Bir stringi başka bir stringe dönüştürmek için en maliyet etkin diziyi bulur.

    >>> maliyetler, islemler = maliyet_hesapla("kedi", "kutu", 1, 2, 3, 3)
    >>> maliyetler[0][:4]
    [0, 3, 6, 9]
    >>> maliyetler[2][:4]
    [6, 4, 3, 6]
    >>> islemler[0][:4]
    ['0', 'Ik', 'Iu', 'It']
    >>> islemler[3][:4]
    ['Ds', 'Ds', 'Rtu', 'Kt']

    >>> maliyet_hesapla("", "", 1, 2, 3, 3)
    ([[0]], [['0']])
    """
    kaynak_dizi = list(kaynak_string)
    hedef_dizi = list(hedef_string)
    kaynak_uzunluk = len(kaynak_dizi)
    hedef_uzunluk = len(hedef_dizi)
    maliyetler = [
        [0 for _ in range(hedef_uzunluk + 1)] for _ in range(kaynak_uzunluk + 1)
    ]
    islemler = [
        ["0" for _ in range(hedef_uzunluk + 1)] for _ in range(kaynak_uzunluk + 1)
    ]

    for i in range(1, kaynak_uzunluk + 1):
        maliyetler[i][0] = i * silme_maliyeti
        islemler[i][0] = f"D{kaynak_dizi[i - 1]}"

    for i in range(1, hedef_uzunluk + 1):
        maliyetler[0][i] = i * ekleme_maliyeti
        islemler[0][i] = f"I{hedef_dizi[i - 1]}"

    for i in range(1, kaynak_uzunluk + 1):
        for j in range(1, hedef_uzunluk + 1):
            if kaynak_dizi[i - 1] == hedef_dizi[j - 1]:
                maliyetler[i][j] = maliyetler[i - 1][j - 1] + kopyalama_maliyeti
                islemler[i][j] = f"C{kaynak_dizi[i - 1]}"
            else:
                maliyetler[i][j] = maliyetler[i - 1][j - 1] + degistirme_maliyeti
                islemler[i][j] = f"R{kaynak_dizi[i - 1]}" + str(hedef_dizi[j - 1])

            if maliyetler[i - 1][j] + silme_maliyeti < maliyetler[i][j]:
                maliyetler[i][j] = maliyetler[i - 1][j] + silme_maliyeti
                islemler[i][j] = f"D{kaynak_dizi[i - 1]}"

            if maliyetler[i][j - 1] + ekleme_maliyeti < maliyetler[i][j]:
                maliyetler[i][j] = maliyetler[i][j - 1] + ekleme_maliyeti
                islemler[i][j] = f"I{hedef_dizi[j - 1]}"

    return maliyetler, islemler


def donusum_birleştir(ops: list[list[str]], i: int, j: int) -> list[str]:
    """
    Ops tablosuna dayalı olarak dönüşümleri birleştirir.

    >>> ops = [['0', 'Ik', 'Iu', 'It'],
    ...        ['Dk', 'Ck', 'Iu', 'It'],
    ...        ['Da', 'Da', 'Rau', 'Rat'],
    ...        ['Ds', 'Ds', 'Rtu', 'Kt']]
    >>> x = len(ops) - 1
    >>> y = len(ops[0]) - 1
    >>> donusum_birleştir(ops, x, y)
    ['Ck', 'Rau', 'Kt']

    >>> ops1 = [['0']]
    >>> x1 = len(ops1) - 1
    >>> y1 = len(ops1[0]) - 1
    >>> donusum_birleştir(ops1, x1, y1)
    []
    """
    if i == 0 and j == 0:
        return []
    elif ops[i][j][0] in {"C", "R"}:
        seq = donusum_birleştir(ops, i - 1, j - 1)
        seq.append(ops[i][j])
        return seq
    elif ops[i][j][0] == "D":
        seq = donusum_birleştir(ops, i - 1, j)
        seq.append(ops[i][j])
        return seq
    else:
        seq = donusum_birleştir(ops, i, j - 1)
        seq.append(ops[i][j])
        return seq


if __name__ == "__main__":
    _, islemler = maliyet_hesapla("Python", "Algoritmalar", -1, 1, 2, 2)

    m = len(islemler)
    n = len(islemler[0])
    dizi = donusum_birleştir(islemler, m - 1, n - 1)

    string = list("Python")
    i = 0
    maliyet = 0

    with open("min_maliyet.txt", "w") as dosya:
        for op in dizi:
            print("".join(string))

            if op[0] == "C":
                dosya.write("%-16s" % "Kopyala %c" % op[1])
                dosya.write("\t\t\t" + "".join(string))
                dosya.write("\r\n")

                maliyet -= 1
            elif op[0] == "R":
                string[i] = op[2]

                dosya.write("%-16s" % ("Değiştir %c" % op[1] + " ile " + str(op[2])))
                dosya.write("\t\t" + "".join(string))
                dosya.write("\r\n")

                maliyet += 1
            elif op[0] == "D":
                string.pop(i)

                dosya.write("%-16s" % "Sil %c" % op[1])
                dosya.write("\t\t\t" + "".join(string))
                dosya.write("\r\n")

                maliyet += 2
            else:
                string.insert(i, op[1])

                dosya.write("%-16s" % "Ekle %c" % op[1])
                dosya.write("\t\t\t" + "".join(string))
                dosya.write("\r\n")

                maliyet += 2

            i += 1

        print("".join(string))
        print("Maliyet: ", maliyet)

        dosya.write("\r\nMinimum maliyet: " + str(maliyet))
