# https://www.chilimath.com/lessons/advanced-algebra/cramers-rule-with-two-variables
# https://en.wikipedia.org/wiki/Cramer%27s_rule


def cramers_rule_2x2(equation1: list[int], equation2: list[int]) -> tuple[float, float]:
    """

    Organised by K. Umut Araz

    İki değişkenli lineer denklemler sistemini çözer.
    :param equation1: 3 sayıdan oluşan liste
    :param equation2: 3 sayıdan oluşan liste
    :return: Çözümün sonucu
    girdi formatı: [a1, b1, d1], [a2, b2, d2]
    determinant = [[a1, b1], [a2, b2]]
    determinant_x = [[d1, b1], [d2, b2]]
    determinant_y = [[a1, d1], [a2, d2]]

    >>> cramers_rule_2x2([2, 3, 0], [5, 1, 0])
    (0.0, 0.0)
    >>> cramers_rule_2x2([0, 4, 50], [2, 0, 26])
    (13.0, 12.5)
    >>> cramers_rule_2x2([11, 2, 30], [1, 0, 4])
    (4.0, -7.0)
    >>> cramers_rule_2x2([4, 7, 1], [1, 2, 0])
    (2.0, -1.0)

    >>> cramers_rule_2x2([1, 2, 3], [2, 4, 6])
    Traceback (most recent call last):
        ...
    ValueError: Sonsuz çözüm. (Tutarlı sistem)
    >>> cramers_rule_2x2([1, 2, 3], [2, 4, 7])
    Traceback (most recent call last):
        ...
    ValueError: Çözüm yok. (Tutarsız sistem)
    >>> cramers_rule_2x2([1, 2, 3], [11, 22])
    Traceback (most recent call last):
        ...
    ValueError: Lütfen geçerli bir denklem girin.
    >>> cramers_rule_2x2([0, 1, 6], [0, 0, 3])
    Traceback (most recent call last):
        ...
    ValueError: Çözüm yok. (Tutarsız sistem)
    >>> cramers_rule_2x2([0, 0, 6], [0, 0, 3])
    Traceback (most recent call last):
        ...
    ValueError: İki denklemin a ve b'si sıfır olamaz.
    >>> cramers_rule_2x2([1, 2, 3], [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Sonsuz çözüm. (Tutarlı sistem)
    >>> cramers_rule_2x2([0, 4, 50], [0, 3, 99])
    Traceback (most recent call last):
        ...
    ValueError: Çözüm yok. (Tutarsız sistem)
    """

    # Girdinin geçerliliğini kontrol et
    if not len(equation1) == len(equation2) == 3:
        raise ValueError("Lütfen geçerli bir denklem girin.")
    if equation1[0] == equation1[1] == equation2[0] == equation2[1] == 0:
        raise ValueError("İki denklemin a ve b'si sıfır olamaz.")

    # Katsayıları çıkar
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    # Matrislerin determinantlarını hesapla
    determinant = a1 * b2 - a2 * b1
    determinant_x = c1 * b2 - c2 * b1
    determinant_y = a1 * c2 - a2 * c1

    # Lineer denklemler sisteminin bir çözümü olup olmadığını kontrol et (Cramer kuralını kullanarak)
    if determinant == 0:
        if determinant_x == determinant_y == 0:
            raise ValueError("Sonsuz çözüm. (Tutarlı sistem)")
        else:
            raise ValueError("Çözüm yok. (Tutarsız sistem)")
    elif determinant_x == determinant_y == 0:
        # Trivial çözüm (Tutarsız sistem)
        return (0.0, 0.0)
    else:
        x = determinant_x / determinant
        y = determinant_y / determinant
        # Non-Trivial Çözüm (Tutarlı sistem)
        return (x, y)
