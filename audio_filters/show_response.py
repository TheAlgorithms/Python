from __future__ import annotations

# Organiser: K. Umut Araz

from abc import abstractmethod
from math import pi
from typing import Protocol

import matplotlib.pyplot as plt
import numpy as np


class FiltreTipi(Protocol):
    @abstractmethod
    def islem(self, ornek: float) -> float:
        """
        y[n] hesapla

        >>> issubclass(FiltreTipi, Protocol)
        True
        """


def sinirlari_al(
    fft_sonuclari: np.ndarray, ornekleme_hizi: int
) -> tuple[int | float, int | float]:
    """
    FFT sonuçlarını yazdırmak için sınırları al

    >>> import numpy
    >>> dizi = numpy.linspace(-20.0, 20.0, 1000)
    >>> sinirlari_al(dizi, 1000)
    (-20, 20)
    """
    en_dusuk = min([-20, np.min(fft_sonuclari[1 : ornekleme_hizi // 2 - 1])])
    en_yuksek = max([20, np.max(fft_sonuclari[1 : ornekleme_hizi // 2 - 1])])
    return en_dusuk, en_yuksek


def frekans_cevabini_goster(filtre_tipi: FiltreTipi, ornekleme_hizi: int) -> None:
    """
    Bir filtrenin frekans cevabını göster

    >>> from audio_filters.iir_filter import IIRFilter
    >>> filt = IIRFilter(4)
    >>> frekans_cevabini_goster(filt, 48000)
    """

    boyut = 512
    girisler = [1] + [0] * (boyut - 1)
    cikislar = [filtre_tipi.islem(madde) for madde in girisler]

    dolgu = [0] * (ornekleme_hizi - boyut)  # sıfır dolgusu
    cikislar += dolgu
    fft_cikis = np.abs(np.fft.fft(cikislar))
    fft_db = 20 * np.log10(fft_cikis)

    # 24'ten Nyquist frekansına kadar log ölçeğinde frekanslar
    plt.xlim(24, ornekleme_hizi / 2 - 1)
    plt.xlabel("Frekans (Hz)")
    plt.xscale("log")

    # Makul sınırlar içinde göster
    sinirlar = sinirlari_al(fft_db, ornekleme_hizi)
    plt.ylim(max([-80, sinirlar[0]]), min([80, sinirlar[1]]))
    plt.ylabel("Kazanç (dB)")

    plt.plot(fft_db)
    plt.show()


def faz_cevabini_goster(filtre_tipi: FiltreTipi, ornekleme_hizi: int) -> None:
    """
    Bir filtrenin faz cevabını göster

    >>> from audio_filters.iir_filter import IIRFilter
    >>> filt = IIRFilter(4)
    >>> faz_cevabini_goster(filt, 48000)
    """

    boyut = 512
    girisler = [1] + [0] * (boyut - 1)
    cikislar = [filtre_tipi.islem(madde) for madde in girisler]

    dolgu = [0] * (ornekleme_hizi - boyut)  # sıfır dolgusu
    cikislar += dolgu
    fft_cikis = np.angle(np.fft.fft(cikislar))

    # 24'ten Nyquist frekansına kadar log ölçeğinde frekanslar
    plt.xlim(24, ornekleme_hizi / 2 - 1)
    plt.xlabel("Frekans (Hz)")
    plt.xscale("log")

    plt.ylim(-2 * pi, 2 * pi)
    plt.ylabel("Faz kayması (Radyan)")
    plt.plot(np.unwrap(fft_cikis, -2 * pi))
    plt.show()
