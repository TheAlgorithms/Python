import numpy as np

"""
Here I have written a simple RNN.
The notation used here were used in the sequence model course
on coursera by Andrew NG
https://www.coursera.org/learn/nlp-sequence-models
"""


def rnn_cell_forward(xt, a_prev, parameters):
    """
     >>> np.random.seed(1)
     >>> xt_tmp = np.random.randn(3, 10)
     >>> a_prev_tmp = np.random.randn(5, 10)
     >>> parameters_tmp = {}
     >>> parameters_tmp['waa'] = np.random.randn(5, 5)
     >>> parameters_tmp['wax'] = np.random.randn(5, 3)
     >>> parameters_tmp['wya'] = np.random.randn(2, 5)
     >>> parameters_tmp['bias'] = np.random.randn(5, 1)
     >>> parameters_tmp['bias_hidden_state_output'] = np.random.randn(2, 1)
     >>> a_next_tmp, yt_pred_tmp, cache_tmp = rnn_cell_forward(\
            xt_tmp, a_prev_tmp,parameters_tmp)
     >>> a_next_tmp.shape == (5,10)
     True
     >>> yt_pred_tmp.shape == (1,10)
     False
    """
    # xt -- your input data at timestep "t"
    # a_prev -- Hidden state at timestep "t-1"

    # wax -- Weight matrix multiplying the input
    # waa -- Weight matrix multiplying the hidden state
    # wya -- Weight matrix relating the hidden-state to the output
    wax = parameters["wax"]
    waa = parameters["waa"]
    wya = parameters["wya"]
    bias = parameters["bias"]
    bias_hidden_state_output = parameters["bias_hidden_state_output"]

    next_hidden_state = np.tanh(np.dot(waa, a_prev) + np.dot(wax, xt) + bias)
    yt_pred = np.tanh(np.dot(wya, next_hidden_state) + bias_hidden_state_output)

    # Required for backpropagation
    cache = (next_hidden_state, a_prev, xt, parameters)

    return next_hidden_state, yt_pred, cache


def forward_propagation_rnn(x, a0, parameters):
    # x -- Input data for every time-step
    # a0 -- Initial hidden state

    # Initialize "caches" which will contain the list of all caches
    caches = []

    n_x, m, t_x = x.shape
    n_y, n_a = parameters["Wya"].shape

    a = np.zeros((n_a, m, t_x))
    y_pred = np.zeros((n_y, m, t_x))
    a_next = a0

    # loop over all time-steps
    for t in range(t_x):
        a_next, yt_pred, cache = rnn_cell_forward(x[:, :, t], a_next, parameters)
        a[:, :, t] = a_next
        y_pred[:, :, t] = yt_pred
        caches.append(cache)
    caches = (caches, x)

    return a, y_pred, caches
