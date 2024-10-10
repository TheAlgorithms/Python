from __future__ import annotations


class IIRFiltre:
    r"""
    N. Dereceden IIR filtre

    Organiser: K. Umut Araz

    [-1, 1] aralığında normalize edilmiş float örneklerle çalıştığı varsayılır.

    ---

    Uygulama detayları:
    https://en.wikipedia.org/wiki/Digital_biquad_filter adresindeki 2. dereceden fonksiyona dayalı olarak,
    bu genelleştirilmiş N. dereceden fonksiyon oluşturulmuştur.

    Aşağıdaki transfer fonksiyonunu kullanarak
    H(z)=\frac{b_{0}+b_{1}z^{-1}+b_{2}z^{-2}+...+b_{k}z^{-k}}{a_{0}+a_{1}z^{-1}+a_{2}z^{-2}+...+a_{k}z^{-k}}
    bunu şu şekilde yeniden yazabiliriz:
    y[n]={\frac{1}{a_{0}}}\left(\left(b_{0}x[n]+b_{1}x[n-1]+b_{2}x[n-2]+...+b_{k}x[n-k]\right)-\left(a_{1}y[n-1]+a_{2}y[n-2]+...+a_{k}y[n-k]\right)\right)
    """

    def __init__(self, derece: int) -> None:
        self.derece = derece

        # a_{0} ... a_{k}
        self.a_katsayı = [1.0] + [0.0] * derece
        # b_{0} ... b_{k}
        self.b_katsayı = [1.0] + [0.0] * derece

        # x[n-1] ... x[n-k]
        self.girdi_geçmişi = [0.0] * self.derece
        # y[n-1] ... y[n-k]
        self.çıktı_geçmişi = [0.0] * self.derece

    def katsayı_ayarla(self, a_katsayı: list[float], b_katsayı: list[float]) -> None:
        """
        IIR filtresi için katsayıları ayarlayın. Her iki liste de derece + 1 boyutunda olmalıdır.
        a_0 bırakılabilir ve varsayılan değer olarak 1.0 kullanılır.

        Bu yöntem scipy'nin filtre tasarım fonksiyonları ile iyi çalışır:
            >>> # 2. dereceden 1000Hz butterworth alçak geçiren filtre yapın
            >>> import scipy.signal
            >>> b_katsayı, a_katsayı = scipy.signal.butter(2, 1000,
            ...                                          btype='lowpass',
            ...                                          fs=48000)
            >>> filtre = IIRFiltre(2)
            >>> filtre.katsayı_ayarla(a_katsayı, b_katsayı)
        """
        if len(a_katsayı) < self.derece:
            a_katsayı = [1.0, *a_katsayı]

        if len(a_katsayı) != self.derece + 1:
            msg = (
                f"{self.derece}-dereceden filtre için a_katsayı'nın {self.derece + 1} elemanlı olması bekleniyordu, "
                f"ancak {len(a_katsayı)} eleman bulundu"
            )
            raise ValueError(msg)

        if len(b_katsayı) != self.derece + 1:
            msg = (
                f"{self.derece}-dereceden filtre için b_katsayı'nın {self.derece + 1} elemanlı olması bekleniyordu, "
                f"ancak {len(b_katsayı)} eleman bulundu"
            )
            raise ValueError(msg)

        self.a_katsayı = a_katsayı
        self.b_katsayı = b_katsayı

    def işlem(self, örnek: float) -> float:
        """
        y[n] değerini hesapla

        >>> filtre = IIRFiltre(2)
        >>> filtre.işlem(0)
        0.0
        """
        sonuç = 0.0

        # 1. indexten başlayın ve 0. indexi en sonda yapın.
        for i in range(1, self.derece + 1):
            sonuç += (
                self.b_katsayı[i] * self.girdi_geçmişi[i - 1]
                - self.a_katsayı[i] * self.çıktı_geçmişi[i - 1]
            )

        sonuç = (sonuç + self.b_katsayı[0] * örnek) / self.a_katsayı[0]

        self.girdi_geçmişi[1:] = self.girdi_geçmişi[:-1]
        self.çıktı_geçmişi[1:] = self.çıktı_geçmişi[:-1]

        self.girdi_geçmişi[0] = örnek
        self.çıktı_geçmişi[0] = sonuç

        return sonuç
