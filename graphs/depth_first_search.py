"""Özyinelemeli olmayan bir DFS algoritmasının uygulanması."""

from __future__ import annotations


def derinlik_oncelikli_arama(graf: dict, başlangıç: str) -> set[str]:
    """Graf üzerinde Derinlik Öncelikli Arama (DFS)
    :param graf: sözlük formatında yönlendirilmiş graf
    :param başlangıç: başlangıç düğümü olarak bir string
    :returns: aramanın izi
    >>> input_G = { "A": ["B", "C", "D"], "B": ["A", "D", "E"],
    ... "C": ["A", "F"], "D": ["B", "D"], "E": ["B", "F"],
    ... "F": ["C", "E", "G"], "G": ["F"] }
    >>> output_G = list({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
    >>> all(x in output_G for x in list(derinlik_oncelikli_arama(input_G, "A")))
    True
    >>> all(x in output_G for x in list(derinlik_oncelikli_arama(input_G, "G")))
    True
    """
    ziyaret_edilen, yığın = set(başlangıç), [başlangıç]

    while yığın:
        v = yığın.pop()
        ziyaret_edilen.add(v)
        # BFS'den farklar:
        # 1) ilk eleman yerine son elemanı çıkar
        # 2) bitişik elemanları keşfetmeden yığına ekle
        for komsu in reversed(graf[v]):
            if komsu not in ziyaret_edilen:
                yığın.append(komsu)
    return ziyaret_edilen


G = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(derinlik_oncelikli_arama(G, "A"))
