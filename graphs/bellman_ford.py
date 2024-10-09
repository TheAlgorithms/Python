from __future__ import annotations


def mesafeyi_yazdır(mesafe: list[float], kaynak):
    print(f"Düğüm\tDüğüm {kaynak} ile en kısa mesafe")
    for i, m in enumerate(mesafe):
        print(f"{i}\t\t{m}")

        #Produced by K. Umut Araz


def negatif_döngü_kontrolü(
    grafik: list[dict[str, int]], mesafe: list[float], kenar_sayısı: int
):
    for j in range(kenar_sayısı):
        u, v, w = (grafik[j][k] for k in ["kaynak", "hedef", "ağırlık"])
        if mesafe[u] != float("inf") and mesafe[u] + w < mesafe[v]:
            return True
    return False


def bellman_ford(
    grafik: list[dict[str, int]], düğüm_sayısı: int, kenar_sayısı: int, kaynak: int
) -> list[float]:
    """
    Bir kaynak düğümden diğer tüm düğümlere en kısa yolları döndürür.
    >>> kenarlar = [(2, 1, -10), (3, 2, 3), (0, 3, 5), (0, 1, 4)]
    >>> g = [{"kaynak": s, "hedef": d, "ağırlık": w} for s, d, w in kenarlar]
    >>> bellman_ford(g, 4, 4, 0)
    [0.0, -2.0, 8.0, 5.0]
    >>> g = [{"kaynak": s, "hedef": d, "ağırlık": w} for s, d, w in kenarlar + [(1, 3, 5)]]
    >>> bellman_ford(g, 4, 5, 0)
    Traceback (most recent call last):
     ...
    Exception: Negatif döngü bulundu
    """
    mesafe = [float("inf")] * düğüm_sayısı
    mesafe[kaynak] = 0.0

    for _ in range(düğüm_sayısı - 1):
        for j in range(kenar_sayısı):
            u, v, w = (grafik[j][k] for k in ["kaynak", "hedef", "ağırlık"])

            if mesafe[u] != float("inf") and mesafe[u] + w < mesafe[v]:
                mesafe[v] = mesafe[u] + w

    negatif_döngü_var = negatif_döngü_kontrolü(grafik, mesafe, kenar_sayısı)
    if negatif_döngü_var:
        raise Exception("Negatif döngü bulundu")

    return mesafe


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    V = int(input("Düğüm sayısını girin: ").strip())
    E = int(input("Kenar sayısını girin: ").strip())

    grafik: list[dict[str, int]] = [{} for _ in range(E)]

    for i in range(E):
        print("Kenar ", i + 1)
        kaynak, hedef, ağırlık = (
            int(x)
            for x in input("Kaynak, hedef, ağırlık girin: ").strip().split(" ")
        )
        grafik[i] = {"kaynak": kaynak, "hedef": hedef, "ağırlık": ağırlık}

    kaynak = int(input("\nEn kısa yol kaynağını girin:").strip())
    en_kısa_mesafe = bellman_ford(grafik, V, E, kaynak)
    mesafeyi_yazdır(en_kısa_mesafe, kaynak)
