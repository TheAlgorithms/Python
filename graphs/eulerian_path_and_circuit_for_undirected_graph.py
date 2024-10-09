# Euler Yolu, grafikte her kenarı tam olarak bir kez ziyaret eden bir yoldur.
# Euler Çevrimi, aynı zamanda başladığı ve bittiği düğümde biten bir Euler Yolu'dur.
# zaman karmaşıklığı O(V+E)
# alan karmaşıklığı O(VE)


# euler yolu geçişini bulmak için dfs kullanımı
def dfs(u, grafik, ziyaret_edilen_kenar, yol=None):
    yol = (yol or []) + [u]
    for v in grafik[u]:
        if ziyaret_edilen_kenar[u][v] is False:
            ziyaret_edilen_kenar[u][v], ziyaret_edilen_kenar[v][u] = True, True
            yol = dfs(v, grafik, ziyaret_edilen_kenar, yol)
    return yol


# grafikte euler yolu veya çevrimi olup olmadığını kontrol etme
def yol_veya_cevrim_kontrol(grafik, max_dugum):
    tek_dereceli_dugumler = 0
    tek_dugum = -1
    for i in range(max_dugum):
        if i not in grafik:
            continue
        if len(grafik[i]) % 2 == 1:
            tek_dereceli_dugumler += 1
            tek_dugum = i
    if tek_dereceli_dugumler == 0:
        return 1, tek_dugum
    if tek_dereceli_dugumler == 2:
        return 2, tek_dugum
    return 3, tek_dugum


def euler_kontrol(grafik, max_dugum):
    ziyaret_edilen_kenar = [[False for _ in range(max_dugum + 1)] for _ in range(max_dugum + 1)]
    kontrol, tek_dugum = yol_veya_cevrim_kontrol(grafik, max_dugum)
    if kontrol == 3:
        print("graf Eulerian değil")
        print("yol yok")
        return
    baslangic_dugumu = 1
    if kontrol == 2:
        baslangic_dugumu = tek_dugum
        print("graf Euler yolu içeriyor")
    if kontrol == 1:
        print("graf Euler çevrimi içeriyor")
    yol = dfs(baslangic_dugumu, grafik, ziyaret_edilen_kenar)
    print(yol)


def ana():
    g1 = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]}
    g2 = {1: [2, 3, 4, 5], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [1, 4]}
    g3 = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2, 5], 5: [4]}
    g4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    g5 = {
        1: [],
        2: [],
        # tüm dereceler sıfır
    }
    max_dugum = 10
    euler_kontrol(g1, max_dugum)
    euler_kontrol(g2, max_dugum)
    euler_kontrol(g3, max_dugum)
    euler_kontrol(g4, max_dugum)
    euler_kontrol(g5, max_dugum)


if __name__ == "__main__":
    ana()
