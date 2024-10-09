"""
FP-GraphMiner - Ağ Grafikleri için Hızlı Sık Kullanılan Desen Madenciliği Algoritması

FP-GraphMiner, bir dizi ağ grafiğini Sık Kullanılan Desen Grafiği (veya FP-Graph) olarak
kompakt bir şekilde temsil eden yeni bir Sık Kullanılan Desen Grafiği Madenciliği algoritmasıdır.
Bu grafik, maksimum sık kullanılan alt grafikleri ve maksimum ortak alt grafikleri de içeren
sık kullanılan alt grafikleri verimli bir şekilde madencilik yapmak için kullanılabilir.

URL: https://www.researchgate.net/publication/235255851
"""

# fmt: off
kenar_dizisi = [
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'bh-e12', 'cd-e2', 'ce-e4',
     'de-e1', 'df-e8', 'dg-e5', 'dh-e10', 'ef-e3', 'eg-e2', 'fg-e6', 'gh-e6', 'hi-e3'],
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'cd-e2', 'de-e1', 'df-e8',
     'ef-e3', 'eg-e2', 'fg-e6'],
    ['ab-e1', 'ac-e3', 'bc-e4', 'bd-e2', 'de-e1', 'df-e8', 'dg-e5', 'ef-e3', 'eg-e2',
     'eh-e12', 'fg-e6', 'fh-e10', 'gh-e6'],
    ['ab-e1', 'ac-e3', 'bc-e4', 'bd-e2', 'bh-e12', 'cd-e2', 'df-e8', 'dh-e10'],
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'cd-e2', 'ce-e4', 'de-e1', 'df-e8',
     'dg-e5', 'ef-e3', 'eg-e2', 'fg-e6']
]
# fmt: on

# Produced By K. Umut Araz


def ayri_kenarlari_al(kenar_dizisi):
    """
    Kenar dizisinden ayrık kenarları döndürür
    >>> sorted(ayri_kenarlari_al(kenar_dizisi))
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    ayri_kenar = set()
    for satir in kenar_dizisi:
        for eleman in satir:
            ayri_kenar.add(eleman[0])
    return list(ayri_kenar)


def bit_kodu_al(kenar_dizisi, ayri_kenar):
    """
    Ayrık kenarın bit kodunu döndürür
    """
    bit_kodu = ["0"] * len(kenar_dizisi)
    for i, satir in enumerate(kenar_dizisi):
        for eleman in satir:
            if ayri_kenar in eleman[0]:
                bit_kodu[i] = "1"
                break
    return "".join(bit_kodu)


def frekans_tablosu_al(kenar_dizisi):
    """
    Frekans Tablosunu Döndürür
    """
    ayri_kenar = ayri_kenarlari_al(kenar_dizisi)
    frekans_tablosu = {}

    for eleman in ayri_kenar:
        bit = bit_kodu_al(kenar_dizisi, eleman)
        s = bit.count("1")
        frekans_tablosu[eleman] = [s, bit]
    # [Ayrık kenar, WT(Bit kodu), Bit kodu] azalan sırayla sakla
    sirali_frekans_tablosu = [
        [k, v[0], v[1]]
        for k, v in sorted(frekans_tablosu.items(), key=lambda v: v[1][0], reverse=True)
    ]
    return sirali_frekans_tablosu


def dugumleri_al(frekans_tablosu):
    """
    Düğümleri Döndürür
    format düğümler={bit kodu: bit kodunu temsil eden kenarlar}
    >>> dugumleri_al([['ab', 5, '11111'], ['ac', 5, '11111'], ['df', 5, '11111'],
    ...               ['bd', 5, '11111'], ['bc', 5, '11111']])
    {'11111': ['ab', 'ac', 'df', 'bd', 'bc']}
    """
    dugumler = {}
    for _, eleman in enumerate(frekans_tablosu):
        dugumler.setdefault(eleman[2], []).append(eleman[0])
    return dugumler


def kume_al(dugumler):
    """
    Küme Döndürür
    format kume:{WT(bit kodu): aynı WT'ye sahip düğümler}
    """
    kume = {}
    for anahtar, deger in dugumler.items():
        kume.setdefault(anahtar.count("1"), {})[anahtar] = deger
    return kume


def destek_al(kume):
    """
    Destek Döndürür
    >>> destek_al({5: {'11111': ['ab', 'ac', 'df', 'bd', 'bc']},
    ...            4: {'11101': ['ef', 'eg', 'de', 'fg'], '11011': ['cd']},
    ...            3: {'11001': ['ad'], '10101': ['dg']},
    ...            2: {'10010': ['dh', 'bh'], '11000': ['be'], '10100': ['gh'],
    ...                '10001': ['ce']},
    ...            1: {'00100': ['fh', 'eh'], '10000': ['hi']}})
    [100.0, 80.0, 60.0, 40.0, 20.0]
    """
    return [i * 100 / len(kume) for i in kume]


def hepsini_yazdir() -> None:
    print("\nDüğümler\n")
    for anahtar, deger in dugumler.items():
        print(anahtar, deger)
    print("\nDestek\n")
    print(destek)
    print("\nKüme\n")
    for anahtar, deger in sorted(kume.items(), reverse=True):
        print(anahtar, deger)
    print("\nGrafik\n")
    for anahtar, deger in grafik.items():
        print(anahtar, deger)
    print("\nSık kullanılan alt grafiklerin Kenar Listesi\n")
    for kenar_listesi in sik_alt_grafik_kenar_listesi:
        print(kenar_listesi)


def kenar_olustur(dugumler, grafik, kume, c1):
    """
    Düğümler arasında kenar oluştur
    """
    for i in kume[c1]:
        sayac = 0
        c2 = c1 + 1
        while c2 < max(kume.keys()):
            for j in kume[c2]:
                """
                Koşul sağlandığında kenar oluşturur
                """
                if int(i, 2) & int(j, 2) == int(i, 2):
                    if tuple(dugumler[i]) in grafik:
                        grafik[tuple(dugumler[i])].append(dugumler[j])
                    else:
                        grafik[tuple(dugumler[i])] = [dugumler[j]]
                    sayac += 1
            if sayac == 0:
                c2 = c2 + 1
            else:
                break


def grafik_olustur(kume, dugumler):
    x = kume[max(kume.keys())]
    kume[max(kume.keys()) + 1] = "Başlık"
    grafik = {}
    for i in x:
        if (["Başlık"],) in grafik:
            grafik[(["Başlık"],)].append(x[i])
        else:
            grafik[(["Başlık"],)] = [x[i]]
    for i in x:
        grafik[(x[i],)] = [["Başlık"]]
    i = 1
    while i < max(kume) - 1:
        kenar_olustur(dugumler, grafik, kume, i)
        i = i + 1
    return grafik


def dfs_yurut(grafik, baslangic, bitis, yol=None):
    """
    Verilen düğümden Başlık düğümüne farklı DFS yürüyüşlerini bul
    """
    yol = (yol or []) + [baslangic]
    if baslangic == bitis:
        yollar.append(yol)
    for dugum in grafik[baslangic]:
        if tuple(dugum) not in yol:
            dfs_yurut(grafik, tuple(dugum), bitis, yol)


def destek_ile_sik_alt_grafik_bul(destek, kume, grafik):
    """
    Birden fazla sık kullanılan alt grafiğin kenarlarını bul
    """
    k = int(destek / 100 * (len(kume) - 1))
    for i in kume[k]:
        dfs_yurut(grafik, tuple(kume[k][i]), (["Başlık"],))


def sik_alt_grafik_kenar_listesi(yollar):
    """
    Sık kullanılan alt grafikler için Kenar listesini döndürür
    """
    sik_alt_kenar_listesi = []
    for kenarlar in yollar:
        kl = []
        for j in range(len(kenarlar) - 1):
            temp = list(kenarlar[j])
            for e in temp:
                kenar = (e[0], e[1])
                kl.append(kenar)
        sik_alt_kenar_listesi.append(kl)
    return sik_alt_kenar_listesi


def on_islem(kenar_dizisi):
    """
    Kenar dizisini ön işleme tabi tut
    >>> on_islem([['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'bh-e12',
    ...            'cd-e2', 'ce-e4', 'de-e1', 'df-e8', 'dg-e5', 'dh-e10', 'ef-e3',
    ...            'eg-e2', 'fg-e6', 'gh-e6', 'hi-e3']])

    """
    for i in range(len(kenar_dizisi)):
        for j in range(len(kenar_dizisi[i])):
            t = kenar_dizisi[i][j].split("-")
            kenar_dizisi[i][j] = t


if __name__ == "__main__":
    on_islem(kenar_dizisi)
    frekans_tablosu = frekans_tablosu_al(kenar_dizisi)
    dugumler = dugumleri_al(frekans_tablosu)
    kume = kume_al(dugumler)
    destek = destek_al(kume)
    grafik = grafik_olustur(kume, dugumler)
    destek_ile_sik_alt_grafik_bul(60, kume, grafik)
    yollar: list = []
    sik_alt_grafik_kenar_listesi = sik_alt_grafik_kenar_listesi(yollar)
    hepsini_yazdir()
