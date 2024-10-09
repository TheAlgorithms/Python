from math import cos, sin, sqrt, tau

from audio_filters.iir_filter import IIRFilter

"""
Butterworth tasarımı ile 2. dereceden IIR filtreler oluşturun.

Kod, https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html adresine dayanmaktadır.
Alternatif olarak, aynı sonuçları vermesi gereken scipy.signal.butter'ı kullanabilirsiniz.
"""


def alçak_geçiren_oluştur(
    frekans: int,
    örnekleme_hızı: int,
    q_faktörü: float = 1 / sqrt(2),
) -> IIRFilter:
    """
    Alçak geçiren bir filtre oluşturur

    >>> filtre = alçak_geçiren_oluştur(1000, 48000)
    >>> filtre.a_koeff + filtre.b_koeff  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427, 0.004277569313094809,
     0.008555138626189618, 0.004277569313094809]
    """
    w0 = tau * frekans / örnekleme_hızı
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_faktörü)

    b0 = (1 - _cos) / 2
    b1 = 1 - _cos

    a0 = 1 + alpha
    a1 = -2 * _cos
    a2 = 1 - alpha

    filtre = IIRFilter(2)
    filtre.koeff_ayarla([a0, a1, a2], [b0, b1, b0])
    return filtre


def yüksek_geçiren_oluştur(
    frekans: int,
    örnekleme_hızı: int,
    q_faktörü: float = 1 / sqrt(2),
) -> IIRFilter:
    """
    Yüksek geçiren bir filtre oluşturur

    >>> filtre = yüksek_geçiren_oluştur(1000, 48000)
    >>> filtre.a_koeff + filtre.b_koeff  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427, 0.9957224306869052,
     -1.9914448613738105, 0.9957224306869052]
    """
    w0 = tau * frekans / örnekleme_hızı
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_faktörü)

    b0 = (1 + _cos) / 2
    b1 = -1 - _cos

    a0 = 1 + alpha
    a1 = -2 * _cos
    a2 = 1 - alpha

    filtre = IIRFilter(2)
    filtre.koeff_ayarla([a0, a1, a2], [b0, b1, b0])
    return filtre


def bant_geçiren_oluştur(
    frekans: int,
    örnekleme_hızı: int,
    q_faktörü: float = 1 / sqrt(2),
) -> IIRFilter:
    """
    Bant geçiren bir filtre oluşturur

    >>> filtre = bant_geçiren_oluştur(1000, 48000)
    >>> filtre.a_koeff + filtre.b_koeff  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427, 0.06526309611002579,
     0, -0.06526309611002579]
    """
    w0 = tau * frekans / örnekleme_hızı
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_faktörü)

    b0 = _sin / 2
    b1 = 0
    b2 = -b0

    a0 = 1 + alpha
    a1 = -2 * _cos
    a2 = 1 - alpha

    filtre = IIRFilter(2)
    filtre.koeff_ayarla([a0, a1, a2], [b0, b1, b2])
    return filtre


def tüm_geçiren_oluştur(
    frekans: int,
    örnekleme_hızı: int,
    q_faktörü: float = 1 / sqrt(2),
) -> IIRFilter:
    """
    Tüm geçiren bir filtre oluşturur

    >>> filtre = tüm_geçiren_oluştur(1000, 48000)
    >>> filtre.a_koeff + filtre.b_koeff  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427, 0.9077040443587427,
     -1.9828897227476208, 1.0922959556412573]
    """
    w0 = tau * frekans / örnekleme_hızı
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_faktörü)

    b0 = 1 - alpha
    b1 = -2 * _cos
    b2 = 1 + alpha

    filtre = IIRFilter(2)
    filtre.koeff_ayarla([b2, b1, b0], [b0, b1, b2])
    return filtre


def tepe_oluştur(
    frekans: int,
    örnekleme_hızı: int,
    kazanç_db: float,
    q_faktörü: float = 1 / sqrt(2),
) -> IIRFilter:
    """
    Tepe bir filtre oluşturur

    >>> filtre = tepe_oluştur(1000, 48000, 6)
    >>> filtre.a_koeff + filtre.b_koeff  # doctest: +NORMALIZE_WHITESPACE
    [1.0653405327119334, -1.9828897227476208, 0.9346594672880666, 1.1303715025601122,
     -1.9828897227476208, 0.8696284974398878]
    """
    w0 = tau * frekans / örnekleme_hızı
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_faktörü)
    büyük_a = 10 ** (kazanç_db / 40)

    b0 = 1 + alpha * büyük_a
    b1 = -2 * _cos
    b2 = 1 - alpha * büyük_a
    a0 = 1 + alpha / büyük_a
    a1 = -2 * _cos
    a2 = 1 - alpha / büyük_a

    filtre = IIRFilter(2)
    filtre.koeff_ayarla([a0, a1, a2], [b0, b1, b2])
    return filtre


def alçak_raf_oluştur(
    frekans: int,
    örnekleme_hızı: int,
    kazanç_db: float,
    q_faktörü: float = 1 / sqrt(2),
) -> IIRFilter:
    """
    Alçak raf bir filtre oluşturur

    >>> filtre = alçak_raf_oluştur(1000, 48000, 6)
    >>> filtre.a_koeff + filtre.b_koeff  # doctest: +NORMALIZE_WHITESPACE
    [3.0409336710888786, -5.608870992220748, 2.602157875636628, 3.139954022810743,
     -5.591841778072785, 2.5201667380627257]
    """
    w0 = tau * frekans / örnekleme_hızı
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_faktörü)
    büyük_a = 10 ** (kazanç_db / 40)
    pmc = (büyük_a + 1) - (büyük_a - 1) * _cos
    ppmc = (büyük_a + 1) + (büyük_a - 1) * _cos
    mpc = (büyük_a - 1) - (büyük_a + 1) * _cos
    pmpc = (büyük_a - 1) + (büyük_a + 1) * _cos
    aa2 = 2 * sqrt(büyük_a) * alpha

    b0 = büyük_a * (pmc + aa2)
    b1 = 2 * büyük_a * mpc
    b2 = büyük_a * (pmc - aa2)
    a0 = ppmc + aa2
    a1 = -2 * pmpc
    a2 = ppmc - aa2

    filtre = IIRFilter(2)
    filtre.koeff_ayarla([a0, a1, a2], [b0, b1, b2])
    return filtre


def yüksek_raf_oluştur(
    frekans: int,
    örnekleme_hızı: int,
    kazanç_db: float,
    q_faktörü: float = 1 / sqrt(2),
) -> IIRFilter:
    """
    Yüksek raf bir filtre oluşturur

    >>> filtre = yüksek_raf_oluştur(1000, 48000, 6)
    >>> filtre.a_koeff + filtre.b_koeff  # doctest: +NORMALIZE_WHITESPACE
    [2.2229172136088806, -3.9587208137297303, 1.7841414181566304, 4.295432981120543,
     -7.922740859457287, 3.6756456963725253]
    """
    w0 = tau * frekans / örnekleme_hızı
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_faktörü)
    büyük_a = 10 ** (kazanç_db / 40)
    pmc = (büyük_a + 1) - (büyük_a - 1) * _cos
    ppmc = (büyük_a + 1) + (büyük_a - 1) * _cos
    mpc = (büyük_a - 1) - (büyük_a + 1) * _cos
    pmpc = (büyük_a - 1) + (büyük_a + 1) * _cos
    aa2 = 2 * sqrt(büyük_a) * alpha

    b0 = büyük_a * (ppmc + aa2)
    b1 = -2 * büyük_a * pmpc
    b2 = büyük_a * (ppmc - aa2)
    a0 = pmc + aa2
    a1 = 2 * mpc
    a2 = pmc - aa2

    filtre = IIRFilter(2)
    filtre.koeff_ayarla([a0, a1, a2], [b0, b1, b2])
    return filtre
