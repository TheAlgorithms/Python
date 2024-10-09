from __future__ import annotations

from abc import abstractmethod
from math import pi
from typing import Protocol

import matplotlib.pyplot as plt
import numpy as np


class FiltreTipi(Protocol):
    @abstractmethod
    def işlem(self, örnek: float) -> float:
        """
        y[n] hesapla

        >>> issubclass(FiltreTipi, Protocol)
        True
        """


def sınırları_al(
    fft_sonuçları: np.ndarray, örnekleme_hızı: int
) -> tuple[int | float, int | float]:
    """
    fft sonuçlarını yazdırmak için sınırları al

    >>> import numpy
    >>> array = numpy.linspace(-20.0, 20.0, 1000)
    >>> sınırları_al(array, 1000)
    (-20, 20)
    """
    en_düşük = min([-20, np.min(fft_sonuçları[1 : örnekleme_hızı // 2 - 1])])
    en_yüksek = max([20, np.max(fft_sonuçları[1 : örnekleme_hızı // 2 - 1])])
    return en_düşük, en_yüksek


def frekans_cevabını_göster(filtre_tipi: FiltreTipi, örnekleme_hızı: int) -> None:
    """
    Bir filtrenin frekans cevabını göster

    >>> from audio_filters.iir_filter import IIRFilter
    >>> filt = IIRFilter(4)
    >>> frekans_cevabını_göster(filt, 48000)
    """

    boyut = 512
    girişler = [1] + [0] * (boyut - 1)
    çıkışlar = [filtre_tipi.işlem(madde) for madde in girişler]

    dolgu = [0] * (örnekleme_hızı - boyut)  # sıfır dolgusu
    çıkışlar += dolgu
    fft_çıkış = np.abs(np.fft.fft(çıkışlar))
    fft_db = 20 * np.log10(fft_çıkış)

    # 24'ten nyquist frekansına kadar log ölçeğinde frekanslar
    plt.xlim(24, örnekleme_hızı / 2 - 1)
    plt.xlabel("Frekans (Hz)")
    plt.xscale("log")

    # Makul sınırlar içinde göster
    sınırlar = sınırları_al(fft_db, örnekleme_hızı)
    plt.ylim(max([-80, sınırlar[0]]), min([80, sınırlar[1]]))
    plt.ylabel("Kazanç (dB)")

    plt.plot(fft_db)
    plt.show()


def faz_cevabını_göster(filtre_tipi: FiltreTipi, örnekleme_hızı: int) -> None:
    """
    Bir filtrenin faz cevabını göster

    >>> from audio_filters.iir_filter import IIRFilter
    >>> filt = IIRFilter(4)
    >>> faz_cevabını_göster(filt, 48000)
    """

    boyut = 512
    girişler = [1] + [0] * (boyut - 1)
    çıkışlar = [filtre_tipi.işlem(madde) for madde in girişler]

    dolgu = [0] * (örnekleme_hızı - boyut)  # sıfır dolgusu
    çıkışlar += dolgu
    fft_çıkış = np.angle(np.fft.fft(çıkışlar))

    # 24'ten nyquist frekansına kadar log ölçeğinde frekanslar
    plt.xlim(24, örnekleme_hızı / 2 - 1)
    plt.xlabel("Frekans (Hz)")
    plt.xscale("log")

    plt.ylim(-2 * pi, 2 * pi)
    plt.ylabel("Faz kayması (Radyan)")
    plt.plot(np.unwrap(fft_çıkış, -2 * pi))
    plt.show()
