"""
Create a Long Short Term Memory (LSTM) network model
An LSTM is a type of Recurrent Neural Network (RNN) as discussed at:
* https://colah.github.io/posts/2015-08-Understanding-LSTMs
* https://en.wikipedia.org/wiki/Long_short-term_memory
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential

if __name__ == "__main__":
    """
    First part of building a model is to get the data and prepare
    it for our model. You can use any dataset for stock prediction
    make sure you set the price column on line number 21.  Here we
    use a dataset which have the price on 3rd column.
    """
    sample_data = pd.read_csv("sample_data.csv", header=None)
    len_data = sample_data.shape[:1][0]
    # If you're using some other dataset input the target column
    actual_data = sample_data.iloc[:, 1:2]
    actual_data = actual_data.to_numpy().reshape(len_data, 1)
    actual_data = MinMaxScaler().fit_transform(actual_data)
    look_back = 10
    forward_days = 5
    periods = 20
    division = len_data - periods * look_back
    train_data = actual_data[:division]
    test_data = actual_data[division - look_back :]
    train_x, train_y = [], []
    test_x, test_y = [], []

    for i in range(len(train_data) - forward_days - look_back + 1):
        train_x.append(train_data[i : i + look_back])
        train_y.append(train_data[i + look_back : i + look_back + forward_days])
    for i in range(len(test_data) - forward_days - look_back + 1):
        test_x.append(test_data[i : i + look_back])
        test_y.append(test_data[i + look_back : i + look_back + forward_days])
    x_train = np.array(train_x)
    x_test = np.array(test_x)
    y_train = np.array([list(i.ravel()) for i in train_y])
    y_test = np.array([list(i.ravel()) for i in test_y])

    model = Sequential()
    model.add(LSTM(128, input_shape=(look_back, 1), return_sequences=True))
    model.add(LSTM(64, input_shape=(128, 1)))
    model.add(Dense(forward_days))
    model.compile(loss="mean_squared_error", optimizer="adam")
    history = model.fit(
        x_train, y_train, epochs=150, verbose=1, shuffle=True, batch_size=4
    )
    pred = model.predict(x_test)
