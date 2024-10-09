#!/usr/bin/python

"""
Geri Yayılım Sinir Ağı (BP) Modeli için Bir Çerçeve

Kullanımı Kolay:
    * İstediğiniz kadar katman ekleyin!
    * Kaybın nasıl azaldığını net bir şekilde görün
Genişletmesi Kolay:
    * Daha fazla aktivasyon fonksiyonu
    * Daha fazla kayıp fonksiyonu
    * Daha fazla optimizasyon yöntemi

Yazar: Stephen Lee
Organiser: K. Umut Araz
Github: https://github.com/arazumut
Github: https://github.com/RiptideBo
Tarih: 2017.11.23
"""

import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x: np.ndarray) -> np.ndarray:
    """Sigmoid aktivasyon fonksiyonu."""
    return 1 / (1 + np.exp(-x))


class DenseLayer:
    """
    BP sinir ağının katmanları
    """

    def __init__(self, units, activation=None, learning_rate=None, is_input_layer=False):
        """
        BP ağının genel bağlı katmanı
        :param units: Sinir birimlerinin sayısı
        :param activation: Aktivasyon fonksiyonu
        :param learning_rate: Öğrenme oranı
        :param is_input_layer: Giriş katmanı olup olmadığı
        """
        self.units = units
        self.weight = None
        self.bias = None
        self.activation = activation if activation is not None else sigmoid
        self.learn_rate = learning_rate if learning_rate is not None else 0.3
        self.is_input_layer = is_input_layer

    def initializer(self, back_units):
        """Ağırlıkları ve bias'ı başlatır."""
        rng = np.random.default_rng()
        self.weight = np.asmatrix(rng.normal(0, 0.5, (self.units, back_units)))
        self.bias = np.asmatrix(rng.normal(0, 0.5, self.units)).T

    def cal_gradient(self):
        """Gradyanı hesaplar."""
        if self.activation == sigmoid:
            gradient_mat = np.dot(self.output, (1 - self.output).T)
            gradient_activation = np.diag(np.diag(gradient_mat))
        else:
            gradient_activation = 1
        return gradient_activation

    def forward_propagation(self, xdata):
        """İleri yayılım işlemi."""
        self.xdata = xdata
        if self.is_input_layer:
            self.wx_plus_b = xdata
            self.output = xdata
            return xdata
        else:
            self.wx_plus_b = np.dot(self.weight, self.xdata) - self.bias
            self.output = self.activation(self.wx_plus_b)
            return self.output

    def back_propagation(self, gradient):
        """Geri yayılım işlemi."""
        gradient_activation = self.cal_gradient()
        gradient = np.asmatrix(np.dot(gradient.T, gradient_activation))

        self._gradient_weight = np.asmatrix(self.xdata)
        self._gradient_bias = -1
        self._gradient_x = self.weight

        self.gradient_weight = np.dot(gradient.T, self._gradient_weight.T)
        self.gradient_bias = gradient * self._gradient_bias
        self.gradient = np.dot(gradient, self._gradient_x).T

        # Ağırlıkları ve bias'ı güncelle
        self.weight -= self.learn_rate * self.gradient_weight
        self.bias -= self.learn_rate * self.gradient_bias.T
        return self.gradient


class BPNN:
    """
    Geri Yayılım Sinir Ağı Modeli
    """

    def __init__(self):
        self.layers = []
        self.train_mse = []
        self.fig_loss = plt.figure()
        self.ax_loss = self.fig_loss.add_subplot(1, 1, 1)

    def add_layer(self, layer):
        """Yeni bir katman ekler."""
        self.layers.append(layer)

    def build(self):
        """Ağı inşa eder."""
        for i, layer in enumerate(self.layers):
            if i == 0:
                layer.is_input_layer = True
            else:
                layer.initializer(self.layers[i - 1].units)

    def summary(self):
        """Ağ yapısını özetler."""
        for i, layer in enumerate(self.layers):
            print(f"------- Katman {i} -------")
            print("Ağırlık şekli: ", np.shape(layer.weight))
            print("Bias şekli: ", np.shape(layer.bias))

    def train(self, xdata, ydata, train_round, accuracy):
        """Ağı eğitir."""
        self.train_round = train_round
        self.accuracy = accuracy

        self.ax_loss.hlines(self.accuracy, 0, self.train_round * 1.1)

        x_shape = np.shape(xdata)
        for _ in range(train_round):
            all_loss = 0
            for row in range(x_shape[0]):
                _xdata = np.asmatrix(xdata[row, :]).T
                _ydata = np.asmatrix(ydata[row, :]).T

                # İleri yayılım
                for layer in self.layers:
                    _xdata = layer.forward_propagation(_xdata)

                loss, gradient = self.cal_loss(_ydata, _xdata)
                all_loss += loss

                # Geri yayılım: giriş katmanı güncellenmez
                for layer in reversed(self.layers[1:]):
                    gradient = layer.back_propagation(gradient)

            mse = all_loss / x_shape[0]
            self.train_mse.append(mse)

            self.plot_loss()

            if mse < self.accuracy:
                print("---- Hedef doğruluğa ulaşıldı ----")
                return mse
        return None

    def cal_loss(self, ydata, ydata_):
        """Kayıp ve gradyanı hesaplar."""
        self.loss = np.sum(np.power((ydata - ydata_), 2))
        self.loss_gradient = 2 * (ydata_ - ydata)
        return self.loss, self.loss_gradient

    def plot_loss(self):
        """Kayıp grafiğini çizer."""
        if self.ax_loss.lines:
            self.ax_loss.lines.remove(self.ax_loss.lines[0])
        self.ax_loss.plot(self.train_mse, "r-")
        plt.ion()
        plt.xlabel("Adım")
        plt.ylabel("Kayıp")
        plt.show()
        plt.pause(0.1)


def example():
    """Modelin örnek kullanımı."""
    rng = np.random.default_rng()
    x = rng.normal(size=(10, 10))
    y = np.asarray(
        [
            [0.8, 0.4],
            [0.4, 0.3],
            [0.34, 0.45],
            [0.67, 0.32],
            [0.88, 0.67],
            [0.78, 0.77],
            [0.55, 0.66],
            [0.55, 0.43],
            [0.54, 0.1],
            [0.1, 0.5],
        ]
    )
    model = BPNN()
    for i in (10, 20, 30, 2):
        model.add_layer(DenseLayer(i))
    model.build()
    model.summary()
    model.train(xdata=x, ydata=y, train_round=100, accuracy=0.01)


if __name__ == "__main__":
    example()
