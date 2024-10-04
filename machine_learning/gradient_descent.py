"""
Doğrusal bir hipotez fonksiyonunun maliyetini en aza indirmek için gradyan iniş algoritmasının uygulanması.
"""

import numpy as np

# Girdi, çıktı çiftlerinin listesi
train_data = (
    ((5, 2, 3), 15),
    ((6, 5, 9), 25),
    ((11, 12, 13), 41),
    ((1, 1, 1), 8),
    ((11, 12, 13), 41),
)
test_data = (((515, 22, 13), 555), ((61, 35, 49), 150))
parameter_vector = [2, 4, 1, 5]
m = len(train_data)
LEARNING_RATE = 0.009


def _error(example_no, data_set="train"):
    """
    :param data_set: eğitim verisi veya test verisi
    :param example_no: hatası kontrol edilecek örnek numarası
    :return: belirtilen örnekteki hata.
    """
    return calculate_hypothesis_value(example_no, data_set) - output(
        example_no, data_set
    )


def _hypothesis_value(data_input_tuple):
    """
    Belirli bir girdi için hipotez fonksiyon değeri hesaplar
    :param data_input_tuple: Belirli bir örneğin girdi demeti
    :return: O noktadaki hipotez fonksiyonunun değeri.
    Not: Sabit bir değere sahip 'bias' girdi vardır.
    Girdi verilerinde açıkça belirtilmemiştir. Ancak, ML hipotez fonksiyonları bunu kullanır.
    Bu nedenle, bunu ayrı olarak ele almalıyız. 36. satır bunu ele alır.
    """
    hyp_val = 0
    for i in range(len(parameter_vector) - 1):
        hyp_val += data_input_tuple[i] * parameter_vector[i + 1]
    hyp_val += parameter_vector[0]
    return hyp_val


def output(example_no, data_set):
    """
    :param data_set: test verisi veya eğitim verisi
    :param example_no: çıktısı alınacak örnek
    :return: o örnek için çıktı
    """
    if data_set == "train":
        return train_data[example_no][1]
    elif data_set == "test":
        return test_data[example_no][1]
    return None


def calculate_hypothesis_value(example_no, data_set):
    """
    Belirli bir örnek için hipotez değeri hesaplar
    :param data_set: test verisi veya eğitim verisi
    :param example_no: hipotez değeri hesaplanacak örnek
    :return: o örnek için hipotez değeri
    """
    if data_set == "train":
        return _hypothesis_value(train_data[example_no][0])
    elif data_set == "test":
        return _hypothesis_value(test_data[example_no][0])
    return None


def summation_of_cost_derivative(index, end=m):
    """
    Maliyet fonksiyonu türevinin toplamını hesaplar
    :param index: türevine göre hesaplanan indeks
    :param end: toplamın bittiği değer, varsayılan m, örnek sayısı
    :return: Maliyet türevinin toplamını döndürür
    Not: Eğer indeks -1 ise, bu, bias parametresine göre toplamın hesaplandığı anlamına gelir.
    """
    summation_value = 0
    for i in range(end):
        if index == -1:
            summation_value += _error(i)
        else:
            summation_value += _error(i) * train_data[i][0][index]
    return summation_value


def get_cost_derivative(index):
    """
    :param index: türevine göre hesaplanacak parametre vektörünün indeksi
    :return: o indekse göre türev
    Not: Eğer indeks -1 ise, bu, bias parametresine göre toplamın hesaplandığı anlamına gelir.
    """
    cost_derivative_value = summation_of_cost_derivative(index, m) / m
    return cost_derivative_value


def run_gradient_descent():
    global parameter_vector
    # Tahmin edilen çıktı için bir tolerans değeri ayarlamak için bu değerleri ayarlayın
    absolute_error_limit = 0.000002
    relative_error_limit = 0
    j = 0
    while True:
        j += 1
        temp_parameter_vector = [0, 0, 0, 0]
        for i in range(len(parameter_vector)):
            cost_derivative = get_cost_derivative(i - 1)
            temp_parameter_vector[i] = (
                parameter_vector[i] - LEARNING_RATE * cost_derivative
            )
        if np.allclose(
            parameter_vector,
            temp_parameter_vector,
            atol=absolute_error_limit,
            rtol=relative_error_limit,
        ):
            break
        parameter_vector = temp_parameter_vector
    print(("İterasyon sayısı:", j))


def test_gradient_descent():
    for i in range(len(test_data)):
        print(("Gerçek çıktı değeri:", output(i, "test")))
        print(("Hipotez çıktısı:", calculate_hypothesis_value(i, "test")))


if __name__ == "__main__":
    run_gradient_descent()
    print("\nDoğrusal bir hipotez fonksiyonu için gradyan iniş test ediliyor.\n")
    test_gradient_descent()
