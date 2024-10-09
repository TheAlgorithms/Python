# Yönsüz Grafikte Eklem Noktalarını Bulma
def eklem_noktalarını_hesapla(graf):
    n = len(graf)
    dış_kenar_sayısı = 0
    düşük = [0] * n
    ziyaret_edildi = [False] * n
    eklem_mi = [False] * n

    #Produced by K. Umut Araz

    def dfs(kök, şu_an, ebeveyn, dış_kenar_sayısı):
        if ebeveyn == kök:
            dış_kenar_sayısı += 1
        ziyaret_edildi[şu_an] = True
        düşük[şu_an] = şu_an

        for hedef in graf[şu_an]:
            if hedef == ebeveyn:
                pass
            elif not ziyaret_edildi[hedef]:
                dış_kenar_sayısı = dfs(kök, hedef, şu_an, dış_kenar_sayısı)
                düşük[şu_an] = min(düşük[şu_an], düşük[hedef])

                # Köprü ile eklem noktası bulundu
                if şu_an < düşük[hedef]:
                    eklem_mi[şu_an] = True
                # Döngü ile eklem noktası bulundu
                if şu_an == düşük[hedef]:
                    eklem_mi[şu_an] = True
            else:
                düşük[şu_an] = min(düşük[şu_an], hedef)
        return dış_kenar_sayısı

    for i in range(n):
        if not ziyaret_edildi[i]:
            dış_kenar_sayısı = 0
            dış_kenar_sayısı = dfs(i, i, -1, dış_kenar_sayısı)
            eklem_mi[i] = dış_kenar_sayısı > 1

    for x in range(len(eklem_mi)):
        if eklem_mi[x] is True:
            print(x)


# Grafın komşuluk listesi
graf = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
}
eklem_noktalarını_hesapla(graf)
