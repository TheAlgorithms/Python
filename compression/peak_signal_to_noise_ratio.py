"""
Tepe Sinyal-Gürültü Oranı - PSNR
    https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio

    Organiser: K. Umut Araz


Kaynak:
https://tutorials.techonical.com/how-to-calculate-psnr-value-of-two-images-using-python
"""

import math
import os

import cv2
import numpy as np

PIXEL_MAX = 255.0

def tepe_sinyal_gurultu_orani(orijinal: np.ndarray, sikistirilmis: np.ndarray) -> float:
    mse = np.mean((orijinal - sikistirilmis) ** 2)
    if mse == 0:
        return 100.0  # MSE sıfırsa, PSNR değeri 100 dB olarak kabul edilir.

    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def main() -> None:
    dir_yolu = os.path.dirname(os.path.realpath(__file__))
    # Görüntüleri yükleme (orijinal görüntü ve sıkıştırılmış görüntü)
    orijinal = cv2.imread(os.path.join(dir_yolu, "image_data/original_image.png"))
    sikistirilmis = cv2.imread(os.path.join(dir_yolu, "image_data/compressed_image.png"), 1)

    orijinal2 = cv2.imread(os.path.join(dir_yolu, "image_data/PSNR-example-base.png"))
    sikistirilmis2 = cv2.imread(
        os.path.join(dir_yolu, "image_data/PSNR-example-comp-10.jpg"), 1
    )

    # Beklenen değer: 29.73dB
    print("-- İlk Test --")
    print(f"PSNR değeri: {tepe_sinyal_gurultu_orani(orijinal, sikistirilmis)} dB")

    # Beklenen değer: 31.53dB (Vikipedi Örneği)
    print("\n-- İkinci Test --")
    print(f"PSNR değeri: {tepe_sinyal_gurultu_orani(orijinal2, sikistirilmis2)} dB")

if __name__ == "__main__":
    main()
