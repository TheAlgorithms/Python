from __future__ import annotations


class IIRFilter:
    r"""
    N-Order IIR filtre
    [-1, 1] aralığında normalize edilmiş float örneklerle çalıştığı varsayılır.

    ---

    Uygulama detayları:
    https://en.wikipedia.org/wiki/Digital_biquad_filter adresindeki 2. dereceden fonksiyona dayalı olarak,
    bu genelleştirilmiş N. dereceden fonksiyon oluşturulmuştur.

    Aşağıdaki transfer fonksiyonunu kullanarak
    H(z)=\frac{b_{0}+b_{1}z^{-1}+b_{2}z^{-2}+...+b_{k}z^{-k}}{a_{0}+a_{1}z^{-1}+a_{2}z^{-2}+...+a_{k}z^{-k}}
    bunu şu şekilde yeniden yazabiliriz
    y[n]={\frac{1}{a_{0}}}\left(\left(b_{0}x[n]+b_{1}x[n-1]+b_{2}x[n-2]+...+b_{k}x[n-k]\right)-\left(a_{1}y[n-1]+a_{2}y[n-2]+...+a_{k}y[n-k]\right)\right)
    """

    def __init__(self, order: int) -> None:
        self.order = order

        # a_{0} ... a_{k}
        self.a_koeff = [1.0] + [0.0] * order
        # b_{0} ... b_{k}
        self.b_koeff = [1.0] + [0.0] * order

        # x[n-1] ... x[n-k]
        self.girdi_geçmişi = [0.0] * self.order
        # y[n-1] ... y[n-k]
        self.çıktı_geçmişi = [0.0] * self.order

    def koeff_ayarla(self, a_koeff: list[float], b_koeff: list[float]) -> None:
        """
        IIR filtresi için katsayıları ayarlayın. Bunlar her ikisi de order + 1 boyutunda olmalıdır.
        a_0 bırakılabilir ve varsayılan değer olarak 1.0 kullanılır.

        Bu yöntem scipy'nin filtre tasarım fonksiyonları ile iyi çalışır
            >>> # 2. dereceden 1000Hz butterworth alçak geçiren filtre yapın
            >>> import scipy.signal
            >>> b_koeff, a_koeff = scipy.signal.butter(2, 1000,
            ...                                          btype='lowpass',
            ...                                          fs=48000)
            >>> filt = IIRFilter(2)
            >>> filt.koeff_ayarla(a_koeff, b_koeff)
        """
        if len(a_koeff) < self.order:
            a_koeff = [1.0, *a_koeff]

        if len(a_koeff) != self.order + 1:
            msg = (
                f"{self.order}-dereceden filtre için a_koeff'un {self.order + 1} elemanlı olması bekleniyordu, "
                f"ancak {len(a_koeff)} eleman bulundu"
            )
            raise ValueError(msg)

        if len(b_koeff) != self.order + 1:
            msg = (
                f"{self.order}-dereceden filtre için b_koeff'un {self.order + 1} elemanlı olması bekleniyordu, "
                f"ancak {len(b_koeff)} eleman bulundu"
            )
            raise ValueError(msg)

        self.a_koeff = a_koeff
        self.b_koeff = b_koeff

    def işlem(self, örnek: float) -> float:
        """
        y[n] hesapla

        >>> filt = IIRFilter(2)
        >>> filt.işlem(0)
        0.0
        """
        sonuç = 0.0

        # 1. indexten başlayın ve 0. indexi en sonda yapın.
        for i in range(1, self.order + 1):
            sonuç += (
                self.b_koeff[i] * self.girdi_geçmişi[i - 1]
                - self.a_koeff[i] * self.çıktı_geçmişi[i - 1]
            )

        sonuç = (sonuç + self.b_koeff[0] * örnek) / self.a_koeff[0]

        self.girdi_geçmişi[1:] = self.girdi_geçmişi[:-1]
        self.çıktı_geçmişi[1:] = self.çıktı_geçmişi[:-1]

        self.girdi_geçmişi[0] = örnek
        self.çıktı_geçmişi[0] = sonuç

        return sonuç
