"""
Horn-Schunck yöntemi, bir dizi görüntünün her bir pikseli için optik akışı tahmin eder.
İki ardışık kare arasında parlaklık sabitliği ve optik akışta düzgünlük varsayarak çalışır.

Faydalı kaynaklar:
Wikipedia: https://en.wikipedia.org/wiki/Horn%E2%80%93Schunck_method
Makale: http://image.diku.dk/imagecanon/material/HornSchunckOptical_Flow.pdf

Organiser: K. Umut Araz
"""

from typing import SupportsIndex

import numpy as np
from scipy.ndimage import convolve


def warp(
    image: np.ndarray, horizontal_flow: np.ndarray, vertical_flow: np.ndarray
) -> np.ndarray:
    """
    Bir görüntünün piksellerini yatay ve dikey akışları kullanarak yeni bir görüntüye kaydırır.
    Geçersiz bir konumdan kaydırılan pikseller 0 olarak ayarlanır.

    Parametreler:
        image: Gri tonlamalı görüntü
        horizontal_flow: Yatay akış
        vertical_flow: Dikey akış

    Döndürür: Kaydırılmış görüntü

    >>> warp(np.array([[0, 1, 2], [0, 3, 0], [2, 2, 2]]), \
    np.array([[0, 1, -1], [-1, 0, 0], [1, 1, 1]]), \
    np.array([[0, 0, 0], [0, 1, 0], [0, 0, 1]]))
    array([[0, 0, 0],
           [3, 1, 0],
           [0, 2, 3]])
    """
    flow = np.stack((horizontal_flow, vertical_flow), 2)

    # Tüm piksel koordinatlarının bir ızgarasını oluşturun ve hedef piksel koordinatlarını elde etmek için akışı çıkarın
    grid = np.stack(
        np.meshgrid(np.arange(0, image.shape[1]), np.arange(0, image.shape[0])), 2
    )
    grid = np.round(grid - flow).astype(np.int32)

    # Orijinal görüntünün dışındaki konumları bulun
    invalid = (grid < 0) | (grid >= np.array([image.shape[1], image.shape[0]]))
    grid[invalid] = 0

    warped = image[grid[:, :, 1], grid[:, :, 0]]

    # Geçersiz konumlardaki pikselleri 0 olarak ayarlayın
    warped[invalid[:, :, 0] | invalid[:, :, 1]] = 0

    return warped


def horn_schunck(
    image0: np.ndarray,
    image1: np.ndarray,
    num_iter: SupportsIndex,
    alpha: float | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Bu fonksiyon Horn-Schunck algoritmasını gerçekleştirir ve tahmini optik akışı döndürür.
    Giriş görüntülerinin gri tonlamalı olduğu ve [0, 1] aralığında normalize edildiği varsayılır.

    Parametreler:
        image0: Dizinin ilk görüntüsü
        image1: Dizinin ikinci görüntüsü
        alpha: Düzenleme sabiti
        num_iter: Gerçekleştirilen iterasyon sayısı

    Döndürür: tahmini yatay ve dikey akış

    >>> np.round(horn_schunck(np.array([[0, 0, 2], [0, 0, 2]]), \
    np.array([[0, 2, 0], [0, 2, 0]]), alpha=0.1, num_iter=110)).\
    astype(np.int32)
    array([[[ 0, -1, -1],
            [ 0, -1, -1]],
    <BLANKLINE>
           [[ 0,  0,  0],
            [ 0,  0,  0]]], dtype=int32)
    """
    if alpha is None:
        alpha = 0.1

    # Akışı başlat
    horizontal_flow = np.zeros_like(image0)
    vertical_flow = np.zeros_like(image0)

    # Türevlerin ve ortalama hızın hesaplanması için çekirdekleri hazırlayın
    kernel_x = np.array([[-1, 1], [-1, 1]]) * 0.25
    kernel_y = np.array([[-1, -1], [1, 1]]) * 0.25
    kernel_t = np.array([[1, 1], [1, 1]]) * 0.25
    kernel_laplacian = np.array(
        [[1 / 12, 1 / 6, 1 / 12], [1 / 6, 0, 1 / 6], [1 / 12, 1 / 6, 1 / 12]]
    )

    # Akışı yinelemeli olarak iyileştirin
    for _ in range(num_iter):
        warped_image = warp(image0, horizontal_flow, vertical_flow)
        derivative_x = convolve(warped_image, kernel_x) + convolve(image1, kernel_x)
        derivative_y = convolve(warped_image, kernel_y) + convolve(image1, kernel_y)
        derivative_t = convolve(warped_image, kernel_t) + convolve(image1, -kernel_t)

        avg_horizontal_velocity = convolve(horizontal_flow, kernel_laplacian)
        avg_vertical_velocity = convolve(vertical_flow, kernel_laplacian)

        # Bu, makalede önerildiği gibi akışı günceller (Adım 12)
        update = (
            derivative_x * avg_horizontal_velocity
            + derivative_y * avg_vertical_velocity
            + derivative_t
        )
        update = update / (alpha**2 + derivative_x**2 + derivative_y**2)

        horizontal_flow = avg_horizontal_velocity - derivative_x * update
        vertical_flow = avg_vertical_velocity - derivative_y * update

    return horizontal_flow, vertical_flow


if __name__ == "__main__":
    import doctest

    doctest.testmod()
