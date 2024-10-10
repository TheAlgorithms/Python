# Kaynak: https://computersciencewiki.org/index.php/Max-pooling_/_Pooling
# Gerekli Kütüphanelerin İçe Aktarılması

#Organiser: K. Umut Araz
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
    
    # Çıktı matrisinin boyutunu hesapla
    maxpool_shape = (arr.shape[0] - boyut) // adim + 1
    # maxpool_shape boyutunda sıfırlardan oluşan çıktı matrisini başlat
    guncellenmis_arr = np.zeros((maxpool_shape, maxpool_shape))

    for i in range(0, arr.shape[0] - boyut + 1, adim):
        for j in range(0, arr.shape[1] - boyut + 1, adim):
            # Havuzlama matrisinin maksimumunu hesapla
            guncellenmis_arr[i // adim][j // adim] = np.max(arr[i : i + boyut, j : j + boyut])

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
    
    # Çıktı matrisinin boyutunu hesapla
    avgpool_shape = (arr.shape[0] - boyut) // adim + 1
    # avgpool_shape boyutunda sıfırlardan oluşan çıktı matrisini başlat
    guncellenmis_arr = np.zeros((avgpool_shape, avgpool_shape))

    for i in range(0, arr.shape[0] - boyut + 1, adim):
        for j in range(0, arr.shape[1] - boyut + 1, adim):
            # Havuzlama matrisinin ortalamasını hesapla
            guncellenmis_arr[i // adim][j // adim] = np.mean(arr[i : i + boyut, j : j + boyut])

    return guncellenmis_arr


# Ana Fonksiyon
if __name__ == "__main__":
    from doctest import testmod

    testmod(name="ortalama_havuzlama", verbose=True)

    # Görüntüyü Yükleme
    goruntu = Image.open("goruntu_yolu")

    # Görüntüyü numpy dizisine dönüştürme ve maksimum havuzlama, sonucu gösterme
    Image.fromarray(maksimum_havuzlama(np.array(goruntu), boyut=3, adim=2)).show()

    # Görüntüyü numpy dizisine dönüştürme ve ortalama havuzlama, sonucu gösterme
    Image.fromarray(ortalama_havuzlama(np.array(goruntu), boyut=3, adim=2)).show()
