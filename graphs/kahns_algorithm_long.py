# Kahn Algoritması kullanarak Yönlendirilmiş Asiklik Grafikte en uzun mesafeyi bulma
def en_uzun_mesafe(grafik):
    giris_derecesi = [0] * len(grafik)
    kuyruk = []
    uzun_mesafe = [1] * len(grafik)

    for degerler in grafik.values():
        for i in degerler:
            giris_derecesi[i] += 1

    for i in range(len(giris_derecesi)):
        if giris_derecesi[i] == 0:
            kuyruk.append(i)

    while kuyruk:
        dugum = kuyruk.pop(0)
        for x in grafik[dugum]:
            giris_derecesi[x] -= 1

            uzun_mesafe[x] = max(uzun_mesafe[x], uzun_mesafe[dugum] + 1)

            if giris_derecesi[x] == 0:
                kuyruk.append(x)

    print(max(uzun_mesafe))


# Grafiğin komşuluk listesi
grafik = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
en_uzun_mesafe(grafik)
