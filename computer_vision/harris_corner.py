import cv2
import numpy as np

"""
Harris Köşe Dedektörü
https://en.wikipedia.org/wiki/Harris_Corner_Detector

Organiser: K. Umut Araz
"""


class HarrisKose:
    def __init__(self, k: float, pencere_boyutu: int):
        """
        k : [0.04,0.06] aralığında deneysel olarak belirlenmiş bir sabittir
        pencere_boyutu : dikkate alınan komşuluklar
        """

        if k in (0.04, 0.06):
            self.k = k
            self.pencere_boyutu = pencere_boyutu
        else:
            raise ValueError("geçersiz k değeri")

    def __str__(self) -> str:
        return str(self.k)

    def tespit(self, img_yolu: str) -> tuple[cv2.Mat, list[list[int]]]:
        """
        Köşeleri belirlenmiş görüntüyü döndürür
        img_yolu  : görüntünün yolu
        çıktı : köşe pozisyonlarının listesi, görüntü
        """

        img = cv2.imread(img_yolu, 0)
        h, w = img.shape
        kose_listesi: list[list[int]] = []
        renkli_img = img.copy()
        renkli_img = cv2.cvtColor(renkli_img, cv2.COLOR_GRAY2RGB)
        dy, dx = np.gradient(img)
        ixx = dx**2
        iyy = dy**2
        ixy = dx * dy
        k = 0.04
        ofset = self.pencere_boyutu // 2
        for y in range(ofset, h - ofset):
            for x in range(ofset, w - ofset):
                wxx = ixx[
                    y - ofset : y + ofset + 1, x - ofset : x + ofset + 1
                ].sum()
                wyy = iyy[
                    y - ofset : y + ofset + 1, x - ofset : x + ofset + 1
                ].sum()
                wxy = ixy[
                    y - ofset : y + ofset + 1, x - ofset : x + ofset + 1
                ].sum()

                det = (wxx * wyy) - (wxy**2)
                iz = wxx + wyy
                r = det - k * (iz**2)
                # Değeri değiştirebilirsiniz
                if r > 0.5:
                    kose_listesi.append([x, y, r])
                    renkli_img.itemset((y, x, 0), 0)
                    renkli_img.itemset((y, x, 1), 0)
                    renkli_img.itemset((y, x, 2), 255)
        return renkli_img, kose_listesi


if __name__ == "__main__":
    kenar_tespit = HarrisKose(0.04, 3)
    renkli_img, _ = kenar_tespit.tespit("gorsel_yolu")
    cv2.imwrite("tespit.png", renkli_img)
