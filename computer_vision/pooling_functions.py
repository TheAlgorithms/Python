# Kaynak : https://computersciencewiki.org/index.php/Max-pooling_/_Pooling
# Kütüphanelerin İçe Aktarılması
import numpy as np
from PIL import Image


# Maksimum Havuzlama Fonksiyonu
def maksimum_havuzlama(arr: np.ndarray, boyut: int, adim: int) -> np.ndarray:
    """
    Bu fonksiyon, 2D matris (görüntü) giriş dizisi üzerinde maksimum havuzlama yapmak için kullanılır.
    Argümanlar:
        arr: numpy dizisi
        boyut: havuzlama matrisinin boyutu
        adim: giriş matrisi üzerinde kaydırılan piksel sayısı
    Döndürür:
        maksimum havuzlanmış matrisin numpy dizisi
    Örnek Girdi Çıktı:
    >>> maksimum_havuzlama([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 6.,  8.],
           [14., 16.]])
    >>> maksimum_havuzlama([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[241., 180.],
           [241., 157.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Giriş dizisi kare matris değil")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0

    # Çıktı matrisinin şeklini hesapla
    maxpool_shape = (arr.shape[0] - boyut) // adim + 1
    # maxpool_shape boyutunda sıfırlardan oluşan çıktı matrisini başlat
    guncellenmis_arr = np.zeros((maxpool_shape, maxpool_shape))

    while i < arr.shape[0]:
        if i + boyut > arr.shape[0]:
            # Matrisin sonuna gelindiyse, döngüyü kır
            break
        while j < arr.shape[1]:
            # Matrisin sonuna gelindiyse, döngüyü kır
            if j + boyut > arr.shape[1]:
                break
            # Havuzlama matrisinin maksimumunu hesapla
            guncellenmis_arr[mat_i][mat_j] = np.max(arr[i : i + boyut, j : j + boyut])
            # Havuzlama matrisini sütun pikselleri kadar kaydır
            j += adim
            mat_j += 1

        # Havuzlama matrisini satır pikselleri kadar kaydır
        i += adim
        mat_i += 1

        # Sütun indeksini 0'a sıfırla
        j = 0
        mat_j = 0

    return guncellenmis_arr


# Ortalama Havuzlama Fonksiyonu
def ortalama_havuzlama(arr: np.ndarray, boyut: int, adim: int) -> np.ndarray:
    """
    Bu fonksiyon, 2D matris (görüntü) giriş dizisi üzerinde ortalama havuzlama yapmak için kullanılır.
    Argümanlar:
        arr: numpy dizisi
        boyut: havuzlama matrisinin boyutu
        adim: giriş matrisi üzerinde kaydırılan piksel sayısı
    Döndürür:
        ortalama havuzlanmış matrisin numpy dizisi
    Örnek Girdi Çıktı:
    >>> ortalama_havuzlama([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 3.,  5.],
           [11., 13.]])
    >>> ortalama_havuzlama([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[161., 102.],
           [114.,  69.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Giriş dizisi kare matris değil")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0

    # Çıktı matrisinin şeklini hesapla
    avgpool_shape = (arr.shape[0] - boyut) // adim + 1
    # avgpool_shape boyutunda sıfırlardan oluşan çıktı matrisini başlat
    guncellenmis_arr = np.zeros((avgpool_shape, avgpool_shape))

    while i < arr.shape[0]:
        # Matrisin sonuna gelindiyse, döngüyü kır
        if i + boyut > arr.shape[0]:
            break
        while j < arr.shape[1]:
            # Matrisin sonuna gelindiyse, döngüyü kır
            if j + boyut > arr.shape[1]:
                break
            # Havuzlama matrisinin ortalamasını hesapla
            guncellenmis_arr[mat_i][mat_j] = int(np.average(arr[i : i + boyut, j : j + boyut]))
            # Havuzlama matrisini sütun pikselleri kadar kaydır
            j += adim
            mat_j += 1

        # Havuzlama matrisini satır pikselleri kadar kaydır
        i += adim
        mat_i += 1
        # Sütun indeksini 0'a sıfırla
        j = 0
        mat_j = 0

    return guncellenmis_arr


# Ana Fonksiyon
if __name__ == "__main__":
    from doctest import testmod

    testmod(name="ortalama_havuzlama", verbose=True)

    # Görüntüyü Yükleme
    goruntu = Image.open("goruntu_yolu")

    # Görüntüyü numpy dizisine dönüştürme ve maksimum havuzlama, sonucu gösterme
    # Görüntünün kare matris olduğundan emin olun

    Image.fromarray(maksimum_havuzlama(np.array(goruntu), boyut=3, adim=2)).show()

    # Görüntüyü numpy dizisine dönüştürme ve ortalama havuzlama, sonucu gösterme
    # Görüntünün kare matris olduğundan emin olun

    Image.fromarray(ortalama_havuzlama(np.array(goruntu), boyut=3, adim=2)).show()
