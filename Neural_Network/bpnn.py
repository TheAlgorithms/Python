'''

A Framework of Back Propagation Neural Network（BP） model

Easy to use:
    * add many layers as you want ！！！
    * clearly see how the loss decreasing
Easy to expand:
    * more activation functions
    * more loss functions
    * more optimization method

Author: Stephen Lee
Github : https://github.com/RiptideBo
Date: 2017.11.23

'''

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-1 * x))

class DenseLayer():
    '''
    Layers of BP neural network
    '''
    def __init__(self,units,activation=None,learning_rate=None,is_input_layer=False):
        '''
        common connected layer of bp network
        :param units: numbers of neural units
        :param activation: activation function
        :param learning_rate: learning rate for paras
        :param is_input_layer: whether it is input layer or not
        '''
        self.units = units
        self.weight = None
        self.bias = None
        self.activation = activation
        if learning_rate is None:
            learning_rate = 0.3
        self.learn_rate = learning_rate
        self.is_input_layer = is_input_layer

    def initializer(self,back_units):
        self.weight = np.asmatrix(np.random.normal(0,0.5,(self.units,back_units)))
        self.bias = np.asmatrix(np.random.normal(0,0.5,self.units)).T
        if self.activation is None:
            self.activation = sigmoid

    def cal_gradient(self):
        if self.activation == sigmoid:
            gradient_mat = np.dot(self.output ,(1- self.output).T)
            gradient_activation = np.diag(np.diag(gradient_mat))
        else:
            gradient_activation = 1
        return gradient_activation

    def forward_propagation(self,xdata):
        self.xdata = xdata
        if self.is_input_layer:
            # input layer
            self.wx_plus_b = xdata
            self.output = xdata
            return xdata
        else:
            self.wx_plus_b = np.dot(self.weight,self.xdata) - self.bias
            self.output = self.activation(self.wx_plus_b)
            return self.output

    def back_propagation(self,gradient):

        gradient_activation = self.cal_gradient() # i * i 维
        gradient = np.asmatrix(np.dot(gradient.T,gradient_activation))

        self._gradient_weight = np.asmatrix(self.xdata)
        self._gradient_bias = -1
        self._gradient_x = self.weight

        self.gradient_weight = np.dot(gradient.T,self._gradient_weight.T)
        self.gradient_bias = gradient * self._gradient_bias
        self.gradient = np.dot(gradient,self._gradient_x).T
        # ----------------------upgrade
        # -----------the Negative gradient direction --------
        self.weight = self.weight - self.learn_rate * self.gradient_weight
        self.bias = self.bias - self.learn_rate * self.gradient_bias.T

        return self.gradient


class BPNN():
    '''
    Back Propagation Neural Network model
    '''
    def __init__(self):
        self.layers = []
        self.train_mse = []
        self.fig_loss = plt.figure()
        self.ax_loss = self.fig_loss.add_subplot(1,1,1)

    def add_layer(self,layer):
        self.layers.append(layer)

    def build(self):
        for i,layer in enumerate(self.layers[:]):
            if i < 1:
                layer.is_input_layer = True
            else:
                layer.initializer(self.layers[i-1].units)

    def summary(self):
        for i,layer in enumerate(self.layers[:]):
            print('------- layer %d -------'%i)
            print('weight.shape ',np.shape(layer.weight))
            print('bias.shape ',np.shape(layer.bias))

    def train(self,xdata,ydata,train_round,accuracy):
        self.train_round = train_round
        self.accuracy = accuracy

        self.ax_loss.hlines(self.accuracy, 0, self.train_round * 1.1)

        x_shape = np.shape(xdata)
        for round_i in range(train_round):
            all_loss = 0
            for row in range(x_shape[0]):
                _xdata = np.asmatrix(xdata[row,:]).T
                _ydata = np.asmatrix(ydata[row,:]).T

                # forward propagation
                for layer in self.layers:
                    _xdata = layer.forward_propagation(_xdata)

                loss, gradient = self.cal_loss(_ydata, _xdata)
                all_loss = all_loss + loss

                # back propagation
                # the input_layer does not upgrade
                for layer in self.layers[:0:-1]:
                    gradient = layer.back_propagation(gradient)

            mse = all_loss/x_shape[0]
            self.train_mse.append(mse)

            self.plot_loss()

            if mse < self.accuracy:
                print('----达到精度----')
                return mse

    def cal_loss(self,ydata,ydata_):
        self.loss = np.sum(np.power((ydata - ydata_),2))
        self.loss_gradient = 2 * (ydata_ - ydata)
        # vector (shape is the same as _ydata.shape)
        return self.loss,self.loss_gradient

    def plot_loss(self):
        if self.ax_loss.lines:
            self.ax_loss.lines.remove(self.ax_loss.lines[0])
        self.ax_loss.plot(self.train_mse, 'r-')
        plt.ion()
        plt.show()
        plt.pause(0.1)




def example():

    x = np.random.randn(10,10)
    y = np.asarray([[0.8,0.4],[0.4,0.3],[0.34,0.45],[0.67,0.32],
                    [0.88,0.67],[0.78,0.77],[0.55,0.66],[0.55,0.43],[0.54,0.1],
                    [0.1,0.5]])

    model = BPNN()
    model.add_layer(DenseLayer(10))
    model.add_layer(DenseLayer(20))
    model.add_layer(DenseLayer(30))
    model.add_layer(DenseLayer(2))

    model.build()

    model.summary()

    model.train(xdata=x,ydata=y,train_round=100,accuracy=0.01)

if __name__ == '__main__':
    example()
