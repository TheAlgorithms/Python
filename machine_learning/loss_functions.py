import numpy as np


def ikili_çapraz_entropi(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    """
    Gerçek etiketler ve tahmin edilen olasılıklar arasındaki ortalama ikili çapraz entropi (BCE) kaybını hesaplayın.

    BCE kaybı, gerçek etiketler (0 veya 1) ve tahmin edilen olasılıklar arasındaki farklılığı ölçer.
    İkili sınıflandırma görevlerinde yaygın olarak kullanılır.

    BCE = -Σ(y_true * ln(y_pred) + (1 - y_true) * ln(1 - y_pred))

    Referans: https://en.wikipedia.org/wiki/Cross_entropy

    Parametreler:
    - y_true: Gerçek ikili etiketler (0 veya 1)
    - y_pred: Sınıf 1 için tahmin edilen olasılıklar
    - epsilon: Sayısal kararsızlığı önlemek için küçük bir sabit

    >>> gerçek_etiketler = np.array([0, 1, 1, 0, 1])
    >>> tahmin_olasılıkları = np.array([0.2, 0.7, 0.9, 0.3, 0.8])
    >>> float(ikili_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları))
    0.2529995012327421
    >>> gerçek_etiketler = np.array([0, 1, 1, 0, 1])
    >>> tahmin_olasılıkları = np.array([0.3, 0.8, 0.9, 0.2])
    >>> ikili_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: Giriş dizilerinin aynı uzunlukta olması gerekir.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Giriş dizilerinin aynı uzunlukta olması gerekir.")

    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # Tahminleri log(0)'dan kaçınmak için kırpın
    bce_loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return np.mean(bce_loss)


def ikili_odak_çapraz_entropi(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    gamma: float = 2.0,
    alpha: float = 0.25,
    epsilon: float = 1e-15,
) -> float:
    """
    Gerçek etiketler ve tahmin edilen olasılıklar arasındaki ortalama ikili odak çapraz entropi (BFCE) kaybını hesaplayın.

    BFCE kaybı, gerçek etiketler (0 veya 1) ve tahmin edilen olasılıklar arasındaki farklılığı ölçer.
    Sınıf dengesizliğini ele alarak zor örneklere odaklanan ikili çapraz entropinin bir varyasyonudur.

    BCFE = -Σ(alpha * (1 - y_pred)**gamma * y_true * log(y_pred)
                + (1 - alpha) * y_pred**gamma * (1 - y_true) * log(1 - y_pred))

    Referans: [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)

    Parametreler:
    - y_true: Gerçek ikili etiketler (0 veya 1).
    - y_pred: Sınıf 1 için tahmin edilen olasılıklar.
    - gamma: Kayıp modülasyon parametresi (varsayılan: 2.0).
    - alpha: Sınıf 1 için ağırlık faktörü (varsayılan: 0.25).
    - epsilon: Sayısal kararsızlığı önlemek için küçük bir sabit.

    >>> gerçek_etiketler = np.array([0, 1, 1, 0, 1])
    >>> tahmin_olasılıkları = np.array([0.2, 0.7, 0.9, 0.3, 0.8])
    >>> float(ikili_odak_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları))
    0.008257977659239775
    >>> gerçek_etiketler = np.array([0, 1, 1, 0, 1])
    >>> tahmin_olasılıkları = np.array([0.3, 0.8, 0.9, 0.2])
    >>> ikili_odak_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: Giriş dizilerinin aynı uzunlukta olması gerekir.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Giriş dizilerinin aynı uzunlukta olması gerekir.")
    # Tahmin edilen olasılıkları log(0)'dan kaçınmak için kırpın
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    bcfe_loss = -(
        alpha * (1 - y_pred) ** gamma * y_true * np.log(y_pred)
        + (1 - alpha) * y_pred**gamma * (1 - y_true) * np.log(1 - y_pred)
    )

    return np.mean(bcfe_loss)


def kategorik_çapraz_entropi(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    """
    Gerçek sınıf etiketleri ve tahmin edilen sınıf olasılıkları arasındaki kategorik çapraz entropi (CCE) kaybını hesaplayın.

    CCE = -Σ(y_true * ln(y_pred))

    Referans: https://en.wikipedia.org/wiki/Cross_entropy

    Parametreler:
    - y_true: Gerçek sınıf etiketleri (one-hot kodlanmış)
    - y_pred: Tahmin edilen sınıf olasılıkları
    - epsilon: Sayısal kararsızlığı önlemek için küçük bir sabit

    >>> gerçek_etiketler = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1], [0.0, 0.1, 0.9]])
    >>> float(kategorik_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları))
    0.567395975254385
    >>> gerçek_etiketler = np.array([[1, 0], [0, 1]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> kategorik_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: Giriş dizilerinin aynı şekle sahip olması gerekir.
    >>> gerçek_etiketler = np.array([[2, 0, 1], [1, 0, 0]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> kategorik_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: y_true one-hot kodlanmış olmalıdır.
    >>> gerçek_etiketler = np.array([[1, 0, 1], [1, 0, 0]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> kategorik_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: y_true one-hot kodlanmış olmalıdır.
    >>> gerçek_etiketler = np.array([[1, 0, 0], [0, 1, 0]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.1], [0.2, 0.7, 0.1]])
    >>> kategorik_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: Tahmin edilen olasılıklar yaklaşık olarak 1'e eşit olmalıdır.
    """
    if y_true.shape != y_pred.shape:
        raise ValueError("Giriş dizilerinin aynı şekle sahip olması gerekir.")

    if np.any((y_true != 0) & (y_true != 1)) :
        raise ValueError("y_true one-hot kodlanmış olmalıdır.")

    if not np.all(np.isclose(np.sum(y_pred, axis=1), 1, rtol=epsilon, atol=epsilon)):
        raise ValueError("Tahmin edilen olasılıklar yaklaşık olarak 1'e eşit olmalıdır.")

    y_pred = np.clip(y_pred, epsilon, 1)  # Tahminleri log(0)'dan kaçınmak için kırpın
    return -np.sum(y_true * np.log(y_pred))


def kategorik_odak_çapraz_entropi(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    alpha: np.ndarray = None,
    gamma: float = 2.0,
    epsilon: float = 1e-15,
) -> float:
    """
    Gerçek etiketler ve çok sınıflı sınıflandırma için tahmin edilen olasılıklar arasındaki ortalama kategorik odak çapraz entropi (CFCE) kaybını hesaplayın.

    CFCE kaybı, çok sınıflı sınıflandırma için ikili odak çapraz entropinin bir genellemesidir.
    Sınıf dengesizliğini ele alarak zor örneklere odaklanır.

    CFCE = -Σ alpha * (1 - y_pred)**gamma * y_true * log(y_pred)

    Referans: [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)

    Parametreler:
    - y_true: One-hot kodlanmış formda gerçek etiketler.
    - y_pred: Her sınıf için tahmin edilen olasılıklar.
    - alpha: Her sınıf için ağırlık faktörleri dizisi.
    - gamma: Kayıp modülasyon parametresi (varsayılan: 2.0).
    - epsilon: Sayısal kararsızlığı önlemek için küçük bir sabit.

    Döndürür:
    - Ortalama kategorik odak çapraz entropi kaybı.

    >>> gerçek_etiketler = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1], [0.0, 0.1, 0.9]])
    >>> alpha = np.array([0.6, 0.2, 0.7])
    >>> float(kategorik_odak_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları, alpha))
    0.0025966118981496423

    >>> gerçek_etiketler = np.array([[0, 1, 0], [0, 0, 1]])
    >>> tahmin_olasılıkları = np.array([[0.05, 0.95, 0], [0.1, 0.8, 0.1]])
    >>> alpha = np.array([0.25, 0.25, 0.25])
    >>> float(kategorik_odak_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları, alpha))
    0.23315276982014324

    >>> gerçek_etiketler = np.array([[1, 0], [0, 1]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> kategorik_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: Giriş dizilerinin aynı şekle sahip olması gerekir.

    >>> gerçek_etiketler = np.array([[2, 0, 1], [1, 0, 0]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> kategorik_odak_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: y_true one-hot kodlanmış olmalıdır.

    >>> gerçek_etiketler = np.array([[1, 0, 1], [1, 0, 0]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1]])
    >>> kategorik_odak_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: y_true one-hot kodlanmış olmalıdır.

    >>> gerçek_etiketler = np.array([[1, 0, 0], [0, 1, 0]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.1], [0.2, 0.7, 0.1]])
    >>> kategorik_odak_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
        ...
    ValueError: Tahmin edilen olasılıklar yaklaşık olarak 1'e eşit olmalıdır.

    >>> gerçek_etiketler = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> tahmin_olasılıkları = np.array([[0.9, 0.1, 0.0], [0.2, 0.7, 0.1], [0.0, 0.1, 0.9]])
    >>> alpha = np.array([0.6, 0.2])
    >>> kategorik_odak_çapraz_entropi(gerçek_etiketler, tahmin_olasılıkları, alpha)
    Traceback (most recent call last):
        ...
    ValueError: alpha'nın uzunluğu sınıf sayısıyla eşleşmelidir.
    """
    if y_true.shape != y_pred.shape:
        raise ValueError("y_true ve y_pred aynı şekle sahip olmalıdır.")

    if alpha is None:
        alpha = np.ones(y_true.shape[1])

    if np.any((y_true != 0) & (y_true != 1)) :
        raise ValueError("y_true one-hot kodlanmış olmalıdır.")

    if len(alpha) != y_true.shape[1]:
        raise ValueError("alpha'nın uzunluğu sınıf sayısıyla eşleşmelidir.")

    if not np.all(np.isclose(np.sum(y_pred, axis=1), 1, rtol=epsilon, atol=epsilon)):
        raise ValueError("Tahmin edilen olasılıklar yaklaşık olarak 1'e eşit olmalıdır.")

    # Tahmin edilen olasılıkları log(0)'dan kaçınmak için kırpın
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    # Her sınıf için kaybı hesaplayın ve sınıflar arasında toplayın
    cfce_loss = -np.sum(
        alpha * np.power(1 - y_pred, gamma) * y_true * np.log(y_pred), axis=1
    )

    return np.mean(cfce_loss)


def menteşe_kaybı(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Gerçek etiketler ve tahmin edilen olasılıklar arasındaki ortalama menteşe kaybını hesaplayın
    destek vektör makineleri (SVM'ler) için.

    Menteşe kaybı = max(0, 1 - true * pred)

    Referans: https://en.wikipedia.org/wiki/Hinge_loss

    Argümanlar:
    - y_true: -1 veya 1 olarak kodlanmış gerçek değerler (gerçek değerler)
    - y_pred: tahmin edilen değerler

    >>> gerçek_etiketler = np.array([-1, 1, 1, -1, 1])
    >>> tahmin = np.array([-4, -0.3, 0.7, 5, 10])
    >>> float(menteşe_kaybı(gerçek_etiketler, tahmin))
    1.52
    >>> gerçek_etiketler = np.array([-1, 1, 1, -1, 1, 1])
    >>> tahmin = np.array([-4, -0.3, 0.7, 5, 10])
    >>> menteşe_kaybı(gerçek_etiketler, tahmin)
    Traceback (most recent call last):
    ...
    ValueError: Tahmin edilen ve gerçek dizilerin uzunluğu aynı olmalıdır.
    >>> gerçek_etiketler = np.array([-1, 1, 10, -1, 1])
    >>> tahmin = np.array([-4, -0.3, 0.7, 5, 10])
    >>> menteşe_kaybı(gerçek_etiketler, tahmin)
    Traceback (most recent call last):
    ...
    ValueError: y_true yalnızca -1 veya 1 değerlerine sahip olabilir.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Tahmin edilen ve gerçek dizilerin uzunluğu aynı olmalıdır.")

    if np.any((y_true != -1) & (y_true != 1)):
        raise ValueError("y_true yalnızca -1 veya 1 değerlerine sahip olabilir.")

    menteşe_kayıpları = np.maximum(0, 1.0 - (y_true * y_pred))
    return np.mean(menteşe_kayıpları)


def huber_kaybı(y_true: np.ndarray, y_pred: np.ndarray, delta: float) -> float:
    """
    Verilen gerçek değerler ve tahmin edilen değerler arasındaki ortalama Huber kaybını hesaplayın.

    Huber kaybı, bir tahmin prosedürü tarafından alınan cezayı tanımlar ve
    regresyon modelleri için bir doğruluk ölçüsü olarak hizmet eder.

    Huber kaybı =
        0.5 * (y_true - y_pred)^2                   eğer |y_true - y_pred| <= delta
        delta * |y_true - y_pred| - 0.5 * delta^2   aksi takdirde

    Referans: https://en.wikipedia.org/wiki/Huber_loss

    Parametreler:
    - y_true: Gerçek değerler (gerçek değerler)
    - y_pred: Tahmin edilen değerler

    >>> gerçek_değerler = np.array([0.9, 10.0, 2.0, 1.0, 5.2])
    >>> tahmin_edilen_değerler = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> bool(np.isclose(huber_kaybı(gerçek_değerler, tahmin_edilen_değerler, 1.0), 2.102))
    True
    >>> gerçek_etiketler = np.array([11.0, 21.0, 3.32, 4.0, 5.0])
    >>> tahmin_olasılıkları = np.array([8.3, 20.8, 2.9, 11.2, 5.0])
    >>> bool(np.isclose(huber_kaybı(gerçek_etiketler, tahmin_olasılıkları, 1.0), 1.80164))
    True
    >>> gerçek_etiketler = np.array([11.0, 21.0, 3.32, 4.0])
    >>> tahmin_olasılıkları = np.array([8.3, 20.8, 2.9, 11.2, 5.0])
    >>> huber_kaybı(gerçek_etiketler, tahmin_olasılıkları, 1.0)
    Traceback (most recent call last):
    ...
    ValueError: Giriş dizilerinin aynı uzunlukta olması gerekir.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Giriş dizilerinin aynı uzunlukta olması gerekir.")

    huber_mse = 0.5 * (y_true - y_pred) ** 2
    huber_mae = delta * (np.abs(y_true - y_pred) - 0.5 * delta)
    return np.where(np.abs(y_true - y_pred) <= delta, huber_mse, huber_mae).mean()


def ortalama_kare_hata(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Gerçek değerler ve tahmin edilen değerler arasındaki ortalama kare hata (MSE) kaybını hesaplayın.

    MSE, gerçek değerler ve tahmin edilen değerler arasındaki kare farkı ölçer ve
    regresyon modelleri için bir doğruluk ölçüsü olarak hizmet eder.

    MSE = (1/n) * Σ(y_true - y_pred)^2

    Referans: https://en.wikipedia.org/wiki/Mean_squared_error

    Parametreler:
    - y_true: Gerçek değerler (gerçek değerler)
    - y_pred: Tahmin edilen değerler

    >>> gerçek_değerler = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> tahmin_edilen_değerler = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> bool(np.isclose(ortalama_kare_hata(gerçek_değerler, tahmin_edilen_değerler), 0.028))
    True
    >>> gerçek_etiketler = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> tahmin_olasılıkları = np.array([0.3, 0.8, 0.9, 0.2])
    >>> ortalama_kare_hata(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
    ...
    ValueError: Giriş dizilerinin aynı uzunlukta olması gerekir.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Giriş dizilerinin aynı uzunlukta olması gerekir.")

    kare_hatalar = (y_true - y_pred) ** 2
    return np.mean(kare_hatalar)


def ortalama_mutlak_hata(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Gerçek (gözlemlenen) ve tahmin edilen değerler arasındaki Ortalama Mutlak Hata (MAE) kaybını hesaplayın.

    MAE, gerçek değerler ve tahmin edilen değerler arasındaki mutlak farkı ölçer.

    Denklem:
    MAE = (1/n) * Σ(abs(y_true - y_pred))

    Referans: https://en.wikipedia.org/wiki/Mean_absolute_error

    Parametreler:
    - y_true: Gerçek değerler (gerçek değerler)
    - y_pred: Tahmin edilen değerler

    >>> gerçek_değerler = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> tahmin_edilen_değerler = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> bool(np.isclose(ortalama_mutlak_hata(gerçek_değerler, tahmin_edilen_değerler), 0.16))
    True
    >>> gerçek_değerler = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> tahmin_edilen_değerler = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> bool(np.isclose(ortalama_mutlak_hata(gerçek_değerler, tahmin_edilen_değerler), 2.16))
    False
    >>> gerçek_etiketler = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> tahmin_olasılıkları = np.array([0.3, 0.8, 0.9, 5.2])
    >>> ortalama_mutlak_hata(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
    ...
    ValueError: Giriş dizilerinin aynı uzunlukta olması gerekir.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Giriş dizilerinin aynı uzunlukta olması gerekir.")

    return np.mean(abs(y_true - y_pred))


def ortalama_kare_logaritmik_hata(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Gerçek değerler ve tahmin edilen değerler arasındaki ortalama kare logaritmik hata (MSLE) kaybını hesaplayın.

    MSLE, gerçek değerler ve tahmin edilen değerler arasındaki kare logaritmik farkı ölçer
    regresyon modelleri için. Özellikle çarpık veya büyük değerli verilerle başa çıkmak için kullanışlıdır ve
    tahmin edilen ve gerçek değerler arasındaki göreceli farklılıkların mutlak farklılıklardan daha önemli olduğu durumlarda kullanılır.

    MSLE = (1/n) * Σ(log(1 + y_true) - log(1 + y_pred))^2

    Referans: https://insideaiml.com/blog/MeanSquared-Logarithmic-Error-Loss-1035

    Parametreler:
    - y_true: Gerçek değerler (gerçek değerler)
    - y_pred: Tahmin edilen değerler

    >>> gerçek_değerler = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> tahmin_edilen_değerler = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> float(ortalama_kare_logaritmik_hata(gerçek_değerler, tahmin_edilen_değerler))
    0.0030860877925181344
    >>> gerçek_etiketler = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> tahmin_olasılıkları = np.array([0.3, 0.8, 0.9, 0.2])
    >>> ortalama_kare_logaritmik_hata(gerçek_etiketler, tahmin_olasılıkları)
    Traceback (most recent call last):
    ...
    ValueError: Giriş dizilerinin aynı uzunlukta olması gerekir.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Giriş dizilerinin aynı uzunlukta olması gerekir.")

    kare_logaritmik_hatalar = (np.log1p(y_true) - np.log1p(y_pred)) ** 2
    return np.mean(kare_logaritmik_hatalar)


def ortalama_mutlak_yüzde_hata(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-15
) -> float:
    """
    y_true ve y_pred arasındaki Ortalama Mutlak Yüzde Hatasını hesaplayın.

    Ortalama Mutlak Yüzde Hatası, tahmin edilen ve gerçek değerler arasındaki mutlak
    yüzde farklarının ortalamasını hesaplar.

    Formül = (Σ|y_true[i]-Y_pred[i]/y_true[i]|)/n

    Kaynak: https://stephenallwright.com/good-mape-score/

    Parametreler:
    y_true (np.ndarray): Gerçek/hedef değerleri içeren Numpy dizisi.
    y_pred (np.ndarray): Tahmin edilen değerleri içeren Numpy dizisi.

    Döndürür:
    float: y_true ve y_pred arasındaki Ortalama Mutlak Yüzde hatası.

    Örnekler:
    >>> y_true = np.array([10, 20, 30, 40])
    >>> y_pred = np.array([12, 18, 33, 45])
    >>> float(mean_absolute_percentage_error(y_true, y_pred))
    0.13125

    >>> y_true = np.array([1, 2, 3, 4])
    >>> y_pred = np.array([2, 3, 4, 5])
    >>> float(mean_absolute_percentage_error(y_true, y_pred))
    0.5208333333333333

    >>> y_true = np.array([34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24])
    >>> y_pred = np.array([37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23])
    >>> float(mean_absolute_percentage_error(y_true, y_pred))
    0.064671076436071
    """
    if len(y_true) != len(y_pred):
        raise ValueError("İki dizinin uzunluğu aynı olmalıdır.")

    y_true = np.where(y_true == 0, epsilon, y_true)
    absolute_percentage_diff = np.abs((y_true - y_pred) / y_true)

    return np.mean(absolute_percentage_diff)


def perplexity_loss(
    y_true: np.ndarray, y_pred: np.ndarray, epsilon: float = 1e-7
) -> float:
    """
    y_true ve y_pred için karmaşıklığı hesaplayın.

    Doğal Dil İşleme (NLP) alanında dil modeli doğruluğunu tahmin etmek için karmaşıklığı hesaplayın.
    Karmaşıklık, modelin tahminlerindeki belirsizliğin bir ölçüsüdür.

    Karmaşıklık Kaybı = exp(-1/N (Σ ln(p(x)))

    Referans:
    https://en.wikipedia.org/wiki/Perplexity

    Argümanlar:
        y_true: Gerçek etiket kodlanmış cümleler (batch_size, cümle uzunluğu) şeklinde
        y_pred: Tahmin edilen cümleler (batch_size, cümle uzunluğu, vocab_size) şeklinde
        epsilon: log(0) için inf almaktan kaçınmak için küçük bir kayan nokta sayısı

    Döndürür:
        y_true ve y_pred arasındaki karmaşıklık kaybı.

    >>> y_true = np.array([[1, 4], [2, 3]])
    >>> y_pred = np.array(
    ...    [[[0.28, 0.19, 0.21 , 0.15, 0.15],
    ...      [0.24, 0.19, 0.09, 0.18, 0.27]],
    ...      [[0.03, 0.26, 0.21, 0.18, 0.30],
    ...       [0.28, 0.10, 0.33, 0.15, 0.12]]]
    ... )
    >>> float(perplexity_loss(y_true, y_pred))
    5.0247347775367945
    >>> y_true = np.array([[1, 4], [2, 3]])
    >>> y_pred = np.array(
    ...    [[[0.28, 0.19, 0.21 , 0.15, 0.15],
    ...      [0.24, 0.19, 0.09, 0.18, 0.27],
    ...      [0.30, 0.10, 0.20, 0.15, 0.25]],
    ...      [[0.03, 0.26, 0.21, 0.18, 0.30],
    ...       [0.28, 0.10, 0.33, 0.15, 0.12],
    ...       [0.30, 0.10, 0.20, 0.15, 0.25]],]
    ... )
    >>> perplexity_loss(y_true, y_pred)
    Traceback (most recent call last):
    ...
    ValueError: y_true ve y_pred cümle uzunlukları eşit olmalıdır.
    >>> y_true = np.array([[1, 4], [2, 11]])
    >>> y_pred = np.array(
    ...    [[[0.28, 0.19, 0.21 , 0.15, 0.15],
    ...      [0.24, 0.19, 0.09, 0.18, 0.27]],
    ...      [[0.03, 0.26, 0.21, 0.18, 0.30],
    ...       [0.28, 0.10, 0.33, 0.15, 0.12]]]
    ... )
    >>> perplexity_loss(y_true, y_pred)
    Traceback (most recent call last):
    ...
    ValueError: Etiket değeri, kelime dağarcığı boyutundan büyük olmamalıdır.
    >>> y_true = np.array([[1, 4]])
    >>> y_pred = np.array(
    ...    [[[0.28, 0.19, 0.21 , 0.15, 0.15],
    ...      [0.24, 0.19, 0.09, 0.18, 0.27]],
    ...      [[0.03, 0.26, 0.21, 0.18, 0.30],
    ...       [0.28, 0.10, 0.33, 0.15, 0.12]]]
    ... )
    >>> perplexity_loss(y_true, y_pred)
    Traceback (most recent call last):
    ...
    ValueError: y_true ve y_pred batch boyutları eşit olmalıdır.
    """

    vocab_size = y_pred.shape[2]

    if y_true.shape[0] != y_pred.shape[0]:
        raise ValueError("y_true ve y_pred batch boyutları eşit olmalıdır.")
    if y_true.shape[1] != y_pred.shape[1]:
        raise ValueError("y_true ve y_pred cümle uzunlukları eşit olmalıdır.")
    if np.max(y_true) > vocab_size:
        raise ValueError("Etiket değeri, kelime dağarcığı boyutundan büyük olmamalıdır.")

    # Yalnızca gerçek sınıf için tahmin değerini seçmek için matris
    filter_matrix = np.array(
        [[list(np.eye(vocab_size)[word]) for word in sentence] for sentence in y_true]
    )

    # Yalnızca gerçek sınıf için tahmin içeren matrisi alın
    true_class_pred = np.sum(y_pred * filter_matrix, axis=2).clip(epsilon, 1)

    # Her cümle için karmaşıklığı hesaplayın
    perp_losses = np.exp(np.negative(np.mean(np.log(true_class_pred), axis=1)))

    return np.mean(perp_losses)


def smooth_l1_loss(y_true: np.ndarray, y_pred: np.ndarray, beta: float = 1.0) -> float:
    """
    y_true ve y_pred arasındaki Smooth L1 Loss'u hesaplayın.

    Smooth L1 Loss, L2 Loss'a göre aykırı değerlere daha az duyarlıdır ve genellikle
    nesne algılama gibi regresyon problemlerinde kullanılır.

    Smooth L1 Loss =
        0.5 * (x - y)^2 / beta, eğer |x - y| < beta
        |x - y| - 0.5 * beta, aksi takdirde

    Referans:
    https://pytorch.org/docs/stable/generated/torch.nn.SmoothL1Loss.html

    Argümanlar:
        y_true: Gerçek değerler dizisi.
        y_pred: Tahmin edilen değerler dizisi.
        beta: L1 ve L2 kaybı arasında geçiş yapmak için eşiği belirtir.

    Döndürür:
        y_true ve y_pred arasındaki hesaplanan Smooth L1 Loss.

    Hatalar:
        ValueError: İki dizinin uzunluğu aynı değilse.

    >>> y_true = np.array([3, 5, 2, 7])
    >>> y_pred = np.array([2.9, 4.8, 2.1, 7.2])
    >>> float(smooth_l1_loss(y_true, y_pred, 1.0))
    0.012500000000000022

    >>> y_true = np.array([2, 4, 6])
    >>> y_pred = np.array([1, 5, 7])
    >>> float(smooth_l1_loss(y_true, y_pred, 1.0))
    0.5

    >>> y_true = np.array([1, 3, 5, 7])
    >>> y_pred = np.array([1, 3, 5, 7])
    >>> float(smooth_l1_loss(y_true, y_pred, 1.0))
    0.0

    >>> y_true = np.array([1, 3, 5])
    >>> y_pred = np.array([1, 3, 5, 7])
    >>> smooth_l1_loss(y_true, y_pred, 1.0)
    Traceback (most recent call last):
    ...
    ValueError: İki dizinin uzunluğu aynı olmalıdır.
    """

    if len(y_true) != len(y_pred):
        raise ValueError("İki dizinin uzunluğu aynı olmalıdır.")

    diff = np.abs(y_true - y_pred)
    loss = np.where(diff < beta, 0.5 * diff**2 / beta, diff - 0.5 * beta)
    return np.mean(loss)


def kullback_leibler_divergence(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Gerçek etiketler ve tahmin edilen olasılıklar arasındaki Kullback-Leibler sapması (KL sapması) kaybını hesaplayın.

    KL sapması kaybı, gerçek etiketler ve tahmin edilen olasılıklar arasındaki farklılığı ölçer.
    Genellikle üretici modellerin eğitiminde kullanılır.

    KL = Σ(y_true * ln(y_true / y_pred))

    Referans: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

    Parametreler:
    - y_true: Gerçek sınıf olasılıkları
    - y_pred: Tahmin edilen sınıf olasılıkları

    Parameters:
    - y_true: True class probabilities
    - y_pred: Predicted class probabilities

    >>> true_labels = np.array([0.2, 0.3, 0.5])
    >>> predicted_probs = np.array([0.3, 0.3, 0.4])
    >>> float(kullback_leibler_divergence(true_labels, predicted_probs))
    0.030478754035472025
    >>> true_labels = np.array([0.2, 0.3, 0.5])
    >>> predicted_probs = np.array([0.3, 0.3, 0.4, 0.5])
    >>> kullback_leibler_divergence(true_labels, predicted_probs)
    Traceback (most recent call last):
        ...
    ValueError: Input arrays must have the same length.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    kl_loss = y_true * np.log(y_true / y_pred)
    return np.sum(kl_loss)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
