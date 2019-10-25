import sys
import numpy

numpy.seterr(all='ignore')


'''
activation function
'''
def sigmoid(x):
    return 1. / (1 + numpy.exp(-x))

def dsigmoid(x):
    return x * (1. - x)

def tanh(x):
    return numpy.tanh(x)

def dtanh(x):
    return 1. - x * x

def softmax(x):
    e = numpy.exp(x - numpy.max(x))  # prevent overflow
    if e.ndim == 1:
        return e / numpy.sum(e, axis=0)
    else:
        return e / numpy.array([numpy.sum(e, axis=1)]).T  # ndim = 2

def ReLU(x):
    return x * (x > 0)

def dReLU(x):
    return 1. * (x > 0)



'''
Dropout
'''
class Dropout(object):
    def __init__(self, input, label,\
                 n_in, hidden_layer_sizes, n_out,\
                 rng=None, activation=ReLU):

        self.x = input
        self.y = label

        self.hidden_layers = []
        self.n_layers = len(hidden_layer_sizes)

        if rng is None:
            rng = numpy.random.RandomState(1234)

        assert self.n_layers > 0


        # construct multi-layer
        for i in xrange(self.n_layers):

            # layer_size
            if i == 0:
                input_size = n_in
            else:
                input_size = hidden_layer_sizes[i-1]

            # layer_input
            if i == 0:
                layer_input = self.x

            else:
                layer_input = self.hidden_layers[-1].output()

            # construct hidden_layer
            hidden_layer = HiddenLayer(input=layer_input,
                                       n_in=input_size,
                                       n_out=hidden_layer_sizes[i],
                                       rng=rng,
                                       activation=activation)

            self.hidden_layers.append(hidden_layer)


            # layer for ouput using Logistic Regression (softmax)
            self.log_layer = LogisticRegression(input=self.hidden_layers[-1].output(),
                                                label=self.y,
                                                n_in=hidden_layer_sizes[-1],
                                                n_out=n_out)


    def train(self, epochs=5000, dropout=True, p_dropout=0.5, rng=None):

        for epoch in xrange(epochs):
            dropout_masks = []  # create different masks in each training epoch

            # forward hidden_layers
            for i in xrange(self.n_layers):
                if i == 0:
                    layer_input = self.x

                layer_input = self.hidden_layers[i].forward(input=layer_input)

                if dropout == True:
                    mask = self.hidden_layers[i].dropout(input=layer_input, p=p_dropout, rng=rng)
                    layer_input *= mask

                    dropout_masks.append(mask)


            # forward & backward log_layer
            self.log_layer.train(input=layer_input)


            # backward hidden_layers
            for i in reversed(xrange(0, self.n_layers)):
                if i == self.n_layers-1:
                    prev_layer = self.log_layer
                else:
                    prev_layer = self.hidden_layers[i+1]

                self.hidden_layers[i].backward(prev_layer=prev_layer)

                if dropout == True:
                    self.hidden_layers[i].d_y *= dropout_masks[i]  # also mask here


    def predict(self, x, dropout=True, p_dropout=0.5):
        layer_input = x

        for i in xrange(self.n_layers):
            if dropout == True:
                self.hidden_layers[i].W = p_dropout * self.hidden_layers[i].W
                self.hidden_layers[i].b = p_dropout * self.hidden_layers[i].b

            layer_input = self.hidden_layers[i].output(input=layer_input)

        return self.log_layer.predict(layer_input)


'''
Hidden Layer
'''
class HiddenLayer(object):
    def __init__(self, input, n_in, n_out,\
                 W=None, b=None, rng=None, activation=tanh):

        if rng is None:
            rng = numpy.random.RandomState(1234)

        if W is None:
            a = 1. / n_in
            W = numpy.array(rng.uniform(  # initialize W uniformly
                low=-a,
                high=a,
                size=(n_in, n_out)))

        if b is None:
            b = numpy.zeros(n_out)  # initialize bias 0

        self.rng = rng
        self.x = input

        self.W = W
        self.b = b

        if activation == tanh:
            self.dactivation = dtanh

        elif activation == sigmoid:
            self.dactivation = dsigmoid

        elif activation == ReLU:
            self.dactivation = dReLU

        else:
            raise ValueError('activation function not supported.')


        self.activation = activation

    def output(self, input=None):
        if input is not None:
            self.x = input

        linear_output = numpy.dot(self.x, self.W) + self.b

        return (linear_output if self.activation is None
                else self.activation(linear_output))

    def sample_h_given_v(self, input=None):
        if input is not None:
            self.x = input

        v_mean = self.output()
        h_sample = self.rng.binomial(size=v_mean.shape,
                                           n=1,
                                           p=v_mean)
        return h_sample

    def forward(self, input=None):
        return self.output(input=input)

    def backward(self, prev_layer, lr=0.1, input=None):
        if input is not None:
            self.x = input

        d_y = self.dactivation(prev_layer.x) * numpy.dot(prev_layer.d_y, prev_layer.W.T)

        self.W += lr * numpy.dot(self.x.T, d_y)
        self.b += lr * numpy.mean(d_y, axis=0)

        self.d_y = d_y


    def dropout(self, input, p, rng=None):
        if rng is None:
            rng = numpy.random.RandomState(123)

        mask = rng.binomial(size=input.shape,
                            n=1,
                            p=1-p)  # p is the prob of dropping

        return mask

'''
Logistic Regression
'''
class LogisticRegression(object):
    def __init__(self, input, label, n_in, n_out):
        self.x = input
        self.y = label
        self.W = numpy.zeros((n_in, n_out))  # initialize W 0
        self.b = numpy.zeros(n_out)          # initialize bias 0


    def train(self, lr=0.1, input=None, L2_reg=0.00):
        if input is not None:
            self.x = input

        p_y_given_x = softmax(numpy.dot(self.x, self.W) + self.b)
        d_y = self.y - p_y_given_x

        self.W += lr * numpy.dot(self.x.T, d_y) - lr * L2_reg * self.W
        self.b += lr * numpy.mean(d_y, axis=0)

        self.d_y = d_y

        # cost = self.negative_log_likelihood()
        # return cost

    def negative_log_likelihood(self):
        sigmoid_activation = softmax(numpy.dot(self.x, self.W) + self.b)

        cross_entropy = - numpy.mean(
            numpy.sum(self.y * numpy.log(sigmoid_activation) +
            (1 - self.y) * numpy.log(1 - sigmoid_activation),
                      axis=1))

        return cross_entropy


    def predict(self, x):
        return softmax(numpy.dot(x, self.W) + self.b)

    def output(self, x):
        return self.predict(x)

def test_dropout(n_epochs=5000, dropout=True, p_dropout=0.5):
    # XOR
    x = numpy.array([[0,  0],
                     [0,  1],
                     [1,  0],
                     [1,  1]])

    y = numpy.array([[0, 1],
                     [1, 0],
                     [1, 0],
                     [0, 1]])

    rng = numpy.random.RandomState(123)

    # construct Dropout MLP
    classifier = Dropout(input=x, label=y, \
                         n_in=2, hidden_layer_sizes=[10, 10], n_out=2, \
                         rng=rng, activation=ReLU)

    # train
    classifier.train(epochs=n_epochs, dropout=dropout, \
                     p_dropout=p_dropout, rng=rng)

    # test
    print(classifier.predict(x))

if __name__ == "__main__":
    test_dropout()
