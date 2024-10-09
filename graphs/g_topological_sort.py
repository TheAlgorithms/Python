# Yazar: Phyllipe Bezerra (https://github.com/pmba)

kıyafetler = {
    0: "iç çamaşırı",
    1: "pantolon",
    2: "kemer",
    3: "takım elbise",
    4: "ayakkabı",
    5: "çorap",
    6: "gömlek",
    7: "kravat",
    8: "saat",
}

graf = [[1, 4], [2, 4], [3], [], [], [4], [2, 7], [3], []]

ziyaret_edildi = [0 for x in range(len(graf))]
yığın = []


def yığını_yazdır(yığın, kıyafetler):
    sıra = 1
    while yığın:
        mevcut_kıyafet = yığın.pop()
        print(sıra, kıyafetler[mevcut_kıyafet])
        sıra += 1


def derinlik_öncelikli_arama(u, ziyaret_edildi, graf):
    ziyaret_edildi[u] = 1
    for v in graf[u]:
        if not ziyaret_edildi[v]:
            derinlik_öncelikli_arama(v, ziyaret_edildi, graf)

    yığın.append(u)


def topolojik_sıralama(graf, ziyaret_edildi):
    for v in range(len(graf)):
        if not ziyaret_edildi[v]:
            derinlik_öncelikli_arama(v, ziyaret_edildi, graf)


if __name__ == "__main__":
    topolojik_sıralama(graf, ziyaret_edildi)
    print(yığın)
    yığını_yazdır(yığın, kıyafetler)
