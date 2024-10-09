"""
Bir grafiği bölmek için Karger's Algoritmasının bir uygulaması.
"""

from __future__ import annotations

import random

#Produced By K. Umut Araz

# Bu grafiğin komşuluk listesi temsili:
# https://en.wikipedia.org/wiki/File:Single_run_of_Karger%E2%80%99s_Mincut_algorithm.svg
TEST_GRAFİK = {
    "1": ["2", "3", "4", "5"],
    "2": ["1", "3", "4", "5"],
    "3": ["1", "2", "4", "5", "10"],
    "4": ["1", "2", "3", "5", "6"],
    "5": ["1", "2", "3", "4", "7"],
    "6": ["7", "8", "9", "10", "4"],
    "7": ["6", "8", "9", "10", "5"],
    "8": ["6", "7", "9", "10"],
    "9": ["6", "7", "8", "10"],
    "10": ["6", "7", "8", "9", "3"],
}


def grafiği_böl(grafik: dict[str, list[str]]) -> set[tuple[str, str]]:
    """
    Karger's Algoritmasını kullanarak bir grafiği böler. Pseudocode buradan
    alınmıştır: https://en.wikipedia.org/wiki/Karger%27s_algorithm.
    Bu fonksiyon rastgele seçimler içerir, bu nedenle tutarlı çıktılar vermez.

    Parametreler:
        grafik: Grafiğin komşuluk listelerini içeren bir sözlük.
            Düğümler string olmalıdır.

    Döndürür:
        Karger's Algoritması tarafından bulunan kesitin kesim kümesi.

    >>> grafik = {'0':['1'], '1':['0']}
    >>> grafiği_böl(grafik)
    {('0', '1')}
    """
    # Küçültülen düğümleri, "içerdiği" tüm düğümlerin listesine eşleyen sözlük.
    küçültülen_düğümler = {düğüm: {düğüm} for düğüm in grafik}

    grafik_kopyası = {düğüm: grafik[düğüm][:] for düğüm in grafik}

    while len(grafik_kopyası) > 2:
        # Rastgele bir kenar seç.
        u = random.choice(list(grafik_kopyası.keys()))
        v = random.choice(grafik_kopyası[u])

        # (u, v) kenarını yeni düğüm uv'ye küçült
        uv = u + v
        uv_komşuları = list(set(grafik_kopyası[u] + grafik_kopyası[v]))
        uv_komşuları.remove(u)
        uv_komşuları.remove(v)
        grafik_kopyası[uv] = uv_komşuları
        for komşu in uv_komşuları:
            grafik_kopyası[komşu].append(uv)

        küçültülen_düğümler[uv] = set(küçültülen_düğümler[u].union(küçültülen_düğümler[v]))

        # u ve v düğümlerini kaldır.
        del grafik_kopyası[u]
        del grafik_kopyası[v]
        for komşu in uv_komşuları:
            if u in grafik_kopyası[komşu]:
                grafik_kopyası[komşu].remove(u)
            if v in grafik_kopyası[komşu]:
                grafik_kopyası[komşu].remove(v)

    # Kesim kümesini bul.
    gruplar = [küçültülen_düğümler[düğüm] for düğüm in grafik_kopyası]
    return {
        (düğüm, komşu)
        for düğüm in gruplar[0]
        for komşu in grafik[düğüm]
        if komşu in gruplar[1]
    }


if __name__ == "__main__":
    print(grafiği_böl(TEST_GRAFİK))
