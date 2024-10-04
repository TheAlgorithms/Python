"""
Mel Frekans Kepstral Katsayıları (MFCC) Hesaplama

MFCC, bir ses sinyalinin kısa vadeli güç spektrumunu daha kompakt ve ayırt edici
bir şekilde temsil etmek için ses ve konuşma işleme alanında yaygın olarak
kullanılan bir algoritmadır. Özellikle konuşma tanıma ve konuşmacı tanıma gibi
ses ve konuşma işleme görevlerinde popülerdir.

Mel Frekans Kepstral Katsayılarının Hesaplanması:
1. Ön İşleme:
   - Bir ses sinyalini yükleyin ve değerlerin belirli bir aralıkta (örneğin,
     -1 ile 1 arasında) olmasını sağlamak için normalleştirin.
   - Ses sinyalini, spektral sızıntıyı azaltmak için pencereleme gibi bir
     teknik kullanarak, üst üste binen sabit uzunlukta segmentlere ayırın.

2. Fourier Dönüşümü:
   - Her ses çerçevesine Hızlı Fourier Dönüşümü (FFT) uygulayarak, zaman
     alanından frekans alanına dönüştürün. Bu, ses çerçevesinin bir dizi
     frekans bileşeni olarak temsil edilmesini sağlar.

3. Güç Spektrumu:
   - FFT'den elde edilen her frekans bileşeninin kare büyüklüğünü alarak güç
     spektrumunu hesaplayın. Bu adım, farklı frekans bantlarındaki enerji
     dağılımını ölçer.

4. Mel Filtrebank:
   - Güç spektrumuna Mel frekans ölçeğinde yerleştirilmiş bir dizi üçgen
     filtrebank uygulayın. Bu filtreler, insan işitme sisteminin frekans
     tepkisini taklit eder. Her filtrebank, kendi bandındaki güç spektrumu
     değerlerini toplar.

5. Logaritmik Sıkıştırma:
   - Dinamik aralığı sıkıştırmak için filtrebank değerlerinin logaritmasını
     (genellikle taban 10) alın. Bu adım, insan kulağının ses şiddetine
     logaritmik tepkisini taklit eder.

6. Ayrık Kosinüs Dönüşümü (DCT):
   - Log filtrebank enerjilerine Ayrık Kosinüs Dönüşümü uygulayarak MFCC
     katsayılarını elde edin. Bu dönüşüm, filtrebank enerjilerini
     dekorreleştirir ve ses sinyalinin en önemli özelliklerini yakalar.

7. Özellik Çıkarımı:
   - Özellik vektörünü oluşturmak için DCT katsayılarının bir alt kümesini
     seçin. Çoğu uygulama için genellikle ilk birkaç katsayı (örneğin, 12-13)
     kullanılır.

Referanslar:
- Mel-Frekans Kepstral Katsayıları (MFCC'ler):
  https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
- Daniel Jurafsky & James H. Martin tarafından yazılan Konuşma ve Dil İşleme:
  https://web.stanford.edu/~jurafsky/slp3/
- Mel Frekans Kepstral Katsayısı (MFCC) eğitimi:
  http://practicalcryptography.com/miscellaneous/machine-learning
  /guide-mel-frequency-cepstral-coefficients-mfccs/

Yazar: Amir Lavasani
"""

import logging

import numpy as np
import scipy.fftpack as fft
from scipy.signal import get_window

logging.basicConfig(filename=f"{__file__}.log", level=logging.INFO)


def mfcc(
    audio: np.ndarray,
    sample_rate: int,
    ftt_size: int = 1024,
    hop_length: int = 20,
    mel_filter_num: int = 10,
    dct_filter_num: int = 40,
) -> np.ndarray:
    """
    Mel Frekans Kepstral Katsayıları (MFCC) hesaplayın.

    Argümanlar:
        audio: Giriş ses sinyali.
        sample_rate: Ses sinyalinin örnekleme hızı (Hz cinsinden).
        ftt_size: FFT penceresinin boyutu (varsayılan 1024).
        hop_length: Çerçeve oluşturma için atlama uzunluğu (varsayılan 20ms).
        mel_filter_num: Mel filtrelerinin sayısı (varsayılan 10).
        dct_filter_num: DCT filtrelerinin sayısı (varsayılan 40).

    Döndürür:
        Giriş ses sinyali için MFCC'lerin matrisi.

    Hata:
        ValueError: Giriş ses sinyali boşsa.

    Örnek:
    >>> sample_rate = 44100  # 44.1 kHz örnekleme hızı
    >>> duration = 2.0  # 2 saniye süre
    >>> t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    >>> audio = 0.5 * np.sin(2 * np.pi * 440.0 * t)  # 440 Hz sinüs dalgası oluştur
    >>> mfccs = mfcc(audio, sample_rate)
    >>> mfccs.shape
    (40, 101)
    """
    logging.info(f"Örnekleme hızı: {sample_rate}Hz")
    logging.info(f"Ses süresi: {len(audio) / sample_rate}s")
    logging.info(f"Ses min: {np.min(audio)}")
    logging.info(f"Ses max: {np.max(audio)}")

    # ses sinyalini normalleştirin
    audio_normalized = normalize(audio)

    logging.info(f"Normalleştirilmiş ses min: {np.min(audio_normalized)}")
    logging.info(f"Normalleştirilmiş ses max: {np.max(audio_normalized)}")

    # ses sinyalini çerçevelere ayırın
    audio_framed = audio_frames(
        audio_normalized, sample_rate, ftt_size=ftt_size, hop_length=hop_length
    )

    logging.info(f"Çerçevelenmiş ses şekli: {audio_framed.shape}")
    logging.info(f"İlk çerçeve: {audio_framed[0]}")

    # frekans alanına dönüştürün
    # Basitlik için Hanning penceresini seçeceğiz.
    window = get_window("hann", ftt_size, fftbins=True)
    audio_windowed = audio_framed * window

    logging.info(f"Pencerelenmiş ses şekli: {audio_windowed.shape}")
    logging.info(f"İlk çerçeve: {audio_windowed[0]}")

    audio_fft = calculate_fft(audio_windowed, ftt_size)
    logging.info(f"fft ses şekli: {audio_fft.shape}")
    logging.info(f"İlk çerçeve: {audio_fft[0]}")

    audio_power = calculate_signal_power(audio_fft)
    logging.info(f"güç ses şekli: {audio_power.shape}")
    logging.info(f"İlk çerçeve: {audio_power[0]}")

    filters = mel_spaced_filterbank(sample_rate, mel_filter_num, ftt_size)
    logging.info(f"filtreler şekli: {filters.shape}")

    audio_filtered = np.dot(filters, np.transpose(audio_power))
    audio_log = 10.0 * np.log10(audio_filtered)
    logging.info(f"audio_log şekli: {audio_log.shape}")

    dct_filters = discrete_cosine_transform(dct_filter_num, mel_filter_num)
    cepstral_coefficents = np.dot(dct_filters, audio_log)

    logging.info(f"cepstral_coefficents şekli: {cepstral_coefficents.shape}")
    return cepstral_coefficents


def normalize(audio: np.ndarray) -> np.ndarray:
    """
    Bir ses sinyalini -1 ile 1 arasında değerlere sahip olacak şekilde normalleştirin.

    Argümanlar:
        audio: Giriş ses sinyali.

    Döndürür:
        Normalleştirilmiş ses sinyali.

    Örnekler:
    >>> audio = np.array([1, 2, 3, 4, 5])
    >>> normalized_audio = normalize(audio)
    >>> float(np.max(normalized_audio))
    1.0
    >>> float(np.min(normalized_audio))
    0.2
    """
    # Tüm ses sinyalini maksimum mutlak değere bölün
    return audio / np.max(np.abs(audio))


def audio_frames(
    audio: np.ndarray,
    sample_rate: int,
    hop_length: int = 20,
    ftt_size: int = 1024,
) -> np.ndarray:
    """
    Bir ses sinyalini üst üste binen çerçevelere ayırın.

    Argümanlar:
        audio: Giriş ses sinyali.
        sample_rate: Ses sinyalinin örnekleme hızı.
        hop_length: Atlama uzunluğu (varsayılan 20ms).
        ftt_size: FFT penceresinin boyutu (varsayılan 1024).

    Döndürür:
        Üst üste binen çerçevelerin dizisi.

    Örnekler:
    >>> audio = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*1000)
    >>> sample_rate = 8000
    >>> frames = audio_frames(audio, sample_rate, hop_length=10, ftt_size=512)
    >>> frames.shape
    (126, 512)
    """

    hop_size = np.round(sample_rate * hop_length / 1000).astype(int)

    # Kenar durumlarını ele almak için ses sinyalini doldurun
    audio = np.pad(audio, int(ftt_size / 2), mode="reflect")

    # Çerçeve sayısını hesaplayın
    frame_count = int((len(audio) - ftt_size) / hop_size) + 1

    # Çerçeveleri depolamak için bir dizi başlatın
    frames = np.zeros((frame_count, ftt_size))

    # Ses sinyalini çerçevelere ayırın
    for n in range(frame_count):
        frames[n] = audio[n * hop_size : n * hop_size + ftt_size]

    return frames


def calculate_fft(audio_windowed: np.ndarray, ftt_size: int = 1024) -> np.ndarray:
    """
    Pencerelenmiş ses verilerinin Hızlı Fourier Dönüşümünü (FFT) hesaplayın.

    Argümanlar:
        audio_windowed: Pencerelenmiş ses sinyali.
        ftt_size: FFT'nin boyutu (varsayılan 1024).

    Döndürür:
        Ses verilerinin FFT'si.

    Örnekler:
    >>> audio_windowed = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    >>> audio_fft = calculate_fft(audio_windowed, ftt_size=4)
    >>> bool(np.allclose(audio_fft[0], np.array([6.0+0.j, -1.5+0.8660254j,
    ...     -1.5-0.8660254j])))
    True
    """
    # Ses verilerini zamanın satırlarda ve kanalların sütunlarda olacak şekilde transpoze edin
    audio_transposed = np.transpose(audio_windowed)

    # FFT sonuçlarını depolamak için bir dizi başlatın
    audio_fft = np.empty(
        (int(1 + ftt_size // 2), audio_transposed.shape[1]),
        dtype=np.complex64,
        order="F",
    )

    # Her kanal için FFT hesaplayın
    for n in range(audio_fft.shape[1]):
        audio_fft[:, n] = fft.fft(audio_transposed[:, n], axis=0)[: audio_fft.shape[0]]

    # FFT sonuçlarını orijinal şekline geri transpoze edin
    return np.transpose(audio_fft)


def calculate_signal_power(audio_fft: np.ndarray) -> np.ndarray:
    """
    Ses sinyalinin gücünü FFT'sinden hesaplayın.

    Argümanlar:
        audio_fft: Ses sinyalinin FFT'si.

    Döndürür:
        Ses sinyalinin gücü.

    Örnekler:
    >>> audio_fft = np.array([1+2j, 2+3j, 3+4j, 4+5j])
    >>> power = calculate_signal_power(audio_fft)
    >>> np.allclose(power, np.array([5, 13, 25, 41]))
    True
    """
    # FFT katsayılarının mutlak değerlerinin karesini alarak gücü hesaplayın
    return np.square(np.abs(audio_fft))


def freq_to_mel(freq: float) -> float:
    """
    Bir frekansı Hertz cinsinden mel ölçeğine dönüştürün.

    Argümanlar:
        freq: Hertz cinsinden frekans.

    Döndürür:
        Mel ölçeğinde frekans.

    Örnekler:
    >>> float(round(freq_to_mel(1000), 2))
    999.99
    """
    # Frekansı mel ölçeğine dönüştürmek için formülü kullanın
    return 2595.0 * np.log10(1.0 + freq / 700.0)


def mel_to_freq(mels: float) -> float:
    """
    Mel ölçeğindeki bir frekansı Hertz'e dönüştürün.

    Argümanlar:
        mels: Mel ölçeğinde frekans.

    Döndürür:
        Hertz cinsinden frekans.

    Örnekler:
    >>> round(mel_to_freq(999.99), 2)
    1000.01
    """
    # Mel ölçeğini frekansa dönüştürmek için formülü kullanın
    return 700.0 * (10.0 ** (mels / 2595.0) - 1.0)


def mel_spaced_filterbank(
    sample_rate: int, mel_filter_num: int = 10, ftt_size: int = 1024
) -> np.ndarray:
    """
    Ses işleme için Mel aralıklı bir filtre bankası oluşturun.

    Argümanlar:
        sample_rate: Sesin örnekleme hızı.
        mel_filter_num: Mel filtrelerinin sayısı (varsayılan 10).
        ftt_size: FFT'nin boyutu (varsayılan 1024).

    Döndürür:
        Mel aralıklı filtre bankası.

    Örnekler:
    >>> float(round(mel_spaced_filterbank(8000, 10, 1024)[0][1], 10))
    0.0004603981
    """
    freq_min = 0
    freq_high = sample_rate // 2

    logging.info(f"Minimum frekans: {freq_min}")
    logging.info(f"Maksimum frekans: {freq_high}")

    # Filtre noktalarını ve mel frekanslarını hesaplayın
    filter_points, mel_freqs = get_filter_points(
        sample_rate,
        freq_min,
        freq_high,
        mel_filter_num,
        ftt_size,
    )

    filters = get_filters(filter_points, ftt_size)

    # filtreleri normalleştirin
    # librosa kütüphanesinden alınmıştır
    enorm = 2.0 / (mel_freqs[2 : mel_filter_num + 2] - mel_freqs[:mel_filter_num])
    return filters * enorm[:, np.newaxis]


def get_filters(filter_points: np.ndarray, ftt_size: int) -> np.ndarray:
    """
    Ses işleme için filtreler oluşturun.

    Argümanlar:
        filter_points: Filtre noktalarının listesi.
        ftt_size: FFT'nin boyutu.

    Döndürür:
        Filtrelerin matrisi.

    Örnekler:
    >>> get_filters(np.array([0, 20, 51, 95, 161, 256], dtype=int), 512).shape
    (4, 257)
    """
    num_filters = len(filter_points) - 2
    filters = np.zeros((num_filters, int(ftt_size / 2) + 1))

    for n in range(num_filters):
        start = filter_points[n]
        mid = filter_points[n + 1]
        end = filter_points[n + 2]

        # Değerleri 0'dan 1'e doğru doğrusal olarak artırın
        filters[n, start:mid] = np.linspace(0, 1, mid - start)

        # Değerleri 1'den 0'a doğru doğrusal olarak azaltın
        filters[n, mid:end] = np.linspace(1, 0, end - mid)

    return filters


def get_filter_points(
    sample_rate: int,
    freq_min: int,
    freq_high: int,
    mel_filter_num: int = 10,
    ftt_size: int = 1024,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Mel frekans filtreleri için filtre noktalarını ve frekansları hesaplayın.

    Argümanlar:
        sample_rate: Sesin örnekleme hızı.
        freq_min: Minimum frekans (Hertz cinsinden).
        freq_high: Maksimum frekans (Hertz cinsinden).
        mel_filter_num: Mel filtrelerinin sayısı (varsayılan 10).
        ftt_size: FFT'nin boyutu (varsayılan 1024).

    Döndürür:
        Filtre noktaları ve karşılık gelen frekanslar.

    Örnekler:
    >>> filter_points = get_filter_points(8000, 0, 4000, mel_filter_num=4, ftt_size=512)
    >>> filter_points[0]
    array([  0,  20,  51,  95, 161, 256])
    >>> filter_points[1]
    array([   0.        ,  324.46707094,  799.33254207, 1494.30973963,
           2511.42581671, 4000.        ])
    """
    # Minimum ve maksimum frekansları mel ölçeğine dönüştürün
    fmin_mel = freq_to_mel(freq_min)
    fmax_mel = freq_to_mel(freq_high)

    logging.info(f"MEL min: {fmin_mel}")
    logging.info(f"MEL max: {fmax_mel}")

    # Eşit aralıklı mel frekansları oluşturun
    mels = np.linspace(fmin_mel, fmax_mel, num=mel_filter_num + 2)

    # Mel frekanslarını tekrar Hertz'e dönüştürün
    freqs = mel_to_freq(mels)

    # Filtre noktalarını tamsayı değerler olarak hesaplayın
    filter_points = np.floor((ftt_size + 1) / sample_rate * freqs).astype(int)

    return filter_points, freqs


def discrete_cosine_transform(dct_filter_num: int, filter_num: int) -> np.ndarray:
    """
    Ayrık Kosinüs Dönüşümü (DCT) temel matrisini hesaplayın.

    Argümanlar:
        dct_filter_num: Üretilecek DCT filtrelerinin sayısı.
        filter_num: fbank filtrelerinin sayısı.

    Döndürür:
        DCT temel matrisi.

    Örnekler:
    >>> float(round(discrete_cosine_transform(3, 5)[0][0], 5))
    0.44721
    """
    basis = np.empty((dct_filter_num, filter_num))
    basis[0, :] = 1.0 / np.sqrt(filter_num)

    samples = np.arange(1, 2 * filter_num, 2) * np.pi / (2.0 * filter_num)

    for i in range(1, dct_filter_num):
        basis[i, :] = np.cos(i * samples) * np.sqrt(2.0 / filter_num)

    return basis


def example(wav_file_path: str = "./path-to-file/sample.wav") -> np.ndarray:
    """
    Bir ses dosyasından Mel Frekans Kepstral Katsayıları (MFCC) hesaplamak için
    örnek bir fonksiyon.

    Argümanlar:
        wav_file_path: WAV ses dosyasının yolu.

    Döndürür:
        np.ndarray: Ses için hesaplanan MFCC'ler.
    """
    from scipy.io import wavfile

    # WAV dosyasından sesi yükleyin
    sample_rate, audio = wavfile.read(wav_file_path)

    # MFCC'leri hesaplayın
    return mfcc(audio, sample_rate)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
