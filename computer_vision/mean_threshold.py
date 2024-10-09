from PIL import Image

"""
Görüntü işleme için ortalama eşikleme algoritması
https://en.wikipedia.org/wiki/Thresholding_(image_processing)
"""


def ortalama_esikleme(goruntu: Image) -> Image:
    """
    goruntu: gri tonlamalı bir PIL görüntü nesnesidir
    """
    yukseklik, genislik = goruntu.size
    ortalama = 0
    pikseller = goruntu.load()
    for i in range(genislik):
        for j in range(yukseklik):
            piksel = pikseller[j, i]
            ortalama += piksel
    ortalama //= genislik * yukseklik

    for j in range(genislik):
        for i in range(yukseklik):
            pikseller[i, j] = 255 if pikseller[i, j] > ortalama else 0
    return goruntu


if __name__ == "__main__":
    goruntu = ortalama_esikleme(Image.open("goruntu_yolu").convert("L"))
    goruntu.save("cikti_goruntu_yolu")
