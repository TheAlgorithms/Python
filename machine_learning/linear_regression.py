"""
Doğrusal regresyon, genellikle öngörücü analiz için kullanılan en temel regresyon türüdür.
Fikir oldukça basittir: bir veri setimiz var ve bununla ilişkili özelliklerimiz var.
Özellikler çok dikkatli seçilmelidir çünkü modelimizin gelecekteki tahminleri ne kadar iyi yapabileceğini belirler.
Bu özelliklerin ağırlıklarını, birçok iterasyon boyunca, veri setimize en iyi uyacak şekilde ayarlamaya çalışırız.
Bu özel kodda, bir CSGO veri seti (ADR vs Rating) kullandım. Veri seti üzerinden en iyi uyumu sağlayacak bir çizgi çizmeye ve parametreleri tahmin etmeye çalışıyoruz.
"""

import numpy as np
import requests


def veri_seti_topla():
    """CSGO veri setini topla
    Veri seti, bir oyuncunun ADR'si ile Rating'ini içerir
    :return : bağlantıdan elde edilen veri seti, matris olarak
    """
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    satırlar = response.text.splitlines()
    veri = []
    for öğe in satırlar:
        öğe = öğe.split(",")
        veri.append(öğe)
    veri.pop(0)  # Bu, listeden etiketleri kaldırmak içindir
    veri_seti = np.matrix(veri)
    return veri_seti


def dik_yokuş_çıkışını_çalıştır(veri_x, veri_y, veri_uzunluğu, alfa, theta):
    """Dik yokuş çıkışını çalıştır ve Özellik vektörünü buna göre güncelle
    :param veri_x   : veri setini içerir
    :param veri_y   : her veri girişiyle ilişkili çıktıyı içerir
    :param veri_uzunluğu : verinin uzunluğu
    :param alfa    : Modelin öğrenme oranı
    :param theta    : Özellik vektörü (modelimizin ağırlıkları)
    ;param return    : Güncellenmiş Özellikler, kullanarak
                       mevcut_özellikler - alfa_ * gradyan(özelliğe göre)
    """
    n = veri_uzunluğu

    çarpım = np.dot(theta, veri_x.transpose())
    çarpım -= veri_y.transpose()
    toplam_gradyan = np.dot(çarpım, veri_x)
    theta = theta - (alfa / n) * toplam_gradyan
    return theta


def kare_hata_toplamı(veri_x, veri_y, veri_uzunluğu, theta):
    """Hata hesaplaması için kare hata toplamını döndür
    :param veri_x    : veri setimizi içerir
    :param veri_y    : çıktıyı içerir (sonuç vektörü)
    :param veri_uzunluğu  : veri setinin uzunluğu
    :param theta     : özellik vektörünü içerir
    :return          : verilen özelliklerden hesaplanan kare hata toplamı
    """
    çarpım = np.dot(theta, veri_x.transpose())
    çarpım -= veri_y.transpose()
    toplam_öğe = np.sum(np.square(çarpım))
    hata = toplam_öğe / (2 * veri_uzunluğu)
    return hata


def doğrusal_regresyon_çalıştır(veri_x, veri_y):
    """Veri seti üzerinde Doğrusal regresyon uygula
    :param veri_x  : veri setimizi içerir
    :param veri_y  : çıktıyı içerir (sonuç vektörü)
    :return        : en iyi uyum çizgisi için özellik (Özellik vektörü)
    """
    iterasyonlar = 100000
    alfa = 0.0001550

    özellik_sayısı = veri_x.shape[1]
    veri_uzunluğu = veri_x.shape[0] - 1

    theta = np.zeros((1, özellik_sayısı))

    for i in range(iterasyonlar):
        theta = dik_yokuş_çıkışını_çalıştır(veri_x, veri_y, veri_uzunluğu, alfa, theta)
        hata = kare_hata_toplamı(veri_x, veri_y, veri_uzunluğu, theta)
        print(f"İterasyon {i + 1} - Hata {hata:.5f}")

    return theta


def ortalama_mutlak_hata(tahmin_edilen_y, orijinal_y):
    """Hata hesaplaması için kare hata toplamını döndür
    :param tahmin_edilen_y   : tahminin çıktısını içerir (sonuç vektörü)
    :param orijinal_y    : beklenen sonuç değerlerini içerir
    :return          : verilen özelliklerden hesaplanan ortalama mutlak hata
    """
    toplam = sum(abs(y - tahmin_edilen_y[i]) for i, y in enumerate(orijinal_y))
    return toplam / len(orijinal_y)


def ana():
    """Sürücü fonksiyonu"""
    veri = veri_seti_topla()

    veri_uzunluğu = veri.shape[0]
    veri_x = np.c_[np.ones(veri_uzunluğu), veri[:, :-1]].astype(float)
    veri_y = veri[:, -1].astype(float)

    theta = doğrusal_regresyon_çalıştır(veri_x, veri_y)
    sonuç_uzunluğu = theta.shape[1]
    print("Sonuç Özellik vektörü : ")
    for i in range(sonuç_uzunluğu):
        print(f"{theta[0, i]:.5f}")


if __name__ == "__main__":
    ana()
