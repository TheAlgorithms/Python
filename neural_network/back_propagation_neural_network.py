import numpy as np
from matplotlib import pyplot as plt


class DenseLayer:
    def __init__(self, units: int, activation=None, learning_rate: float = 0.3):
        self.units = units
        self.weight = None
        self.bias = None
        self.activation = activation if activation else sigmoid
        self.learning_rate = learning_rate

    def initializer(self, back_units: int):
        self.weight = np.random.normal(0, 0.5, (self.units, back_units))
        self.bias = np.random.normal(0, 0.5, self.units).reshape(-1, 1)

    def forward_propagation(self, xdata: np.ndarray) -> np.ndarray:
        self.wx_plus_b = np.dot(self.weight, xdata) - self.bias
        self.output = self.activation(self.wx_plus_b)
        return self.output

    def back_propagation(self, gradient: np.ndarray) -> np.ndarray:
        gradient_activation = self.cal_gradient()
        gradient = np.dot(gradient.T, gradient_activation)
        self.weight -= self.learning_rate * np.dot(gradient.T, self.xdata)
        self.bias -= self.learning_rate * gradient
        return gradient

    def cal_gradient(self) -> np.ndarray:
        if self.activation == sigmoid:
            return np.diag(np.diag(np.dot(self.output, (1 - self.output).T)))
        else:
            return 1


class BPNN:
    def __init__(self):
        self.layers = []
        self.train_mse = []
        self.fig_loss = plt.figure()
        self.ax_loss = self.fig_loss.add_subplot(1, 1, 1)

    def add_layer(self, layer: DenseLayer):
        self.layers.append(layer)

    def build(self):
        for i, layer in enumerate(self.layers):
            if i == 0:
                layer.is_input_layer = True
            else:
                layer.initializer(self.layers[i - 1].units)

    def summary(self):
        for i, layer in enumerate(self.layers):
            print(f"------- layer {i} -------")
            print("weight.shape ", layer.weight.shape)
            print("bias.shape ", layer.bias.shape)

    def train(
        self, xdata: np.ndarray, ydata: np.ndarray, train_round: int, accuracy: float
    ):
        self.train_round = train_round
        self.accuracy = accuracy

        self.ax_loss.hlines(accuracy, 0, train_round * 1.1)

        for _ in range(train_round):
            all_loss = 0
            for row in range(xdata.shape[0]):
                _xdata = xdata[row, :].reshape(-1, 1)
                _ydata = ydata[row, :].reshape(-1, 1)

                # forward propagation
                for layer in self.layers:
                    _xdata = layer.forward_propagation(_xdata)

                loss, gradient = self.cal_loss(_ydata, _xdata)
                all_loss += loss

                # back propagation
                for layer in reversed(self.layers):
                    gradient = layer.back_propagation(gradient)

            mse = all_loss / xdata.shape[0]
            self.train_mse.append(mse)

            self.plot_loss()

            if mse < accuracy:
                print("----达到精度----")
                return mse
        return None

    def cal_loss(self, ydata: np.ndarray, ydata_: np.ndarray) -> tuple:
        loss = np.sum(np.power(ydata - ydata_, 2))
        loss_gradient = 2 * (ydata_ - ydata)
        return loss, loss_gradient

    def plot_loss(self):
        if self.ax_loss.lines:
            self.ax_loss.lines.remove(self.ax_loss.lines[0])
        self.ax_loss.plot(self.train_mse, "r-")
        plt.ion()
        plt.xlabel("step")
        plt.ylabel("loss")
        plt.show()
        plt.pause(0.1)


def example():
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
